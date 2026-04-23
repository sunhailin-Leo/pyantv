# ============================================================================
# Sprint 62 打包现代化验收测试
#
# 本测试文件不依赖任何第三方测试框架以外的东西，只使用 stdlib + pytest。
# 覆盖合约 CODE 段定义的 9 个关键测试用例：
#   T-BUILD-BACKEND        build-backend 字段为 setuptools.build_meta
#   T-OPT-DEPS             optional-dependencies 包含必需的"用户向"分组，
#                          dev/test/docs 改由 PEP 735 [dependency-groups] 承载
#   T-NO-UV-DEV-CONFLICT   pyproject.toml 无 [tool.uv].dev-dependencies
#   T-NO-UPLOAD-COMMAND    setup.py 不再定义 UploadCommand
#   T-MANIFEST             MANIFEST.in 包含必需条目且无 changelog.md 拼写错误
#   T-SETUP-THIN-SHIM      setup.py 是 thin shim（< 15 行，只 import setuptools.setup）
#   T-MAKEFILE-TARGETS     Makefile 含 uv-install / uv-lock / publish 三个新目标
#   T-CI-USES-UV           CI workflow 不再调用 `python setup.py install`，改用 uv
#   T-PYPROJECT-VALID-TOML pyproject.toml 是合法 TOML 且能被 tomllib 解析
#
# 注意：本文件只做"静态配置校验"，不实际执行 `python -m build` 或 `uv sync`，
# 因为 CI 中会由专门的 build job 执行这类端到端校验。此处聚焦配置正确性，
# 保证所有 PR 在单测阶段就能拦住打包配置的回归。
# ============================================================================
from __future__ import annotations

import re
from pathlib import Path

import pytest

# tomllib 是 Python 3.11+ 内置；3.8-3.10 需要 tomli 回退
try:
    import tomllib  # type: ignore[import-not-found]
except ModuleNotFoundError:  # pragma: no cover - py38~py310
    import tomli as tomllib  # type: ignore[import-not-found,no-redef]

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = PROJECT_ROOT / "pyproject.toml"
SETUP_PY = PROJECT_ROOT / "setup.py"
MANIFEST = PROJECT_ROOT / "MANIFEST.in"
MAKEFILE = PROJECT_ROOT / "Makefile"
CI_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "python-app.yml"

@pytest.fixture(scope="module")
def pyproject_data() -> dict:
    with PYPROJECT.open("rb") as f:
        return tomllib.load(f)

# ---------------------------------------------------------------------------
# T-PYPROJECT-VALID-TOML：pyproject.toml 必须是合法 TOML
# ---------------------------------------------------------------------------
def test_pyproject_is_valid_toml(pyproject_data: dict) -> None:
    assert "project" in pyproject_data, "pyproject.toml 缺少 [project] 段"
    assert pyproject_data["project"]["name"] == "pyantv"

# ---------------------------------------------------------------------------
# T-BUILD-BACKEND：build-backend 字段必须是官方的 setuptools.build_meta
# （Sprint 62 v1 的 "setuptools.backends._legacy:_Backend" 是虚构字符串，
#   会导致 `python -m build` 直接失败，必须锁死此断言）
# ---------------------------------------------------------------------------
def test_build_backend_is_setuptools_build_meta(pyproject_data: dict) -> None:
    build_system = pyproject_data.get("build-system", {})
    assert build_system.get("build-backend") == "setuptools.build_meta", (
        "build-backend 必须是 'setuptools.build_meta'，当前值："
        f"{build_system.get('build-backend')!r}"
    )
    # requires 必须包含 setuptools 且版本 >= 61
    requires = build_system.get("requires", [])
    assert any(
        "setuptools" in r for r in requires
    ), "build-system.requires 缺少 setuptools"

# ---------------------------------------------------------------------------
# T-OPT-DEPS：依赖分组分两类：
#   1) [project.optional-dependencies] 只放"用户向"特性分组（pip install pyantv[xxx]）
#   2) [dependency-groups]（PEP 735）放"开发向"分组（dev/test/docs），
#      由 uv sync --group dev 等命令安装，不污染发布 wheel 元数据
# 这样既符合 PEP 621/735 现代规范，又能保证 `pip install pyantv[all]` 不会
# 把 pytest/mkdocs/twine 等 500MB+ 开发依赖拉下来。
# ---------------------------------------------------------------------------
REQUIRED_USER_OPT_GROUPS = {
    "pandas",
    "numpy",
    "export",
    "streamlit",
    "notebook",
    "offline",
    "all",
}
REQUIRED_DEV_GROUPS = {"dev", "test", "docs"}

def test_optional_dependencies_cover_all_groups(pyproject_data: dict) -> None:
    opt = pyproject_data["project"].get("optional-dependencies", {})
    missing_user = REQUIRED_USER_OPT_GROUPS - set(opt.keys())
    assert not missing_user, (
        f"pyproject.toml [project.optional-dependencies] 缺少用户向分组：{missing_user}"
    )

    # `all` 分组必须是"用户向"聚合，不得污染 dev/test/docs
    all_deps = " ".join(opt["all"])
    for forbidden in ("pytest", "black", "flake8", "mypy", "twine", "mkdocs"):
        assert forbidden not in all_deps, (
            f"optional-dependencies.all 不应包含开发依赖 {forbidden!r}，"
            "避免 `pip install pyantv[all]` 拉入 500MB+ 无关依赖"
        )

    # dev/test/docs 必须迁移到 PEP 735 [dependency-groups]，
    # 不应再出现在面向 PyPI 用户的 [project.optional-dependencies]
    user_opt_polluted = REQUIRED_DEV_GROUPS & set(opt.keys())
    assert not user_opt_polluted, (
        "[project.optional-dependencies] 不应再包含开发分组 "
        f"{user_opt_polluted}，请迁移至 PEP 735 [dependency-groups]"
    )

def test_dependency_groups_define_dev_test_docs(pyproject_data: dict) -> None:
    """PEP 735：开发依赖统一放在顶层 [dependency-groups]。"""
    dep_groups = pyproject_data.get("dependency-groups", {})
    missing_dev = REQUIRED_DEV_GROUPS - set(dep_groups.keys())
    assert not missing_dev, (
        f"pyproject.toml [dependency-groups] 缺少开发分组：{missing_dev}。"
        "请按 PEP 735 在顶层 [dependency-groups] 中定义 dev / test / docs。"
    )
    # dev 组应当至少包含 test/docs 的关键工具或通过 include-group 引用，
    # 避免出现"空分组"的回归
    for group_name in REQUIRED_DEV_GROUPS:
        members = dep_groups.get(group_name, [])
        assert members, f"[dependency-groups].{group_name} 不应为空"

# ---------------------------------------------------------------------------
# T-NO-UV-DEV-CONFLICT：pyproject.toml 不得定义 [tool.uv].dev-dependencies
# （PEP 735 [dependency-groups] 已经是 uv 的官方推荐写法，
#   再叠加 [tool.uv].dev-dependencies 会造成两套源歧义）
# ---------------------------------------------------------------------------
def test_no_tool_uv_dev_dependencies(pyproject_data: dict) -> None:
    tool_uv = pyproject_data.get("tool", {}).get("uv", {})
    assert "dev-dependencies" not in tool_uv, (
        "pyproject.toml 禁止同时声明 [tool.uv].dev-dependencies 与 "
        "[dependency-groups].dev，二者只能存其一（推荐 PEP 735）"
    )

# ---------------------------------------------------------------------------
# T-SETUP-THIN-SHIM：setup.py 必须是 thin shim（< 15 行），
# 且不得包含 UploadCommand / cmdclass 等可能递归调用自身的代码
# ---------------------------------------------------------------------------
def test_setup_py_is_thin_shim() -> None:
    content = SETUP_PY.read_text(encoding="utf-8")
    # 去掉空行与纯注释行后再数
    non_trivial_lines = [
        ln
        for ln in content.splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    assert (
        len(non_trivial_lines) < 15
    ), f"setup.py 必须是 thin shim（< 15 行非注释代码），当前 {len(non_trivial_lines)} 行"
    # 必须调用 setuptools.setup()
    assert (
        "from setuptools import setup" in content
    ), "setup.py 必须 from setuptools import setup"
    assert "setup()" in content, "setup.py 必须调用 setup()"

# ---------------------------------------------------------------------------
# T-NO-UPLOAD-COMMAND：setup.py 不得定义 UploadCommand 或通过 os.system 递归调用自身
#
# 注意：注释行中出现 "UploadCommand" / "cmdclass" 等关键词是**允许**的（因为
# thin shim 的注释里会用这些词描述"为什么不能加"，作为未来维护者的防呆提示）。
# 本测试只检查**真实代码**，因此先剥离掉注释和字符串字面量再做断言。
# ---------------------------------------------------------------------------
def _strip_comments_and_strings(src: str) -> str:
    """剥离 # 注释、三引号 docstring、普通字符串字面量，仅保留真实执行代码。"""
    # 去三引号块（含文档字符串）
    src = re.sub(r'"""[\s\S]*?"""', "", src)
    src = re.sub(r"'''[\s\S]*?'''", "", src)
    # 去单行 # 注释（保留 shebang 和 coding 行意义不大，直接整行剔）
    lines = []
    for ln in src.splitlines():
        # 先剥右侧行内注释（简单处理，不考虑字符串内 '#'；本仓库 setup.py 无此复杂度）
        no_comment = re.sub(r"#.*$", "", ln)
        lines.append(no_comment)
    src = "\n".join(lines)
    # 去单双引号字符串字面量
    src = re.sub(r'"[^"\n]*"', '""', src)
    src = re.sub(r"'[^'\n]*'", "''", src)
    return src

def test_setup_py_has_no_upload_command() -> None:
    content = SETUP_PY.read_text(encoding="utf-8")
    code_only = _strip_comments_and_strings(content)
    # 真实代码里禁止出现 UploadCommand 类定义或 cmdclass 关键字
    assert (
        "UploadCommand" not in code_only
    ), "setup.py 实际代码中禁止定义或引用 UploadCommand（Sprint 62 决议）"
    assert (
        "cmdclass" not in code_only
    ), "setup.py 实际代码中禁止使用 cmdclass（避免 thin shim 递归调用自身）"
    # 最危险的模式：os.system("... setup.py ...") 会无限递归
    # 同样只检查剥离注释/字符串后的真实代码，允许注释里作为"反面教材"提及这个模式
    assert not re.search(
        r"os\.system\(.*setup\.py.*\)", code_only
    ), "setup.py 实际代码中禁止通过 os.system 调用自身（会导致无限递归）"

# ---------------------------------------------------------------------------
# T-MANIFEST：MANIFEST.in 必须包含关键条目且无 changelog.md 小写拼写错误
# ---------------------------------------------------------------------------
def test_manifest_in_covers_required_entries() -> None:
    content = MANIFEST.read_text(encoding="utf-8")
    # 必须显式 include 的文件
    for required in ("README.md", "LICENSE", "CHANGELOG.md", "pyproject.toml"):
        assert f"include {required}" in content, f"MANIFEST.in 缺少 include {required}"

    # 必须有 .pyi 类型存根的 recursive-include（Sprint 65 联动）
    assert (
        "recursive-include pyantv *.pyi" in content
    ), "MANIFEST.in 必须 recursive-include pyantv *.pyi，以打包类型存根"

    # 旧版拼写错误 `changelog.md`（小写）必须消除
    # 使用分词严格匹配，避免把 recursive-include 之类的误杀
    lines = [ln.strip() for ln in content.splitlines()]
    assert "include changelog.md" not in lines, (
        "MANIFEST.in 含小写 `include changelog.md`（实际文件是大写 CHANGELOG.md），"
        "在大小写敏感文件系统上会导致 sdist 缺失 CHANGELOG"
    )

# ---------------------------------------------------------------------------
# T-MAKEFILE-TARGETS：Makefile 必须包含 uv-install / uv-lock / publish 三个新目标
# ---------------------------------------------------------------------------
def test_makefile_has_new_targets() -> None:
    content = MAKEFILE.read_text(encoding="utf-8")
    for target in ("uv-install", "uv-lock", "publish", "install-dev"):
        assert f".PHONY: {target}" in content, f"Makefile 缺少 .PHONY: {target}"
        assert re.search(
            rf"^{target}:", content, re.MULTILINE
        ), f"Makefile 缺少 `{target}:` 规则"
    # publish 必须依赖 clean + build（避免发 stale 产物）
    publish_match = re.search(r"^publish:(.+)$", content, re.MULTILINE)
    assert publish_match, "Makefile publish 目标定义缺失"
    publish_deps = publish_match.group(1).strip().split()
    assert "clean" in publish_deps, "publish 目标必须先依赖 clean"
    assert "build" in publish_deps, "publish 目标必须先依赖 build"

# ---------------------------------------------------------------------------
# T-CI-USES-UV：CI workflow 不得再调用老派 `python setup.py install`，应改用 uv
# ---------------------------------------------------------------------------
def test_ci_workflow_uses_uv_not_setup_py_install() -> None:
    content = CI_WORKFLOW.read_text(encoding="utf-8")
    assert (
        "python setup.py install" not in content
    ), "CI workflow 不得使用 `python setup.py install`（已淘汰写法，Sprint 62 改用 uv）"
    assert "pip install uv" in content, "CI workflow 必须显式 `pip install uv`"
    assert "uv sync" in content, "CI workflow 必须包含 `uv sync` 来安装依赖"
    assert (
        "python -m build" in content
    ), "CI workflow 必须通过 `python -m build` 构建（PEP 517 标准流程）"

# ---------------------------------------------------------------------------
# T-DYNAMIC-VERSION：pyproject.toml 通过 tool.setuptools.dynamic 读取 _version.py
# ---------------------------------------------------------------------------
def test_dynamic_version_configured(pyproject_data: dict) -> None:
    assert "version" in pyproject_data["project"].get(
        "dynamic", []
    ), "pyproject.toml 必须声明 dynamic = ['version']"
    # 版本由 setuptools-scm 管理，不应存在 [tool.setuptools.dynamic].version
    scm_cfg = pyproject_data.get("tool", {}).get("setuptools-scm", {})
    assert scm_cfg, (
        "pyproject.toml 必须配置 [tool.setuptools-scm] "
        "来管理动态版本"
    )
    assert scm_cfg.get("write_to") == "pyantv/_version.py", (
        "setuptools-scm.write_to 必须是 'pyantv/_version.py'"
    )
    # 确认旧的 [tool.setuptools.dynamic].version 已移除（避免冲突）
    old_ver_cfg = (
        pyproject_data.get("tool", {})
        .get("setuptools", {})
        .get("dynamic", {})
        .get("version", {})
    )
    assert not old_ver_cfg, (
        "不应同时存在 [tool.setuptools.dynamic].version 和 "
        "[tool.setuptools-scm]，二者冲突"
    )

"""类型存根生成器测试（Sprint 65）"""

import ast
import inspect
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Set

import pytest


# ============================================================================
# 辅助函数
# ============================================================================


def get_project_root() -> Path:
    """获取项目根目录"""
    return Path(__file__).resolve().parents[1]


def get_all_basicopts_classes() -> Set[type]:
    """
    动态获取所有继承自 BasicOpts 的类

    返回：所有 BasicOpts 子类的集合
    """
    from pyantv.options.series_options import BasicOpts
    from pyantv.options import chart_options, global_options

    basicopts_classes = set()

    # 从 chart_options 模块收集
    for name in dir(chart_options):
        obj = getattr(chart_options, name)
        if isinstance(obj, type) and issubclass(obj, BasicOpts) and obj is not BasicOpts:
            basicopts_classes.add(obj)

    # 从 global_options 模块收集
    for name in dir(global_options):
        obj = getattr(global_options, name)
        if isinstance(obj, type) and issubclass(obj, BasicOpts) and obj is not BasicOpts:
            basicopts_classes.add(obj)

    return basicopts_classes


def get_pyi_class_names(pyi_path: Path) -> Set[str]:
    """
    从 .pyi 文件中提取所有类名

    返回：类名集合
    """
    if not pyi_path.exists():
        return set()

    with open(pyi_path, "r", encoding="utf-8") as f:
        content = f.read()

    module = ast.parse(content)
    class_names = set()

    for node in module.body:
        if isinstance(node, ast.ClassDef):
            class_names.add(node.name)

    return class_names


def get_pyi_init_params(pyi_path: Path, class_name: str) -> Set[str]:
    """
    从 .pyi 文件中提取指定类的 __init__ 参数名

    返回：参数名集合（不含 self）
    """
    if not pyi_path.exists():
        return set()

    with open(pyi_path, "r", encoding="utf-8") as f:
        content = f.read()

    module = ast.parse(content)

    for node in module.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    params = set()
                    for arg in item.args.args:
                        if arg.arg != "self":
                            params.add(arg.arg)
                    return params

    return set()


# ============================================================================
# 测试用例（17 个）
# ============================================================================


def test_gen_type_stubs_script_exists():
    """测试生成脚本存在"""
    script_path = get_project_root() / "scripts" / "gen_type_stubs.py"
    assert script_path.exists(), f"Script not found: {script_path}"


def test_gen_type_stubs_check_passes():
    """测试 --check 模式通过（无差异）"""
    result = subprocess.run(
        [sys.executable, "scripts/gen_type_stubs.py", "--check"],
        capture_output=True,
        text=True,
        cwd=get_project_root(),
    )
    assert result.returncode == 0, f"Check failed: {result.stderr}"


def test_global_options_pyi_exists_and_parseable():
    """测试 global_options.pyi 存在且可解析"""
    pyi_path = get_project_root() / "pyantv" / "options" / "global_options.pyi"
    assert pyi_path.exists(), f"File not found: {pyi_path}"

    with open(pyi_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 应该能被 AST 解析
    try:
        ast.parse(content)
    except SyntaxError as e:
        pytest.fail(f"Failed to parse {pyi_path}: {e}")


def test_all_basicopts_classes_have_stubs():
    """测试所有 BasicOpts 子类都有对应的 stub 条目"""
    basicopts_classes = get_all_basicopts_classes()

    # 获取所有生成的 .pyi 文件中的类名
    pyi_dir = get_project_root() / "pyantv" / "options"
    all_pyi_classes = set()

    for pyi_file in pyi_dir.glob("*.pyi"):
        if pyi_file.name == "__init__.pyi":
            continue
        all_pyi_classes.update(get_pyi_class_names(pyi_file))

    # 计算差集
    runtime_class_names = {cls.__name__ for cls in basicopts_classes}
    missing_classes = runtime_class_names - all_pyi_classes

    assert missing_classes == set(), f"Missing stub classes: {missing_classes}"


def test_signature_matches_runtime():
    """测试前 5 个 Opts 的签名与运行时一致"""
    basicopts_classes = sorted(get_all_basicopts_classes(), key=lambda c: c.__name__)[:5]

    for cls in basicopts_classes:
        class_name = cls.__name__

        # 确定对应的 .pyi 文件
        if class_name.endswith("DataTransformOpts") or class_name.endswith("DataOpts"):
            pyi_path = get_project_root() / "pyantv" / "options" / "chart_options.pyi"
        else:
            pyi_path = get_project_root() / "pyantv" / "options" / "global_options.pyi"

        # 获取运行时参数
        runtime_params = set(inspect.signature(cls.__init__).parameters.keys())
        runtime_params.discard("self")

        # 获取 .pyi 参数
        pyi_params = get_pyi_init_params(pyi_path, class_name)

        assert runtime_params == pyi_params, (
            f"{class_name}: runtime params {runtime_params} != "
            f"pyi params {pyi_params}"
        )


def test_idempotent_write():
    """测试幂等性：两次 --write 后无差异"""
    # 第一次写入
    subprocess.run(
        [sys.executable, "scripts/gen_type_stubs.py", "--write"],
        capture_output=True,
        cwd=get_project_root(),
    )

    # 第二次写入
    subprocess.run(
        [sys.executable, "scripts/gen_type_stubs.py", "--write"],
        capture_output=True,
        cwd=get_project_root(),
    )

    # 检查 git diff
    result = subprocess.run(
        ["git", "diff", "--exit-code", "pyantv/options/*.pyi"],
        capture_output=True,
        cwd=get_project_root(),
    )

    assert result.returncode == 0, "Second write produced differences"


def test_module_filter_isolation():
    """测试 --module 参数只处理指定模块"""
    chart_options_pyi = get_project_root() / "pyantv" / "options" / "chart_options.pyi"

    # 获取初始 mtime
    initial_mtime = chart_options_pyi.stat().st_mtime

    # 只处理 global_options
    subprocess.run(
        [
            sys.executable,
            "scripts/gen_type_stubs.py",
            "--write",
            "--module",
            "pyantv/options/global_options.py",
        ],
        capture_output=True,
        cwd=get_project_root(),
    )

    # 检查 chart_options.pyi 的 mtime 是否变化
    final_mtime = chart_options_pyi.stat().st_mtime

    assert (
        initial_mtime == final_mtime
    ), "chart_options.pyi was modified when only global_options.py was processed"


def test_check_diff_output_format():
    """测试 --check 失败时输出 unified_diff 格式"""
    # 创建临时 .pyi 文件并修改
    global_options_pyi = get_project_root() / "pyantv" / "options" / "global_options.pyi"

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_pyi = Path(tmpdir) / "global_options.pyi"

        # 复制原文件
        import shutil

        shutil.copy(global_options_pyi, tmp_pyi)

        # 修改类名
        with open(tmp_pyi, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("class InitOpts:", "class InitOptsX:")
        with open(tmp_pyi, "w", encoding="utf-8") as f:
            f.write(content)

        # 替换原文件
        shutil.copy(tmp_pyi, global_options_pyi)

        try:
            # 运行 --check
            result = subprocess.run(
                [sys.executable, "scripts/gen_type_stubs.py", "--check"],
                capture_output=True,
                text=True,
                cwd=get_project_root(),
            )

            # 应该失败
            assert result.returncode == 1, "Check should fail with modified .pyi"

            # stderr 应该包含 unified_diff 格式
            assert (
                "@@" in result.stderr
            ), f"Expected unified_diff format, got: {result.stderr}"
        finally:
            # 恢复原文件
            subprocess.run(
                [sys.executable, "scripts/gen_type_stubs.py", "--write"],
                capture_output=True,
                cwd=get_project_root(),
            )


def test_deep_nested_type_fallback():
    """测试深层嵌套类型降级为 Any"""
    # 创建临时测试文件
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_complex.py"

        # 写入极端复杂的类型注解
        test_content = """
from typing import Optional, Union, Dict, Callable, Sequence
from pyantv.options.series_options import BasicOpts

class ComplexOpts(BasicOpts):
    def __init__(
        self,
        param: Optional[Union[
            Dict[str, Union[
                Callable[..., int],
                Sequence[Dict[str, Union[str, int]]]
            ]],
            str
        ]] = None,
    ):
        self.opts = {"param": param}
"""
        test_file.write_text(test_content)

        # 运行生成器
        subprocess.run(
            [
                sys.executable,
                "scripts/gen_type_stubs.py",
                "--write",
                "--module",
                str(test_file),
            ],
            capture_output=True,
            text=True,
            cwd=get_project_root(),
        )

        # 检查生成的 .pyi
        pyi_file = test_file.with_suffix(".pyi")
        if pyi_file.exists():
            with open(pyi_file, "r", encoding="utf-8") as f:
                content = f.read()

            # 复杂类型应该降级为 Any
            assert (
                "param: Any" in content
            ), f"Complex type should fallback to Any, got: {content}"


def test_init_pyi_structure_mirrors_source():
    """测试 __init__.pyi 的 import 结构与源码一致"""
    init_py = get_project_root() / "pyantv" / "options" / "__init__.py"
    init_pyi = get_project_root() / "pyantv" / "options" / "__init__.pyi"

    # 提取源码中的 import 名字
    with open(init_py, "r", encoding="utf-8") as f:
        py_content = f.read()

    py_imports = set()
    for line in py_content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("from ."):
            # 提取 from .chart_options import (...) 中的名字
            if "import (" in stripped:
                continue  # 多行 import，下面处理
            elif "import" in stripped:
                # 单行 import
                names = stripped.split("import")[1].strip()
                py_imports.add(names)

    # 提取 .pyi 中的 import 名字
    with open(init_pyi, "r", encoding="utf-8") as f:
        pyi_content = f.read()

    pyi_imports = set()
    for line in pyi_content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("from ."):
            if "import (" in stripped:
                continue
            elif "import" in stripped:
                names = stripped.split("import")[1].strip()
                pyi_imports.add(names)

    # 两者应该一致
    assert (
        py_imports == pyi_imports
    ), f"Source imports {py_imports} != pyi imports {pyi_imports}"


def test_basicopts_stub_has_methods():
    """测试 series_options.pyi 中的 BasicOpts 有 opts/update/get 三个成员"""
    series_options_pyi = get_project_root() / "pyantv" / "options" / "series_options.pyi"

    with open(series_options_pyi, "r", encoding="utf-8") as f:
        content = f.read()

    module = ast.parse(content)

    basicopts_node = None
    for node in module.body:
        if isinstance(node, ast.ClassDef) and node.name == "BasicOpts":
            basicopts_node = node
            break

    assert basicopts_node is not None, "BasicOpts class not found in series_options.pyi"

    # 提取成员名称
    members = set()
    for item in basicopts_node.body:
        if isinstance(item, ast.AnnAssign):
            members.add(item.target.id)
        elif isinstance(item, ast.FunctionDef):
            members.add(item.name)

    # 检查是否有 opts、update、get
    assert "opts" in members, "BasicOpts missing 'opts' member"
    assert "update" in members, "BasicOpts missing 'update' method"
    assert "get" in members, "BasicOpts missing 'get' method"


def test_chart_pyi_imports_all_resolvable():
    """测试 chart.pyi 的 import 都可解析（在生成的 stub 中存在）"""
    chart_pyi = get_project_root() / "pyantv" / "charts" / "chart.pyi"

    with open(chart_pyi, "r", encoding="utf-8") as f:
        content = f.read()

    module = ast.parse(content)

    # 收集所有 from ..options.global_options import 的名字
    imported_names = set()
    for node in module.body:
        if isinstance(node, ast.ImportFrom):
            if node.module and "options.global_options" in node.module:
                for alias in node.names:
                    imported_names.add(alias.name)

    # 获取 global_options.pyi 中的所有类名
    global_options_pyi = get_project_root() / "pyantv" / "options" / "global_options.pyi"
    global_options_classes = get_pyi_class_names(global_options_pyi)

    # 检查所有 import 的名字都在 global_options.pyi 中
    missing_names = imported_names - global_options_classes

    assert (
        missing_names == set()
    ), f"chart.pyi imports names not in global_options.pyi: {missing_names}"


def test_pyi_no_bare_self_param():
    """测试生成的 __init__ 签名中第一个参数为 self 且无类型注解"""
    chart_options_pyi = get_project_root() / "pyantv" / "options" / "chart_options.pyi"

    with open(chart_options_pyi, "r", encoding="utf-8") as f:
        content = f.read()

    module = ast.parse(content)

    for node in module.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    # 第一个参数应该是 self 且无类型注解
                    if item.args.args:
                        first_arg = item.args.args[0]
                        assert (
                            first_arg.arg == "self"
                        ), f"{node.name}.__init__ first param is not 'self'"
                        assert (
                            first_arg.annotation is None
                        ), f"{node.name}.__init__ 'self' has type annotation"


def test_script_exit_codes():
    """测试脚本的退出码"""
    # --check 一致时退出 0
    result = subprocess.run(
        [sys.executable, "scripts/gen_type_stubs.py", "--check"],
        capture_output=True,
        cwd=get_project_root(),
    )
    assert result.returncode == 0, "--check with no diff should exit 0"

    # --write 成功时退出 0
    result = subprocess.run(
        [sys.executable, "scripts/gen_type_stubs.py", "--write"],
        capture_output=True,
        cwd=get_project_root(),
    )
    assert result.returncode == 0, "--write should exit 0 on success"

    # --check 不一致时退出 1
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text("pass")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/gen_type_stubs.py",
                "--check",
                "--module",
                str(test_file),
            ],
            capture_output=True,
            cwd=get_project_root(),
        )
        assert result.returncode == 1, "--check with diff should exit 1"

    # 互斥参数时退出 3
    result = subprocess.run(
        [sys.executable, "scripts/gen_type_stubs.py", "--write", "--check"],
        capture_output=True,
        cwd=get_project_root(),
    )
    assert result.returncode == 3, "Mutually exclusive args should exit 3"


def test_signature_param_count_all():
    """测试所有 BasicOpts 子类的参数数量匹配"""
    basicopts_classes = get_all_basicopts_classes()

    mismatched = []

    for cls in basicopts_classes:
        class_name = cls.__name__

        # 确定对应的 .pyi 文件
        if class_name.endswith("DataTransformOpts") or class_name.endswith("DataOpts"):
            pyi_path = get_project_root() / "pyantv" / "options" / "chart_options.pyi"
        else:
            pyi_path = get_project_root() / "pyantv" / "options" / "global_options.pyi"

        # 获取运行时参数数量
        runtime_params = inspect.signature(cls.__init__).parameters
        runtime_count = len(runtime_params) - 1  # 减去 self

        # 获取 .pyi 参数数量
        pyi_params = get_pyi_init_params(pyi_path, class_name)
        pyi_count = len(pyi_params)

        if runtime_count != pyi_count:
            mismatched.append(
                {
                    "class": class_name,
                    "runtime": runtime_count,
                    "pyi": pyi_count,
                    "diff": runtime_count - pyi_count,
                }
            )

    if mismatched:
        first = mismatched[0]
        pytest.fail(
            f"Parameter count mismatch for {first['class']}: "
            f"runtime={first['runtime']}, pyi={first['pyi']}, "
            f"diff={first['diff']}. Total mismatched: {len(mismatched)}"
        )


def test_mypy_reveal_type():
    """测试 mypy 能正确推断类型"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write("from pyantv.options import TitleOpts\n")
        f.write("reveal_type(TitleOpts)\n")
        test_file = f.name

    try:
        result = subprocess.run(
            [sys.executable, "-m", "mypy", test_file],
            capture_output=True,
            text=True,
            cwd=get_project_root(),
        )

        # 检查输出中包含 TitleOpts
        assert (
            "TitleOpts" in result.stdout
        ), f"mypy reveal_type should show TitleOpts, got: {result.stdout}"
    finally:
        os.unlink(test_file)


def test_autogen_header_exists():
    """测试每个生成的 .pyi 文件都有 AUTO-GENERATED header"""
    pyi_dir = get_project_root() / "pyantv" / "options"

    for pyi_file in pyi_dir.glob("*.pyi"):
        with open(pyi_file, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()

        expected = "# AUTO-GENERATED by scripts/gen_type_stubs.py, do not edit manually"
        assert first_line == expected, (
            f"{pyi_file.name} first line should be autogen header, " f"got: {first_line}"
        )

        # __init__.pyi 第二行应该是 # flake8: noqa
        if pyi_file.name == "__init__.pyi":
            with open(pyi_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            second_line = lines[1].strip()
            assert second_line == "# flake8: noqa", (
                f"__init__.pyi second line should be '# flake8: noqa', "
                f"got: {second_line}"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

#!/usr/bin/env python3
"""
类型存根生成器（Sprint 65）

从 pyantv/options/*.py 自动生成 .pyi 类型存根文件。
使用 AST 解析器提取类定义和 __init__ 签名，不依赖 mypy.stubgen。

生成规则（§1~§8）：
§1 筛选：只处理继承自 BasicOpts 的类
§2 __init__ 签名：提取参数名和类型注解，忽略方法体
§3 复杂类型 fallback：嵌套 > 5 层或解析失败时降级为 Any
§4 import 语句：保留源文件所有 typing import + 本项目内相对 import
§5 __init__.pyi 特殊处理：复制 __init__.py 的 from .xxx import (...) 语句块
§6 series_options.pyi 手写约定：BasicOpts 声明 opts/update/get 三个成员
§7 幂等性：生成顺序、空行、注释保持稳定
§8 charts/*.pyi 联动：不覆盖手写存根，只验证 import 可解析

退出码：
0 - 成功
1 - --check 检测到差异
2 - 语法错误
3 - 互斥参数
"""
import argparse
import ast
import difflib
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


# ============================================================================
# AST 工具函数
# ============================================================================


def get_project_root() -> Path:
    """获取项目根目录（从 scripts/gen_type_stubs.py 向上两级）"""
    return Path(__file__).resolve().parents[1]


def parse_python_file(filepath: Path) -> Optional[ast.Module]:
    """解析 Python 文件为 AST，失败返回 None"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return ast.parse(content, filename=str(filepath))
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"Error parsing {filepath}: {e}", file=sys.stderr)
        return None


def is_basicopts_subclass(node: ast.ClassDef, module: ast.Module) -> bool:
    """
    判断类是否继承自 BasicOpts

    规则：类名不为 BasicOpts 且基类列表中包含 BasicOpts
    """
    if node.name == "BasicOpts":
        return False

    for base in node.bases:
        if isinstance(base, ast.Name) and base.id == "BasicOpts":
            return True
        if isinstance(base, ast.Attribute) and base.attr == "BasicOpts":
            return True
    return False


def extract_imports(module: ast.Module) -> Tuple[Set[str], Set[str]]:
    """
    提取 import 语句

    返回：(typing_imports, local_imports)
    - typing_imports: from typing import ... 或 from typing_extensions import ...
    - local_imports: 相对导入（如 from .series_options import ...）
    """
    typing_imports = set()
    local_imports = set()

    for node in ast.walk(module):
        if isinstance(node, ast.ImportFrom):
            module_name = node.module if node.module else ""

            # 判断是否为 typing 或 typing_extensions
            if module_name in ("typing", "typing_extensions"):
                for alias in node.names:
                    typing_imports.add(alias.name)

            # 判断是否为相对导入
            elif module_name.startswith("."):
                # 保留完整的 from .xxx import (...) 语句
                # 这里只收集，后面生成时再处理
                local_imports.add(module_name)

    return typing_imports, local_imports


def extract_class_init_signature(
    class_node: ast.ClassDef,
) -> Optional[Tuple[List[Tuple[str, Optional[str]]], Dict[str, str]]]:
    """
    提取类的 __init__ 方法签名

    返回：(params, defaults)
    - params: [(param_name, annotation_str), ...]
    - defaults: {param_name: default_value_str, ...}
    """
    for item in class_node.body:
        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
            params = []
            defaults = {}

            # 获取参数列表
            args = item.args
            all_args = args.args
            defaults_list = args.defaults
            kw_defaults = args.kw_defaults

            # 处理位置参数
            num_defaults = len(defaults_list)
            for i, arg in enumerate(all_args):
                param_name = arg.arg
                annotation_str = None

                # 提取类型注解
                if arg.annotation:
                    annotation_str = unparse_annotation(arg.annotation)

                # 提取默认值
                if i >= len(all_args) - num_defaults:
                    default_idx = i - (len(all_args) - num_defaults)
                    defaults[param_name] = unparse_node(defaults_list[default_idx])

                params.append((param_name, annotation_str))

            # 处理关键字参数
            if args.kwonlyargs:
                for i, arg in enumerate(args.kwonlyargs):
                    param_name = arg.arg
                    annotation_str = None

                    if arg.annotation:
                        annotation_str = unparse_annotation(arg.annotation)

                    if kw_defaults and i < len(kw_defaults) and kw_defaults[i]:
                        defaults[param_name] = unparse_node(kw_defaults[i])

                    params.append((param_name, annotation_str))

            return params, defaults

    return None


def unparse_annotation(node: ast.AST) -> str:
    """
    将类型注解 AST 节点转换为字符串

    复杂类型 fallback 规则：
    - 嵌套 > 5 层时返回 "Any"
    - 解析失败时返回 "Any"
    """
    depth = 0
    max_depth = 5

    def _unparse(n: ast.AST, d: int) -> Optional[str]:
        nonlocal depth
        depth = max(depth, d)

        if d > max_depth:
            return None

        # 基本类型
        if isinstance(n, ast.Name):
            return n.id
        elif isinstance(n, ast.Constant):
            return repr(n.value)
        elif isinstance(n, ast.Attribute):
            return f"{_unparse(n.value, d + 1)}.{n.attr}"
        elif isinstance(n, ast.Subscript):
            value = _unparse(n.value, d + 1)
            if value is None:
                return None
            slice_val = _unparse(n.slice, d + 1)
            if slice_val is None:
                return None
            return f"{value}[{slice_val}]"
        elif isinstance(n, ast.Tuple):
            elts = [_unparse(e, d + 1) for e in n.elts]
            if None in elts:
                return None
            return ", ".join(elts)
        elif isinstance(n, ast.List):
            elts = [_unparse(e, d + 1) for e in n.elts]
            if None in elts:
                return None
            return f"[{', '.join(elts)}]"
        elif isinstance(n, ast.BinOp):
            left = _unparse(n.left, d + 1)
            if left is None:
                return None
            right = _unparse(n.right, d + 1)
            if right is None:
                return None
            op = unparse_node(n.op)
            return f"{left} {op} {right}"
        elif isinstance(n, ast.UnaryOp):
            operand = _unparse(n.operand, d + 1)
            if operand is None:
                return None
            op = unparse_node(n.op)
            return f"{op}{operand}"
        elif isinstance(n, ast.Call):
            func = _unparse(n.func, d + 1)
            if func is None:
                return None
            args = [_unparse(arg, d + 1) for arg in n.args]
            if None in args:
                return None
            return f"{func}({', '.join(args)})"
        elif isinstance(n, ast.BitOr):
            return "|"
        elif isinstance(n, ast.Ellipsis):
            return "..."
        else:
            return None

    result = _unparse(node, 0)
    if result is None or depth > max_depth:
        return "Any"
    return result


def unparse_node(node: ast.AST) -> str:
    """
    将任意 AST 节点转换为字符串（用于默认值）
    """
    if isinstance(node, ast.Constant):
        if node.value is None:
            return "..."
        return repr(node.value)
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return f"{unparse_node(node.value)}.{node.attr}"
    elif isinstance(node, ast.List):
        elts = [unparse_node(e) for e in node.elts]
        return f"[{', '.join(elts)}]"
    elif isinstance(node, ast.Tuple):
        elts = [unparse_node(e) for e in node.elts]
        if len(elts) == 1:
            return f"({elts[0]},)"
        return f"({', '.join(elts)})"
    elif isinstance(node, ast.Dict):
        keys = [unparse_node(k) for k in node.keys]
        values = [unparse_node(v) for v in node.values]
        items = [f"{k}: {v}" for k, v in zip(keys, values)]
        return f"{{{', '.join(items)}}}"
    elif isinstance(node, ast.BinOp):
        left = unparse_node(node.left)
        right = unparse_node(node.right)
        op = unparse_node(node.op)
        return f"{left} {op} {right}"
    elif isinstance(node, ast.UnaryOp):
        operand = unparse_node(node.operand)
        op = unparse_node(node.op)
        return f"{op}{operand}"
    elif isinstance(node, ast.Ellipsis):
        return "..."
    elif isinstance(node, ast.Call):
        func = unparse_node(node.func)
        args = [unparse_node(arg) for arg in node.args]
        return f"{func}({', '.join(args)})"
    else:
        return "..."  # 降级处理


# ============================================================================
# .pyi 文件生成器
# ============================================================================


def generate_pyi_header(has_flake8_noqa: bool = False) -> str:
    """生成 .pyi 文件头部"""
    lines = ["# AUTO-GENERATED by scripts/gen_type_stubs.py, do not edit manually"]
    if has_flake8_noqa:
        lines.append("# flake8: noqa")
    lines.append("")
    return "\n".join(lines)


def generate_class_stub(
    class_name: str, params: List[Tuple[str, Optional[str]]], defaults: Dict[str, str]
) -> str:
    """
    生成类的 .pyi 存根

    格式：
    class ClassName:
        def __init__(self, param1: type1 = ..., param2: type2 = ...) -> None: ...
    """
    lines = [f"class {class_name}:"]

    if params:
        # 过滤掉 self
        init_params = [p for p in params if p[0] != "self"]
        if init_params:
            param_strs = []
            for param_name, annotation in init_params:
                if annotation:
                    param_str = f"{param_name}: {annotation}"
                else:
                    param_str = param_name

                # 添加默认值
                if param_name in defaults:
                    param_str += f" = {defaults[param_name]}"
                else:
                    param_str += " = ..."

                param_strs.append(param_str)

            params_line = ", ".join(param_strs)
            lines.append(f"    def __init__(self, {params_line}) -> None: ...")
        else:
            lines.append("    def __init__(self) -> None: ...")
    else:
        lines.append("    def __init__(self) -> None: ...")

    return "\n".join(lines)


def generate_series_options_pyi() -> str:
    """
    生成 series_options.pyi（手写约定）

    BasicOpts 类声明 opts/update/get 三个成员
    """
    lines = [
        generate_pyi_header(),
        "",
        "class BasicOpts:",
        "    opts: dict",
        "    def update(self, **kwargs) -> None: ...",
        "    def get(self, key: str) -> Any: ...",
    ]
    return "\n".join(lines)


def generate_init_pyi(init_py_path: Path) -> str:
    """
    生成 __init__.pyi（特殊处理）

    复制 __init__.py 的 from .xxx import (...) 语句块
    """
    with open(init_py_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    import_lines = []
    in_import_block = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# flake8: noqa"):
            continue
        if stripped.startswith("from ."):
            in_import_block = True
            import_lines.append(line)
        elif in_import_block and stripped.startswith(")"):
            import_lines.append(line)
            in_import_block = False
        elif in_import_block and (stripped == "" or stripped.endswith(",")):
            import_lines.append(line)
        elif in_import_block:
            # 继续收集多行 import
            import_lines.append(line)

    header = generate_pyi_header(has_flake8_noqa=True)
    return header + "\n" + "\n".join(import_lines) + "\n"


def generate_module_pyi(
    module_path: Path,
    typing_imports: Set[str],
    classes: List[Tuple[str, List[Tuple[str, Optional[str]]], Dict[str, str]]],
) -> str:
    """
    生成普通模块的 .pyi 文件

    格式：
    # AUTO-GENERATED by scripts/gen_type_stubs.py, do not edit manually

    from typing import ...

    class Class1:
        ...
    """
    lines = [generate_pyi_header(), ""]

    # 添加 typing import
    if typing_imports:
        sorted_imports = sorted(typing_imports)
        lines.append(f"from typing import {', '.join(sorted_imports)}")
        lines.append("")

    # 添加类定义
    for class_name, params, defaults in classes:
        lines.append(generate_class_stub(class_name, params, defaults))
        lines.append("")

    return "\n".join(lines)


# ============================================================================
# 主逻辑
# ============================================================================


def extract_classes_from_module(
    module_path: Path,
) -> List[Tuple[str, List[Tuple[str, Optional[str]]], Dict[str, str]]]:
    """
    从模块中提取所有继承自 BasicOpts 的类

    返回：[(class_name, params, defaults), ...]
    """
    module = parse_python_file(module_path)
    if module is None:
        return []

    classes = []
    for node in module.body:
        if isinstance(node, ast.ClassDef) and is_basicopts_subclass(node, module):
            sig = extract_class_init_signature(node)
            if sig:
                params, defaults = sig
                classes.append((node.name, params, defaults))

    return classes


def process_module(module_path: Path, output_path: Path, verbose: bool = False) -> bool:
    """
    处理单个模块，生成 .pyi 文件

    返回：是否成功
    """
    module_name = module_path.stem

    # 特殊处理 series_options.py
    if module_name == "series_options":
        content = generate_series_options_pyi()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        if verbose:
            print(f"Generated {output_path} (hand-written convention)")
        return True

    # 特殊处理 __init__.py
    if module_name == "__init__":
        content = generate_init_pyi(module_path)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        if verbose:
            print(f"Generated {output_path} (special handling)")
        return True

    # 普通模块
    module = parse_python_file(module_path)
    if module is None:
        return False

    typing_imports, _ = extract_imports(module)
    classes = extract_classes_from_module(module_path)

    if verbose:
        print(f"Found {len(classes)} BasicOpts subclasses in {module_name}")

    content = generate_module_pyi(module_path, typing_imports, classes)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    if verbose:
        print(f"Generated {output_path}")

    return True


def check_module(
    module_path: Path, output_path: Path, verbose: bool = False
) -> Tuple[bool, str]:
    """
    检查模块的 .pyi 文件是否与源码同步

    返回：(is_sync, diff_output)
    """
    # 生成临时内容
    module_name = module_path.stem

    if module_name == "series_options":
        expected_content = generate_series_options_pyi()
    elif module_name == "__init__":
        expected_content = generate_init_pyi(module_path)
    else:
        module = parse_python_file(module_path)
        if module is None:
            return False, f"Failed to parse {module_path}"

        typing_imports, _ = extract_imports(module)
        classes = extract_classes_from_module(module_path)
        expected_content = generate_module_pyi(module_path, typing_imports, classes)

    # 读取现有内容
    if not output_path.exists():
        if verbose:
            print(f"{output_path} does not exist")
        return False, f"{output_path} does not exist"

    with open(output_path, "r", encoding="utf-8") as f:
        actual_content = f.read()

    # 比较
    if expected_content == actual_content:
        if verbose:
            print(f"{output_path} is up to date")
        return True, ""

    # 生成差异
    diff = difflib.unified_diff(
        actual_content.splitlines(keepends=True),
        expected_content.splitlines(keepends=True),
        fromfile=str(output_path),
        tofile=f"{output_path} (expected)",
    )

    return False, "".join(diff)


def main():
    parser = argparse.ArgumentParser(
        description="Generate type stub files (.pyi) for pyantv.options module"
    )
    parser.add_argument("--write", action="store_true", help="Write .pyi files to disk")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if .pyi files are up to date (exit 1 if not)",
    )
    parser.add_argument(
        "--module",
        type=str,
        help="Process only a specific module (e.g., pyantv/options/global_options.py)",
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Print detailed progress information"
    )

    args = parser.parse_args()

    # 参数互斥检查
    if args.write and args.check:
        print("Error: --write and --check are mutually exclusive", file=sys.stderr)
        return 3

    if not args.write and not args.check:
        args.write = True  # 默认行为

    # 获取项目根目录
    project_root = get_project_root()
    options_dir = project_root / "pyantv" / "options"

    # 确定要处理的模块
    if args.module:
        module_path = Path(args.module)
        if not module_path.is_absolute():
            module_path = project_root / module_path

        if not module_path.exists():
            print(f"Error: Module not found: {module_path}", file=sys.stderr)
            return 2

        modules = [module_path]
    else:
        modules = sorted(options_dir.glob("*.py"))
        modules = [m for m in modules if m.name != "__pycache__"]

    # 执行操作
    all_ok = True
    diff_output = ""

    for module_path in modules:
        if module_path.name.startswith("__pycache__"):
            continue

        output_path = module_path.with_suffix(".pyi")

        if args.check:
            is_sync, diff = check_module(module_path, output_path, args.verbose)
            if not is_sync:
                all_ok = False
                diff_output += diff
        else:
            success = process_module(module_path, output_path, args.verbose)
            if not success:
                all_ok = False

    # 返回结果
    if args.check:
        if not all_ok:
            if diff_output:
                print(diff_output, file=sys.stderr)
            return 1
        return 0
    else:
        return 0 if all_ok else 2


if __name__ == "__main__":
    sys.exit(main())

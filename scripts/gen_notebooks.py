#!/usr/bin/env python
"""从 example/*.py 自动生成 Jupyter Notebook 文件。"""
import argparse
import ast
import json
import sys
from pathlib import Path


def parse_example_file(file_path):
    """解析 example 文件，提取 import 和核心代码。"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    tree = ast.parse(content)

    imports = []
    core_code = []

    for node in tree.body:
        # 提取 import 语句
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(f"import {alias.name}")
                if alias.asname:
                    imports[-1] += f" as {alias.asname}"
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                imports.append(f"from {module} import {alias.name}")
                if alias.asname:
                    imports[-1] += f" as {alias.asname}"
        # 提取核心代码（函数调用、赋值等）
        elif isinstance(node, (ast.Expr, ast.Assign, ast.FunctionDef)):
            try:
                code = ast.get_source_segment(content, node)
                if code:
                    core_code.append(code)
            except Exception:
                pass

    return imports, core_code


def generate_notebook(example_path, output_path, verbose=False):
    """生成 notebook 文件。"""
    imports, core_code = parse_example_file(example_path)

    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    # 添加标题 cell
    chart_name = (
        Path(example_path).stem.replace("_example", "").replace("_", " ").title()
    )
    notebook["cells"].append(
        {"cell_type": "markdown", "metadata": {}, "source": [f"# {chart_name}\n"]}
    )

    # 添加 pip install cell
    notebook["cells"].append(
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["!pip install pyantv"],
        }
    )

    # 添加 import cell
    if imports:
        notebook["cells"].append(
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": imports,
            }
        )

    # 添加核心代码 cell
    if core_code:
        notebook["cells"].append(
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": core_code,
            }
        )

    # 写入文件
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

    if verbose:
        print(f"Generated: {output_path}")
        print(f"  Imports: {len(imports)}")
        print(f"  Code lines: {len(core_code)}")

    return True


def check_notebook(example_path, notebook_path, verbose=False):
    """检查现有 notebook 是否与 example 一致。"""
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except Exception as e:
        if verbose:
            print(f"Failed to read {notebook_path}: {e}")
        return False

    imports, core_code = parse_example_file(example_path)

    # 检查代码 cell 数量
    code_cells = [c for c in existing.get("cells", []) if c.get("cell_type") == "code"]
    expected_code_cells = 2  # pip install + imports + core code

    if len(code_cells) < expected_code_cells:
        if verbose:
            print(
                f"Check failed: {notebook_path} has "
                f"{len(code_cells)} code cells, "
                f"expected at least {expected_code_cells}"
            )
        return False

    if verbose:
        print(f"Check passed: {notebook_path}")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate Jupyter notebooks from example/*.py files"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write generated notebooks to notebooks/ directory",
    )
    parser.add_argument(
        "--check", action="store_true", help="Check if existing notebooks match examples"
    )
    parser.add_argument(
        "--example", type=str, help="Process only the specified example file"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # 参数验证
    if not args.write and not args.check:
        print("Error: Must specify --write or --check", file=sys.stderr)
        return 3

    if args.write and args.check:
        print("Error: Cannot specify both --write and --check", file=sys.stderr)
        return 3

    # 确定示例目录和输出目录
    example_dir = Path("example")
    notebooks_dir = Path("notebooks")

    if not example_dir.exists():
        print(f"Error: {example_dir} directory not found", file=sys.stderr)
        return 2

    if args.write and not notebooks_dir.exists():
        notebooks_dir.mkdir(parents=True, exist_ok=True)

    # 扫描 example 文件
    example_files = []
    if args.example:
        example_path = Path(args.example)
        if not example_path.exists():
            print(f"Error: Example file {args.example} not found", file=sys.stderr)
            return 3
        example_files.append(example_path)
    else:
        example_files = sorted(example_dir.glob("*_example.py"))

    if not example_files:
        print("Error: No example files found", file=sys.stderr)
        return 2

    # 处理每个文件
    success_count = 0
    fail_count = 0

    for example_file in example_files:
        notebook_name = example_file.stem.replace("_example", "") + ".ipynb"
        notebook_path = notebooks_dir / notebook_name

        try:
            if args.write:
                if generate_notebook(example_file, notebook_path, args.verbose):
                    success_count += 1
                else:
                    fail_count += 1
            elif args.check:
                if check_notebook(example_file, notebook_path, args.verbose):
                    success_count += 1
                else:
                    fail_count += 1
        except Exception as e:
            if args.verbose:
                print(f"Error processing {example_file}: {e}")
            fail_count += 1

    # 输出结果
    if args.verbose:
        total = len(example_files)
        print(
            f"\nProcessed {total} files: "
            f"{success_count} success, {fail_count} failed"
        )

    if args.check and fail_count > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

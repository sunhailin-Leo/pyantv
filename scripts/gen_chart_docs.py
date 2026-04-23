#!/usr/bin/env python3
"""
Chart documentation generator for pyantv.

Generates markdown documentation for chart types by parsing Python source files
and matching with example code.

Usage:
    python scripts/gen_chart_docs.py --write    # Generate/update docs
    python scripts/gen_chart_docs.py --check    # Check if docs are up-to-date

Exit codes:
    0 - Success
    1 - Check mode detected differences
    2 - Parse failure
    3 - Invalid arguments
"""

import argparse
import ast
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class ChartDocGenerator:
    """Generate markdown documentation for chart classes."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.basic_charts_dir = project_root / "pyantv" / "charts" / "basic_charts"
        self.composition_charts_dir = (
            project_root / "pyantv" / "charts" / "composition_charts"
        )
        self.example_dir = project_root / "example"
        self.docs_charts_dir = project_root / "docs" / "charts"

    def parse_chart_class(self, file_path: Path) -> Optional[Dict]:
        """Parse a chart Python file and extract class information."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Check if it inherits from Chart
                    has_chart_base = False
                    for base in node.bases:
                        if isinstance(base, ast.Name) and base.id == "Chart":
                            has_chart_base = True
                            break
                        elif isinstance(base, ast.Attribute) and base.attr == "Chart":
                            has_chart_base = True
                            break

                    if has_chart_base:
                        docstring = ast.get_docstring(node)
                        overview = ""
                        config_items = []

                        if docstring:
                            lines = docstring.strip().split("\n")
                            overview_lines = []
                            in_config = False
                            for line in lines:
                                line = line.strip()
                                if line.startswith("配置项:") or line.startswith(
                                    "Configuration:"
                                ):
                                    in_config = True
                                    continue
                                if in_config:
                                    if line.startswith("-") or line.startswith("*"):
                                        config_items.append(line.lstrip("- *").strip())
                                    elif not line:
                                        continue
                                    else:
                                        break
                                else:
                                    if line:
                                        overview_lines.append(line)
                            overview = "\n".join(overview_lines)

                        return {
                            "name": node.name,
                            "file_name": file_path.stem,
                            "overview": overview,
                            "config_items": config_items,
                        }
        except Exception as e:
            print(f"Error parsing {file_path}: {e}", file=sys.stderr)
            return None

        return None

    def find_example_code(self, chart_name: str) -> Optional[str]:
        """Find example code for a chart type."""
        # Try multiple naming patterns
        patterns = [
            f"{chart_name.lower()}_example.py",
            f"{chart_name.lower()}_example.html",
        ]

        for pattern in patterns:
            example_file = self.example_dir / pattern
            if example_file.exists():
                try:
                    with open(example_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    # Return first 500 characters as preview
                    return content[:500]
                except Exception:
                    pass

        return None

    def generate_markdown(self, chart_info: Dict) -> str:
        """Generate markdown content for a chart."""
        name = chart_info["name"]
        overview = chart_info.get("overview", "暂无描述")
        config_items = chart_info.get("config_items", [])

        md = f"""# {name}

## 概述

{overview}

## 配置项

"""

        if config_items:
            for item in config_items:
                md += f"- {item}\n"
        else:
            md += "暂无配置项说明\n"

        md += """
## 示例

```python
"""

        example_code = self.find_example_code(name)
        if example_code:
            md += example_code
        else:
            md += "# 示例代码暂未添加\n"

        md += """```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)
"""
        return md

    def discover_charts(self) -> List[Dict]:
        """Discover all chart classes in the codebase."""
        charts = []

        # Parse basic_charts directory
        if self.basic_charts_dir.exists():
            for py_file in sorted(self.basic_charts_dir.glob("*.py")):
                if py_file.name == "__init__.py":
                    continue
                chart_info = self.parse_chart_class(py_file)
                if chart_info:
                    charts.append(chart_info)

        # Parse composition_charts directory for geo_view
        if self.composition_charts_dir.exists():
            geo_view_file = self.composition_charts_dir / "geo_view.py"
            if geo_view_file.exists():
                chart_info = self.parse_chart_class(geo_view_file)
                if chart_info:
                    charts.append(chart_info)

        return charts

    def generate_docs(self, write: bool = False) -> Tuple[int, List[str]]:
        """Generate documentation for all charts."""
        charts = self.discover_charts()

        if not charts:
            print("No charts found!", file=sys.stderr)
            return 2, []

        # Ensure docs/charts directory exists
        self.docs_charts_dir.mkdir(parents=True, exist_ok=True)

        generated_files = []
        differences = []

        for chart_info in charts:
            file_name = f"{chart_info['file_name']}.md"
            output_path = self.docs_charts_dir / file_name

            content = self.generate_markdown(chart_info)

            if write:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(content)
                generated_files.append(file_name)
            else:
                # Check mode: compare with existing file
                if output_path.exists():
                    with open(output_path, "r", encoding="utf-8") as f:
                        existing_content = f.read()
                    if existing_content != content:
                        differences.append(file_name)
                else:
                    differences.append(file_name)

        if differences:
            return 1, differences
        return 0, generated_files


def main():
    parser = argparse.ArgumentParser(
        description="Generate chart documentation for pyantv"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--write", action="store_true", help="Write generated documentation to disk"
    )
    group.add_argument(
        "--check", action="store_true", help="Check if documentation is up-to-date"
    )

    args = parser.parse_args()

    # Get project root (assuming script is in scripts/ directory)
    project_root = Path(__file__).parent.parent

    generator = ChartDocGenerator(project_root)

    exit_code, result = generator.generate_docs(write=args.write)

    if args.write:
        print(f"Generated {len(result)} chart documentation files:")
        for f in sorted(result):
            print(f"  - docs/charts/{f}")
    elif args.check:
        if exit_code == 0:
            print("All documentation is up-to-date.")
        else:
            print(f"Documentation is out-of-date for {len(result)} files:")
            for f in sorted(result):
                print(f"  - docs/charts/{f}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()

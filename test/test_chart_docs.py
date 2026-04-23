"""
Tests for chart documentation generator.

This module tests the functionality of the gen_chart_docs.py script,
including check mode, file existence, and content validation.
"""

import subprocess
import sys
from pathlib import Path


class TestChartDocs:
    """Test suite for chart documentation generation."""

    @staticmethod
    def get_project_root() -> Path:
        """Get the project root directory."""
        return Path(__file__).parent.parent

    @staticmethod
    def get_docs_charts_dir() -> Path:
        """Get the docs/charts directory."""
        return TestChartDocs.get_project_root() / "docs" / "charts"

    @staticmethod
    def get_gen_script_path() -> Path:
        """Get the path to the gen_chart_docs.py script."""
        return TestChartDocs.get_project_root() / "scripts" / "gen_chart_docs.py"

    @staticmethod
    def get_expected_chart_files() -> list:
        """Get the list of expected chart documentation files."""
        return [
            "arc.md",
            "area.md",
            "beeswarm.md",
            "box.md",
            "boxplot.md",
            "cell.md",
            "chord.md",
            "connector.md",
            "density.md",
            "force_graph.md",
            "funnel.md",
            "gauge.md",
            "geo_path.md",
            "geo_view.md",
            "heatmap.md",
            "image.md",
            "interval.md",
            "interval3d.md",
            "line.md",
            "line3d.md",
            "link.md",
            "liquid.md",
            "pack.md",
            "partition.md",
            "path.md",
            "point.md",
            "point3d.md",
            "polygon.md",
            "range.md",
            "rect.md",
            "sankey.md",
            "shape.md",
            "text.md",
            "tree.md",
            "treemap.md",
            "vector.md",
            "waterfall.md",
            "wordcloud.md",
        ]

    def test_check_mode_consistency(self):
        """Test that --check mode returns 0 when docs are up-to-date."""
        script_path = self.get_gen_script_path()
        result = subprocess.run(
            [sys.executable, str(script_path), "--check"], capture_output=True, text=True
        )
        assert result.returncode == 0, (
            f"Check mode should return 0 when docs are up-to-date. "
            f"Got return code {result.returncode}. "
            f"stdout: {result.stdout}, stderr: {result.stderr}"
        )
        print("✓ Test --check mode consistency: PASSED")

    def test_index_md_exists(self):
        """Test that docs/charts/index.md exists."""
        index_path = self.get_docs_charts_dir() / "index.md"
        assert (
            index_path.exists()
        ), f"docs/charts/index.md should exist but was not found at {index_path}"
        print("✓ Test index.md exists: PASSED")

    def test_chart_files_exist(self):
        """Test that all expected chart .md files exist."""
        docs_dir = self.get_docs_charts_dir()
        expected_files = self.get_expected_chart_files()

        missing_files = []
        for filename in expected_files:
            file_path = docs_dir / filename
            if not file_path.exists():
                missing_files.append(filename)

        assert (
            not missing_files
        ), "The following chart documentation files " "are missing: {}".format(
            missing_files
        )
        count = len(expected_files)
        print("✓ Test all {} chart files exist: PASSED".format(count))

    def test_chart_files_have_h2_sections(self):
        """Test that each chart .md file has at least 4 h2 sections."""
        docs_dir = self.get_docs_charts_dir()
        expected_files = self.get_expected_chart_files()

        insufficient_files = []
        for filename in expected_files:
            file_path = docs_dir / filename
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Count h2 sections (##)
            h2_count = content.count("## ")
            if h2_count < 4:
                insufficient_files.append((filename, h2_count))

        assert (
            not insufficient_files
        ), "The following files have fewer than 4 " "h2 sections: {}".format(
            insufficient_files
        )
        print("✓ Test chart files have ≥4 h2 sections: PASSED")

    def test_index_md_content(self):
        """Test that index.md contains expected sections."""
        index_path = self.get_docs_charts_dir() / "index.md"
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()

        expected_sections = [
            "统计图表",
            "分布图",
            "关系图",
            "地理图",
            "特殊图",
            "3D 图表",
            "组合图表",
            "基础标记",
        ]

        missing_sections = []
        for section in expected_sections:
            if section not in content:
                missing_sections.append(section)

        assert (
            not missing_sections
        ), f"index.md is missing expected sections: {missing_sections}"
        print("✓ Test index.md contains all expected sections: PASSED")

    def test_index_no_pie_chart(self):
        """Test that index.md does not contain pie chart reference."""
        index_path = self.get_docs_charts_dir() / "index.md"
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read().lower()

        # Check that "pie" is not mentioned as a standalone chart
        # Allow "pie" in comments or as part of other words
        assert "pie.md" not in content, (
            "index.md should not contain pie.md reference "
            "(pie is not an independent class)"
        )
        print("✓ Test index.md does not contain pie chart: PASSED")

    def run_all_tests(self):
        """Run all tests and report results."""
        tests = [
            ("Check mode consistency", self.test_check_mode_consistency),
            ("index.md exists", self.test_index_md_exists),
            ("Chart files exist", self.test_chart_files_exist),
            ("Chart files have h2 sections", self.test_chart_files_have_h2_sections),
            ("index.md content", self.test_index_md_content),
            ("No pie chart in index", self.test_index_no_pie_chart),
        ]

        passed = 0
        failed = 0

        print("\n" + "=" * 60)
        print("Running Chart Documentation Tests")
        print("=" * 60 + "\n")

        for test_name, test_func in tests:
            try:
                test_func()
                passed += 1
            except AssertionError as e:
                print(f"✗ Test {test_name}: FAILED")
                print(f"  Error: {e}")
                failed += 1
            except Exception as e:
                print(f"✗ Test {test_name}: ERROR")
                print(f"  Unexpected error: {e}")
                failed += 1

        print("\n" + "=" * 60)
        print(f"Test Results: {passed} passed, {failed} failed")
        print("=" * 60 + "\n")

        return failed == 0


def main():
    """Main entry point for running tests."""
    tester = TestChartDocs()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

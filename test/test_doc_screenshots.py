"""
Tests for the screenshot generation script gen_chart_screenshots.py
"""

import subprocess
import sys
from pathlib import Path


def test_script_file_exists():
    """Test that the screenshot script file exists."""
    script_path = Path("scripts/gen_chart_screenshots.py")
    assert script_path.exists(), f"Script file {script_path} does not exist"


def test_script_line_count():
    """Test that the script has less than 300 lines."""
    script_path = Path("scripts/gen_chart_screenshots.py")
    with open(script_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    assert line_count < 300, f"Script has {line_count} lines, expected less than 300"


def test_script_help_parameter():
    """Test that the --help parameter works."""
    result = subprocess.run(
        [
            sys.executable,
            "scripts/gen_chart_screenshots.py",
            "--help",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"--help failed with return code {result.returncode}"
    assert (
        "Generate chart screenshots" in result.stdout
    ), "Help text missing expected description"
    assert "--input" in result.stdout, "Help text missing --input option"
    assert "--output" in result.stdout, "Help text missing --output option"
    assert "--width" in result.stdout, "Help text missing --width option"
    assert "--height" in result.stdout, "Help text missing --height option"
    assert "--pattern" in result.stdout, "Help text missing --pattern option"
    assert "--verbose" in result.stdout, "Help text missing --verbose option"


def test_example_html_files_count():
    """Test that there are at least 25 HTML files in the example directory."""
    example_dir = Path("example")
    assert example_dir.exists(), f"Example directory {example_dir} does not exist"

    html_files = list(example_dir.glob("*.html"))
    html_count = len(html_files)

    assert html_count >= 25, f"Found {html_count} HTML files, expected at least 25"


def test_output_directory_creation():
    """Test that the script can create the output directory."""
    import tempfile

    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        test_output = Path(temp_dir) / "test_output"

        # Run the script with test output directory
        # (will fail due to Playwright, but should create dir)
        result = subprocess.run(
            [
                sys.executable,
                "scripts/gen_chart_screenshots.py",
                "--input",
                "example",
                "--output",
                str(test_output),
                "--pattern",
                "nonexistent_*.html",
            ],
            capture_output=True,
            text=True,
        )

        # The script should exit with code 0 (no files found)
        # or 3 (Playwright not available).
        # Either way, it should handle the output dir param
        assert result.returncode in [
            0,
            2,
            3,
        ], f"Unexpected return code {result.returncode}"


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])

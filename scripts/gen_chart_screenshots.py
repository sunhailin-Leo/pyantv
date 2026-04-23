#!/usr/bin/env python3
"""
Generate chart screenshots from example HTML files using Playwright.

This script scans the example/ directory for *_example.html files and
generates PNG screenshots using Playwright's headless Chromium browser.
"""

import argparse
import sys
from pathlib import Path


def check_playwright_available():
    """Check if Playwright is installed and available."""
    try:
        __import__("playwright.sync_api")
        return True
    except ImportError:
        return False


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate chart screenshots from example HTML files"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="example",
        help="Input directory containing HTML files (default: example)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="docs/assets/charts",
        help="Output directory for PNG screenshots (default: docs/assets/charts)",
    )
    parser.add_argument(
        "--width", type=int, default=800, help="Viewport width in pixels (default: 800)"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=600,
        help="Viewport height in pixels (default: 600)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="*_example.html",
        help="File pattern to match (default: *_example.html)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def find_html_files(input_dir, pattern):
    """Find HTML files matching the pattern."""
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist", file=sys.stderr)
        sys.exit(2)

    html_files = sorted(input_path.glob(pattern))
    return html_files


def generate_screenshot(html_file, output_path, width, height, verbose):
    """Generate a screenshot for a single HTML file."""
    try:
        from playwright.sync_api import sync_playwright

        # Read HTML content
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Skip empty or whitespace-only files
        if not html_content.strip():
            if verbose:
                print(f"Skipping empty file: {html_file.name}")
            return False

        # Generate screenshot
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})
            page.set_content(html_content, wait_until="networkidle")

            # Wait a bit for any animations
            page.wait_for_timeout(1000)

            # Create output directory if needed
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Take screenshot
            page.screenshot(path=str(output_path))
            browser.close()

            if verbose:
                print(f"Generated: {output_path}")
            return True

    except Exception as e:
        print(f"Error processing {html_file.name}: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point."""
    # Check Playwright availability
    if not check_playwright_available():
        print(
            "Error: Playwright is not installed. Please install it with:",
            file=sys.stderr,
        )
        print("  pip install playwright", file=sys.stderr)
        print("  playwright install chromium", file=sys.stderr)
        sys.exit(3)

    # Parse arguments
    args = parse_args()

    # Find HTML files
    html_files = find_html_files(args.input, args.pattern)

    if not html_files:
        print(f"No HTML files found matching pattern '{args.pattern}' in '{args.input}'")
        sys.exit(0)

    if args.verbose:
        print(f"Found {len(html_files)} HTML files")

    # Generate screenshots
    success_count = 0
    failure_count = 0

    for html_file in html_files:
        # Generate output filename
        chart_name = html_file.stem  # Remove .html extension
        output_path = Path(args.output) / f"{chart_name}.png"

        # Generate screenshot
        if generate_screenshot(
            html_file, output_path, args.width, args.height, args.verbose
        ):
            success_count += 1
        else:
            failure_count += 1

    # Summary
    if args.verbose:
        print(f"\nSummary: {success_count} succeeded, {failure_count} failed")

    # Exit with appropriate code
    if failure_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

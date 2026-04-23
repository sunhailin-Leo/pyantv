"""
Performance benchmark tests for pyantv rendering operations.

Uses real pyantv API calls (Line chart) to measure set_data,
dump_options, and render_embed performance across various data sizes.
"""

import argparse
import json
import os
import time
from typing import Any, Dict, List

from pyantv import Line
from pyantv.data.pipeline import downsample


def generate_data(count: int) -> List[Dict[str, Any]]:
    """
    Generate test data for benchmarking.

    Args:
        count: Number of data points to generate

    Returns:
        List of dictionaries with test data
    """
    return [
        {
            "date": f"2024-01-{i % 30 + 1:02d}",
            "value": i * 10,
            "category": f"cat_{i % 5}",
        }
        for i in range(count)
    ]


def benchmark_set_data(data_sizes: List[int]) -> Dict[int, float]:
    """
    Benchmark set_data operation using real pyantv Line chart.

    Args:
        data_sizes: List of data sizes to test

    Returns:
        Dictionary mapping data size to execution time in seconds
    """
    results: Dict[int, float] = {}
    for size in data_sizes:
        data = generate_data(size)
        start_time = time.time()
        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")
        end_time = time.time()
        results[size] = end_time - start_time
    return results


def benchmark_dump_options(data_sizes: List[int]) -> Dict[int, float]:
    """
    Benchmark dump_options operation using real pyantv Line chart.

    Args:
        data_sizes: List of data sizes to test

    Returns:
        Dictionary mapping data size to execution time in seconds
    """
    results: Dict[int, float] = {}
    for size in data_sizes:
        data = generate_data(size)
        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")
        start_time = time.time()
        _ = chart.dump_options()
        end_time = time.time()
        results[size] = end_time - start_time
    return results


def benchmark_render_embed(data_sizes: List[int]) -> Dict[int, float]:
    """
    Benchmark render_embed operation using real pyantv Line chart.

    Args:
        data_sizes: List of data sizes to test

    Returns:
        Dictionary mapping data size to execution time in seconds
    """
    results: Dict[int, float] = {}
    for size in data_sizes:
        data = generate_data(size)
        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")
        start_time = time.time()
        _ = chart.render_embed()
        end_time = time.time()
        results[size] = end_time - start_time
    return results


def benchmark_html_size(data_sizes: List[int]) -> Dict[int, int]:
    """
    Benchmark HTML size for different data sizes.

    Args:
        data_sizes: List of data sizes to test

    Returns:
        Dictionary mapping data size to HTML size in bytes
    """
    results: Dict[int, int] = {}
    for size in data_sizes:
        data = generate_data(size)
        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")
        html = chart.render_embed()
        results[size] = len(html)
    return results


def benchmark_compact_vs_pretty(data_sizes: List[int]) -> Dict[int, Dict[str, Any]]:
    """
    Benchmark HTML size reduction with compact mode.

    Args:
        data_sizes: List of data sizes to test

    Returns:
        Dictionary mapping data size to size reduction metrics
    """
    results: Dict[int, Dict[str, Any]] = {}
    for size in data_sizes:
        data = generate_data(size)
        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")

        html_pretty = chart.render_embed(compact=False)
        html_compact = chart.render_embed(compact=True)

        size_reduction = (len(html_pretty) - len(html_compact)) / len(html_pretty)
        results[size] = {
            "pretty_size": len(html_pretty),
            "compact_size": len(html_compact),
            "reduction_ratio": size_reduction,
        }
    return results


def benchmark_downsample(data_size: int, max_points: int) -> float:
    """
    Benchmark downsample operation.

    Args:
        data_size: Original data size
        max_points: Target max points after downsampling

    Returns:
        Execution time in seconds
    """
    data = generate_data(data_size)
    start_time = time.time()
    downsample(
        data=data,
        max_points=max_points,
        method="lttb",
        x_field="date",
        y_field="value",
    )
    end_time = time.time()
    return end_time - start_time


def run_all() -> None:
    """
    Run all benchmark tests and print results.
    Tests with data sizes: 100, 1000, 10000, 100000
    """
    data_sizes = [100, 1000, 10000, 100000]

    print("=== Performance Benchmarks ===\n")

    print("set_data benchmark:")
    set_data_results = benchmark_set_data(data_sizes)
    for size, elapsed in set_data_results.items():
        print(f"  {size} items: {elapsed:.4f}s")

    print("\ndump_options benchmark:")
    dump_results = benchmark_dump_options(data_sizes)
    for size, elapsed in dump_results.items():
        print(f"  {size} items: {elapsed:.4f}s")

    print("\nrender_embed benchmark:")
    render_results = benchmark_render_embed(data_sizes)
    for size, elapsed in render_results.items():
        print(f"  {size} items: {elapsed:.4f}s")

    print("\n=== HTML Size Benchmarks ===\n")

    print("HTML size benchmark:")
    html_size_results = benchmark_html_size(data_sizes)
    for size, size_bytes in html_size_results.items():
        print(f"  {size} items: {size_bytes:,} bytes")

    print("\nCompact vs Pretty benchmark:")
    compact_results = benchmark_compact_vs_pretty(data_sizes)
    for size, metrics in compact_results.items():
        print(f"  {size} items:")
        print(f"    Pretty: {metrics['pretty_size']:,} bytes")
        print(f"    Compact: {metrics['compact_size']:,} bytes")
        print(f"    Reduction: {metrics['reduction_ratio']:.2%}")

    print("\n=== Downsample Benchmarks ===\n")

    print("LTTB 100k to 1k:")
    lttb_time = benchmark_downsample(100000, 1000)
    print(f"  Time: {lttb_time:.4f}s ({lttb_time * 1000:.2f}ms)")


def save_baseline(output_path: str = "benchmarks/baselines/baseline.json") -> None:
    """
    Save benchmark results to baseline file.

    Args:
        output_path: Path to save baseline JSON
    """
    data_sizes = [100, 1000, 10000, 100000]

    baseline = {
        "set_data": benchmark_set_data(data_sizes),
        "dump_options": benchmark_dump_options(data_sizes),
        "render_embed": benchmark_render_embed(data_sizes),
        "html_size": benchmark_html_size(data_sizes),
        "compact_vs_pretty": benchmark_compact_vs_pretty(data_sizes),
        "downsample_lttb_100k_to_1k": benchmark_downsample(100000, 1000),
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(baseline, f, indent=2)

    print(f"Baseline saved to {output_path}")


def compare_baseline(baseline_path: str = "benchmarks/baselines/baseline.json") -> None:
    """
    Compare current benchmark results with baseline.

    Args:
        baseline_path: Path to baseline JSON file
    """
    if not os.path.exists(baseline_path):
        print(f"Baseline file not found: {baseline_path}")
        return

    with open(baseline_path, "r") as f:
        baseline = json.load(f)

    data_sizes = [100, 1000, 10000, 100000]

    print("=== Baseline Comparison ===\n")

    current_set_data = benchmark_set_data(data_sizes)
    baseline_set_data = baseline.get("set_data", {})

    print("set_data comparison:")
    for size in data_sizes:
        if size in baseline_set_data:
            current = current_set_data[size]
            baseline_val = baseline_set_data[size]
            change = (current - baseline_val) / baseline_val
            print(
                f"  {size} items: {current:.4f}s"
                f" (baseline: {baseline_val:.4f}s,"
                f" change: {change:+.2%})"
            )
            if abs(change) > 0.2:
                print("    ⚠️  WARNING: Performance regression > 20%")

    current_dump = benchmark_dump_options(data_sizes)
    baseline_dump = baseline.get("dump_options", {})

    print("\ndump_options comparison:")
    for size in data_sizes:
        if size in baseline_dump:
            current = current_dump[size]
            baseline_val = baseline_dump[size]
            change = (current - baseline_val) / baseline_val
            print(
                f"  {size} items: {current:.4f}s"
                f" (baseline: {baseline_val:.4f}s,"
                f" change: {change:+.2%})"
            )
            if abs(change) > 0.2:
                print("    ⚠️  WARNING: Performance regression > 20%")

    current_downsample = benchmark_downsample(100000, 1000)
    baseline_downsample = baseline.get("downsample_lttb_100k_to_1k")

    print("\nLTTB 100k to 1k comparison:")
    if baseline_downsample:
        change = (
            (current_downsample - baseline_downsample)
            / baseline_downsample
        )
        print(f"  Current: {current_downsample:.4f}s")
        print(f"  Baseline: {baseline_downsample:.4f}s")
        print(f"  Change: {change:+.2%}")
        if abs(change) > 0.2:
            print("    ⚠️  WARNING: Performance regression > 20%")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="pyantv performance benchmarks")
    parser.add_argument(
        "--save-baseline",
        action="store_true",
        help="Save benchmark results to baseline file",
    )
    parser.add_argument(
        "--compare-baseline",
        action="store_true",
        help="Compare current results with baseline",
    )
    parser.add_argument(
        "--baseline-path",
        type=str,
        default="benchmarks/baselines/baseline.json",
        help="Path to baseline JSON file",
    )

    args = parser.parse_args()

    if args.save_baseline:
        save_baseline(args.baseline_path)
    elif args.compare_baseline:
        compare_baseline(args.baseline_path)
    else:
        run_all()

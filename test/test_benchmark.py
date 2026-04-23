"""
Tests for the benchmark module with real pyantv API calls.
"""

import time

from benchmarks.bench_render import (
    generate_data,
    benchmark_set_data,
    benchmark_dump_options,
    benchmark_render_embed,
)


def test_generate_data():
    """Test that generate_data creates the correct number of items."""
    data = generate_data(10)
    assert len(data) == 10


def test_generate_data_format():
    """Test that generated data has the correct format."""
    data = generate_data(5)
    assert all("date" in item for item in data)
    assert all("value" in item for item in data)
    assert all("category" in item for item in data)
    assert data[0]["value"] == 0
    assert data[1]["value"] == 10


def test_benchmark_set_data_small():
    """Test set_data benchmark with small data using real pyantv API."""
    results = benchmark_set_data([100])
    assert 100 in results
    assert results[100] >= 0


def test_benchmark_dump_options_small():
    """Test dump_options benchmark with small data using real pyantv API."""
    results = benchmark_dump_options([100])
    assert 100 in results
    assert results[100] >= 0


def test_benchmark_render_embed_small():
    """Test render_embed benchmark with small data using real pyantv API."""
    results = benchmark_render_embed([100])
    assert 100 in results
    assert results[100] >= 0


def test_large_data_set_data():
    """Test that set_data with 10K data completes within 5 seconds."""
    from pyantv import Line

    data = generate_data(10000)
    start_time = time.time()
    chart = Line()
    chart.set_data(data=data)
    chart.set_encode(x_field_name="date", y_field_name="value")
    elapsed = time.time() - start_time
    assert elapsed < 5.0

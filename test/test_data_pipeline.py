"""Tests for pyantv.data.pipeline module."""

import pytest

from pyantv.data.pipeline import (
    bin_data,
    aggregate,
    sample,
    pivot,
    normalize,
)


class TestBinData:
    """Tests for bin_data function."""

    def test_bin_data_basic(self):
        """Test basic binning functionality."""
        data = [{"value": i} for i in range(1, 11)]
        result = bin_data(data, "value", bins=2)
        assert len(result) == 10
        assert "bin" in result[0]
        assert result[0]["bin"] == "[1.0, 5.5)"
        assert result[9]["bin"] == "[5.5, 10.0)"

    def test_bin_data_empty_raises(self):
        """Test that empty data raises ValueError."""
        with pytest.raises(ValueError, match="data cannot be empty"):
            bin_data([], "value")

    def test_bin_data_missing_field_raises(self):
        """Test that missing field raises ValueError."""
        data = [{"value": 1}]
        with pytest.raises(ValueError, match="field 'x' does not exist"):
            bin_data(data, "x")

    def test_bin_data_non_numerical_raises(self):
        """Test that non-numerical field raises ValueError."""
        data = [{"value": "not a number"}]
        with pytest.raises(ValueError, match="must contain numerical"):
            bin_data(data, "value")


class TestAggregate:
    """Tests for aggregate function."""

    def test_aggregate_sum(self):
        """Test sum aggregation."""
        data = [
            {"category": "A", "value": 10},
            {"category": "A", "value": 20},
            {"category": "B", "value": 30},
        ]
        result = aggregate(data, "category", "value", "sum")
        assert len(result) == 2
        assert result[0] == {"category": "A", "value": 30}
        assert result[1] == {"category": "B", "value": 30}

    def test_aggregate_mean(self):
        """Test mean aggregation."""
        data = [
            {"category": "A", "value": 10},
            {"category": "A", "value": 20},
            {"category": "B", "value": 30},
        ]
        result = aggregate(data, "category", "value", "mean")
        assert len(result) == 2
        assert result[0]["value"] == 15.0
        assert result[1]["value"] == 30.0

    def test_aggregate_count(self):
        """Test count aggregation."""
        data = [
            {"category": "A", "value": 10},
            {"category": "A", "value": 20},
            {"category": "B", "value": 30},
        ]
        result = aggregate(data, "category", "value", "count")
        assert len(result) == 2
        assert result[0]["value"] == 2
        assert result[1]["value"] == 1

    def test_aggregate_invalid_method(self):
        """Test that invalid method raises ValueError."""
        data = [{"category": "A", "value": 10}]
        with pytest.raises(ValueError, match="method must be one of"):
            aggregate(data, "category", "value", "invalid")


class TestSample:
    """Tests for sample function."""

    def test_sample_by_n(self):
        """Test sampling by number."""
        data = [{"value": i} for i in range(10)]
        result = sample(data, n=3, seed=42)
        assert len(result) == 3
        assert len(set(r["value"] for r in result)) == 3

    def test_sample_by_fraction(self):
        """Test sampling by fraction."""
        data = [{"value": i} for i in range(10)]
        result = sample(data, fraction=0.5, seed=42)
        assert len(result) == 5

    def test_sample_no_args_raises(self):
        """Test that missing both n and fraction raises ValueError."""
        data = [{"value": 1}]
        with pytest.raises(ValueError, match="Either n or fraction must be"):
            sample(data)


class TestPivot:
    """Tests for pivot function."""

    def test_pivot_basic(self):
        """Test basic pivot functionality."""
        data = [
            {"date": "2024-01", "category": "A", "value": 10},
            {"date": "2024-01", "category": "B", "value": 20},
            {"date": "2024-02", "category": "A", "value": 30},
        ]
        result = pivot(data, "date", "category", "value")
        assert len(result) == 2
        assert result[0] == {"date": "2024-01", "A": 10, "B": 20}
        assert result[1] == {"date": "2024-02", "A": 30}


class TestNormalize:
    """Tests for normalize function."""

    def test_normalize_min_max(self):
        """Test min-max normalization."""
        data = [{"value": i} for i in range(1, 11)]
        result = normalize(data, "value", method="min-max")
        assert result[0]["value"] == 0.0
        assert result[9]["value"] == 1.0

    def test_normalize_z_score(self):
        """Test z-score normalization."""
        data = [{"value": 1}, {"value": 2}, {"value": 3}]
        result = normalize(data, "value", method="z-score")
        assert abs(result[1]["value"]) < 0.001  # Mean should be ~0

    def test_normalize_invalid_method(self):
        """Test that invalid method raises ValueError."""
        data = [{"value": 1}]
        with pytest.raises(ValueError, match="method must be one of"):
            normalize(data, "value", method="invalid")


# --- 覆盖率补齐测试 ---


class TestBinDataEdgeCases:
    """Test edge cases for bin_data function."""

    def test_bin_data_equal_values(self):
        """所有值相同时的分箱。"""
        data = [{"v": 5}, {"v": 5}, {"v": 5}]
        result = bin_data(data, "v", bins=3)
        assert len(result) == 3
        # 所有值相同，应该都在同一个 bin
        assert all(r["bin"] is not None for r in result)

    def test_bin_data_with_none_values(self):
        """数据中包含 None 值。"""
        data = [{"v": 1}, {"v": None}, {"v": 10}]
        with pytest.raises(ValueError, match="must contain numerical"):
            bin_data(data, "v", bins=2)

    def test_bin_data_last_bin_inclusive(self):
        """最后一个 bin 包含最大值。"""
        data = [{"v": i} for i in range(10)]
        result = bin_data(data, "v", bins=5)
        last = result[-1]
        assert last["bin"] is not None

    def test_bin_data_not_list_raises(self):
        """非 list 数据抛出 TypeError。"""
        with pytest.raises(TypeError, match="data must be a list"):
            bin_data("not a list", "v")

    def test_bin_data_non_numerical_field(self):
        """非数值字段抛出异常。"""
        data = [{"v": "a"}, {"v": "b"}]
        with pytest.raises(ValueError, match="must contain numerical"):
            bin_data(data, "v", bins=2)


class TestAggregateEdgeCases:
    """Test edge cases for aggregate function."""

    def test_aggregate_min(self):
        """测试 min 聚合。"""
        data = [
            {"g": "A", "v": 10},
            {"g": "A", "v": 20},
        ]
        result = aggregate(data, "g", "v", "min")
        assert result[0]["v"] == 10

    def test_aggregate_max(self):
        """测试 max 聚合。"""
        data = [
            {"g": "A", "v": 10},
            {"g": "A", "v": 20},
        ]
        result = aggregate(data, "g", "v", "max")
        assert result[0]["v"] == 20

    def test_aggregate_not_list_raises(self):
        """非 list 数据抛出 TypeError。"""
        with pytest.raises(TypeError, match="data must be a list"):
            aggregate("not list", "g", "v")

    def test_aggregate_missing_group_field(self):
        """分组字段不存在抛出 ValueError。"""
        data = [{"v": 10}]
        with pytest.raises(ValueError, match="does not exist"):
            aggregate(data, "g", "v")

    def test_aggregate_missing_value_field(self):
        """值字段不存在抛出 ValueError。"""
        data = [{"g": "A"}]
        with pytest.raises(ValueError, match="does not exist"):
            aggregate(data, "g", "v")

    def test_aggregate_empty_raises(self):
        """空数据抛出 ValueError。"""
        with pytest.raises(ValueError, match="data cannot be empty"):
            aggregate([], "g", "v")


class TestSampleEdgeCases:
    """Test edge cases for sample function."""

    def test_sample_with_fraction(self):
        """按比例采样。"""
        data = [{"v": i} for i in range(100)]
        result = sample(data, fraction=0.1, seed=42)
        assert len(result) == 10

    def test_sample_not_list_raises(self):
        """非 list 数据抛出 TypeError。"""
        with pytest.raises(TypeError, match="data must be a list"):
            sample("not list", n=5)

    def test_sample_with_seed(self):
        """使用种子的可重复采样。"""
        data = [{"v": i} for i in range(50)]
        r1 = sample(data, n=5, seed=123)
        r2 = sample(data, n=5, seed=123)
        assert r1 == r2

    def test_sample_n_larger_than_data(self):
        """n 大于数据量时返回全部。"""
        data = [{"v": i} for i in range(5)]
        result = sample(data, n=100)
        assert len(result) == 5


class TestPivotEdgeCases:
    """Test edge cases for pivot function."""

    def test_pivot_not_list_raises(self):
        """非 list 数据抛出 TypeError。"""
        with pytest.raises(TypeError, match="data must be a list"):
            pivot("not list", "idx", "col", "val")

    def test_pivot_empty_raises(self):
        """空数据抛出 ValueError。"""
        with pytest.raises(ValueError, match="data cannot be empty"):
            pivot([], "idx", "col", "val")


class TestNormalizeEdgeCases:
    """Test edge cases for normalize function."""

    def test_normalize_equal_values_min_max(self):
        """所有值相同时 min-max 归一化。"""
        data = [{"v": 5}, {"v": 5}, {"v": 5}]
        result = normalize(data, "v", method="min-max")
        assert all(r["v"] == 0.0 for r in result)

    def test_normalize_equal_values_z_score(self):
        """所有值相同时 z-score 归一化。"""
        data = [{"v": 5}, {"v": 5}, {"v": 5}]
        result = normalize(data, "v", method="z-score")
        assert all(r["v"] == 0.0 for r in result)

    def test_normalize_with_output_field(self):
        """指定输出字段名。"""
        data = [{"v": 10}, {"v": 20}]
        result = normalize(data, "v", output_field="v_norm")
        assert "v_norm" in result[0]
        assert "v" in result[0]  # 原字段保留

    def test_normalize_not_list_raises(self):
        """非 list 数据抛出 TypeError。"""
        with pytest.raises(TypeError, match="data must be a list"):
            normalize("not list", "v")

    def test_normalize_empty_raises(self):
        """空数据抛出 ValueError。"""
        with pytest.raises(ValueError, match="data cannot be empty"):
            normalize([], "v")

    def test_normalize_missing_field(self):
        """字段不存在时抛出 ValueError。"""
        data = [{"x": 1}]
        with pytest.raises(ValueError, match="does not exist"):
            normalize(data, "v")

    def test_normalize_non_numerical_field(self):
        """非数值字段抛出 ValueError。"""
        data = [{"v": "abc"}, {"v": "def"}]
        with pytest.raises(ValueError, match="numerical"):
            normalize(data, "v")


class TestSampleMoreEdgeCases:
    """sample 函数的更多边界测试。"""

    def test_sample_both_n_and_fraction_raises(self):
        """同时指定 n 和 fraction 抛出 ValueError。"""
        data = [{"v": i} for i in range(10)]
        with pytest.raises(ValueError, match="both"):
            sample(data, n=5, fraction=0.5)

    def test_sample_negative_n_raises(self):
        """n 为负数抛出 ValueError。"""
        data = [{"v": i} for i in range(10)]
        with pytest.raises(ValueError, match="positive"):
            sample(data, n=-1)

    def test_sample_zero_n_raises(self):
        """n 为 0 抛出 ValueError。"""
        data = [{"v": i} for i in range(10)]
        with pytest.raises(ValueError, match="positive"):
            sample(data, n=0)

    def test_sample_fraction_zero_raises(self):
        """fraction 为 0 抛出 ValueError。"""
        data = [{"v": i} for i in range(10)]
        with pytest.raises(ValueError, match="fraction"):
            sample(data, fraction=0)

    def test_sample_fraction_negative_raises(self):
        """fraction 为负数抛出 ValueError。"""
        data = [{"v": i} for i in range(10)]
        with pytest.raises(ValueError, match="fraction"):
            sample(data, fraction=-0.5)

    def test_sample_fraction_over_one_raises(self):
        """fraction 大于 1 抛出 ValueError。"""
        data = [{"v": i} for i in range(10)]
        with pytest.raises(ValueError, match="fraction"):
            sample(data, fraction=1.5)

    def test_sample_empty_raises(self):
        """空数据抛出 ValueError。"""
        with pytest.raises(ValueError, match="empty"):
            sample([], n=5)


class TestPivotMoreEdgeCases:
    """pivot 函数的更多边界测试。"""

    def test_pivot_missing_field_raises(self):
        """字段不存在抛出 ValueError。"""
        data = [{"a": 1, "b": 2}]
        with pytest.raises(ValueError, match="does not exist"):
            pivot(data, "a", "b", "missing")

    def test_pivot_duplicate_index_column_raises(self):
        """重复 index-column 对抛出 ValueError。"""
        data = [
            {"idx": "A", "col": "X", "val": 1},
            {"idx": "A", "col": "X", "val": 2},
        ]
        with pytest.raises(ValueError, match="Duplicate"):
            pivot(data, "idx", "col", "val")

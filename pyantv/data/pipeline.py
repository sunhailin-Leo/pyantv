"""Data preprocessing pipeline functions for pyantv.

This module provides common data preprocessing functions that accept
list[dict] format data and return list[dict] format data.
"""

import copy
import datetime
import math
import random
import statistics
from typing import Any, List, Optional


def bin_data(
    data: List[dict],
    field: str,
    bins: int = 10,
    output_field: str = "bin",
) -> List[dict]:
    """Bin numerical data into discrete intervals.

    Args:
        data: List of dictionaries containing the data.
        field: Name of the numerical field to bin.
        bins: Number of bins to create. Defaults to 10.
        output_field: Name of the output field for bin labels.
            Defaults to "bin".

    Returns:
        List of dictionaries with the original data plus a new
        field containing bin labels.

    Raises:
        ValueError: If data is empty, field does not exist,
            or field values are not numerical.
        TypeError: If data is not a list.

    Examples:
        >>> data = [{"value": 1}, {"value": 5}, {"value": 10}]
        >>> result = bin_data(data, "value", bins=2)
        >>> result[0]["bin"]
        '[1.0, 5.5)'
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data cannot be empty")

    if field not in data[0]:
        raise ValueError(f"field '{field}' does not exist in data")

    values = [row[field] for row in data]

    for val in values:
        if not isinstance(val, (int, float)):
            raise ValueError(f"field '{field}' must contain numerical values")

    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        bin_width = 1.0
    else:
        bin_width = (max_val - min_val) / bins

    result = []
    for row in data:
        val = row[field]
        bin_index = int((val - min_val) / bin_width)
        if bin_index >= bins:
            bin_index = bins - 1

        bin_start = min_val + bin_index * bin_width
        bin_end = bin_start + bin_width

        new_row = copy.deepcopy(row)
        new_row[output_field] = f"[{bin_start:.1f}, {bin_end:.1f})"
        result.append(new_row)

    return result


def aggregate(
    data: List[dict],
    group_by: str,
    field: str,
    method: str = "sum",
) -> List[dict]:
    """Aggregate data by grouping and applying a method.

    Args:
        data: List of dictionaries containing the data.
        group_by: Name of the field to group by.
        field: Name of the field to aggregate.
        method: Aggregation method. Supported methods: "sum",
            "mean", "count", "min", "max". Defaults to "sum".

    Returns:
        List of dictionaries with aggregated results.

    Raises:
        ValueError: If data is empty, fields do not exist,
            or method is invalid.
        TypeError: If data is not a list.

    Examples:
        >>> data = [
        ...     {"category": "A", "value": 10},
        ...     {"category": "A", "value": 20},
        ...     {"category": "B", "value": 30},
        ... ]
        >>> result = aggregate(data, "category", "value", "sum")
        >>> result
        [{'category': 'A', 'value': 30}, {'category': 'B', 'value': 30}]
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data cannot be empty")

    if group_by not in data[0]:
        raise ValueError(f"field '{group_by}' does not exist in data")

    if field not in data[0]:
        raise ValueError(f"field '{field}' does not exist in data")

    valid_methods = ["sum", "mean", "count", "min", "max"]
    if method not in valid_methods:
        raise ValueError(
            f"method must be one of {valid_methods}, got '{method}'"
        )

    groups = {}
    for row in data:
        key = row[group_by]
        if key not in groups:
            groups[key] = []
        groups[key].append(row[field])

    result = []
    for key, values in groups.items():
        if method == "sum":
            agg_value = sum(values)
        elif method == "mean":
            agg_value = statistics.mean(values)
        elif method == "count":
            agg_value = len(values)
        elif method == "min":
            agg_value = min(values)
        elif method == "max":
            agg_value = max(values)

        result.append({group_by: key, field: agg_value})

    return result


def sample(
    data: List[dict],
    n: Optional[int] = None,
    fraction: Optional[float] = None,
    seed: Optional[int] = None,
) -> List[dict]:
    """Randomly sample data.

    Args:
        data: List of dictionaries containing the data.
        n: Number of samples to take. If None, must provide fraction.
        fraction: Fraction of data to sample (0.0 to 1.0).
            If None, must provide n.
        seed: Random seed for reproducibility. Defaults to None.

    Returns:
        List of sampled dictionaries.

    Raises:
        ValueError: If data is empty, both n and fraction are None,
            both n and fraction are provided, or n/fraction is invalid.
        TypeError: If data is not a list.

    Examples:
        >>> data = [{"value": i} for i in range(10)]
        >>> result = sample(data, n=3, seed=42)
        >>> len(result)
        3
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data cannot be empty")

    if n is None and fraction is None:
        raise ValueError("Either n or fraction must be provided")

    if n is not None and fraction is not None:
        raise ValueError("Cannot specify both n and fraction")

    if seed is not None:
        random.seed(seed)

    if n is not None:
        if n <= 0:
            raise ValueError(f"n must be positive, got {n}")
        if n > len(data):
            n = len(data)
        indices = random.sample(range(len(data)), n)
    else:
        if fraction <= 0 or fraction > 1:
            raise ValueError(f"fraction must be in (0, 1], got {fraction}")
        n = int(len(data) * fraction)
        indices = random.sample(range(len(data)), n)

    return [copy.deepcopy(data[i]) for i in indices]


def pivot(
    data: List[dict],
    index_field: str,
    columns_field: str,
    values_field: str,
) -> List[dict]:
    """Pivot long format data to wide format.

    Args:
        data: List of dictionaries containing the data.
        index_field: Name of the field to use as index (rows).
        columns_field: Name of the field to use as columns.
        values_field: Name of the field containing values.

    Returns:
        List of dictionaries in wide format.

    Raises:
        ValueError: If data is empty, fields do not exist,
            or data has duplicate index-column pairs.
        TypeError: If data is not a list.

    Examples:
        >>> data = [
        ...     {"date": "2024-01", "category": "A", "value": 10},
        ...     {"date": "2024-01", "category": "B", "value": 20},
        ...     {"date": "2024-02", "category": "A", "value": 30},
        ... ]
        >>> result = pivot(data, "date", "category", "value")
        >>> result[0]
        {'date': '2024-01', 'A': 10, 'B': 20}
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data cannot be empty")

    required_fields = [index_field, columns_field, values_field]
    for field in required_fields:
        if field not in data[0]:
            raise ValueError(f"field '{field}' does not exist in data")

    pivot_dict = {}
    for row in data:
        index_val = row[index_field]
        col_val = row[columns_field]
        val_val = row[values_field]

        if index_val not in pivot_dict:
            pivot_dict[index_val] = {index_field: index_val}

        if col_val in pivot_dict[index_val]:
            raise ValueError(
                f"Duplicate index-column pair found: "
                f"index={index_val}, column={col_val}"
            )

        pivot_dict[index_val][col_val] = val_val

    return list(pivot_dict.values())


def normalize(
    data: List[dict],
    field: str,
    method: str = "min-max",
    output_field: Optional[str] = None,
) -> List[dict]:
    """Normalize numerical data.

    Args:
        data: List of dictionaries containing the data.
        field: Name of the field to normalize.
        method: Normalization method. Supported methods:
            "min-max" (scale to [0, 1]), "z-score" (standardize).
            Defaults to "min-max".
        output_field: Name of the output field for normalized values.
            If None, overwrites the original field. Defaults to None.

    Returns:
        List of dictionaries with normalized values.

    Raises:
        ValueError: If data is empty, field does not exist,
            field values are not numerical, or method is invalid.
        TypeError: If data is not a list.

    Examples:
        >>> data = [{"value": 1}, {"value": 5}, {"value": 10}]
        >>> result = normalize(data, "value", method="min-max")
        >>> result[0]["value"]
        0.0
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data cannot be empty")

    if field not in data[0]:
        raise ValueError(f"field '{field}' does not exist in data")

    values = [row[field] for row in data]

    for val in values:
        if not isinstance(val, (int, float)):
            raise ValueError(f"field '{field}' must contain numerical values")

    valid_methods = ["min-max", "z-score"]
    if method not in valid_methods:
        raise ValueError(
            f"method must be one of {valid_methods}, got '{method}'"
        )

    if output_field is None:
        output_field = field

    result = []

    if method == "min-max":
        min_val = min(values)
        max_val = max(values)

        if min_val == max_val:
            normalized = [0.0 for _ in values]
        else:
            normalized = [
                (val - min_val) / (max_val - min_val) for val in values
            ]
    else:
        mean_val = statistics.mean(values)
        stdev_val = statistics.stdev(values) if len(values) > 1 else 0.0

        if stdev_val == 0:
            normalized = [0.0 for _ in values]
        else:
            normalized = [
                (val - mean_val) / stdev_val for val in values
            ]

    for i, row in enumerate(data):
        new_row = copy.deepcopy(row)
        new_row[output_field] = normalized[i]
        result.append(new_row)

    return result


def _convert_x_to_timestamp(x_value: Any) -> float:
    """Convert x value to timestamp for LTTB calculation.

    Supports numeric, datetime, and date string inputs.

    Args:
        x_value: The x value to convert.

    Returns:
        Timestamp as float.

    Raises:
        ValueError: If x_value cannot be converted to timestamp.
    """
    if isinstance(x_value, (int, float)):
        return float(x_value)
    elif isinstance(x_value, datetime.datetime):
        return float(x_value.timestamp())
    elif isinstance(x_value, datetime.date):
        return float(datetime.datetime.combine(x_value, datetime.time.min).timestamp())
    elif isinstance(x_value, str):
        try:
            dt = datetime.datetime.fromisoformat(x_value)
            return float(dt.timestamp())
        except ValueError:
            raise ValueError(
                f"Cannot convert x value '{x_value}' to timestamp. "
                "Expected datetime string in ISO format."
            )
    else:
        raise ValueError(
            f"Unsupported x value type: {type(x_value).__name__}. "
            "Expected numeric, datetime, or date string."
        )


def downsample(
    data: List[dict],
    max_points: int,
    method: str = 'lttb',
    x_field: Optional[str] = None,
    y_field: Optional[str] = None,
    random_state: Optional[int] = None,
) -> List[dict]:
    """降采样数据到指定点数。

    支持三种降采样方法：
    - 'lttb': Largest-Triangle-Three-Buckets，保留数据形状特征
    - 'uniform': 均匀采样，保证时序稳定性
    - 'random': 随机采样，可固定 seed 保证可重现

    Args:
        data: 待降采样的数据列表。
        max_points: 目标最大点数。
        method: 降采样方法，支持 'lttb'（默认）、'uniform'、'random'。
        x_field: LTTB 方法需要的 x 轴字段名，支持数值、datetime、日期字符串（自动转换为时间戳）。
        y_field: LTTB 方法需要的 y 轴字段名（数值类型）。
        random_state: random 方法的随机种子，用于可重现结果。

    Returns:
        降采样后的数据列表。

    Raises:
        ValueError: 数据为空、字段不存在、max_points 非法、method 非法时。
        TypeError: 当 data 不是列表时。

    Examples:
        >>> data = [{"x": i, "y": i * 2} for i in range(1000)]
        >>> result = downsample(
        ...     data, max_points=100, method="lttb",
        ...     x_field="x", y_field="y",
        ... )
        >>> len(result)
        100
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data cannot be empty")

    if max_points <= 0:
        raise ValueError(f"max_points must be positive, got {max_points}")

    if len(data) <= max_points:
        return [copy.deepcopy(row) for row in data]

    valid_methods = ['lttb', 'uniform', 'random']
    if method not in valid_methods:
        raise ValueError(
            f"method must be one of {valid_methods}, got '{method}'"
        )

    if method == 'lttb':
        if x_field is None or y_field is None:
            raise ValueError(
                "x_field and y_field are required for lttb method"
            )
        if x_field not in data[0]:
            raise ValueError(f"field '{x_field}' does not exist in data")
        if y_field not in data[0]:
            raise ValueError(f"field '{y_field}' does not exist in data")

        return _downsample_lttb(data, max_points, x_field, y_field)
    elif method == 'uniform':
        return _downsample_uniform(data, max_points)
    else:
        return _downsample_random(data, max_points, random_state)


def _downsample_lttb(
    data: List[dict],
    max_points: int,
    x_field: str,
    y_field: str,
) -> List[dict]:
    """Largest-Triangle-Three-Buckets (LTTB) 降采样算法。

    保留首末端点，通过计算三角形面积选择最具代表性的点。

    Args:
        data: 输入数据列表。
        max_points: 目标点数。
        x_field: x 轴字段名。
        y_field: y 轴字段名。

    Returns:
        降采样后的数据列表。
    """
    n = len(data)
    if n <= max_points:
        return [copy.deepcopy(row) for row in data]

    bucket_size = (n - 2) / (max_points - 2)

    result = []
    result.append(copy.deepcopy(data[0]))

    a = 0

    for i in range(max_points - 2):
        avg_x_start = 0
        avg_x_end = 0
        avg_y_start = 0
        avg_y_end = 0

        avg_range_start = int(math.floor((i + 0) * bucket_size) + 1)
        avg_range_end = int(math.floor((i + 1) * bucket_size) + 1)
        avg_range_length = avg_range_end - avg_range_start

        while avg_range_start < avg_range_end:
            avg_x_start += _convert_x_to_timestamp(data[avg_range_start][x_field])
            avg_y_start += float(data[avg_range_start][y_field])
            avg_range_start += 1

        avg_x_start /= avg_range_length
        avg_y_start /= avg_range_length

        avg_range_start = int(math.floor((i + 1) * bucket_size) + 1)
        avg_range_end = int(math.floor((i + 2) * bucket_size) + 1)
        avg_range_end = min(avg_range_end, n)
        avg_range_length = avg_range_end - avg_range_start

        while avg_range_start < avg_range_end:
            avg_x_end += _convert_x_to_timestamp(data[avg_range_start][x_field])
            avg_y_end += float(data[avg_range_start][y_field])
            avg_range_start += 1

        avg_x_end /= avg_range_length
        avg_y_end /= avg_range_length

        point_a_x = _convert_x_to_timestamp(data[a][x_field])
        point_a_y = float(data[a][y_field])

        max_area = -1
        max_area_point = a + 1

        range_start = int(math.floor((i + 0) * bucket_size) + 1)
        range_end = int(math.floor((i + 1) * bucket_size) + 1)
        range_end = min(range_end, n)

        for j in range(range_start, range_end):
            point_x = _convert_x_to_timestamp(data[j][x_field])
            point_y = float(data[j][y_field])

            area = abs(
                (point_a_x - avg_x_end) * (point_y - point_a_y)
                - (point_a_x - point_x) * (avg_y_end - point_a_y)
            ) * 0.5

            if area > max_area:
                max_area = area
                max_area_point = j

        result.append(copy.deepcopy(data[max_area_point]))
        a = max_area_point

    result.append(copy.deepcopy(data[-1]))
    return result


def _downsample_uniform(
    data: List[dict],
    max_points: int,
) -> List[dict]:
    """均匀采样，保证时序稳定性。

    Args:
        data: 输入数据列表。
        max_points: 目标点数。

    Returns:
        降采样后的数据列表。
    """
    n = len(data)
    if n <= max_points:
        return [copy.deepcopy(row) for row in data]

    step = n / max_points
    result = []

    for i in range(max_points):
        index = int(i * step)
        result.append(copy.deepcopy(data[index]))

    return result


def _downsample_random(
    data: List[dict],
    max_points: int,
    random_state: Optional[int] = None,
) -> List[dict]:
    """随机采样，保留原始顺序。

    Args:
        data: 输入数据列表。
        max_points: 目标点数。
        random_state: 随机种子。

    Returns:
        降采样后的数据列表（按原始索引排序）。
    """
    n = len(data)
    if n <= max_points:
        return [copy.deepcopy(row) for row in data]

    if random_state is not None:
        random.seed(random_state)

    indices = random.sample(range(n), max_points)
    indices.sort()

    result = [copy.deepcopy(data[i]) for i in indices]
    return result

"""
数据转换预设示例：展示 pyantv 的数据转换预设函数用法。

包括排序、堆叠、归一化、分组、抖动等数据变换。
"""

from pyantv import Interval, Area
from pyantv.presets import (
    with_sort_by,
    with_stack,
    with_normalize,
    with_group,
)

SAMPLE_DATA = [
    {"category": "A", "value": 120, "type": "X"},
    {"category": "B", "value": 200, "type": "X"},
    {"category": "C", "value": 150, "type": "X"},
    {"category": "D", "value": 80, "type": "X"},
    {"category": "A", "value": 90, "type": "Y"},
    {"category": "B", "value": 160, "type": "Y"},
    {"category": "C", "value": 130, "type": "Y"},
    {"category": "D", "value": 110, "type": "Y"},
]


def demo_sort_by():
    """排序：按指定字段排序数据。"""
    chart = Interval()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(x_field_name="category", y_field_name="value")
    with_sort_by(chart, field="value", order="descending")
    chart.render("transform_sort_by.html")
    print("Generated: transform_sort_by.html")


def demo_stack():
    """堆叠：将多个系列堆叠显示。"""
    chart = Interval()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(
        x_field_name="category",
        y_field_name="value",
        color_field="type",
    )
    with_stack(chart)
    chart.render("transform_stack.html")
    print("Generated: transform_stack.html")


def demo_normalize():
    """归一化：将堆叠数据归一化为百分比。"""
    chart = Interval()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(
        x_field_name="category",
        y_field_name="value",
        color_field="type",
    )
    with_stack(chart)
    with_normalize(chart)
    chart.render("transform_normalize.html")
    print("Generated: transform_normalize.html")


def demo_group():
    """分组：按字段分组显示。"""
    chart = Interval()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(
        x_field_name="category",
        y_field_name="value",
        color_field="type",
    )
    with_group(chart, channels=["color"])
    chart.render("transform_group.html")
    print("Generated: transform_group.html")


if __name__ == "__main__":
    demo_sort_by()
    demo_stack()
    demo_normalize()
    demo_group()
    print("\nAll data transform preset demos generated!")

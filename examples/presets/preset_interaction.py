"""
交互预设示例：展示 pyantv 的交互预设函数用法。

包括元素高亮、元素选择、框选高亮、框选过滤、鱼眼、滑块过滤等。
"""

from pyantv import Line, Interval
from pyantv.presets import (
    with_element_highlight,
    with_element_select,
    with_brush_highlight,
    with_brush_filter,
    with_fisheye,
    with_slider_filter,
    with_tooltip,
)

SAMPLE_DATA = [
    {"month": "Jan", "value": 120, "type": "A"},
    {"month": "Feb", "value": 200, "type": "A"},
    {"month": "Mar", "value": 150, "type": "A"},
    {"month": "Apr", "value": 80, "type": "A"},
    {"month": "Jan", "value": 90, "type": "B"},
    {"month": "Feb", "value": 160, "type": "B"},
    {"month": "Mar", "value": 130, "type": "B"},
    {"month": "Apr", "value": 110, "type": "B"},
]


def demo_element_highlight():
    """元素高亮：鼠标悬停时高亮元素。"""
    chart = Interval()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(x_field_name="month", y_field_name="value", color_field="type")
    with_element_highlight(chart)
    with_tooltip(chart)
    chart.render("interaction_element_highlight.html")
    print("Generated: interaction_element_highlight.html")


def demo_element_select():
    """元素选择：点击选中元素。"""
    chart = Interval()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(x_field_name="month", y_field_name="value", color_field="type")
    with_element_select(chart)
    chart.render("interaction_element_select.html")
    print("Generated: interaction_element_select.html")


def demo_brush_highlight():
    """框选高亮：拖动框选区域内的元素高亮。"""
    chart = Line()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(x_field_name="month", y_field_name="value", color_field="type")
    with_brush_highlight(chart)
    chart.render("interaction_brush_highlight.html")
    print("Generated: interaction_brush_highlight.html")


def demo_slider_filter():
    """滑块过滤：通过滑块筛选数据范围。"""
    chart = Line()
    chart.set_data(data=SAMPLE_DATA)
    chart.set_encode(x_field_name="month", y_field_name="value", color_field="type")
    with_slider_filter(chart, x_axis=True)
    chart.render("interaction_slider_filter.html")
    print("Generated: interaction_slider_filter.html")


if __name__ == "__main__":
    demo_element_highlight()
    demo_element_select()
    demo_brush_highlight()
    demo_slider_filter()
    print("\nAll interaction preset demos generated!")

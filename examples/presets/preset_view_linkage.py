"""图表联动示例：展示 View 的 link_tooltip 和 link_brush 联动功能。

通过 View 容器组合多个子图表，并启用 tooltip 联动和框选联动，
实现鼠标悬停和框选操作在多个图表间的同步交互。
"""
from pyantv import Line, Interval
from pyantv.charts.composition_charts.view import View


# ── 示例数据 ────────────────────────────────────────
sales_data = [
    {"month": "Jan", "revenue": 120, "orders": 45},
    {"month": "Feb", "revenue": 180, "orders": 62},
    {"month": "Mar", "revenue": 250, "orders": 78},
    {"month": "Apr", "revenue": 210, "orders": 56},
    {"month": "May", "revenue": 340, "orders": 95},
    {"month": "Jun", "revenue": 290, "orders": 88},
]


# ── 示例 1: Tooltip 联动 ─────────────────────────────
# 鼠标悬停在一个图表上时，另一个图表也会显示相同月份的数据
line_chart = (
    Line()
    .set_data(data=sales_data)
    .set_encode(x_field_name="month", y_field_name="revenue")
    .set_title("Revenue Trend")
)

bar_chart = (
    Interval()
    .set_data(data=sales_data)
    .set_encode(x_field_name="month", y_field_name="orders")
    .set_title("Order Count")
)

tooltip_view = (
    View()
    .add_child(line_chart)
    .add_child(bar_chart)
    .link_tooltip(shared=True)
    .set_size(is_auto_fit=True)
)

tooltip_view.render("view_tooltip_linkage.html")
print("Tooltip linkage example rendered to view_tooltip_linkage.html")


# ── 示例 2: Brush 框选联动 ────────────────────────────
# 在一个图表中框选区域时，另一个图表会同步高亮对应数据
line_chart_2 = (
    Line()
    .set_data(data=sales_data)
    .set_encode(x_field_name="month", y_field_name="revenue")
    .set_title("Revenue (Brush Linked)")
)

bar_chart_2 = (
    Interval()
    .set_data(data=sales_data)
    .set_encode(x_field_name="month", y_field_name="orders")
    .set_title("Orders (Brush Linked)")
)

brush_view = (
    View()
    .add_child(line_chart_2)
    .add_child(bar_chart_2)
    .link_brush(brush_type="x", shared=True)
    .set_size(is_auto_fit=True)
)

brush_view.render("view_brush_linkage.html")
print("Brush linkage example rendered to view_brush_linkage.html")


# ── 示例 3: 同时启用 Tooltip + Brush 联动 ─────────────
line_chart_3 = (
    Line()
    .set_data(data=sales_data)
    .set_encode(x_field_name="month", y_field_name="revenue")
    .set_title("Revenue (Full Linked)")
)

bar_chart_3 = (
    Interval()
    .set_data(data=sales_data)
    .set_encode(x_field_name="month", y_field_name="orders")
    .set_title("Orders (Full Linked)")
)

combined_view = (
    View()
    .add_child(line_chart_3)
    .add_child(bar_chart_3)
    .link_tooltip()
    .link_brush(brush_type="rect")
    .set_size(is_auto_fit=True)
)

combined_view.render("view_combined_linkage.html")
print("Combined linkage example rendered to view_combined_linkage.html")

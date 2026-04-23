"""
差分面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#difference-area
"""
from pyantv import options as opts
from pyantv.charts import View, Area

data = [
    {"month": "Jan", "actual": 120, "forecast": 100},
    {"month": "Feb", "actual": 135, "forecast": 130},
    {"month": "Mar", "actual": 148, "forecast": 155},
    {"month": "Apr", "actual": 160, "forecast": 150},
    {"month": "May", "actual": 175, "forecast": 180},
    {"month": "Jun", "actual": 190, "forecast": 185},
    {"month": "Jul", "actual": 205, "forecast": 210},
    {"month": "Aug", "actual": 220, "forecast": 200},
    {"month": "Sep", "actual": 235, "forecast": 240},
    {"month": "Oct", "actual": 250, "forecast": 245},
    {"month": "Nov", "actual": 265, "forecast": 270},
    {"month": "Dec", "actual": 280, "forecast": 260},
]

actual_area = (
    Area()
    .set_encode(x_field_name="month", y_field_name="actual")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.4),
    )
)

forecast_area = (
    Area()
    .set_encode(x_field_name="month", y_field_name="forecast")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#61DDAA", fill_opacity=0.4),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[actual_area.options, forecast_area.options])
    .set_global_options(title_opts=opts.TitleOpts(title="差分面积图"))
)
chart.render("difference_area.html")

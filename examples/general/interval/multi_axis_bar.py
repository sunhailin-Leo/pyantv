"""
多轴条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#multi-axis-bar
"""
from pyantv import options as opts
from pyantv.charts import View, Interval

data = [
    {"city": "北京", "temperature": 25, "humidity": 45},
    {"city": "上海", "temperature": 28, "humidity": 65},
    {"city": "广州", "temperature": 32, "humidity": 80},
    {"city": "深圳", "temperature": 30, "humidity": 75},
    {"city": "杭州", "temperature": 27, "humidity": 60},
    {"city": "成都", "temperature": 24, "humidity": 55},
]

temp_chart = (
    Interval()
    .set_encode(x_field_name="city", y_field_name="temperature", color_field="#5B8FF9")
    .set_global_options(
        title_opts=opts.TitleOpts(title="多轴条形图"),
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="温度 (°C)"),
            ),
        ),
    )
)

humidity_chart = (
    Interval()
    .set_encode(x_field_name="city", y_field_name="humidity", color_field="#61DDAA")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="湿度 (%)"),
            ),
        ),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[temp_chart.get_options(), humidity_chart.get_options()])
)
chart.render("multi_axis_bar.html")

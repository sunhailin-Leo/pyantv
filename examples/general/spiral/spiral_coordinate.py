"""
螺旋坐标系
G2 文档: https://g2.antv.antgroup.com/examples/general/spiral/#spiral-coordinate
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [{"month": f"2023-{str(i).zfill(2)}", "value": v} for i, v in enumerate(
    [30, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90], 1
)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="螺旋坐标系"),
        coordinate_opts=opts.CoordinateHelixOpts(),
    )
)
chart.render("spiral_coordinate.html")

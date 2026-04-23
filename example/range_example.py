import unittest

from pyantv import options as opts
from pyantv.charts import View, LineX, LineY, Range, Point
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


line_x = LineX().set_data(data=[0])

line_y = LineY().set_data(data=[0])

range_ = (
    Range()
    .set_data(
        data=[
            {"x": [-25, 0], "y": [-30, 0], "region": "1"},
            {"x": [-25, 0], "y": [0, 20], "region": "2"},
            {"x": [0, 5], "y": [-30, 0], "region": "2"},
            {"x": [0, 5], "y": [0, 20], "region": "1"},
        ]
    )
    .set_encode(
        x_field_name="x",
        y_field_name="y",
        color_field="region",
    )
    .set_scale(
        color_scale_opts=opts.ScaleBaseOpts(
            range_=["#d8d0c0", "#a3dda1"],
            is_independent=True,
            # guide: null ???
        )
    )
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            fill_opacity=0.2,
        )
    )
)

point = (
    Point()
    .set_encode(
        x_field_name="change in female rate",
        y_field_name="change in male rate",
        size_field="pop",
        color_field="continent",
        shape_field="point",
    )
    .set_scale(
        color_scale_opts=opts.ScaleBaseOpts(
            range_=[
                "#ffd500",
                "#82cab2",
                "#193442",
                "#d18768",
                "#7e827a",
            ],
        ),
        x_scale_opts=opts.ScaleLinearOpts(domain=[-25, 5]),
        y_scale_opts=opts.ScaleLinearOpts(domain=[-30, 20]),
        size_scale_opts=opts.ScaleLinearOpts(range_=[4, 30]),
    )
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            stroke="#bbb",
            fill_opacity=0.8,
        ),
        axis_opts=opts.AxisOpts(
            x_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=False,
            ),
            y_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=False,
            ),
        ),
    )
)


c = (
    View()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://gw.alipayobjects.com/os/bmw-prod/"
            "0b37279d-1674-42b4-b285-29683747ad9a.json"
        )
    )
    .set_view_children(
        children=[
            line_x.get_options(),
            line_y.get_options(),
            range_.get_options(),
            point.get_options(),
        ]
    )
)

c.render("range_example.html")

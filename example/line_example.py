from pyantv import options as opts
from pyantv.charts import View, Line, Point


TEST_LINE_DATA = [
    {"year": "1991", "value": 3},
    {"year": "1992", "value": 4},
    {"year": "1993", "value": 3.5},
    {"year": "1994", "value": 5},
    {"year": "1995", "value": 4.9},
    {"year": "1996", "value": 6},
    {"year": "1997", "value": 7},
    {"year": "1998", "value": 9},
    {"year": "1999", "value": 13},
]

line = (
    Line()
    .set_global_options(
        label_opts=[
            opts.LabelOpts(
                text_opts="value",
                style_opts=opts.BaseChartStyleOpts(dx=-10, dy=-12),
            )
        ]
    )
)

point = Point().set_global_options(
    tooltip_opts=False,
    style_opts=opts.BaseChartStyleOpts(fill="white"),
)

c = (
    View()
    .set_data(data=TEST_LINE_DATA)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_view_children(
        children=[
            line.options,
            point.options,
        ]
    )
    .set_scale(
        x_scale_opts=opts.ScaleBandOpts(range_=[0, 1]),
        y_scale_opts=opts.ScaleLinearOpts(domain_min=0, is_nice=True),
    )
    .render("line_example.html")
)

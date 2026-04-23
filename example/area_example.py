from pyantv import options as opts
from pyantv.charts import Area, Line, View
from pyantv.commons.utils import JsCode

TEST_AREA_DATA = [
    {"year": "1991", "value": 15468},
    {"year": "1992", "value": 16100},
    {"year": "1993", "value": 15900},
    {"year": "1994", "value": 17409},
    {"year": "1995", "value": 17000},
    {"year": "1996", "value": 31056},
    {"year": "1997", "value": 31982},
    {"year": "1998", "value": 32040},
    {"year": "1999", "value": 33233},
]


area = (
    Area()
    .set_encode(
        x_field_name=JsCode("(d) => d.year"),
        y_field_name="value",
        shape_field="area",
    )
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(
                axis_label_opts=opts.AxisLabelOpts(
                    label_formatter="~s",
                ),
                axis_title_opts=False,
            ),
        ),
        style_opts=opts.BaseChartStyleOpts(opacity=0.2),
    )
)

line = Line().set_encode(
    x_field_name="year",
    y_field_name="value",
    shape_field="line",
)

view = (
    View()
    .set_data(data=TEST_AREA_DATA)
    .set_view_children(
        children=[
            area.get_options(),
            line.get_options(),
        ]
    )
)
view.render("area_example.html")


c = (
    Area()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://assets.antv.antgroup.com/g2/aapl.json",
        )
    )
    .set_encode(
        x_field_name=JsCode("(d) => new Date(d.date)"),
        y_field_name=JsCode(
            "(d) => (new Date(d.date).getUTCMonth() <= 3 ? NaN : d.close)",
        ),
    )
    .set_area_style(
        is_connect=True,
        connect_style_opts=opts.BaseChartStyleOpts(
            fill="grey",
            fill_opacity=0.15,
        ),
    )
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            fill="skyblue",
            opacity=0.5,
            stroke="yellow",
        ),
    )
)
c.render("area_example.html")

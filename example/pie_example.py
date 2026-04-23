from pyantv import options as opts
from pyantv.charts import Interval
from pyantv.commons.utils import JsCode

TEST_PIE_DATA = [
    {"item": "事例一", "count": 40, "percent": 0.4},
    {"item": "事例二", "count": 21, "percent": 0.21},
    {"item": "事例三", "count": 17, "percent": 0.17},
    {"item": "事例四", "count": 13, "percent": 0.13},
    {"item": "事例五", "count": 9, "percent": 0.09},
]

c = (
    Interval()
    .set_data(data=TEST_PIE_DATA)
    .set_encode(y_field_name="percent", color_field="item")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(outer_radius=0.8),
        label_opts=[
            opts.LabelOpts(
                position="outside",
                text_opts=JsCode("(data) => `${data.item}: ${data.percent * 100}%`"),
            )
        ],
        tooltip_opts=opts.TooltipOpts(
            items=[
                JsCode("(data) => ({name: data.item, value: `${data.percent * 100}%`})")
            ]
        ),
        legend_opts=opts.LegendCategoryOpts(
            color_legend_opts=opts.LegendCategoryCfgOpts(
                position="bottom",
                layout_opts=opts.LegendLayoutOpts(
                    justify_content="center",
                ),
            )
        ),
    )
    .render("pie_example.html")
)

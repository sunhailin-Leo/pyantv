import unittest

from pyantv import options as opts
from pyantv.charts import Wordcloud, Gauge
from pyantv.globals import ChartType

from test import chart_base_test


c = (
    Gauge(
        render_opts=opts.RenderOpts(
            is_auto_fit=True,
        ),
    )
    .set_data(
        data={
            "value": {
                "target": 120,
                "total": 400,
                "name": "score",
            }
        }
    )
    .set_global_options(legend_opts=False)
)
c.render("gauge_example.html")

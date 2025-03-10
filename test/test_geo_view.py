import unittest

from pyantv import options as opts
from pyantv.charts import GeoView, GeoPath
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class TestGeoViewChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.GEOVIEW)
    def test_geo_view_base(self):
        geo_path_1 = (
            GeoPath()
            .set_data(data={"type": "graticule10"})
            .set_geo_path_style(
                base_style_opts=opts.BaseChartStyleOpts(
                    stroke="#ccc",
                    fill="none",
                )
            )
        )

        geo_path_2 = (
            GeoPath()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/countries-50m.json",
                    transform=[
                        opts.FeatureDataTransformOpts(name="land"),
                    ],
                )
            )
            .set_geo_path_style(
                base_style_opts=opts.BaseChartStyleOpts(
                    fill="black",
                )
            )
        )

        geo_path_3 = (
            GeoPath()
            .set_data(data={"type": "sphere"})
            .set_geo_path_style(
                base_style_opts=opts.BaseChartStyleOpts(
                    stroke="black",
                    fill="none",
                )
            )
        )

        c = (
            GeoView()
            .add_js_dependencies(*["topojson-client"])
            .add_js_funcs(
                JsCode(
                    """
                G2.register('data.feature', ({ name }) => {
                    return (data) => topojson.feature(data, data.objects[name]).features;
                });
                """
                ).js_code
            )
            .set_geo_view_children(
                children=[
                    geo_path_1.get_options(),
                    geo_path_2.get_options(),
                    geo_path_3.get_options(),
                ]
            )
            .set_global_options(coordinate_opts={"type": "orthographic"})
        )

        return c

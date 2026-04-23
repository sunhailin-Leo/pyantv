"""WaterFall 瀑布图基础功能测试。"""

import unittest


from pyantv.charts.basic_charts.waterfall import WaterFall


SAMPLE_DATA = [
    {"type": "日用品", "money": 120},
    {"type": "伙食费", "money": 900},
    {"type": "交通费", "money": 200},
    {"type": "水电费", "money": 300},
    {"type": "房租", "money": 1200},
]


class TestWaterFallBasic(unittest.TestCase):
    """验证 WaterFall 基本功能。"""

    def test_default_type_is_interval(self):
        """验证 WaterFall 底层 mark type 为 interval。"""
        chart = WaterFall()
        self.assertEqual(chart.options.get("type"), "interval")

    def test_is_instance_of_chart(self):
        """验证 WaterFall 是 Chart 的子类。"""
        from pyantv.charts.chart import Chart

        chart = WaterFall()
        self.assertIsInstance(chart, Chart)

    def test_preset_transform(self):
        """验证构造时自动预置 stackY + diffX transform。"""
        chart = WaterFall()
        transforms = chart.options.get("transform", [])
        self.assertEqual(len(transforms), 2)
        self.assertEqual(transforms[0]["type"], "stackY")
        self.assertEqual(transforms[1]["type"], "diffX")

    def test_set_data_and_encode(self):
        """验证设置数据和编码。"""
        chart = (
            WaterFall()
            .set_data(data=SAMPLE_DATA)
            .set_encode(x_field_name="type", y_field_name="money")
        )
        self.assertEqual(chart.options.get("data"), SAMPLE_DATA)
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("x"), "type")
        self.assertEqual(encode.get("y"), "money")


class TestWaterFallChaining(unittest.TestCase):
    """验证 WaterFall 链式调用。"""

    def test_chain_returns_self(self):
        """验证 set_data 和 set_encode 返回 self。"""
        chart = WaterFall()
        result = chart.set_data(data=SAMPLE_DATA)
        self.assertIs(result, chart)
        result = chart.set_encode(x_field_name="type", y_field_name="money")
        self.assertIs(result, chart)

    def test_full_chain(self):
        """验证完整链式调用。"""
        from pyantv import opts

        chart = (
            WaterFall()
            .set_data(data=SAMPLE_DATA)
            .set_encode(x_field_name="type", y_field_name="money")
            .set_style(style_opts=opts.BaseChartStyleOpts(fill="steelblue"))
        )
        self.assertEqual(chart.options.get("type"), "interval")
        self.assertIn("style", chart.options)


class TestWaterFallFromData(unittest.TestCase):
    """验证 WaterFall 继承 from_data 快捷方法。"""

    def test_from_data(self):
        """验证 WaterFall.from_data 正确创建图表。"""
        chart = WaterFall.from_data(
            data=SAMPLE_DATA,
            x_field_name="type",
            y_field_name="money",
        )
        self.assertIsInstance(chart, WaterFall)
        self.assertEqual(chart.options.get("type"), "interval")
        self.assertEqual(chart.options.get("data"), SAMPLE_DATA)
        transforms = chart.options.get("transform", [])
        self.assertEqual(len(transforms), 2)
        self.assertEqual(transforms[0]["type"], "stackY")
        self.assertEqual(transforms[1]["type"], "diffX")


class TestWaterFallGlobalOptions(unittest.TestCase):
    """验证 WaterFall 全局选项。"""

    def test_set_global_options_preserves_transform(self):
        """验证 set_global_options 中的 transform 会覆盖预置值。"""
        from pyantv import opts

        chart = WaterFall()
        chart.set_global_options(
            transform_opts=[
                opts.TransformStackYOpts(),
                opts.TransformDiffXOpts(),
            ]
        )
        transforms = chart.options.get("transform", [])
        self.assertGreaterEqual(len(transforms), 2)

    def test_set_global_options_with_axis(self):
        """验证 set_global_options 可以设置 axis。"""
        chart = (
            WaterFall()
            .set_data(data=SAMPLE_DATA)
            .set_encode(x_field_name="type", y_field_name="money")
            .set_global_options(axis_opts=False)
        )
        self.assertFalse(chart.options.get("axis"))


class TestWaterFallImport(unittest.TestCase):
    """验证 WaterFall 可以从顶层导入。"""

    def test_import_from_pyantv(self):
        """验证 from pyantv import WaterFall 可用。"""
        from pyantv import WaterFall as WF

        chart = WF()
        self.assertEqual(chart.options.get("type"), "interval")

    def test_import_from_charts(self):
        """验证 from pyantv.charts import WaterFall 可用。"""
        from pyantv.charts import WaterFall as WF

        chart = WF()
        self.assertEqual(chart.options.get("type"), "interval")

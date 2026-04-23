"""from_data 快捷构建方法测试。"""

import unittest

from pyantv.charts import Line, Interval, Area, Point, Funnel, Beeswarm


class TestFromDataBasic(unittest.TestCase):
    """验证 from_data() 类方法的基本功能。"""

    def test_line_from_data(self):
        """验证 Line.from_data 创建正确的图表。"""
        chart = Line.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        )
        self.assertIsInstance(chart, Line)
        self.assertEqual(chart.options.get("type"), "line")
        self.assertEqual(chart.options.get("data"), [{"x": 1, "y": 2}])
        self.assertEqual(chart.options.get("encode", {}).get("x"), "x")
        self.assertEqual(chart.options.get("encode", {}).get("y"), "y")

    def test_interval_from_data(self):
        """验证 Interval.from_data 创建正确的图表。"""
        chart = Interval.from_data(
            data=[{"month": "Jan", "value": 100}],
            x_field_name="month",
            y_field_name="value",
        )
        self.assertIsInstance(chart, Interval)
        self.assertEqual(chart.options.get("type"), "interval")

    def test_area_from_data(self):
        """验证 Area.from_data 创建正确的图表。"""
        chart = Area.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        )
        self.assertIsInstance(chart, Area)
        self.assertEqual(chart.options.get("type"), "area")

    def test_point_from_data(self):
        """验证 Point.from_data 创建正确的图表。"""
        chart = Point.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        )
        self.assertIsInstance(chart, Point)
        self.assertEqual(chart.options.get("type"), "point")


class TestFromDataEncodeFields(unittest.TestCase):
    """验证 from_data() 的编码字段传递。"""

    def test_color_field(self):
        """验证 color_field 正确传递。"""
        chart = Line.from_data(
            data=[{"x": 1, "y": 2, "c": "A"}],
            x_field_name="x",
            y_field_name="y",
            color_field="c",
        )
        self.assertEqual(chart.options.get("encode", {}).get("color"), "c")

    def test_size_field(self):
        """验证 size_field 正确传递。"""
        chart = Point.from_data(
            data=[{"x": 1, "y": 2, "s": 10}],
            x_field_name="x",
            y_field_name="y",
            size_field="s",
        )
        self.assertEqual(chart.options.get("encode", {}).get("size"), "s")

    def test_shape_field(self):
        """验证 shape_field 正确传递。"""
        chart = Point.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
            shape_field="circle",
        )
        self.assertEqual(chart.options.get("encode", {}).get("shape"), "circle")

    def test_series_field(self):
        """验证 series_field 正确传递。"""
        chart = Line.from_data(
            data=[{"x": 1, "y": 2, "s": "A"}],
            x_field_name="x",
            y_field_name="y",
            series_field="s",
        )
        self.assertEqual(chart.options.get("encode", {}).get("series"), "s")

    def test_minimal_no_encode(self):
        """验证仅传 data 不传编码字段也能正常工作。"""
        chart = Line.from_data(data=[{"x": 1, "y": 2}])
        self.assertIsInstance(chart, Line)
        self.assertEqual(chart.options.get("data"), [{"x": 1, "y": 2}])


class TestFromDataChaining(unittest.TestCase):
    """验证 from_data() 返回值支持链式调用。"""

    def test_chain_set_theme(self):
        """验证 from_data 后可以继续链式调用 set_theme。"""
        chart = Line.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        ).set_theme(theme="dark")
        self.assertEqual(chart.render_options.get("theme"), "dark")

    def test_chain_set_style(self):
        """验证 from_data 后可以继续链式调用 set_style。"""
        from pyantv import opts

        chart = Interval.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        ).set_style(style_opts=opts.BaseChartStyleOpts(fill="steelblue"))
        self.assertIn("style", chart.options)

    def test_chain_set_events(self):
        """验证 from_data 后可以继续链式调用 set_events。"""
        from pyantv.globals import ChartEvent

        chart = Line.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        ).set_events(
            {
                ChartEvent.ELEMENT_CLICK: "(ev) => { console.log(ev); }",
            }
        )
        self.assertEqual(len(list(chart.js_events.items)), 1)


class TestFromDataSubclassInheritance(unittest.TestCase):
    """验证子类正确继承 from_data()。"""

    def test_funnel_from_data_uses_overridden_set_encode(self):
        """验证 Funnel.from_data 调用子类重写的 set_encode，自动注入 shape。"""
        chart = Funnel.from_data(
            data=[{"stage": "A", "value": 100}],
            x_field_name="stage",
            y_field_name="value",
        )
        self.assertIsInstance(chart, Funnel)
        self.assertEqual(chart.options.get("type"), "interval")
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("shape"), "funnel")

    def test_beeswarm_from_data(self):
        """验证 Beeswarm.from_data 正确继承。"""
        chart = Beeswarm.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        )
        self.assertIsInstance(chart, Beeswarm)
        self.assertEqual(chart.options.get("type"), "beeswarm")


class TestFromDataInitOpts(unittest.TestCase):
    """验证 from_data() 的初始化选项传递。"""

    def test_custom_init_opts(self):
        """验证自定义 init_opts 正确传递。"""
        from pyantv import opts

        chart = Line.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
            init_opts=opts.InitOpts(width="800px", height="600px"),
        )
        self.assertEqual(chart.width, "800px")
        self.assertEqual(chart.height, "600px")

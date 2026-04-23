"""事件系统（ChartEvent 常量 + set_events API）测试。"""

import unittest

from pyantv.charts import Line, Interval
from pyantv.globals import ChartEvent


class TestChartEvent(unittest.TestCase):
    """验证 ChartEvent 枚举常量的正确性。"""

    def test_lifecycle_events(self):
        """验证生命周期事件常量值。"""
        self.assertEqual(ChartEvent.BEFORE_RENDER, "beforerender")
        self.assertEqual(ChartEvent.AFTER_RENDER, "afterrender")
        self.assertEqual(ChartEvent.BEFORE_PAINT, "beforepaint")
        self.assertEqual(ChartEvent.AFTER_PAINT, "afterpaint")
        self.assertEqual(ChartEvent.BEFORE_CHANGE_DATA, "beforechangedata")
        self.assertEqual(ChartEvent.AFTER_CHANGE_DATA, "afterchangedata")
        self.assertEqual(ChartEvent.BEFORE_DESTROY, "beforedestroy")
        self.assertEqual(ChartEvent.AFTER_DESTROY, "afterdestroy")

    def test_pointer_events(self):
        """验证指针/鼠标事件常量值。"""
        self.assertEqual(ChartEvent.CLICK, "click")
        self.assertEqual(ChartEvent.DBLCLICK, "dblclick")
        self.assertEqual(ChartEvent.POINTER_TAP, "pointertap")
        self.assertEqual(ChartEvent.POINTER_DOWN, "pointerdown")
        self.assertEqual(ChartEvent.POINTER_UP, "pointerup")
        self.assertEqual(ChartEvent.POINTER_MOVE, "pointermove")
        self.assertEqual(ChartEvent.POINTER_OVER, "pointerover")
        self.assertEqual(ChartEvent.POINTER_OUT, "pointerout")
        self.assertEqual(ChartEvent.POINTER_ENTER, "pointerenter")
        self.assertEqual(ChartEvent.POINTER_LEAVE, "pointerleave")

    def test_element_events(self):
        """验证元素事件常量值。"""
        self.assertEqual(ChartEvent.ELEMENT_CLICK, "element:click")
        self.assertEqual(ChartEvent.ELEMENT_DBLCLICK, "element:dblclick")
        self.assertEqual(ChartEvent.ELEMENT_POINTER_ENTER, "element:pointerenter")
        self.assertEqual(ChartEvent.ELEMENT_POINTER_LEAVE, "element:pointerleave")
        self.assertEqual(ChartEvent.ELEMENT_HIGHLIGHT, "element:highlight")
        self.assertEqual(ChartEvent.ELEMENT_UNHIGHLIGHT, "element:unhighlight")
        self.assertEqual(ChartEvent.ELEMENT_SELECT, "element:select")
        self.assertEqual(ChartEvent.ELEMENT_UNSELECT, "element:unselect")

    def test_plot_events(self):
        """验证绘图区事件常量值。"""
        self.assertEqual(ChartEvent.PLOT_CLICK, "plot:click")
        self.assertEqual(ChartEvent.PLOT_DBLCLICK, "plot:dblclick")
        self.assertEqual(ChartEvent.PLOT_POINTER_MOVE, "plot:pointermove")

    def test_interaction_events(self):
        """验证交互事件常量值。"""
        self.assertEqual(ChartEvent.BRUSH_FILTER, "brush:filter")
        self.assertEqual(ChartEvent.BRUSH_HIGHLIGHT, "brush:highlight")
        self.assertEqual(ChartEvent.LEGEND_FILTER, "legend:filter")
        self.assertEqual(ChartEvent.LEGEND_RESET, "legend:reset")
        self.assertEqual(ChartEvent.TOOLTIP_SHOW, "tooltip:show")
        self.assertEqual(ChartEvent.TOOLTIP_HIDE, "tooltip:hide")
        self.assertEqual(ChartEvent.SLIDER_FILTER, "slider:filter")
        self.assertEqual(ChartEvent.SCROLLBAR_FILTER, "scrollbar:filter")


class TestSetEvents(unittest.TestCase):
    """验证 set_events() 方法的正确性。"""

    def test_set_events_basic(self):
        """验证 set_events 基本功能。"""
        chart = Line()
        chart.set_events(
            {
                ChartEvent.ELEMENT_CLICK: "(ev) => { console.log(ev.data); }",
            }
        )
        events = list(chart.js_events.items)
        self.assertEqual(len(events), 1)
        self.assertIn("element:click", events[0])
        self.assertIn("console.log(ev.data)", events[0])

    def test_set_events_multiple(self):
        """验证 set_events 支持多个事件。"""
        chart = Line()
        chart.set_events(
            {
                ChartEvent.ELEMENT_CLICK: "(ev) => { console.log('click'); }",
                ChartEvent.PLOT_POINTER_MOVE: "(ev) => { console.log('move'); }",
            }
        )
        events = list(chart.js_events.items)
        self.assertEqual(len(events), 2)

    def test_set_events_chain(self):
        """验证 set_events 返回 self 支持链式调用。"""
        chart = Line()
        result = chart.set_events(
            {
                ChartEvent.CLICK: "(ev) => {}",
            }
        )
        self.assertIs(result, chart)

    def test_set_events_empty(self):
        """验证 set_events 传入空字典不报错。"""
        chart = Line()
        result = chart.set_events({})
        self.assertIs(result, chart)
        self.assertEqual(len(list(chart.js_events.items)), 0)

    def test_set_events_none(self):
        """验证 set_events 传入 None 不报错。"""
        chart = Line()
        result = chart.set_events(None)
        self.assertIs(result, chart)
        self.assertEqual(len(list(chart.js_events.items)), 0)

    def test_set_events_generates_correct_js(self):
        """验证 set_events 生成正确的 JS 代码格式。"""
        chart = Interval()
        chart.set_events(
            {
                ChartEvent.ELEMENT_CLICK: "(ev) => { alert(ev.data); }",
            }
        )
        events = list(chart.js_events.items)
        self.assertEqual(len(events), 1)
        expected_prefix = f"antv_chart_{chart.chart_id}.on("
        self.assertTrue(events[0].startswith(expected_prefix))
        self.assertIn("'element:click'", events[0])
        self.assertIn("(ev) => { alert(ev.data); }", events[0])
        self.assertTrue(events[0].endswith(");"))

    def test_set_events_with_string_event_type(self):
        """验证 set_events 支持自定义字符串事件类型。"""
        chart = Line()
        chart.set_events(
            {
                "custom:event": "(ev) => { console.log('custom'); }",
            }
        )
        events = list(chart.js_events.items)
        self.assertEqual(len(events), 1)
        self.assertIn("'custom:event'", events[0])

    def test_set_events_with_jscode(self):
        """验证 set_events 支持 JsCode 回调，且生成纯净 JS 代码。"""
        from pyantv.commons.utils import JsCode, PLACEHOLDER

        chart = Line()
        callback = JsCode("(ev) => { console.log(ev); }")
        chart.set_events(
            {
                ChartEvent.AFTER_RENDER: callback,
            }
        )
        events = list(chart.js_events.items)
        self.assertEqual(len(events), 1)
        self.assertIn("afterrender", events[0])
        self.assertIn("(ev) => { console.log(ev); }", events[0])
        self.assertNotIn(PLACEHOLDER, events[0])
        self.assertNotIn("JsCode(", events[0])

    def test_set_events_full_chain(self):
        """验证 set_events 在完整链式调用中的使用。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_events(
                {
                    ChartEvent.ELEMENT_CLICK: "(ev) => { console.log(ev.data); }",
                }
            )
        )
        self.assertEqual(chart.options.get("type"), "line")
        self.assertEqual(len(list(chart.js_events.items)), 1)

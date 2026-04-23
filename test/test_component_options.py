"""组件选项（Tooltip、Label、Legend 等）测试。"""

import unittest
from pyantv.options import (
    LegendTitleOpts,
    LegendLayoutOpts,
    LegendCategoryCfgOpts,
    TooltipItemOpts,
    TooltipOpts,
    LabelOpts,
    ScrollBarStyleOpts,
    SliderStyleOpts,
)


class TestComponentOptions(unittest.TestCase):

    def test_legend_title_opts_with_params(self):
        """验证 LegendTitleOpts 带参数时 opts 字典正确映射。"""
        obj = LegendTitleOpts(title="Legend", title_spacing=8, title_font_size=14)
        self.assertEqual(obj.opts["title"], "Legend")
        self.assertEqual(obj.opts["titleSpacing"], 8)
        self.assertEqual(obj.opts["titleFontSize"], 14)

    def test_legend_layout_opts_with_params(self):
        """验证 LegendLayoutOpts 带参数时 opts 字典正确映射。"""
        obj = LegendLayoutOpts(cols=2, col_padding=10, row_padding=5)
        self.assertEqual(obj.opts["cols"], 2)
        self.assertEqual(obj.opts["colPadding"], 10)
        self.assertEqual(obj.opts["rowPadding"], 5)

    def test_legend_category_cfg_opts_with_params(self):
        """验证 LegendCategoryCfgOpts 带参数时 opts 字典正确映射。"""
        title = LegendTitleOpts(title="Category")
        layout = LegendLayoutOpts(cols=2)
        obj = LegendCategoryCfgOpts(
            position="right", title_opts=title, layout_opts=layout
        )
        self.assertEqual(obj.opts["position"], "right")
        self.assertEqual(
            obj.opts["title"],
            {
                "title": "Category",
                "titleSpacing": None,
                "titleInset": None,
                "titlePosition": None,
                "titleFontSize": None,
                "titleFontFamily": None,
                "titleFontWeight": None,
                "titleFill": None,
                "titleFillOpacity": None,
                "titleStroke": None,
                "titleStrokeOpacity": None,
            },
        )
        self.assertEqual(
            obj.opts["layout"],
            {
                "cols": 2,
                "colPadding": None,
                "rowPadding": None,
                "maxRows": None,
                "maxCols": None,
                "justifyContent": None,
                "alignItems": None,
                "flexDirection": None,
            },
        )

    def test_tooltip_item_opts_with_params(self):
        """验证 TooltipItemOpts 带参数时 opts 字典正确映射。"""
        obj = TooltipItemOpts(field="value", channel="y", value_formatter="{d}")
        self.assertEqual(obj.opts["field"], "value")
        self.assertEqual(obj.opts["channel"], "y")
        self.assertEqual(obj.opts["valueFormatter"], "{d}")

    def test_tooltip_opts_with_params(self):
        """验证 TooltipOpts 带参数时 opts 字典正确映射。"""
        item = TooltipItemOpts(field="value")
        obj = TooltipOpts(title="Tooltip", items=[item])
        self.assertEqual(obj.opts["title"], "Tooltip")
        self.assertEqual(obj.opts["items"][0].opts["field"], "value")

    def test_label_opts_with_params(self):
        """验证 LabelOpts 带参数时 opts 字典正确映射。"""
        obj = LabelOpts(font_size=12, text_align="center", fill="#333")
        self.assertEqual(obj.opts["fontSize"], 12)
        self.assertEqual(obj.opts["textAlign"], "center")
        self.assertEqual(obj.opts["fill"], "#333")

    def test_scrollbar_style_opts_with_params(self):
        """验证 ScrollBarStyleOpts 带参数时 opts 字典正确映射。"""
        obj = ScrollBarStyleOpts(is_round=True, thumb_fill="#ccc", track_size=10)
        self.assertEqual(obj.opts["isRound"], True)
        self.assertEqual(obj.opts["thumbFill"], "#ccc")
        self.assertEqual(obj.opts["trackSize"], 10)

    def test_slider_style_opts_with_params(self):
        """验证 SliderStyleOpts 带参数时 opts 字典正确映射。"""
        obj = SliderStyleOpts(selection_fill="#ddd", handle_icon_size=12)
        self.assertEqual(obj.opts["selectionFill"], "#ddd")
        self.assertEqual(obj.opts["handleIconSize"], 12)


if __name__ == "__main__":
    unittest.main()

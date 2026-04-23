"""测试 Chart 类方法的参数类型校验。"""

import pytest

from pyantv import Line


class TestMethodValidation:
    """测试 Chart 类方法的参数类型校验。"""

    def test_set_encode_invalid_x_field(self):
        """测试 set_encode 传入无效的 x_field_name 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_encode"):
            chart.set_encode(x_field_name=123)

    def test_set_encode_invalid_y_field(self):
        """测试 set_encode 传入无效的 y_field_name 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_encode"):
            chart.set_encode(y_field_name=456)

    def test_set_encode_valid_str(self):
        """测试 set_encode 传入有效的字符串类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_encode(x_field_name="x", y_field_name="y")

    def test_set_encode_valid_list(self):
        """测试 set_encode 传入有效的列表类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_encode(x_field_name=["x", "y"], y_field_name=["a", "b"])

    def test_set_encode_valid_none(self):
        """测试 set_encode 传入 None 值。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_encode(x_field_name=None, y_field_name=None)

    def test_set_style_invalid(self):
        """测试 set_style 传入无效的 style_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_style"):
            chart.set_style(style_opts=123)

    def test_set_style_valid_dict(self):
        """测试 set_style 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_style(style_opts={"fill": "red"})

    def test_set_style_valid_none(self):
        """测试 set_style 传入 None 值。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_style(style_opts=None)

    def test_set_labels_invalid(self):
        """测试 set_labels 传入无效的 label_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_labels"):
            chart.set_labels(label_opts=123)

    def test_set_labels_valid_dict(self):
        """测试 set_labels 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_labels(label_opts={"text": "value"})

    def test_set_labels_valid_none(self):
        """测试 set_labels 传入 None 值。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_labels(label_opts=None)

    def test_set_tooltip_invalid(self):
        """测试 set_tooltip 传入无效的 tooltip_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_tooltip"):
            chart.set_tooltip(tooltip_opts=123)

    def test_set_tooltip_valid_dict(self):
        """测试 set_tooltip 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_tooltip(tooltip_opts={"show": True})

    def test_set_axis_invalid(self):
        """测试 set_axis 传入无效的 axis_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_axis"):
            chart.set_axis(axis_opts=123)

    def test_set_axis_valid_dict(self):
        """测试 set_axis 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_axis(axis_opts={"title": "X Axis"})

    def test_set_legend_invalid(self):
        """测试 set_legend 传入无效的 legend_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_legend"):
            chart.set_legend(legend_opts=42)

    def test_set_legend_valid_dict(self):
        """测试 set_legend 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_legend(legend_opts={"position": "top"})

    def test_set_theme_invalid(self):
        """测试 set_theme 传入无效的 theme 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_theme\\(\\) expected str or dict"):
            chart.set_theme(theme=123)

    def test_set_theme_valid_str(self):
        """测试 set_theme 传入有效的字符串类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_theme(theme="dark")

    def test_set_theme_valid_dict(self):
        """测试 set_theme 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_theme(theme={"type": "dark"})

    def test_set_theme_valid_none(self):
        """测试 set_theme 传入 None 值。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_theme(theme=None)

    def test_set_transform_invalid(self):
        """测试 set_transform 传入无效的 transform_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_transform"):
            chart.set_transform(transform_opts="invalid")

    def test_set_transform_valid_dict(self):
        """测试 set_transform 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_transform(transform_opts={"type": "groupX"})

    def test_set_transform_valid_list(self):
        """测试 set_transform 传入有效的列表类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_transform(transform_opts=[])

    def test_set_transform_valid_none(self):
        """测试 set_transform 传入 None 值。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_transform(transform_opts=None)

    def test_set_coordinate_invalid(self):
        """测试 set_coordinate 传入无效的 coordinate_opts 类型。"""
        chart = Line()
        with pytest.raises(TypeError, match="set_coordinate"):
            chart.set_coordinate(coordinate_opts=123)

    def test_set_coordinate_valid_dict(self):
        """测试 set_coordinate 传入有效的字典类型。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_coordinate(coordinate_opts={"type": "polar"})

    def test_set_coordinate_valid_none(self):
        """测试 set_coordinate 传入 None 值。"""
        chart = Line()
        # 应该正常执行，不抛出异常
        chart.set_coordinate(coordinate_opts=None)

"""Animation 动画枚举常量和缓动函数测试。"""

import unittest

from pyantv.globals import AnimationType, EasingType
from pyantv.charts import Line
from pyantv.options import AnimateOpts, AnimatePropertiesOpts


class TestAnimationConstants(unittest.TestCase):

    def test_animation_type_constants(self):
        """验证动画类型枚举常量值正确。"""
        self.assertEqual(AnimationType.FADE_IN, "fadeIn")
        self.assertEqual(AnimationType.FADE_OUT, "fadeOut")
        self.assertEqual(AnimationType.GROW_IN_X, "growInX")
        self.assertEqual(AnimationType.GROW_IN_Y, "growInY")
        self.assertEqual(AnimationType.SCALE_IN_X, "scaleInX")
        self.assertEqual(AnimationType.SCALE_IN_Y, "scaleInY")
        self.assertEqual(AnimationType.WAVE_IN, "waveIn")
        self.assertEqual(AnimationType.ZOOM_IN, "zoomIn")
        self.assertEqual(AnimationType.ZOOM_OUT, "zoomOut")
        self.assertEqual(AnimationType.PATH_IN, "pathIn")
        self.assertEqual(AnimationType.MORPH, "morph")

    def test_easing_type_constants(self):
        """验证缓动函数枚举常量值正确。"""
        self.assertEqual(EasingType.LINEAR, "linear")
        self.assertEqual(EasingType.EASE, "ease")
        self.assertEqual(EasingType.EASE_IN, "ease-in")
        self.assertEqual(EasingType.EASE_OUT, "ease-out")
        self.assertEqual(EasingType.EASE_IN_OUT, "ease-in-out")
        self.assertEqual(EasingType.EASE_IN_CUBIC, "ease-in-cubic")
        self.assertEqual(EasingType.EASE_OUT_BOUNCE, "ease-out-bounce")
        self.assertEqual(EasingType.EASE_IN_OUT_ELASTIC, "ease-in-out-elastic")

    def test_animation_constants_with_animate_opts(self):
        """验证动画常量可以与 AnimatePropertiesOpts 配合使用。"""
        enter = AnimatePropertiesOpts(
            type_=AnimationType.FADE_IN,
            duration=800,
            easing=EasingType.EASE_IN_OUT,
        )
        self.assertEqual(enter.opts["type"], "fadeIn")
        self.assertEqual(enter.opts["easing"], "ease-in-out")

    def test_animation_constants_integration(self):
        """验证动画常量在完整图表构建链路中正确使用。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_animate(
                animate_opts=AnimateOpts(
                    enter_opts=AnimatePropertiesOpts(
                        type_=AnimationType.WAVE_IN,
                        duration=1000,
                        easing=EasingType.EASE_OUT_CUBIC,
                    ),
                    exit_opts=AnimatePropertiesOpts(
                        type_=AnimationType.FADE_OUT,
                        duration=500,
                    ),
                )
            )
        )
        anim = line.options.get("animate")
        self.assertEqual(anim.opts["enter"].opts["type"], "waveIn")
        self.assertEqual(anim.opts["enter"].opts["easing"], "ease-out-cubic")
        self.assertEqual(anim.opts["exit"].opts["type"], "fadeOut")

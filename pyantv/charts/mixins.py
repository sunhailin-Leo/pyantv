from __future__ import annotations

from ..render import engine

import sys
from typing import Any

if sys.version_info >= (3, 11):
    from typing import Self
else:
    try:
        from typing_extensions import Self
    except ImportError:
        Self = Any  # type: ignore[assignment,misc]


_VALID_RENDERERS = ("canvas", "svg", "webgl")


class ChartMixin:
    def add_js_dependencies(self, *dependencies: str) -> Self:
        """添加 JS 依赖。

        :param dependencies: JS 依赖包名称，可传入多个。
        :returns: 图表对象自身，支持链式调用。
        """
        for dependency in dependencies:
            self.js_dependencies.add(dependency)
        return self

    def add_js_funcs(self, *fns: str) -> Self:
        """添加自定义 JS 函数。

        :param fns: JS 函数代码字符串，可传入多个。
        :returns: 图表对象自身，支持链式调用。
        """
        for fn in fns:
            self.js_functions.add(fn)
        return self

    def add_js_events(self, *fns: str) -> Self:
        """添加 JS 事件。

        :param fns: JS 事件代码字符串，可传入多个。
        :returns: 图表对象自身，支持链式调用。
        """
        for fn in fns:
            self.js_events.add(fn)
        return self

    def load_javascript(self):
        """加载 JavaScript 资源。

        :returns: Javascript 对象。
        """
        return engine.load_javascript(self)

    def use_renderer(self, renderer_type: str = "canvas") -> Self:
        """切换渲染器类型。

        :param renderer_type: 渲染器类型，可选 ``canvas``、``svg``、``webgl``。
        :returns: 图表对象自身，支持链式调用。
        :raises TypeError: 当 renderer_type 不是字符串时。
        :raises ValueError: 当 renderer_type 不是合法值时。
        """
        if not isinstance(renderer_type, str):
            raise TypeError(
                "use_renderer() expected str, got {} (type: {})".format(
                    renderer_type, type(renderer_type).__name__
                )
            )
        renderer_lower = renderer_type.lower()
        if renderer_lower not in _VALID_RENDERERS:
            raise ValueError(
                "Unsupported renderer '{}', must be one of: {}".format(
                    renderer_type, ", ".join(_VALID_RENDERERS)
                )
            )
        self.options.update(renderer=renderer_lower)
        return self

    def use_rough(self, roughness: float = 1.5, bowing: float = 1.0) -> Self:
        """启用手绘风格渲染（Rough 插件）。

        :param roughness: 粗糙度，值越大线条越粗糙。
        :param bowing: 弯曲度，值越大线条越弯曲。
        :returns: 图表对象自身，支持链式调用。
        """
        self.add_js_dependencies("antv@G-Rough")
        self.options.update(
            rough={"roughness": roughness, "bowing": bowing}
        )
        return self

    def use_lottie(self, autoplay: bool = True) -> Self:
        """启用 Lottie 动画插件。

        :param autoplay: 是否自动播放动画。
        :returns: 图表对象自身，支持链式调用。
        """
        self.add_js_dependencies("antv@G-Lottie")
        self.options.update(lottie={"autoplay": autoplay})
        return self


class JsonRenderMixin:
    def set_json_encoder(self, encoder: Any = None) -> Self:
        """设置自定义 JSON 编码器。

        :param encoder: 自定义 JSON 编码器类。
        :returns: 图表对象自身，支持链式调用。
        """
        self.json_encoder = encoder

        return self

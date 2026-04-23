import datetime
import uuid

import simplejson as json
from jinja2 import Environment

from ..commons import utils
from ..globals import CurrentConfig
from ..options import InitOpts, RenderOpts
from ..options.series_options import BasicOpts
from ..render import engine
from ..types import Optional, Union
from .mixins import ChartMixin, JsonRenderMixin


class Base(ChartMixin, JsonRenderMixin):
    """
    `Base` is the root class for all graphical class, it provides
    part of the initialization parameters and common methods
    """

    def __init__(
        self,
        init_opts: Union[InitOpts, dict] = InitOpts(),
        render_opts: Union[RenderOpts, dict] = RenderOpts(),
    ):
        if not isinstance(init_opts, (InitOpts, dict)):
            raise TypeError(
                "init_opts expected InitOpts or dict, "
                "got {} (type: {})".format(
                    init_opts, type(init_opts).__name__
                )
            )
        if not isinstance(render_opts, (RenderOpts, dict)):
            raise TypeError(
                "render_opts expected RenderOpts or dict, "
                "got {} (type: {})".format(
                    render_opts, type(render_opts).__name__
                )
            )

        # default json encoder
        self.json_encoder = None

        _opts = init_opts
        if isinstance(init_opts, InitOpts):
            _opts = init_opts.opts

        _render_opts = render_opts
        if isinstance(render_opts, RenderOpts):
            _render_opts = render_opts.opts

        self.width = _opts.get("width", "900px")
        self.height = _opts.get("height", "500px")
        self.horizontal_center = (
            "text-align:center; margin: auto"
            if _opts.get("is_horizontal_center", False)
            else ""
        )
        self.page_title = _opts.get("page_title", CurrentConfig.PAGE_TITLE)
        self.fill_bg = _opts.get("fill_bg", False)
        self.bg_color = _opts.get("bg_color")

        self.options: dict = {}
        self.init_options: dict = _opts
        self.render_options: dict = _render_opts
        self.chart_id = _render_opts.get("container") or uuid.uuid4().hex
        self.render_options.update(container=self.chart_id)
        self._embed_js = _opts.get("is_embed_js")

        self.js_host: Optional[str] = _opts.get("js_host") or self._get_default_js_host()
        self.js_dependencies: utils.OrderedSet = utils.OrderedSet("antv@G2")
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_events: utils.OrderedSet = utils.OrderedSet()
        self.options.update(backgroundColor=self.bg_color)

        self._is_geo_chart: bool = False

        self._render_cache: dict = dict()

    @staticmethod
    def _get_default_js_host() -> str:
        """获取默认的 JS host，优先使用 offline host。

        优先级：OFFLINE_HOST > 环境变量 PYANTV_OFFLINE_HOST > ONLINE_HOST。

        :returns: 当前应使用的 host URL。
        """
        from ..offline import get_active_host

        return get_active_host()

    def get_chart_id(self) -> str:
        """获取图表唯一标识。

        :returns: 图表的唯一标识符。
        """
        return self.chart_id

    def get_render_options(self) -> dict:
        """获取渲染配置字典。

        :returns: 渲染配置字典。
        """
        return utils.remove_key_with_none_value(self.render_options)

    def get_options(self) -> dict:
        """获取图表配置字典。

        :returns: 图表配置字典。
        """
        return utils.remove_key_with_none_value(self.options)

    def dump_render_options(self):
        """序列化渲染配置为 JSON 字符串。

        :returns: JSON 格式的渲染配置字符串。
        """
        return utils.replace_placeholder(
            json.dumps(
                self.get_render_options(),
                default=default,
                ignore_nan=True,
                cls=self.json_encoder,
            )
        )

    def dump_options(self, compact: bool = False) -> str:
        """序列化图表配置为 JSON 字符串。

        :param compact: 是否使用紧凑格式（无缩进、无空格），默认 False。
        :returns: JSON 配置字符串。
        """
        if compact:
            return utils.replace_placeholder(
                json.dumps(
                    self.get_options(),
                    separators=(',', ':'),
                    default=default,
                    ignore_nan=True,
                    cls=self.json_encoder,
                )
            )
        return utils.replace_placeholder(
            json.dumps(
                self.get_options(),
                indent=4,
                default=default,
                ignore_nan=True,
                cls=self.json_encoder,
            )
        )

    def dump_options_with_quotes(self) -> str:
        """序列化图表配置（保留引号）。

        :returns: 保留引号的 JSON 配置字符串。
        """
        return utils.replace_placeholder_with_quotes(
            json.dumps(
                self.get_options(),
                indent=4,
                default=default,
                ignore_nan=True,
                cls=self.json_encoder,
            )
        )

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_chart.html",
        env: Optional[Environment] = None,
        compact: bool = False,
        **kwargs,
    ) -> str:
        """渲染图表为 HTML 文件。

        :param path: 输出文件路径，默认 ``render.html``。
        :param template_name: 模板文件名称，默认 ``simple_chart.html``。
        :param env: Jinja2 环境对象，默认使用全局环境。
        :param compact: 是否使用紧凑格式 dump_options。
        :returns: 输出文件的绝对路径。
        """
        self._prepare_render(compact=compact)
        return engine.render(self, path, template_name, env, **kwargs)

    def render_embed(
        self,
        template_name: str = "simple_chart.html",
        env: Optional[Environment] = None,
        compact: bool = False,
        **kwargs,
    ) -> str:
        """渲染图表为 HTML 字符串。

        :param template_name: 模板文件名称，默认 ``simple_chart.html``。
        :param env: Jinja2 环境对象，默认使用全局环境。
        :param compact: 是否使用紧凑格式 dump_options。
        :returns: HTML 字符串。
        """
        self._prepare_render(compact=compact)
        return engine.render_embed(self, template_name, env, **kwargs)

    def _repr_html_(self) -> Optional[str]:
        """Jupyter Notebook HTML 表示。

        返回完整的 iframe HTML 字符串，包含 AntV G2 CDN script 和图表配置。
        使用 iframe srcdoc 嵌入，避免 CSS/JS 污染宿主页面。
        非 Notebook 环境下返回 None（IPython 协议规范）。

        :returns: HTML 内容字符串或 None。
        """
        from ..render.notebook import build_iframe_html, is_notebook

        if not is_notebook():
            return None

        self._prepare_render()
        # 解析 JS/CSS 依赖链接
        from ..render.engine import RenderEngine
        RenderEngine().generate_js_link(self)

        return build_iframe_html(
            chart_options_json=self.json_contents,
            js_links=getattr(self, "dependencies", []),
            css_links=getattr(self, "css_libs", []),
            chart_id=self.chart_id,
            render_options_json=self.render_contents,
        )

    def render_notebook(self):
        """在 Notebook 中渲染图表。

        :returns: HTML 对象，用于在 Jupyter Notebook 中显示。
        """
        self.chart_id = uuid.uuid4().hex
        self._prepare_render()
        return engine.render_notebook(
            self, "nb_jupyter_notebook.html", "nb_jupyter_lab.html"
        )

    def save_as_image(
        self,
        path: str = "chart.png",
        width: int = 1200,
        height: int = 800,
    ):
        """将图表导出为 PNG 图片。

        需要安装 Playwright（``pip install playwright``）并执行
        ``playwright install chromium`` 安装浏览器。

        :param path: 输出文件路径，默认 ``chart.png``。
        :param width: 视口宽度（像素），默认 1200。
        :param height: 视口高度（像素），默认 800。
        :raises ImportError: 当 Playwright 未安装时。
        """
        from ..render.export import export_png

        export_png(self, path=path, width=width, height=height)

    def render_widget(self, width="100%", height="500px"):
        """在 Jupyter Lab 中以 Widget 形式渲染图表。

        需要安装 ipywidgets（pip install ipywidgets）。

        :param width: Widget 宽度，默认 "100%"。
        :param height: Widget 高度，默认 "500px"。
        :returns: ipywidgets.HTML Widget 对象。
        :raises ImportError: 当 ipywidgets 未安装时。
        """
        from ..web.widget import render_widget as _render_widget
        return _render_widget(self, width=width, height=height)

    def save_as_svg(
        self,
        path: str = "chart.svg",
        width: int = 1200,
        height: int = 800,
    ):
        """将图表导出为 SVG 矢量图。

        需要安装 Playwright（``pip install playwright``）并执行
        ``playwright install chromium`` 安装浏览器。

        :param path: 输出文件路径，默认 ``chart.svg``。
        :param width: 视口宽度（像素），默认 1200。
        :param height: 视口高度（像素），默认 800。
        :raises ImportError: 当 Playwright 未安装时。
        """
        from ..render.export import export_svg

        export_svg(self, path=path, width=width, height=height)

    def _validate_config(self):
        """渲染前配置完整性校验，缺少关键配置时发出警告。

        组合图表（含 ``children`` 的 View 等）会跳过校验，
        因为数据和编码由子图表提供。
        """
        import warnings

        if self.options.get("children"):
            return

        chart_type = self.options.get("type") or getattr(
            self, "_chart_type", None
        )
        data = self.options.get("data")
        encode = self.options.get("encode")

        if data is None and chart_type is not None:
            warnings.warn(
                "Chart '{}' has no data set. "
                "Call set_data() before render().".format(
                    chart_type or self.__class__.__name__
                ),
                UserWarning,
                stacklevel=4,
            )

        if encode is None and chart_type is not None:
            warnings.warn(
                "Chart '{}' has no encode set. "
                "Call set_encode() before render().".format(
                    chart_type or self.__class__.__name__
                ),
                UserWarning,
                stacklevel=4,
            )

    def export_config(self) -> dict:
        """导出图表的完整配置为可序列化字典。

        返回包含 ``options`` 和 ``render_options`` 的字典，
        可通过 :meth:`from_config` 重新加载。所有 Opts 对象会被
        自动转换为纯字典，保证结果可直接 JSON 序列化。

        :returns: 图表配置字典。

        Examples:
            >>> config = chart.export_config()
            >>> import json
            >>> json.dump(config, open("chart_config.json", "w"))
        """
        options = json.loads(
            json.dumps(
                self.get_options(),
                default=default,
                ignore_nan=True,
                cls=self.json_encoder,
            )
        )
        return {
            "chart_class": "{}.{}".format(
                self.__class__.__module__,
                self.__class__.__name__,
            ),
            "options": options,
            "render_options": self.get_render_options(),
            "init_options": utils.remove_key_with_none_value(
                self.init_options
            ),
        }

    @classmethod
    def from_config(cls, config: dict):
        """从配置字典创建图表实例。

        :param config: 由 :meth:`export_config` 生成的配置字典。
        :returns: 新的图表实例。

        Examples:
            >>> import json
            >>> config = json.load(open("chart_config.json"))
            >>> chart = Line.from_config(config)
        """
        init_options = config.get("init_options", {})
        render_options = config.get("render_options", {})
        chart = cls(
            init_opts=init_options if init_options else InitOpts(),
            render_opts=render_options if render_options else RenderOpts(),
        )
        options = config.get("options", {})
        chart.options.update(options)
        return chart

    def _prepare_render(self, compact: bool = False):
        self._validate_config()
        self.render_contents = self.dump_render_options()
        self.json_contents = self.dump_options(compact=compact)
        self._render_cache.clear()
        if self._embed_js:
            self._render_cache["javascript"] = (
                self.load_javascript().load_javascript_contents()
            )


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, utils.JsCode):
        return (
            o.replace("\\n|\\t", "").replace(r"\\n", "\n").replace(r"\\t", "\t").js_code
        )
    if isinstance(o, BasicOpts):
        # if isinstance(o.opts, Sequence):
        #     return [utils.remove_key_with_none_value(item) for item in o.opts]
        # else:
        return utils.remove_key_with_none_value(o.opts)

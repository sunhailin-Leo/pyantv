import os
from collections.abc import Iterable

from jinja2 import Environment

from ..commons import utils
from ..datasets import EXTRA, FILENAMES
from ..globals import CurrentConfig, NotebookType, RenderSepType
from ..types import Any, Optional
from .display import HTML, Javascript


def write_utf8_html_file(file_name: str, html_content: str):
    """写入 UTF-8 HTML 文件。

    :param file_name: 输出文件路径。
    :param html_content: HTML 内容字符串。
    """
    with open(
        file=file_name, mode="w+", encoding="utf-8", newline=RenderSepType.SepType
    ) as html_file:
        html_file.write(html_content)


_template_cache: dict = {}


class RenderEngine:
    def __init__(self, env: Optional[Environment] = None):
        """初始化渲染引擎。

        :param env: Jinja2 环境对象，默认使用全局环境。
        """
        self.env = env or CurrentConfig.GLOBAL_ENV

    def _get_template(self, template_name: str):
        """获取模板，优先从缓存中读取以避免重复解析。

        :param template_name: 模板文件名称。
        :returns: 编译好的 Jinja2 模板对象。
        """
        cache_key = (id(self.env), template_name)
        cached = _template_cache.get(cache_key)
        if cached is not None:
            return cached
        tpl = self.env.get_template(template_name)
        _template_cache[cache_key] = tpl
        return tpl

    @staticmethod
    def generate_js_link(chart: Any) -> Any:
        """解析图表依赖并生成 JS/CSS 资源链接。"""
        if not chart.js_host:
            chart.js_host = CurrentConfig.ONLINE_HOST
        links = []
        css_links = []
        for dep in chart.js_dependencies.items:
            if dep in FILENAMES:
                f, ext = FILENAMES[dep]
                _link = "{}{}.{}".format(chart.js_host, f, ext)
                links.append(_link)
            else:
                found = False
                for url, files in EXTRA.items():
                    if dep in files:
                        f, ext = files[dep]
                        _link = "{}{}.{}".format(url, f, ext)
                        if ext == "css":
                            css_links.append(_link)
                        else:
                            links.append(_link)
                        found = True
                        break
                if not found:
                    import warnings
                    warnings.warn(
                        "Unknown dependency '{}', skipping.".format(dep)
                    )
        chart.dependencies = links
        chart.css_libs = css_links
        return chart

    def render_chart_to_file(self, template_name: str, chart: Any, path: str, **kwargs):
        """渲染图表到文件。

        :param template_name: 模板文件名称。
        :param chart: 图表或页面对象。
        :param path: 输出文件路径。
        """
        tpl = self._get_template(template_name)
        html = utils.replace_placeholder(
            tpl.render(chart=self.generate_js_link(chart), **kwargs)
        )
        write_utf8_html_file(path, html)

    def render_chart_to_template(self, template_name: str, chart: Any, **kwargs) -> str:
        """渲染图表为模板字符串。

        :param template_name: 模板文件名称。
        :param chart: 图表或页面对象。
        :returns: 渲染后的 HTML 字符串。
        """
        tpl = self._get_template(template_name)
        return utils.replace_placeholder(
            tpl.render(chart=self.generate_js_link(chart), **kwargs)
        )

    def render_chart_to_notebook(self, template_name: str, **kwargs) -> str:
        """渲染图表到 Notebook。

        :param template_name: 模板文件名称。
        :returns: 渲染后的 HTML 字符串。
        """
        tpl = self._get_template(template_name)
        return utils.replace_placeholder(tpl.render(**kwargs))


def render(
    chart, path: str, template_name: str, env: Optional[Environment], **kwargs
) -> str:
    """渲染入口。

    :param chart: 图表或页面对象。
    :param path: 输出文件路径。
    :param template_name: 模板文件名称。
    :param env: Jinja2 环境对象。
    :returns: 输出文件的绝对路径。
    """
    RenderEngine(env).render_chart_to_file(
        template_name=template_name, chart=chart, path=path, **kwargs
    )
    return os.path.abspath(path)


def render_embed(
    chart, template_name: str, env: Optional[Environment], **kwargs
) -> str:
    """嵌入式渲染。

    :param chart: 图表或页面对象。
    :param template_name: 模板文件名称。
    :param env: Jinja2 环境对象。
    :returns: 渲染后的 HTML 字符串。
    """
    return RenderEngine(env).render_chart_to_template(
        template_name=template_name, chart=chart, **kwargs
    )


def render_notebook(self, notebook_template, lab_template):
    """Notebook 渲染。

    :param notebook_template: Jupyter Notebook 模板名称。
    :param lab_template: Jupyter Lab 模板名称。
    :returns: HTML 对象，用于在 Notebook 中显示。
    """
    instance = self if isinstance(self, Iterable) else (self,)
    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
        require_config = utils.produce_require_dict(self.js_dependencies, self.js_host)
        return HTML(
            RenderEngine().render_chart_to_notebook(
                template_name=notebook_template,
                charts=instance,
                config_items=require_config["config_items"],
                libraries=require_config["libraries"],
            )
        )

    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_LAB:
        return HTML(
            RenderEngine().render_chart_to_notebook(
                template_name=lab_template, charts=instance
            )
        )

    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.NTERACT:
        return HTML(self.render_embed())

    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.ZEPPELIN:
        print("%html " + self.render_embed())


def load_javascript(chart):
    """加载 JS 资源。

    :param chart: 图表对象。
    :returns: Javascript 对象。
    """
    scripts = []
    for dep in chart.js_dependencies.items:
        f, ext = FILENAMES[dep]
        scripts.append("{}{}.{}".format(CurrentConfig.ONLINE_HOST, f, ext))
    return Javascript(lib=scripts)

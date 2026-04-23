import http.client
from urllib.parse import urlparse

from ..types import Optional, Sequence, Union


class HTML:
    """HTML 显示包装类，用于在 Jupyter Notebook 中显示 HTML 内容。"""

    def __init__(self, data: Optional[str] = None):
        """初始化 HTML 对象。

        :param data: HTML 内容字符串。
        """
        self.data = data

    def _repr_html_(self):
        """Jupyter Notebook HTML 表示。

        :returns: HTML 内容字符串。
        """
        return self.data

    def __html__(self):
        """通用 HTML 表示。

        :returns: HTML 内容字符串。
        """
        return self._repr_html_()


_lib_t1 = """new Promise(function(resolve, reject) {
    var script = document.createElement("script");
    script.onload = resolve;
    script.onerror = reject;
    script.src = "%s";
    document.head.appendChild(script);
}).then(() => {
"""

_lib_t2 = """
});"""

_css_t = """var link = document.createElement("link");
    link.ref = "stylesheet";
    link.type = "text/css";
    link.href = "%s";
    document.head.appendChild(link);
"""


class Javascript:
    """JavaScript 显示包装类，用于在 Jupyter Notebook 中执行 JavaScript 代码。"""

    def __init__(
        self,
        data: Optional[str] = None,
        lib: Optional[Union[str, Sequence]] = None,
        css: Optional[Union[str, Sequence]] = None,
    ):
        """初始化 Javascript 对象。

        :param data: JavaScript 代码字符串。
        :param lib: JS 库 URL，可以是字符串或列表。
        :param css: CSS 库 URL，可以是字符串或列表。
        """
        if isinstance(lib, str):
            lib = [lib]
        elif lib is None:
            lib = []
        if isinstance(css, str):
            css = [css]
        elif css is None:
            css = []
        self.lib = lib
        self.css = css
        self.data = data or ""
        self.javascript_contents = dict()

    def _repr_javascript_(self):
        """Jupyter Notebook JavaScript 表示。

        :returns: 完整的 JavaScript 代码字符串（包含依赖加载）。
        """
        r = ""
        for c in self.css:
            r += _css_t % c
        for d in self.lib:
            r += _lib_t1 % d
        r += self.data
        r += _lib_t2 * len(self.lib)
        return r

    def load_javascript_contents(self):
        """从远程加载 JS 依赖内容，带超时和错误处理。"""
        for lib in self.lib:
            parsed_url = urlparse(lib)

            host: str = str(parsed_url.hostname)
            port: int = parsed_url.port
            path: str = parsed_url.path

            resp: Optional[http.client.HTTPResponse] = None
            try:
                conn = http.client.HTTPSConnection(host, port, timeout=15)
                conn.request("GET", path)
                resp = conn.getresponse()
                if resp.status not in [200, 302]:
                    raise RuntimeError("Cannot load JavaScript lib: %s" % lib)
                self.javascript_contents[lib] = resp.read().decode("utf-8")
            except (http.client.HTTPException, OSError) as exc:
                import warnings
                warnings.warn(
                    "Failed to load '{}': {}".format(lib, exc)
                )
            finally:
                if resp is not None:
                    resp.close()
        return self

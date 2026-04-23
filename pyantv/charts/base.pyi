from typing import Any, Optional

from jinja2 import Environment

from ..commons.utils import OrderedSet
from ..options import InitOpts, RenderOpts
from .mixins import ChartMixin, JsonRenderMixin

class Base(ChartMixin, JsonRenderMixin):
    json_encoder: Any
    width: str
    height: str
    horizontal_center: str
    page_title: str
    fill_bg: bool
    bg_color: Optional[str]
    options: dict
    init_options: dict
    render_options: dict
    chart_id: str
    js_host: Optional[str]
    js_dependencies: OrderedSet
    js_functions: OrderedSet
    js_events: OrderedSet
    render_contents: str
    json_contents: str

    def __init__(
        self,
        init_opts: InitOpts | dict = ...,
        render_opts: RenderOpts | dict = ...,
    ) -> None: ...
    def get_chart_id(self) -> str: ...
    def get_render_options(self) -> dict: ...
    def get_options(self) -> dict: ...
    def dump_render_options(self) -> str: ...
    def dump_options(self) -> str: ...
    def dump_options_with_quotes(self) -> str: ...
    def render(
        self,
        path: str = ...,
        template_name: str = ...,
        env: Optional[Environment] = ...,
        **kwargs: Any,
    ) -> str: ...
    def render_embed(
        self,
        template_name: str = ...,
        env: Optional[Environment] = ...,
        **kwargs: Any,
    ) -> str: ...
    def render_notebook(self) -> Any: ...

import os

from jinja2 import Environment, FileSystemLoader


class _FileType:
    SVG: str = "svg"
    PNG: str = "png"
    JPEG: str = "jpeg"
    HTML: str = "html"


class _ChartType:
    ARC: str = "arc"
    AREA: str = "area"
    BEESWARM: str = "beeswarm"
    BOX: str = "box"
    BOXPLOT: str = "boxplot"
    CELL: str = "cell"
    CHORD: str = "chord"
    CONNECTOR: str = "connector"
    DENSITY: str = "density"
    FACETCIRCLE: str = "facetCircle"
    FACETRECT: str = "facetRect"
    FORCEGRAPH: str = "forceGraph"
    GAUGE: str = "gauge"
    GEOPATH: str = "geoPath"
    GEOVIEW: str = "geoView"
    HEATMAP: str = "heatmap"
    IMAGE: str = "image"
    INTERVAL: str = "interval"
    INTERVAL3D: str = "interval3D"
    LINE: str = "line"
    LINE3D: str = "line3D"
    LINEX: str = "lineX"
    LINEY: str = "lineY"
    LINK: str = "link"
    LIQUID: str = "liquid"
    PACK: str = "pack"
    PARTITION: str = "partition"
    PATH: str = "path"
    POINT: str = "point"
    POINT3D: str = "point3D"
    POLYGON: str = "polygon"
    RANGE: str = "range"
    RANGEX: str = "rangeX"
    RANGEY: str = "rangeY"
    RECT: str = "rect"
    REPEATMATRIX: str = "repeatMatrix"
    SANKEY: str = "sankey"
    SHAPE: str = "shape"
    SPACEFLEX: str = "spaceFlex"
    SPACELAYER: str = "spaceLayer"
    TEXT: str = "text"
    TIMINGKEYFRAME: str = "timingKeyframe"
    TREE: str = "tree"
    TREEMAP: str = "treemap"
    VECTOR: str = "vector"
    VIEW: str = "view"
    WORDCLOUD: str = "wordCloud"


class _ThemeType:
    CLASSIC = "classic"
    DARK = "dark"
    ACADEMY = "academy"


class _AnimationType:
    FADE_IN = "fadeIn"
    FADE_OUT = "fadeOut"
    GROW_IN_X = "growInX"
    GROW_IN_Y = "growInY"
    SCALE_IN_X = "scaleInX"
    SCALE_IN_Y = "scaleInY"
    SCALE_OUT_X = "scaleOutX"
    SCALE_OUT_Y = "scaleOutY"
    WAVE_IN = "waveIn"
    ZOOM_IN = "zoomIn"
    ZOOM_OUT = "zoomOut"
    PATH_IN = "pathIn"
    MORPH = "morph"


class _EasingType:
    LINEAR = "linear"
    EASE = "ease"
    EASE_IN = "ease-in"
    EASE_OUT = "ease-out"
    EASE_IN_OUT = "ease-in-out"
    EASE_IN_QUAD = "ease-in-quad"
    EASE_OUT_QUAD = "ease-out-quad"
    EASE_IN_OUT_QUAD = "ease-in-out-quad"
    EASE_IN_CUBIC = "ease-in-cubic"
    EASE_OUT_CUBIC = "ease-out-cubic"
    EASE_IN_OUT_CUBIC = "ease-in-out-cubic"
    EASE_IN_BACK = "ease-in-back"
    EASE_OUT_BACK = "ease-out-back"
    EASE_IN_OUT_BACK = "ease-in-out-back"
    EASE_IN_BOUNCE = "ease-in-bounce"
    EASE_OUT_BOUNCE = "ease-out-bounce"
    EASE_IN_OUT_BOUNCE = "ease-in-out-bounce"
    EASE_IN_ELASTIC = "ease-in-elastic"
    EASE_OUT_ELASTIC = "ease-out-elastic"
    EASE_IN_OUT_ELASTIC = "ease-in-out-elastic"


class _ChartEvent:
    """G2 图表事件类型常量。

    事件命名遵循 ``{prefix}:{bindEvent}`` 模式。
    前缀包括 element、plot、component、legend、axis、label、tooltip 等。
    """

    # --- 生命周期事件 ---
    BEFORE_RENDER: str = "beforerender"
    AFTER_RENDER: str = "afterrender"
    BEFORE_PAINT: str = "beforepaint"
    AFTER_PAINT: str = "afterpaint"
    BEFORE_CHANGE_DATA: str = "beforechangedata"
    AFTER_CHANGE_DATA: str = "afterchangedata"
    BEFORE_CLEAR: str = "beforeclear"
    AFTER_CLEAR: str = "afterclear"
    BEFORE_DESTROY: str = "beforedestroy"
    AFTER_DESTROY: str = "afterdestroy"
    BEFORE_CHANGE_SIZE: str = "beforechangesize"
    AFTER_CHANGE_SIZE: str = "afterchangesize"

    # --- 指针/鼠标事件（无前缀，全局级别） ---
    CLICK: str = "click"
    DBLCLICK: str = "dblclick"
    POINTER_TAP: str = "pointertap"
    POINTER_DOWN: str = "pointerdown"
    POINTER_UP: str = "pointerup"
    POINTER_MOVE: str = "pointermove"
    POINTER_OVER: str = "pointerover"
    POINTER_OUT: str = "pointerout"
    POINTER_ENTER: str = "pointerenter"
    POINTER_LEAVE: str = "pointerleave"

    # --- 元素事件 ---
    ELEMENT_CLICK: str = "element:click"
    ELEMENT_DBLCLICK: str = "element:dblclick"
    ELEMENT_POINTER_DOWN: str = "element:pointerdown"
    ELEMENT_POINTER_UP: str = "element:pointerup"
    ELEMENT_POINTER_MOVE: str = "element:pointermove"
    ELEMENT_POINTER_OVER: str = "element:pointerover"
    ELEMENT_POINTER_OUT: str = "element:pointerout"
    ELEMENT_POINTER_ENTER: str = "element:pointerenter"
    ELEMENT_POINTER_LEAVE: str = "element:pointerleave"
    ELEMENT_HIGHLIGHT: str = "element:highlight"
    ELEMENT_UNHIGHLIGHT: str = "element:unhighlight"
    ELEMENT_SELECT: str = "element:select"
    ELEMENT_UNSELECT: str = "element:unselect"

    # --- 绘图区事件 ---
    PLOT_CLICK: str = "plot:click"
    PLOT_DBLCLICK: str = "plot:dblclick"
    PLOT_POINTER_DOWN: str = "plot:pointerdown"
    PLOT_POINTER_UP: str = "plot:pointerup"
    PLOT_POINTER_MOVE: str = "plot:pointermove"
    PLOT_POINTER_OVER: str = "plot:pointerover"
    PLOT_POINTER_OUT: str = "plot:pointerout"
    PLOT_POINTER_ENTER: str = "plot:pointerenter"
    PLOT_POINTER_LEAVE: str = "plot:pointerleave"

    # --- 组件事件 ---
    COMPONENT_CLICK: str = "component:click"
    COMPONENT_DBLCLICK: str = "component:dblclick"
    COMPONENT_POINTER_DOWN: str = "component:pointerdown"
    COMPONENT_POINTER_UP: str = "component:pointerup"
    COMPONENT_POINTER_MOVE: str = "component:pointermove"
    COMPONENT_POINTER_OVER: str = "component:pointerover"
    COMPONENT_POINTER_OUT: str = "component:pointerout"
    COMPONENT_POINTER_ENTER: str = "component:pointerenter"
    COMPONENT_POINTER_LEAVE: str = "component:pointerleave"

    # --- 交互事件 ---
    BRUSH_FILTER: str = "brush:filter"
    BRUSH_HIGHLIGHT: str = "brush:highlight"
    BRUSH_REMOVE: str = "brush:remove"
    BRUSH_START: str = "brush:start"
    BRUSH_END: str = "brush:end"
    LEGEND_FILTER: str = "legend:filter"
    LEGEND_RESET: str = "legend:reset"
    LEGEND_HIGHLIGHT: str = "legend:highlight"
    LEGEND_UNHIGHLIGHT: str = "legend:unhighlight"
    TOOLTIP_SHOW: str = "tooltip:show"
    TOOLTIP_HIDE: str = "tooltip:hide"
    TOOLTIP_DISABLE: str = "tooltip:disable"
    TOOLTIP_ENABLE: str = "tooltip:enable"
    SLIDER_FILTER: str = "slider:filter"
    SCROLLBAR_FILTER: str = "scrollbar:filter"


class _NotebookType:
    JUPYTER_NOTEBOOK = "jupyter_notebook"
    JUPYTER_LAB = "jupyter_lab"
    NTERACT = "nteract"
    ZEPPELIN = "zeppelin"


class _OnlineHost:
    DEFAULT_HOST = "https://unpkg.com/"
    NOTEBOOK_HOST = "http://localhost:8888/nbextensions/assets/"


class _RenderSepType:
    SepType = os.linesep


FileType = _FileType()
ChartType = _ChartType
ChartEvent = _ChartEvent()
ThemeType = _ThemeType()
AnimationType = _AnimationType()
EasingType = _EasingType()
NotebookType = _NotebookType()
OnlineHostType = _OnlineHost()
RenderSepType = _RenderSepType()


class _CurrentConfig:
    PAGE_TITLE = "Awesome-pyantv"
    ONLINE_HOST = OnlineHostType.DEFAULT_HOST
    OFFLINE_HOST = ""  # 离线 host，优先于 ONLINE_HOST 使用
    NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    GLOBAL_ENV = Environment(
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=True,
        loader=FileSystemLoader(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "render", "templates"
            )
        ),
    )


CurrentConfig = _CurrentConfig()

__all__ = [
    "FileType",
    "ChartType",
    "ChartEvent",
    "ThemeType",
    "AnimationType",
    "EasingType",
    "NotebookType",
    "OnlineHostType",
    "RenderSepType",
    "CurrentConfig",
]

import os

from jinja2 import Environment, FileSystemLoader


class _FileType:
    SVG: str = "svg"
    PNG: str = "png"
    JPEG: str = "jpeg"
    HTML: str = "html"


class _ChartType:
    AREA: str = "area"
    BOX: str = "box"
    BOXPLOT: str = "boxplot"
    CELL: str = "cell"
    CHORD: str = "chord"
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
NotebookType = _NotebookType()
OnlineHostType = _OnlineHost()
RenderSepType = _RenderSepType()


class _CurrentConfig:
    PAGE_TITLE = "Awesome-pyantv"
    ONLINE_HOST = OnlineHostType.DEFAULT_HOST
    NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    GLOBAL_ENV = Environment(
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        loader=FileSystemLoader(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "render", "templates"
            )
        ),
    )


CurrentConfig = _CurrentConfig()

"""预设配置模块。

提供常用图表配置组合的快捷函数，让用户一行代码即可应用
复杂的样式、交互、动画等配置。

所有 preset 函数接受一个 Chart 实例，应用预设配置后返回该实例，
支持链式调用。

Examples:
    >>> from pyantv import Line
    >>> from pyantv.presets import with_dark_theme, with_smooth_animation
    >>> chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
    >>> with_dark_theme(chart)
    >>> with_smooth_animation(chart)
"""

from . import options as opts
from .commons.utils import JsCode


def with_dark_theme(chart):
    """应用暗色主题。

    :param chart: 图表实例。
    :returns: 应用暗色主题后的图表实例。
    """
    chart.set_theme(theme="dark")
    return chart


def with_classic_theme(chart):
    """应用经典主题。

    :param chart: 图表实例。
    :returns: 应用经典主题后的图表实例。
    """
    chart.set_theme(theme="classic")
    return chart


def with_academy_theme(chart):
    """应用学术主题。

    :param chart: 图表实例。
    :returns: 应用学术主题后的图表实例。
    """
    chart.set_theme(theme="academy")
    return chart


def with_smooth_animation(chart, duration=1000, easing="ease-in-out-cubic"):
    """应用平滑入场动画。

    :param chart: 图表实例。
    :param duration: 动画时长（毫秒）。
    :param easing: 缓动函数名称。
    :returns: 应用动画后的图表实例。
    """
    chart.set_animate(
        animate_opts=opts.AnimateOpts(
            enter_opts=opts.AnimatePropertiesOpts(
                type_="fadeIn",
                duration=duration,
                easing=easing,
            )
        )
    )
    return chart


def with_tooltip(chart, shared=True, show_crosshairs=False):
    """应用标准 tooltip 配置。

    :param chart: 图表实例。
    :param shared: 是否共享 tooltip（多系列时显示所有系列数据）。
    :param show_crosshairs: 是否显示十字准线。
    :returns: 应用 tooltip 后的图表实例。
    """
    tooltip_config = {"shared": shared}
    if show_crosshairs:
        tooltip_config["crosshairs"] = True
    chart.set_tooltip(tooltip_opts=tooltip_config)
    return chart


def with_auto_fit(chart):
    """启用自适应容器大小。

    :param chart: 图表实例。
    :returns: 应用自适应后的图表实例。
    """
    chart.set_global_options(is_auto_fit=True)
    return chart


def with_legend_hidden(chart):
    """隐藏图例。

    :param chart: 图表实例。
    :returns: 隐藏图例后的图表实例。
    """
    chart.set_legend(legend_opts=False)
    return chart


def with_axis_hidden(chart):
    """隐藏所有坐标轴。

    :param chart: 图表实例。
    :returns: 隐藏坐标轴后的图表实例。
    """
    chart.set_axis(axis_opts=False)
    return chart


def with_labels(chart, font_size=12, position="outside"):
    """应用标准数据标签配置。

    :param chart: 图表实例。
    :param font_size: 标签字号。
    :param position: 标签位置（``"inside"``、``"outside"``、``"top"`` 等）。
    :returns: 应用标签后的图表实例。
    """
    chart.set_labels(
        label_opts=opts.LabelOpts(
            font_size=font_size,
            position=position,
        )
    )
    return chart


def with_padding(chart, top=20, right=20, bottom=20, left=20):
    """应用统一内边距。

    :param chart: 图表实例。
    :param top: 上内边距。
    :param right: 右内边距。
    :param bottom: 下内边距。
    :param left: 左内边距。
    :returns: 应用内边距后的图表实例。
    """
    chart.set_global_options(
        padding_top=top,
        padding_right=right,
        padding_bottom=bottom,
        padding_left=left,
    )
    return chart


def with_transpose(chart):
    """转置坐标系（将柱形图变为条形图）。

    :param chart: 图表实例。
    :returns: 转置后的图表实例。
    """
    chart.set_coordinate(
        coordinate_opts=opts.CoordinateTransposeOpts()
    )
    return chart


def with_polar(chart):
    """应用极坐标系（将柱形图变为玫瑰图等）。

    :param chart: 图表实例。
    :returns: 应用极坐标后的图表实例。
    """
    chart.set_coordinate(
        coordinate_opts=opts.CoordinatePolarOpts()
    )
    return chart


# ---------------------------------------------------------------------------
# 自定义主题预设
# ---------------------------------------------------------------------------

_TECH_THEME = {
    "color": [
        "#00d4ff", "#0088ff", "#7c4dff",
        "#ff4081", "#ff6e40", "#ffab40",
    ],
    "view": {"viewFill": "#0a1628"},
    "axis": {
        "gridStroke": "rgba(255,255,255,0.08)",
        "labelFill": "rgba(255,255,255,0.65)",
        "titleFill": "rgba(255,255,255,0.85)",
        "lineStroke": "rgba(255,255,255,0.15)",
        "tickStroke": "rgba(255,255,255,0.15)",
    },
}

_BUSINESS_THEME = {
    "color": [
        "#2f54eb", "#597ef7", "#85a5ff",
        "#adc6ff", "#d6e4ff", "#f0f5ff",
    ],
    "view": {"viewFill": "#ffffff"},
    "axis": {
        "gridStroke": "#f0f0f0",
        "labelFill": "#595959",
        "titleFill": "#262626",
    },
}

_FRESH_THEME = {
    "color": [
        "#36cfc9", "#73d13d", "#ffc53d",
        "#ff7a45", "#f759ab", "#9254de",
    ],
    "view": {"viewFill": "#f6ffed"},
    "axis": {
        "gridStroke": "#d9f7be",
        "labelFill": "#389e0d",
        "titleFill": "#135200",
    },
}


def with_tech_theme(chart):
    """应用科技风主题（深色背景 + 霓虹色系）。

    :param chart: 图表实例。
    :returns: 应用科技风主题后的图表实例。
    """
    chart.set_theme(theme=_TECH_THEME)
    return chart


def with_business_theme(chart):
    """应用商务风主题（白色背景 + 蓝色系）。

    :param chart: 图表实例。
    :returns: 应用商务风主题后的图表实例。
    """
    chart.set_theme(theme=_BUSINESS_THEME)
    return chart


def with_fresh_theme(chart):
    """应用清新风主题（浅绿背景 + 多彩色系）。

    :param chart: 图表实例。
    :returns: 应用清新风主题后的图表实例。
    """
    chart.set_theme(theme=_FRESH_THEME)
    return chart


# ---------------------------------------------------------------------------
# 数据格式化预设
# ---------------------------------------------------------------------------

def format_number(separator=",", precision=0):
    """生成数值格式化 JsCode（千分位分隔符）。

    :param separator: 千分位分隔符，默认逗号。
    :param precision: 小数位数。
    :returns: JsCode 对象，可用于 tooltip/label 的 formatter。

    Examples:
        >>> from pyantv.presets import format_number
        >>> chart.set_labels(label_opts=opts.LabelOpts(
        ...     formatter=format_number(precision=2)
        ... ))
    """
    js_code = (
        "(d) => d.toLocaleString('en-US', "
        "{{minimumFractionDigits: {p}, maximumFractionDigits: {p}}})"
    ).format(p=precision)
    return JsCode(js_code)


def format_percent(precision=1):
    """生成百分比格式化 JsCode。

    :param precision: 小数位数。
    :returns: JsCode 对象。

    Examples:
        >>> from pyantv.presets import format_percent
        >>> chart.set_labels(label_opts=opts.LabelOpts(
        ...     formatter=format_percent()
        ... ))
    """
    js_code = "(d) => (d * 100).toFixed({p}) + '%'".format(p=precision)
    return JsCode(js_code)


def format_currency(symbol="$", precision=2):
    """生成货币格式化 JsCode。

    :param symbol: 货币符号。
    :param precision: 小数位数。
    :returns: JsCode 对象。

    Examples:
        >>> from pyantv.presets import format_currency
        >>> chart.set_labels(label_opts=opts.LabelOpts(
        ...     formatter=format_currency(symbol="¥")
        ... ))
    """
    js_code = (
        "(d) => '{sym}' + d.toLocaleString('en-US', "
        "{{minimumFractionDigits: {p}, maximumFractionDigits: {p}}})"
    ).format(sym=symbol, p=precision)
    return JsCode(js_code)


def format_date(pattern="YYYY-MM-DD"):
    """生成日期格式化 JsCode。

    :param pattern: 日期格式模式。支持 ``YYYY``、``MM``、``DD``、
        ``HH``、``mm``、``ss``。
    :returns: JsCode 对象。

    Examples:
        >>> from pyantv.presets import format_date
        >>> chart.set_labels(label_opts=opts.LabelOpts(
        ...     formatter=format_date("YYYY/MM/DD")
        ... ))
    """
    js_body = (
        "(d) => {"
        " const dt = new Date(d);"
        " const Y = dt.getFullYear();"
        " const M = String(dt.getMonth()+1).padStart(2,'0');"
        " const D = String(dt.getDate()).padStart(2,'0');"
        " const H = String(dt.getHours()).padStart(2,'0');"
        " const m = String(dt.getMinutes()).padStart(2,'0');"
        " const s = String(dt.getSeconds()).padStart(2,'0');"
        " return '" + pattern + "'"
        ".replace('YYYY',Y)"
        ".replace('MM',M)"
        ".replace('DD',D)"
        ".replace('HH',H)"
        ".replace('mm',m)"
        ".replace('ss',s);"
        "}"
    )
    return JsCode(js_body)


# ---------------------------------------------------------------------------
# 批量导出工具
# ---------------------------------------------------------------------------

def batch_export_png(charts, output_dir, width=1200, height=800):
    """批量导出多个图表为 PNG 图片。

    :param charts: 图表列表，每个元素为 ``(chart, filename)`` 元组
        或单个图表对象（自动命名为 ``chart_0.png`` 等）。
    :param output_dir: 输出目录路径。
    :param width: 视口宽度。
    :param height: 视口高度。
    :raises ImportError: 当 Playwright 未安装时。

    Examples:
        >>> from pyantv.presets import batch_export_png
        >>> batch_export_png(
        ...     [(line, "line.png"), (bar, "bar.png")],
        ...     output_dir="./exports",
        ... )
    """
    import os
    from .render.export import export_png

    os.makedirs(output_dir, exist_ok=True)

    for index, item in enumerate(charts):
        if isinstance(item, tuple):
            chart, filename = item
        else:
            chart = item
            filename = "chart_{}.png".format(index)

        output_path = os.path.join(output_dir, filename)
        export_png(chart, output_path, width=width, height=height)


# ---------------------------------------------------------------------------
# 交互预设
# ---------------------------------------------------------------------------

def with_element_highlight(chart, background=False):
    """启用元素高亮交互（鼠标悬停时高亮当前元素）。

    :param chart: 图表实例。
    :param background: 是否显示高亮背景。
    :returns: 应用交互后的图表实例。
    """
    config = {"elementHighlight": {"background": background}}
    chart.set_interaction(interaction_opts=config)
    return chart


def with_element_select(chart, background=False):
    """启用元素选中交互（点击选中元素）。

    :param chart: 图表实例。
    :param background: 是否显示选中背景。
    :returns: 应用交互后的图表实例。
    """
    config = {"elementSelect": {"background": background}}
    chart.set_interaction(interaction_opts=config)
    return chart


def with_brush_highlight(chart):
    """启用框选高亮交互（拖拽框选区域内的元素高亮）。

    :param chart: 图表实例。
    :returns: 应用交互后的图表实例。
    """
    config = {"brushHighlight": True}
    chart.set_interaction(interaction_opts=config)
    return chart


def with_brush_filter(chart):
    """启用框选过滤交互（拖拽框选区域外的元素隐藏）。

    :param chart: 图表实例。
    :returns: 应用交互后的图表实例。
    """
    config = {"brushFilter": True}
    chart.set_interaction(interaction_opts=config)
    return chart


def with_fisheye(chart):
    """启用鱼眼放大镜交互。

    :param chart: 图表实例。
    :returns: 应用交互后的图表实例。
    """
    config = {"fisheye": True}
    chart.set_interaction(interaction_opts=config)
    return chart


def with_slider_filter(chart, x_axis=True, y_axis=False):
    """启用滑块过滤交互。

    :param chart: 图表实例。
    :param x_axis: 是否在 x 轴启用滑块。
    :param y_axis: 是否在 y 轴启用滑块。
    :returns: 应用交互后的图表实例。
    """
    slider_config = {}
    if x_axis:
        slider_config["x"] = {}
    if y_axis:
        slider_config["y"] = {}
    chart.set_global_options(slider_opts=slider_config)
    return chart


# ---------------------------------------------------------------------------
# 数据转换预设
# ---------------------------------------------------------------------------

def with_sort_by(chart, field, order="ascending"):
    """应用排序数据转换。

    :param chart: 图表实例。
    :param field: 排序字段名。
    :param order: 排序方向（``"ascending"`` 或 ``"descending"``）。
    :returns: 应用排序后的图表实例。
    """
    reverse = order == "descending"
    transform = {"type": "sortX", "reverse": reverse, "by": "y"}
    chart.set_transform(transform_opts=transform)
    return chart


def with_stack(chart):
    """应用堆叠数据转换（适用于堆叠柱状图/面积图）。

    :param chart: 图表实例。
    :returns: 应用堆叠后的图表实例。
    """
    chart.set_transform(transform_opts={"type": "stackY"})
    return chart


def with_normalize(chart):
    """应用归一化数据转换（适用于百分比堆叠图）。

    :param chart: 图表实例。
    :returns: 应用归一化后的图表实例。
    """
    chart.set_transform(
        transform_opts=[{"type": "stackY"}, {"type": "normalizeY"}]
    )
    return chart


def with_group(chart, channels=None):
    """应用分组数据转换。

    :param chart: 图表实例。
    :param channels: 分组通道列表，默认 ``["x"]``。
    :returns: 应用分组后的图表实例。
    """
    if channels is None:
        channels = ["x"]
    chart.set_transform(
        transform_opts={"type": "dodgeX"}
    )
    return chart


def with_jitter(chart):
    """应用抖动数据转换（避免数据点重叠）。

    :param chart: 图表实例。
    :returns: 应用抖动后的图表实例。
    """
    chart.set_transform(transform_opts={"type": "jitterX"})
    return chart

# 坐标轴 Options

坐标轴 Options 控制图表 x 轴和 y 轴的显示、样式、标签、刻度等。

## AxisOpts

坐标轴总配置，用于配置 x 轴和 y 轴。

**参数：**
- `x_axis_opts` (Union[AxisCfgOpts, bool]): x 轴配置
- `y_axis_opts` (Union[AxisCfgOpts, bool]): y 轴配置

**示例：**
```python
from pyantv import options as opts

chart.set_axis(axis_opts=opts.AxisOpts(
    x_axis_opts=opts.AxisCfgOpts(
        axis_label_opts=opts.AxisLabelOpts(
            is_show_label=True,
            label_font_size=12
        )
    ),
    y_axis_opts=opts.AxisCfgOpts(
        axis_grid_opts=opts.AxisGridOpts(
            is_show_grid=True
        )
    )
))
```

---

## AxisCfgOpts

坐标轴配置，包含标题、线条、刻度、标签、网格等子配置。

**参数：**
- `axis_title_opts` (Union[AxisTitleOpts, bool]): 坐标轴标题配置
- `axis_line_opts` (Union[AxisLineOpts, bool]): 坐标轴线配置
- `axis_tick_opts` (Union[AxisTickOpts, bool]): 坐标轴刻度配置
- `axis_label_opts` (Union[AxisLabelOpts, bool]): 坐标轴标签配置
- `axis_grid_opts` (Union[AxisGridOpts, bool]): 坐标轴网格配置
- `animate_opts` (Union[EffectTimingOpts, bool]): 动画配置

---

## AxisTitleOpts

坐标轴标题配置。

**参数：**
- `title` (Union[bool, Numeric, JSFunc]): 标题内容
- `title_spacing` (Numeric): 标题间距
- `title_position` (str): 标题位置
- `title_font_size` (Numeric): 标题字号
- `title_font_family` (str): 标题字体
- `title_font_weight` (Numeric): 标题字重
- `title_stroke` (str): 标题描边
- `title_stroke_opacity` (Numeric): 标题描边透明度

---

## AxisLineOpts

坐标轴线配置。

**参数：**
- `is_show_line` (bool): 是否显示轴线
- `is_show_arrow` (bool): 是否显示箭头
- `line_extension` (Sequence[Numeric]): 线条延伸
- `line_arrow` (JSFunc): 箭头样式
- `line_arrow_offset` (Numeric): 箭头偏移
- `line_arrow_size` (Numeric): 箭头大小
- `line_width` (Numeric): 线条宽度
- `line_dash` (Sequence[Numeric]): 虚线样式
- `line_stroke` (str): 线条颜色
- `line_stroke_opacity` (Numeric): 线条透明度

---

## AxisTickOpts

坐标轴刻度配置。

**参数：**
- `is_show_tick` (bool): 是否显示刻度
- `tick_filter` (JSFunc): 刻度过滤
- `tick_formatter` (JSFunc): 刻度格式化
- `tick_direction` (str): 刻度方向
- `tick_length` (Union[JSFunc, Numeric]): 刻度长度
- `tick_line_width` (Union[JSFunc, Numeric]): 刻度线宽
- `tick_line_dash` (Union[JSFunc, Sequence[Numeric]]): 刻度虚线
- `tick_stroke` (Union[JSFunc]): 刻度颜色
- `tick_stroke_opacity` (Union[JSFunc, Numeric]): 刻度透明度

---

## AxisLabelOpts

坐标轴标签配置。

**参数：**
- `is_show_label` (bool): 是否显示标签
- `label_opacity` (Union[JSFunc, Numeric]): 标签透明度
- `label_filter` (JSFunc): 标签过滤
- `label_formatter` (JSFunc): 标签格式化
- `transform` (Sequence): 标签变换
- `label_auto_hide` (Union[bool, dict]): 自动隐藏
- `label_auto_rotate` (Union[bool, dict]): 自动旋转
- `label_auto_ellipsis` (Union[bool, dict]): 自动省略
- `label_auto_wrap` (Union[bool, dict]): 自动换行
- `label_align` (str): 标签对齐
- `label_direction` (str): 标签方向
- `label_spacing` (Numeric): 标签间距
- `label_line_width` (Union[JSFunc, Numeric]): 标签线宽
- `label_line_dash` (Union[JSFunc, Sequence[Numeric]]): 标签虚线
- `label_font_size` (Union[JSFunc, Numeric]): 标签字号
- `label_font_family` (JSFunc): 标签字体
- `label_font_weight` (Union[JSFunc, Numeric]): 标签字重
- `label_fill` (Union[JSFunc]): 标签颜色
- `label_fill_opacity` (Union[JSFunc, Numeric]): 标签透明度
- `label_stroke` (Union[JSFunc]): 标签描边
- `label_stroke_opacity` (Union[JSFunc, Numeric]): 描边透明度

---

## AxisGridOpts

坐标轴网格配置。

**参数：**
- `is_show_grid` (bool): 是否显示网格
- `grid_filter` (JSFunc): 网格过滤
- `grid_length` (Union[JSFunc, Numeric]): 网格长度
- `grid_area_fill` (JSFunc): 网格区域填充
- `grid_line_width` (Numeric): 网格线宽
- `grid_line_dash` (Sequence[Numeric]): 网格虚线
- `grid_stroke` (str): 网格颜色
- `grid_stroke_opacity` (Numeric): 网格透明度

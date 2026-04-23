# 样式 Options

样式 Options 提供基础样式配置。

## BaseChartStyleOpts

基础图表样式配置。

**参数：**
- `text` (JSFunc): 文本
- `text_align` (JSFunc): 文本对齐
- `position` (JSFunc): 位置
- `fill` (JSFunc): 填充颜色
- `fill_opacity` (Union[Numeric, JSFunc]): 填充透明度
- `stroke` (JSFunc): 描边
- `stroke_opacity` (Union[Numeric, JSFunc]): 描边透明度
- `line_width` (Union[Numeric, JSFunc]): 线宽
- `line_dash` (Union[Sequence, JSFunc]): 虚线
- `line_cap` (JSFunc): 线端样式
- `opacity` (Union[Numeric, JSFunc]): 透明度
- `shadow_color` (JSFunc): 阴影颜色
- `shadow_offset_x` (Union[Numeric, JSFunc]): 阴影 X 偏移
- `shadow_offset_y` (Union[Numeric, JSFunc]): 阴影 Y 偏移
- `cursor` (JSFunc): 光标
- `dx` (Union[Numeric, JSFunc]): X 偏移
- `dy` (Union[Numeric, JSFunc]): Y 偏移
- `inset` (Numeric): 内边距
- `radius` (Numeric): 圆角
- `background` (Union[bool, JSFunc]): 背景
- `background_fill` (JSFunc): 背景填充
- `font_weight` (Union[Numeric, JSFunc]): 字重
- `font_size` (Union[Numeric, JSFunc]): 字号
- `spacing` (Numeric): 间距

**示例：**
```python
from pyantv import options as opts

style = opts.BaseChartStyleOpts(
    fill="#1890ff",
    stroke="#096dd9",
    line_width=2,
    opacity=0.8
)
```

---

## BaseChartRadiusInsetStyleOpts

圆角和内边距样式配置。

**参数：**
- `radius` (Union[Numeric, JSFunc]): 圆角
- `radius_top_left` (Union[Numeric, JSFunc]): 左上圆角
- `radius_top_right` (Union[Numeric, JSFunc]): 右上圆角
- `radius_bottom_left` (Union[Numeric, JSFunc]): 左下圆角
- `radius_bottom_right` (Union[Numeric, JSFunc]): 右下圆角
- `inner_radius_top_left` (Union[Numeric, JSFunc]): 内左上圆角
- `inner_radius_top_right` (Union[Numeric, JSFunc]): 内右上圆角
- `inner_radius_bottom_left` (Union[Numeric, JSFunc]): 内左下圆角
- `inner_radius_bottom_right` (Union[Numeric, JSFunc]): 内右下圆角
- `inset` (Union[Numeric, JSFunc]): 内边距
- `inset_left` (Union[Numeric, JSFunc]): 左内边距
- `inset_right` (Union[Numeric, JSFunc]): 右内边距
- `inset_bottom` (Union[Numeric, JSFunc]): 下内边距
- `inset_top` (Union[Numeric, JSFunc]): 上内边距

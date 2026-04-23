# 标签 Options

标签 Options 控制数据标签的显示、格式化、样式等。

## LabelOpts

标签配置。

**参数：**
- `text_opts` (JSFunc): 文本配置
- `font_size` (Union[Numeric, JSFunc]): 字号
- `font_family` (JSFunc): 字体
- `font_weight` (Union[Numeric, JSFunc]): 字重
- `line_height` (Union[Numeric, JSFunc]): 行高
- `text_align` (JSFunc): 文本对齐
- `text_baseline` (JSFunc): 文本基线
- `fill` (JSFunc): 填充颜色
- `fill_opacity` (Union[Numeric, JSFunc]): 填充透明度
- `stroke` (JSFunc): 描边
- `stroke_opacity` (Union[Numeric, JSFunc]): 描边透明度
- `line_width` (Union[Numeric, JSFunc]): 线宽
- `line_dash` (Union[Sequence[Numeric], JSFunc]): 虚线
- `opacity` (Union[Numeric, JSFunc]): 透明度
- `shadow_color` (JSFunc): 阴影颜色
- `shadow_blur` (Union[Numeric, JSFunc]): 阴影模糊
- `shadow_offset_x` (Union[Numeric, JSFunc]): 阴影 X 偏移
- `shadow_offset_y` (Union[Numeric, JSFunc]): 阴影 Y 偏移
- `cursor` (JSFunc): 光标
- `position` (str): 位置
- `is_connector` (bool): 是否显示连接线
- `connector_style_opts` (BaseChartStyleOpts): 连接线样式
- `is_background` (bool): 是否显示背景
- `background_style_opts` (BaseChartStyleOpts): 背景样式
- `transform` (LabelTransform): 转换
- `formatter` (JSFunc): 格式化
- `selector` (str): 选择器
- `render` (JSFunc): 渲染
- `style_opts` (BaseChartStyleOpts): 样式

**示例：**
```python
from pyantv import options as opts

chart.set_labels(label_opts=opts.LabelOpts(
    position="outside",
    font_size=12,
    fill="#333",
    formatter=lambda d: f"{d:.2f}"
))
```

---

## LabelTransformContrastReverseOpts

对比反转转换，根据阈值反转标签颜色。

**参数：**
- `threshold` (Numeric): 阈值
- `palette` (Union[str, Sequence[str]]): 调色板

---

## LabelTransformOverflowHideOpts

溢出隐藏转换，隐藏超出边界的标签。

**参数：** 无

---

## LabelTransformOverlapDodgeYOpts

重叠避让转换，在 Y 轴方向上避让重叠的标签。

**参数：**
- `max_iterations` (Numeric): 最大迭代次数
- `padding` (Numeric): 间距
- `max_error` (Numeric): 最大误差

---

## LabelTransformOverlapHideOpts

重叠隐藏转换，隐藏重叠的标签。

**参数：** 无

---

## LabelTransformExceedAdjustOpts

超出调整转换，调整超出边界的标签位置。

**参数：** 无

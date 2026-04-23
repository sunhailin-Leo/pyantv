# 交互 Options

交互 Options 控制图表的交互行为和样式。

## InteractionOpts

交互总配置，包含所有交互类型。

**参数：**
- `brush_axis_highlight_opts` (InteractionBrushAxisHighlightOpts): 框选坐标轴高亮
- `brush_filter_opts` (InteractionBrushFilterOpts): 框选过滤
- `brush_highlight_opts` (InteractionBrushHighlightOpts): 框选高亮
- `brush_x_filter_opts` (InteractionBrushXFilterOpts): X 轴框选过滤
- `brush_x_highlight_opts` (InteractionBrushXHighlightOpts): X 轴框选高亮
- `brush_y_filter_opts` (InteractionBrushYFilterOpts): Y 轴框选过滤
- `brush_y_highlight_opts` (InteractionBrushYHighlightOpts): Y 轴框选高亮
- `chart_index_opts` (InteractionChartIndexOpts): 图表索引
- `element_highlight_opts` (InteractionElementHighlightOpts): 元素高亮
- `element_highlight_by_color_opts` (InteractionElementHighlightByColorOpts): 按颜色高亮
- `element_highlight_by_x_opts` (InteractionElementHighlightByXOpts): 按 X 轴高亮
- `element_select_opts` (InteractionElementSelectOpts): 元素选中
- `element_select_by_color_opts` (InteractionElementSelectByColorOpts): 按颜色选中
- `element_select_by_x_opts` (InteractionElementSelectByXOpts): 按 X 轴选中
- `fisheye_opts` (InteractionFishEyeOpts): 鱼眼效果
- `legend_filter_opts` (InteractionLegendFilterOpts): 图例过滤
- `legend_highlight_opts` (InteractionLegendHighlightOpts): 图例高亮
- `poptip_opts` (InteractionPopTipOpts): 弹出提示
- `tooltip_opts` (InteractionTooltipOpts): Tooltip 配置

**示例：**
```python
from pyantv import options as opts

chart.set_interaction(interaction_opts=opts.InteractionOpts(
    element_highlight_opts=opts.InteractionElementHighlightOpts(
        is_background=True
    ),
    tooltip_opts=opts.InteractionTooltipOpts(
        is_shared=True,
        is_crosshairs=True
    )
))
```

---

## InteractionElementHighlightOpts

元素高亮交互配置。

**参数：**
- `is_background` (bool): 是否显示背景
- `offset` (Numeric): 偏移
- `background_style_opts` (InteractionBackgroundStyleOpts): 背景样式

---

## InteractionElementSelectOpts

元素选中交互配置。

**参数：**
- `is_background` (bool): 是否显示背景
- `offset` (Numeric): 偏移
- `background_style_opts` (InteractionBackgroundStyleOpts): 背景样式
- `is_single` (bool): 是否单选

---

## InteractionFishEyeOpts

鱼眼效果交互配置。

**参数：**
- `wait` (Numeric): 等待时间
- `is_leading` (bool): 是否前置
- `is_trailing` (bool): 是否后置

---

## InteractionTooltipOpts

Tooltip 交互配置。

**参数：**
- `wait` (Numeric): 等待时间
- `is_leading` (bool): 是否前置
- `is_trailing` (bool): 是否后置
- `is_shared` (bool): 是否共享
- `is_series` (bool): 是否按系列
- `is_body` (bool): 是否显示主体
- `is_marker` (bool): 是否显示标记
- `is_group_name` (bool): 是否显示组名
- `position` (str): 位置
- `mount` (JSFunc): 挂载点
- `bounding` (InteractionTooltipBBoxOpts): 边界框
- `offset` (Sequence[Numeric]): 偏移
- `is_crosshairs` (bool): 是否显示十字准线
- `is_crosshairs_x` (bool): 是否显示 X 轴十字准线
- `is_crosshairs_y` (bool): 是否显示 Y 轴十字准线
- `crosshairs_style_opts` (InteractionCrossHairsStyleOpts): 十字准线样式
- `marker_type` (JSFunc): 标记类型
- `render` (JSFunc): 渲染
- `sort_` (JSFunc): 排序
- `filter_` (JSFunc): 过滤
- `is_disable_native` (bool): 是否禁用原生
- `css` (JSFunc): CSS 样式

---

## InteractionBrushHighlightOpts

框选高亮交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `is_series` (bool): 是否按系列
- `is_facet` (bool): 是否按分面
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionBrushFilterOpts

框选过滤交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionLegendFilterOpts

图例过滤交互配置。

**参数：** 无

---

## InteractionLegendHighlightOpts

图例高亮交互配置。

**参数：** 无

---

## InteractionBackgroundStyleOpts

背景样式配置。

**参数：**
- `background_fill` (JSFunc): 背景填充
- `background_fill_opacity` (Union[Numeric, JSFunc]): 背景填充透明度
- `background_stroke` (JSFunc): 背景描边
- `background_stroke_opacity` (Union[Numeric, JSFunc]): 背景描边透明度
- `background_line_width` (Union[Numeric, JSFunc]): 背景线宽
- `background_line_dash` (Union[Sequence, JSFunc]): 背景虚线
- `background_opacity` (Union[Numeric, JSFunc]): 背景透明度
- `background_shadow_color` (JSFunc): 背景阴影颜色
- `background_shadow_offset_x` (Union[Numeric, JSFunc]): 背景阴影 X 偏移
- `background_shadow_offset_y` (Union[Numeric, JSFunc]): 背景阴影 Y 偏移
- `background_cursor` (JSFunc): 背景光标

---

## InteractionMaskStyleOpts

遮罩样式配置。

**参数：**
- `mask_fill` (JSFunc): 遮罩填充
- `mask_fill_opacity` (Union[Numeric, JSFunc]): 遮罩填充透明度
- `mask_stroke` (JSFunc): 遮罩描边
- `mask_stroke_opacity` (Union[Numeric, JSFunc]): 遮罩描边透明度
- `mask_line_width` (Union[Numeric, JSFunc]): 遮罩线宽
- `mask_line_dash` (Union[Sequence, JSFunc]): 遮罩虚线
- `mask_opacity` (Union[Numeric, JSFunc]): 遮罩透明度
- `mask_shadow_color` (JSFunc): 遮罩阴影颜色
- `mask_shadow_offset_x` (Union[Numeric, JSFunc]): 遮罩阴影 X 偏移
- `mask_shadow_offset_y` (Union[Numeric, JSFunc]): 遮罩阴影 Y 偏移
- `mask_cursor` (JSFunc): 遮罩光标

---

## InteractionCrossHairsStyleOpts

十字准线样式配置。

**参数：**
- `crosshairs_fill` (JSFunc): 十字准线填充
- `crosshairs_fill_opacity` (Union[Numeric, JSFunc]): 十字准线填充透明度
- `crosshairs_stroke` (JSFunc): 十字准线描边
- `crosshairs_stroke_opacity` (Union[Numeric, JSFunc]): 十字准线描边透明度
- `crosshairs_line_width` (Union[Numeric, JSFunc]): 十字准线线宽
- `crosshairs_line_dash` (Union[Sequence, JSFunc]): 十字准线虚线
- `crosshairs_opacity` (Union[Numeric, JSFunc]): 十字准线透明度
- `crosshairs_shadow_color` (JSFunc): 十字准线阴影颜色
- `crosshairs_shadow_offset_x` (Union[Numeric, JSFunc]): 十字准线阴影 X 偏移
- `crosshairs_shadow_offset_y` (Union[Numeric, JSFunc]): 十字准线阴影 Y 偏移
- `crosshairs_cursor` (JSFunc): 十字准线光标

---

## InteractionTooltipBBoxOpts

Tooltip 边界框配置。

**参数：**
- `x_` (Numeric): X 坐标
- `y_` (Numeric): Y 坐标
- `width` (Numeric): 宽度
- `height` (Numeric): 高度

---

## InteractionPopTipOpts

弹出提示配置。

**参数：**
- `offset_x` (Numeric): X 偏移
- `offset_y` (Numeric): Y 偏移
- `tip_style_opts` (InteractionTipStyleOpts): 提示样式

---

## InteractionTipStyleOpts

提示样式配置。

**参数：**
- `tip_fill` (JSFunc): 提示填充
- `tip_fill_opacity` (Union[Numeric, JSFunc]): 提示填充透明度
- `tip_stroke` (JSFunc): 提示描边
- `tip_stroke_opacity` (Union[Numeric, JSFunc]): 提示描边透明度
- `tip_line_width` (Union[Numeric, JSFunc]): 提示线宽
- `tip_line_dash` (Union[Sequence, JSFunc]): 提示虚线
- `tip_opacity` (Union[Numeric, JSFunc]): 提示透明度
- `tip_shadow_color` (JSFunc): 提示阴影颜色
- `tip_shadow_offset_x` (Union[Numeric, JSFunc]): 提示阴影 X 偏移
- `tip_shadow_offset_y` (Union[Numeric, JSFunc]): 提示阴影 Y 偏移
- `tip_cursor` (JSFunc): 提示光标

---

## InteractionChartIndexOpts

图表索引配置。

**参数：**
- `label_formatter` (JSFunc): 标签格式化
- `rule_style_opts` (InteractionRuleStyleOpts): 参考线样式
- `label_style_opts` (InteractionLabelStyleOpts): 标签样式

---

## InteractionRuleStyleOpts

参考线样式配置。

**参数：**
- `rule_fill` (JSFunc): 参考线填充
- `rule_fill_opacity` (Union[Numeric, JSFunc]): 参考线填充透明度
- `rule_stroke` (JSFunc): 参考线描边
- `rule_stroke_opacity` (Union[Numeric, JSFunc]): 参考线描边透明度
- `rule_line_width` (Union[Numeric, JSFunc]): 参考线线宽
- `rule_line_dash` (Union[Sequence, JSFunc]): 参考线虚线
- `rule_opacity` (Union[Numeric, JSFunc]): 参考线透明度
- `rule_shadow_color` (JSFunc): 参考线阴影颜色
- `rule_shadow_offset_x` (Union[Numeric, JSFunc]): 参考线阴影 X 偏移
- `rule_shadow_offset_y` (Union[Numeric, JSFunc]): 参考线阴影 Y 偏移
- `rule_cursor` (JSFunc): 参考线光标

---

## InteractionLabelStyleOpts

标签样式配置。

**参数：**
- `label_fill` (JSFunc): 标签填充
- `label_fill_opacity` (Union[Numeric, JSFunc]): 标签填充透明度
- `label_stroke` (JSFunc): 标签描边
- `label_stroke_opacity` (Union[Numeric, JSFunc]): 标签描边透明度
- `label_line_width` (Union[Numeric, JSFunc]): 标签线宽
- `label_line_dash` (Union[Sequence, JSFunc]): 标签虚线
- `label_opacity` (Union[Numeric, JSFunc]): 标签透明度
- `label_shadow_color` (JSFunc): 标签阴影颜色
- `label_shadow_offset_x` (Union[Numeric, JSFunc]): 标签阴影 X 偏移
- `label_shadow_offset_y` (Union[Numeric, JSFunc]): 标签阴影 Y 偏移
- `label_cursor` (JSFunc): 标签光标

---

## InteractionElementHighlightByColorOpts

按颜色高亮交互配置。

**参数：**
- `is_link` (bool): 是否显示连接线
- `is_background` (bool): 是否显示背景
- `offset` (Numeric): 偏移
- `link_style_opts` (InteractionLinkStyleOpts): 连接线样式
- `background_style_opts` (InteractionBackgroundStyleOpts): 背景样式

---

## InteractionElementHighlightByXOpts

按 X 轴高亮交互配置。

**参数：**
- `is_background` (bool): 是否显示背景
- `offset` (Numeric): 偏移
- `background_style_opts` (InteractionBackgroundStyleOpts): 背景样式

---

## InteractionElementSelectByColorOpts

按颜色选中交互配置。

**参数：**
- `is_link` (bool): 是否显示连接线
- `is_background` (bool): 是否显示背景
- `offset` (Numeric): 偏移
- `link_style_opts` (InteractionLinkStyleOpts): 连接线样式
- `background_style_opts` (InteractionBackgroundStyleOpts): 背景样式

---

## InteractionElementSelectByXOpts

按 X 轴选中交互配置。

**参数：**
- `is_link` (bool): 是否显示连接线
- `is_background` (bool): 是否显示背景
- `offset` (Numeric): 偏移
- `link_style_opts` (InteractionLinkStyleOpts): 连接线样式
- `background_style_opts` (InteractionBackgroundStyleOpts): 背景样式
- `is_single` (bool): 是否单选

---

## InteractionLinkStyleOpts

连接线样式配置。

**参数：**
- `link_fill` (JSFunc): 连接线填充
- `link_fill_opacity` (Union[Numeric, JSFunc]): 连接线填充透明度
- `link_stroke` (JSFunc): 连接线描边
- `link_stroke_opacity` (Union[Numeric, JSFunc]): 连接线描边透明度
- `link_line_width` (Union[Numeric, JSFunc]): 连接线线宽
- `link_line_dash` (Union[Sequence, JSFunc]): 连接线虚线
- `link_opacity` (Union[Numeric, JSFunc]): 连接线透明度
- `link_shadow_color` (JSFunc): 连接线阴影颜色
- `link_shadow_offset_x` (Union[Numeric, JSFunc]): 连接线阴影 X 偏移
- `link_shadow_offset_y` (Union[Numeric, JSFunc]): 连接线阴影 Y 偏移
- `link_cursor` (JSFunc): 连接线光标

---

## InteractionBrushAxisHighlightOpts

框选坐标轴高亮交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionBrushXFilterOpts

X 轴框选过滤交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionBrushXHighlightOpts

X 轴框选高亮交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `is_series` (bool): 是否按系列
- `is_facet` (bool): 是否按分面
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionBrushYFilterOpts

Y 轴框选过滤交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionBrushYHighlightOpts

Y 轴框选高亮交互配置。

**参数：**
- `is_reverse` (bool): 是否反转
- `is_series` (bool): 是否按系列
- `is_facet` (bool): 是否按分面
- `mask_style_opts` (InteractionMaskStyleOpts): 遮罩样式

---

## InteractionCrossHairsXStyleOpts

X 轴十字准线样式配置。

**参数：**
- `crosshairsx_fill` (JSFunc): 十字准线填充
- `crosshairsx_fill_opacity` (Union[Numeric, JSFunc]): 十字准线填充透明度
- `crosshairsx_stroke` (JSFunc): 十字准线描边
- `crosshairsx_stroke_opacity` (Union[Numeric, JSFunc]): 十字准线描边透明度
- `crosshairsx_line_width` (Union[Numeric, JSFunc]): 十字准线线宽
- `crosshairsx_line_dash` (Union[Sequence, JSFunc]): 十字准线虚线
- `crosshairsx_opacity` (Union[Numeric, JSFunc]): 十字准线透明度
- `crosshairsx_shadow_color` (JSFunc): 十字准线阴影颜色
- `crosshairsx_shadow_offset_x` (Union[Numeric, JSFunc]): 十字准线阴影 X 偏移
- `crosshairsx_shadow_offset_y` (Union[Numeric, JSFunc]): 十字准线阴影 Y 偏移
- `crosshairsx_cursor` (JSFunc): 十字准线光标

---

## InteractionCrossHairsYStyleOpts

Y 轴十字准线样式配置。

**参数：**
- `crosshairsy_fill` (JSFunc): 十字准线填充
- `crosshairsy_fill_opacity` (Union[Numeric, JSFunc]): 十字准线填充透明度
- `crosshairsy_stroke` (JSFunc): 十字准线描边
- `crosshairsy_stroke_opacity` (Union[Numeric, JSFunc]): 十字准线描边透明度
- `crosshairsy_line_width` (Union[Numeric, JSFunc]): 十字准线线宽
- `crosshairsy_line_dash` (Union[Sequence, JSFunc]): 十字准线虚线
- `crosshairsy_opacity` (Union[Numeric, JSFunc]): 十字准线透明度
- `crosshairsy_shadow_color` (JSFunc): 十字准线阴影颜色
- `crosshairsy_shadow_offset_x` (Union[Numeric, JSFunc]): 十字准线阴影 X 偏移
- `crosshairsy_shadow_offset_y` (Union[Numeric, JSFunc]): 十字准线阴影 Y 偏移
- `crosshairsy_cursor` (JSFunc): 十字准线光标

---

## InteractionMarkerStyleOpts

标记样式配置。

**参数：**
- `marker_fill` (JSFunc): 标记填充
- `marker_fill_opacity` (Union[Numeric, JSFunc]): 标记填充透明度
- `marker_stroke` (JSFunc): 标记描边
- `marker_stroke_opacity` (Union[Numeric, JSFunc]): 标记描边透明度
- `marker_line_width` (Union[Numeric, JSFunc]): 标记线宽
- `marker_line_dash` (Union[Sequence, JSFunc]): 标记虚线
- `marker_opacity` (Union[Numeric, JSFunc]): 标记透明度
- `marker_shadow_color` (JSFunc): 标记阴影颜色
- `marker_shadow_offset_x` (Union[Numeric, JSFunc]): 标记阴影 X 偏移
- `marker_shadow_offset_y` (Union[Numeric, JSFunc]): 标记阴影 Y 偏移
- `marker_cursor` (JSFunc): 标记光标

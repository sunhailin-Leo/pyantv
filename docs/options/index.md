# Options 总览

Options 是 pyantv 提供的配置项类，用于精细控制图表的各个方面。每个 Option 类对应图表的一个配置维度，通过传入参数来定制图表行为。

## 按分类浏览

### 坐标轴 (7 个)
控制 x 轴和 y 轴的显示、样式、标签、刻度等
- [坐标轴详情](axis.md)
- `AxisTitleOpts` - 坐标轴标题
- `AxisLineOpts` - 坐标轴线
- `AxisTickOpts` - 坐标轴刻度
- `AxisLabelOpts` - 坐标轴标签
- `AxisGridOpts` - 坐标轴网格
- `AxisCfgOpts` - 坐标轴配置
- `AxisOpts` - 坐标轴总配置

### 图例 (6 个)
控制图例的显示、样式、布局等
- [图例详情](legend.md)
- `LegendTitleOpts` - 图例标题
- `LegendLayoutOpts` - 图例布局
- `LegendCategoryCfgOpts` - 分类图例配置
- `LegendCategoryOpts` - 分类图例
- `LegendAxisOpts` - 连续图例配置
- `LegendContinuousOpts` - 连续图例

### 提示框 (2 个)
控制 tooltip 的显示、内容、样式等
- [提示框详情](tooltip.md)
- `TooltipItemOpts` - 提示框单项
- `TooltipOpts` - 提示框配置

### 标签 (6 个)
控制数据标签的显示、格式化、样式等
- [标签详情](label.md)
- `LabelTransformContrastReverseOpts` - 对比反转转换
- `LabelTransformOverflowHideOpts` - 溢出隐藏转换
- `LabelTransformOverlapDodgeYOpts` - 重叠避让转换
- `LabelTransformOverlapHideOpts` - 重叠隐藏转换
- `LabelTransformExceedAdjustOpts` - 超出调整转换
- `LabelOpts` - 标签配置

### 样式 (2 个)
基础样式配置
- [样式详情](style.md)
- `BaseChartStyleOpts` - 基础图表样式
- `BaseChartRadiusInsetStyleOpts` - 圆角和内边距样式

### 比例尺 (12 个)
控制数据到视觉属性的映射
- [比例尺详情](scale.md)
- `ScaleBaseOpts` - 比例尺基类
- `ScaleBandOpts` - 分段比例尺
- `ScaleLinearOpts` - 线性比例尺
- `ScaleLogOpts` - 对数比例尺
- `ScaleOrdinalOpts` - 序数比例尺
- `ScalePointOpts` - 点比例尺
- `ScalePowOpts` - 幂比例尺
- `ScaleQuantileOpts` - 分位数比例尺
- `ScaleQuantizeOpts` - 量化比例尺
- `ScaleSqrtOpts` - 平方根比例尺
- `ScaleThresholdOpts` - 阈值比例尺
- `ScaleTimeOpts` - 时间比例尺

### 交互 (37 个)
控制图表的交互行为和样式
- [交互详情](interaction.md)
- `InteractionMaskStyleOpts` - 遮罩样式
- `InteractionBrushAxisHighlightOpts` - 框选坐标轴高亮
- `InteractionBrushFilterOpts` - 框选过滤
- `InteractionBrushHighlightOpts` - 框选高亮
- `InteractionBrushXFilterOpts` - X 轴框选过滤
- `InteractionBrushXHighlightOpts` - X 轴框选高亮
- `InteractionBrushYFilterOpts` - Y 轴框选过滤
- `InteractionBrushYHighlightOpts` - Y 轴框选高亮
- `InteractionRuleStyleOpts` - 参考线样式
- `InteractionLabelStyleOpts` - 标签样式
- `InteractionChartIndexOpts` - 图表索引
- `InteractionBackgroundStyleOpts` - 背景样式
- `InteractionElementHighlightOpts` - 元素高亮
- `InteractionElementHighlightByColorOpts` - 按颜色高亮
- `InteractionElementHighlightByXOpts` - 按 X 轴高亮
- `InteractionElementSelectOpts` - 元素选中
- `InteractionElementSelectByColorOpts` - 按颜色选中
- `InteractionElementSelectByXOpts` - 按 X 轴选中
- `InteractionFishEyeOpts` - 鱼眼效果
- `InteractionLegendFilterOpts` - 图例过滤
- `InteractionLegendHighlightOpts` - 图例高亮
- `InteractionTipStyleOpts` - 提示样式
- `InteractionPopTipOpts` - 弹出提示
- `InteractionTooltipBBoxOpts` - Tooltip 边界框
- `InteractionCrossHairsStyleOpts` - 十字准线样式
- `InteractionCrossHairsXStyleOpts` - X 轴十字准线样式
- `InteractionCrossHairsYStyleOpts` - Y 轴十字准线样式
- `InteractionMarkerStyleOpts` - 标记样式
- `InteractionTooltipOpts` - Tooltip 配置
- `InteractionOpts` - 交互总配置

### 动画 (3 个)
控制图表的动画效果
- [动画详情](animation.md)
- `AnimatePropertiesOpts` - 动画属性
- `AnimateOpts` - 动画配置
- `EffectTimingOpts` - 效果时机

### 注解 (3 个)
在图表上添加标注
- [注解详情](annotation.md)
- `LineAnnotationOpts` - 参考线标注
- `RegionAnnotationOpts` - 区域标注
- `TextAnnotationOpts` - 文本标注

### 标题 (1 个)
控制图表标题
- [标题详情](title.md)
- `TitleOpts` - 标题配置

### 滚动条 (3 个)
控制滚动条的显示和样式
- [滚动条详情](scrollbar.md)
- `ScrollBarStyleOpts` - 滚动条样式
- `ScrollBarCfgOpts` - 滚动条配置
- `ScrollBarOpts` - 滚动条总配置

### 滑块 (3 个)
控制滑块的显示和样式
- [滑块详情](slider.md)
- `SliderStyleOpts` - 滑块样式
- `SliderCfgOpts` - 滑块配置
- `SliderOpts` - 滑块总配置

## 快速参考

| 分类 | 类数量 | 说明 |
|------|--------|------|
| 坐标轴 | 7 | 控制坐标轴显示和样式 |
| 图例 | 6 | 控制图例显示和样式 |
| 提示框 | 2 | 控制提示框内容和样式 |
| 标签 | 6 | 控制数据标签显示和样式 |
| 样式 | 2 | 基础样式配置 |
| 比例尺 | 12 | 数据到视觉属性的映射 |
| 交互 | 37 | 图表交互行为和样式 |
| 动画 | 3 | 动画效果控制 |
| 注解 | 3 | 图表标注 |
| 标题 | 1 | 图表标题 |
| 滚动条 | 3 | 滚动条控制 |
| 滑块 | 3 | 滑块控制 |
| **总计** | **88** | |

## 使用示例

```python
from pyantv import Line
from pyantv import options as opts

# 创建图表
chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")

# 使用 Options 配置图表
chart.set_axis(axis_opts=opts.AxisOpts(
    x_axis_opts=opts.AxisCfgOpts(
        axis_label_opts=opts.AxisLabelOpts(
            is_show_label=True,
            label_font_size=12
        )
    )
))

chart.set_tooltip(tooltip_opts=opts.TooltipOpts(
    title="数据详情",
    items=[
        opts.TooltipItemOpts(field="x", name="X轴"),
        opts.TooltipItemOpts(field="y", name="Y轴")
    ]
))

chart.render("chart.html")
```

## 与 Presets 的区别

- **Presets**: 提供预设的配置组合，一行代码即可应用常用配置，适合快速上手
- **Options**: 提供精细的配置项，可以精确控制每个细节，适合深度定制

建议先使用 Presets 快速构建图表，再根据需要使用 Options 进行微调。

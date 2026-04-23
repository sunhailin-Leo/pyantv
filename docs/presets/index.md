# Presets 总览

Presets 是 pyantv 提供的预设配置函数，让你能够通过一行代码快速应用常用的图表配置组合。所有 Preset 函数都支持链式调用，可以组合使用。

## 按分类浏览

### 主题 (6 个)
预设颜色方案和整体视觉风格
- [主题详情](themes.md)
- `with_dark_theme` - 暗色主题
- `with_classic_theme` - 经典主题
- `with_academy_theme` - 学术主题
- `with_tech_theme` - 科技风主题
- `with_business_theme` - 商务风主题
- `with_fresh_theme` - 清新风主题

### 动画 (1 个)
控制图表的入场动画效果
- [动画详情](animation.md)
- `with_smooth_animation` - 平滑入场动画

### 布局 (5 个)
控制图表的容器、图例、坐标轴、标签和内边距
- [布局详情](layout.md)
- `with_auto_fit` - 自适应容器大小
- `with_legend_hidden` - 隐藏图例
- `with_axis_hidden` - 隐藏所有坐标轴
- `with_labels` - 启用并配置数据标签
- `with_padding` - 应用统一内边距

### 坐标系 (2 个)
改变图表的坐标系类型
- [坐标系详情](coordinate.md)
- `with_transpose` - 转置坐标系
- `with_polar` - 应用极坐标系

### 交互 (7 个)
增强图表的用户交互能力
- [交互详情](interaction.md)
- `with_tooltip` - 应用标准 tooltip
- `with_element_highlight` - 元素高亮交互
- `with_element_select` - 元素选中交互
- `with_brush_highlight` - 框选高亮交互
- `with_brush_filter` - 框选过滤交互
- `with_fisheye` - 鱼眼放大镜交互
- `with_slider_filter` - 滑块过滤交互

### 数据转换 (5 个)
对数据进行排序、堆叠、归一化等转换
- [数据转换详情](transform.md)
- `with_sort_by` - 应用排序
- `with_stack` - 应用堆叠
- `with_normalize` - 应用归一化
- `with_group` - 应用分组
- `with_jitter` - 应用抖动

### 格式化 (4 个)
生成格式化函数用于标签和提示框
- [格式化详情](formatting.md)
- `format_number` - 数值格式化
- `format_percent` - 百分比格式化
- `format_currency` - 货币格式化
- `format_date` - 日期格式化

### 工具函数 (1 个)
图表批量处理工具
- `batch_export_png` - 批量导出多个图表为 PNG（依赖 Playwright）

## 快速参考

| 分类 | 函数数量 | 说明 |
|------|---------|------|
| 主题 | 6 | 预设颜色方案和视觉风格 |
| 动画 | 1 | 入场动画效果 |
| 布局 | 5 | 容器、图例、坐标轴、标签、内边距 |
| 坐标系 | 2 | 坐标系类型转换 |
| 交互 | 7 | 鼠标交互增强 |
| 数据转换 | 5 | 数据预处理 |
| 格式化 | 4 | 数据显示格式化 |
| 工具函数 | 1 | 批量导出 |
| **总计** | **31** | |

## 使用示例

```python
from pyantv import Line
from pyantv.presets import (
    with_dark_theme,
    with_smooth_animation,
    with_tooltip,
    with_padding
)

# 创建图表
chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")

# 链式调用多个 Preset
with_dark_theme(chart)
with_smooth_animation(chart, duration=800)
with_tooltip(chart, shared=True, show_crosshairs=True)
with_padding(chart, top=30, right=30, bottom=50, left=60)

# 渲染图表
chart.render("chart.html")
```

## 批量导出

`batch_export_png` 函数可以批量导出多个图表为 PNG 图片：

```python
from pyantv.presets import batch_export_png

batch_export_png(
    [(line_chart, "line.png"), (bar_chart, "bar.png")],
    output_dir="./exports",
    width=1200,
    height=800
)
```

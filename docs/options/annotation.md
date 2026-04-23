# 注解 Options

注解 Options 用于在图表上添加标注。

## LineAnnotationOpts

参考线标注配置。

**参数：**
- `x` (Union[Numeric, str]): X 轴位置
- `y` (Union[Numeric, str]): Y 轴位置
- `x_start` (Union[Numeric, str]): X 轴起点
- `x_end` (Union[Numeric, str]): X 轴终点
- `y_start` (Union[Numeric, str]): Y 轴起点
- `y_end` (Union[Numeric, str]): Y 轴终点
- `text` (str): 标注文本
- `style` (dict): 样式配置

**示例：**
```python
from pyantv import options as opts

# 添加水平参考线
chart.set_annotation(annotation_opts=opts.LineAnnotationOpts(
    y=100,
    text="目标值",
    style={"stroke": "#ff0000", "lineWidth": 2}
))

# 添加垂直参考线
chart.set_annotation(annotation_opts=opts.LineAnnotationOpts(
    x="2023-01-01",
    text="起始日期",
    style={"stroke": "#1890ff", "lineWidth": 2}
))
```

---

## RegionAnnotationOpts

区域标注配置。

**参数：**
- `x_start` (Union[Numeric, str]): X 轴起点
- `x_end` (Union[Numeric, str]): X 轴终点
- `y_start` (Union[Numeric, str]): Y 轴起点
- `y_end` (Union[Numeric, str]): Y 轴终点
- `fill` (str): 填充颜色
- `fill_opacity` (float): 填充透明度
- `style` (dict): 样式配置

**示例：**
```python
from pyantv import options as opts

# 添加水平区域标注
chart.set_annotation(annotation_opts=opts.RegionAnnotationOpts(
    y_start=50,
    y_end=100,
    fill="#1890ff",
    fill_opacity=0.2
))

# 添加垂直区域标注
chart.set_annotation(annotation_opts=opts.RegionAnnotationOpts(
    x_start="2023-01-01",
    x_end="2023-06-01",
    fill="#52c41a",
    fill_opacity=0.2
))
```

---

## TextAnnotationOpts

文本标注配置。

**参数：**
- `x` (Union[Numeric, str]): X 坐标
- `y` (Union[Numeric, str]): Y 坐标
- `text` (str): 标注文本
- `font_size` (Numeric): 字号
- `fill` (str): 填充颜色
- `style` (dict): 样式配置

**示例：**
```python
from pyantv import options as opts

# 添加文本标注
chart.set_annotation(annotation_opts=opts.TextAnnotationOpts(
    x=100,
    y=200,
    text="重要数据点",
    font_size=14,
    fill="#333333",
    style={"fontWeight": "bold"}
))
```

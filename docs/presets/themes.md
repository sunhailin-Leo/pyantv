# 主题 Presets

主题 Presets 提供预设的颜色方案和整体视觉风格，让你快速改变图表的外观。

## 内置主题

### with_dark_theme

应用暗色主题，使用 AntV G2 内置的暗色主题配置。

**函数签名：**
```python
def with_dark_theme(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用暗色主题后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_dark_theme

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_dark_theme(chart)
chart.render("dark_theme.html")
```

---

### with_classic_theme

应用经典主题，使用 AntV G2 内置的经典主题配置。

**函数签名：**
```python
def with_classic_theme(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用经典主题后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_classic_theme

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_classic_theme(chart)
chart.render("classic_theme.html")
```

---

### with_academy_theme

应用学术主题，使用 AntV G2 内置的学术主题配置。

**函数签名：**
```python
def with_academy_theme(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用学术主题后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_academy_theme

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_academy_theme(chart)
chart.render("academy_theme.html")
```

---

### with_tech_theme

应用科技风主题，使用深色背景搭配霓虹色系（青色、蓝色、紫色、粉色、橙色）。

**函数签名：**
```python
def with_tech_theme(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用科技风主题后的图表实例

**颜色方案：**
```python
[
    "#00d4ff", "#0088ff", "#7c4dff",
    "#ff4081", "#ff6e40", "#ffab40"
]
```

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_tech_theme

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_tech_theme(chart)
chart.render("tech_theme.html")
```

---

### with_business_theme

应用商务风主题，使用白色背景搭配蓝色系渐变。

**函数签名：**
```python
def with_business_theme(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用商务风主题后的图表实例

**颜色方案：**
```python
[
    "#2f54eb", "#597ef7", "#85a5ff",
    "#adc6ff", "#d6e4ff", "#f0f5ff"
]
```

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_business_theme

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_business_theme(chart)
chart.render("business_theme.html")
```

---

### with_fresh_theme

应用清新风主题，使用浅绿背景搭配多彩色系（青色、绿色、黄色、橙色、粉色、紫色）。

**函数签名：**
```python
def with_fresh_theme(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用清新风主题后的图表实例

**颜色方案：**
```python
[
    "#36cfc9", "#73d13d", "#ffc53d",
    "#ff7a45", "#f759ab", "#9254de"
]
```

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_fresh_theme

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_fresh_theme(chart)
chart.render("fresh_theme.html")
```

## 主题对比

| 主题 | 背景色 | 适用场景 |
|------|--------|---------|
| `dark_theme` | 深色 | 数据大屏、夜间模式 |
| `classic_theme` | 浅色 | 通用场景 |
| `academy_theme` | 浅色 | 学术报告、论文 |
| `tech_theme` | 深色 (#0a1628) | 科技展示、监控面板 |
| `business_theme` | 白色 | 商业报告、仪表盘 |
| `fresh_theme` | 浅绿 (#f6ffed) | 轻松场景、教育展示 |

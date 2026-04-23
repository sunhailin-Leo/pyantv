# 格式化 Presets

格式化 Presets 生成格式化函数，用于在标签（label）和提示框（tooltip）中格式化数据显示。

## format_number

生成数值格式化 JsCode，支持千分位分隔符和小数位数控制。

**函数签名：**
```python
def format_number(separator=",", precision=0)
```

**参数：**
- `separator` (str, 可选): 千分位分隔符，默认 `","`
- `precision` (int, 可选): 小数位数，默认 `0`

**返回：** JsCode 对象，可用于 `LabelOpts` 或 `tooltip_opts` 的 `formatter`

**示例：**
```python
from pyantv import Interval
from pyantv.presets import format_number
from pyantv import options as opts

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 整数格式化（千分位）
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_number(precision=0)
))

# 保留两位小数
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_number(precision=2)
))

chart.render("formatted_number.html")
```

**效果：**
- `1234.567` → `1,234.57`（precision=2）
- `1234567` → `1,234,567`（precision=0）

---

## format_percent

生成百分比格式化 JsCode，将数值转换为百分比形式。

**函数签名：**
```python
def format_percent(precision=1)
```

**参数：**
- `precision` (int, 可选): 小数位数，默认 `1`

**返回：** JsCode 对象

**示例：**
```python
from pyantv import Interval
from pyantv.presets import format_percent
from pyantv import options as opts

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 保留一位小数
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_percent(precision=1)
))

# 保留两位小数
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_percent(precision=2)
))

chart.render("formatted_percent.html")
```

**效果：**
- `0.1234` → `12.3%`（precision=1）
- `0.5678` → `56.78%`（precision=2）

---

## format_currency

生成货币格式化 JsCode，支持自定义货币符号和小数位数。

**函数签名：**
```python
def format_currency(symbol="$", precision=2)
```

**参数：**
- `symbol` (str, 可选): 货币符号，默认 `"$"`
- `precision` (int, 可选): 小数位数，默认 `2`

**返回：** JsCode 对象

**示例：**
```python
from pyantv import Interval
from pyantv.presets import format_currency
from pyantv import options as opts

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 美元格式
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_currency(symbol="$", precision=2)
))

# 人民币格式
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_currency(symbol="¥", precision=2)
))

# 欧元格式
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_currency(symbol="€", precision=2)
))

chart.render("formatted_currency.html")
```

**效果：**
- `1234.567` → `$1,234.57`（symbol="$"）
- `1234.567` → `¥1,234.57`（symbol="¥"）

---

## format_date

生成日期格式化 JsCode，支持自定义日期格式模式。

**函数签名：**
```python
def format_date(pattern="YYYY-MM-DD")
```

**参数：**
- `pattern` (str, 可选): 日期格式模式，默认 `"YYYY-MM-DD"`

**返回：** JsCode 对象

**支持的占位符：**
- `YYYY` - 四位年份
- `MM` - 两位月份（01-12）
- `DD` - 两位日期（01-31）
- `HH` - 两位小时（00-23）
- `mm` - 两位分钟（00-59）
- `ss` - 两位秒数（00-59）

**示例：**
```python
from pyantv import Line
from pyantv.presets import format_date
from pyantv import options as opts

chart = Line.from_data(data=data, x_field_name="date", y_field_name="value")

# 默认格式：YYYY-MM-DD
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_date()
))

# 自定义格式：YYYY/MM/DD
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_date("YYYY/MM/DD")
))

# 带时间的格式：YYYY-MM-DD HH:mm
chart.set_labels(label_opts=opts.LabelOpts(
    formatter=format_date("YYYY-MM-DD HH:mm")
))

chart.render("formatted_date.html")
```

**效果：**
- `2023-04-23T14:30:00Z` → `2023-04-23`（pattern="YYYY-MM-DD"）
- `2023-04-23T14:30:00Z` → `2023/04/23`（pattern="YYYY/MM/DD"）
- `2023-04-23T14:30:00Z` → `2023-04-23 14:30`（pattern="YYYY-MM-DD HH:mm"）

## 在 Tooltip 中使用

格式化函数也可以用于 tooltip：

```python
from pyantv import Line
from pyantv.presets import format_number, format_date
from pyantv import options as opts

chart = Line.from_data(data=data, x_field_name="date", y_field_name="value")

# 在 tooltip 中使用格式化
tooltip_config = {
    "shared": True,
    "fields": {
        "value": {
            "formatter": format_number(precision=2)
        },
        "date": {
            "formatter": format_date("YYYY-MM-DD")
        }
    }
}
chart.set_tooltip(tooltip_opts=tooltip_config)

chart.render("tooltip_formatted.html")
```

## 格式化对比

| Preset | 数据类型 | 主要用途 | 常用场景 |
|--------|---------|---------|---------|
| `format_number` | 数值 | 千分位、小数位数 | 金额、数量、指标 |
| `format_percent` | 数值 | 百分比转换 | 占比、增长率 |
| `format_currency` | 数值 | 货币符号+千分位 | 金额显示 |
| `format_date` | 日期 | 日期格式化 | 时间轴、日期标签 |

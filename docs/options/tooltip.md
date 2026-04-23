# 提示框 Options

提示框 Options 控制图表 tooltip 的显示、内容、样式等。

## TooltipOpts

提示框配置。

**参数：**
- `title` (Union[JSFunc, dict]): 标题
- `items` (Sequence[Union[TooltipItemOpts, JSFunc]]): 提示项列表

**示例：**
```python
from pyantv import options as opts

chart.set_tooltip(tooltip_opts=opts.TooltipOpts(
    title="数据详情",
    items=[
        opts.TooltipItemOpts(field="x", name="X轴"),
        opts.TooltipItemOpts(field="y", name="Y轴")
    ]
))
```

---

## TooltipItemOpts

提示框单项配置。

**参数：**
- `field` (str): 字段名
- `channel` (str): 通道名
- `value_formatter` (str): 值格式化
- `name` (str): 显示名称

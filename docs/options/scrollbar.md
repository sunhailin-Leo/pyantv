# 滚动条 Options

滚动条 Options 控制滚动条的显示和样式。

## ScrollBarOpts

滚动条总配置，用于配置 x 轴和 y 轴滚动条。

**参数：**
- `x_scroll_bar_opts` (ScrollBarCfgOpts): x 轴滚动条配置
- `y_scroll_bar_opts` (ScrollBarCfgOpts): y 轴滚动条配置

**示例：**
```python
from pyantv import options as opts

chart.set_global_options(scroll_bar_opts=opts.ScrollBarOpts(
    x_scroll_bar_opts=opts.ScrollBarCfgOpts(
        ratio=0.5,
        is_slidable=True
    )
))
```

---

## ScrollBarCfgOpts

滚动条配置。

**参数：**
- `ratio` (Numeric): 滚动条比例
- `value` (Numeric): 滚动条值
- `is_slidable` (bool): 是否可滑动
- `is_scrollable` (bool): 是否可滚动
- `style_opts` (ScrollBarStyleOpts): 滚动条样式

---

## ScrollBarStyleOpts

滚动条样式配置。

**参数：**
- `is_round` (bool): 是否圆角
- `padding` (Union[Numeric, Sequence[Numeric]]): 内边距
- `thumb_fill` (str): 滑块填充
- `thumb_fill_opacity` (Numeric): 滑块填充透明度
- `thumb_stroke` (str): 滑块描边
- `thumb_stroke_opacity` (Numeric): 滑块描边透明度
- `track_size` (Numeric): 轨道大小
- `track_fill` (str): 轨道填充
- `track_fill_opacity` (Numeric): 轨道填充透明度
- `track_stroke` (str): 轨道描边
- `track_stroke_opacity` (Numeric): 轨道描边透明度

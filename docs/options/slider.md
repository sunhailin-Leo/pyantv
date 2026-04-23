# 滑块 Options

滑块 Options 控制滑块的显示和样式。

## SliderOpts

滑块总配置，用于配置 x 轴和 y 轴滑块。

**参数：**
- `x_slider_opts` (SliderCfgOpts): x 轴滑块配置
- `y_slider_opts` (SliderCfgOpts): y 轴滑块配置

**示例：**
```python
from pyantv import options as opts

chart.set_global_options(slider_opts=opts.SliderOpts(
    x_slider_opts=opts.SliderCfgOpts(
        is_slidable=True,
        is_brushable=True
    )
))
```

---

## SliderCfgOpts

滑块配置。

**参数：**
- `values` (Numeric): 滑块值
- `is_slidable` (bool): 是否可滑动
- `is_brushable` (bool): 是否可框选
- `is_show_handle` (bool): 是否显示手柄
- `is_show_handle_label` (bool): 是否显示手柄标签
- `is_show_label_on_interaction` (bool): 交互时是否显示标签
- `is_auto_fit_label` (bool): 是否自动调整标签
- `formatter` (JSFunc): 格式化函数
- `spark_line_type` (str): 迷你图类型
- `spark_line_is_stack` (bool): 迷你图是否堆叠
- `spark_line_range` (Sequence[Numeric]): 迷你图范围
- `spark_line_color` (Union[Sequence[str], JSFunc]): 迷你图颜色
- `is_spark_line_smooth` (bool): 迷你图是否平滑
- `spark_line_stroke` (str): 迷你图描边
- `spark_line_stroke_opacity` (Numeric): 迷你图描边透明度
- `spark_line_dash` (Sequence[Numeric]): 迷你图虚线
- `spark_line_area_fill` (str): 迷你图区域填充
- `spark_line_area_fill_opacity` (Numeric): 迷你图区域填充透明度
- `spark_line_column_fill` (str): 迷你图柱状填充
- `spark_line_column_fill_opacity` (Numeric): 迷你图柱状填充透明度
- `spark_line_is_group` (bool): 迷你图是否分组
- `spark_line_spacing` (Numeric): 迷你图间距
- `style_opts` (SliderStyleOpts): 滑块样式

---

## SliderStyleOpts

滑块样式配置。

**参数：**
- `padding` (Union[Numeric, Sequence[Numeric]]): 内边距
- `selection_fill` (str): 选中区域填充
- `selection_fill_opacity` (Numeric): 选中区域填充透明度
- `selection_stroke` (str): 选中区域描边
- `selection_stroke_opacity` (Numeric): 选中区域描边透明度
- `track_fill` (str): 轨道填充
- `track_fill_opacity` (Numeric): 轨道填充透明度
- `track_stroke` (str): 轨道描边
- `track_stroke_opacity` (Numeric): 轨道描边透明度
- `handle_icon_size` (Numeric): 手柄图标大小
- `handle_icon_fill` (Numeric): 手柄图标填充
- `handle_icon_fill_opacity` (Numeric): 手柄图标填充透明度
- `handle_icon_stroke` (str): 手柄图标描边
- `handle_icon_stroke_opacity` (Numeric): 手柄图标描边透明度
- `handle_label_font_size` (Numeric): 手柄标签字号
- `handle_label_font_weight` (Union[Numeric, str]): 手柄标签字重
- `handle_label_stroke` (str): 手柄标签描边
- `handle_label_stroke_opacity` (Numeric): 手柄标签描边透明度

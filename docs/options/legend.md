# 图例 Options

图例 Options 控制图例的显示、样式、布局等。

## LegendCategoryOpts

分类图例，用于离散型数据（如颜色、形状编码）。

**参数：**
- `color_legend_opts` (Union[LegendCategoryCfgOpts, bool]): 颜色图例配置
- `size_legend_opts` (Union[LegendCategoryCfgOpts, bool]): 大小图例配置

**示例：**
```python
from pyantv import options as opts

chart.set_legend(legend_opts=opts.LegendCategoryOpts(
    color_legend_opts=opts.LegendCategoryCfgOpts(
        position="bottom"
    )
))
```

---

## LegendContinuousOpts

连续图例，用于连续型数据（如颜色渐变）。

**参数：**
- `x_legend_opts` (LegendAxisOpts): x 轴图例配置
- `y_legend_opts` (LegendAxisOpts): y 轴图例配置

---

## LegendAxisOpts

连续图例配置（颜色条图例）。

**参数：**
- `color` (Union[Sequence[str], JSFunc]): 颜色
- `is_block` (bool): 是否为块状
- `type_` (str): 类型
- `ribbon_size` (Numeric): 带状大小
- `ribbon_fill` (str): 带状填充
- `ribbon_fill_opacity` (Numeric): 带状填充透明度
- `ribbon_stroke` (str): 带状描边
- `ribbon_stroke_opacity` (Numeric): 带状描边透明度
- `is_show_handle` (bool): 是否显示手柄
- `is_show_handle_label` (bool): 是否显示手柄标签
- `handle_formatter` (JSFunc): 手柄格式化
- `is_slidable` (bool): 是否可滑动
- `range_` (Sequence[Numeric]): 范围
- `step` (Numeric): 步长
- `handle_marker_fill` (JSFunc): 手柄标记填充
- `handle_marker_fill_opacity` (Union[Numeric, JSFunc]): 手柄标记填充透明度
- `handle_marker_stroke` (JSFunc): 手柄标记描边
- `handle_marker_stroke_opacity` (Union[Numeric, JSFunc]): 手柄标记描边透明度
- `handle_label_font_size` (Union[Numeric, JSFunc]): 手柄标签字号
- `handle_label_font_family` (JSFunc): 手柄标签字体
- `handle_label_font_weight` (Union[Numeric, JSFunc]): 手柄标签字重
- `handle_label_fill` (JSFunc): 手柄标签颜色
- `handle_label_fill_opacity` (Union[Numeric, JSFunc]): 手柄标签透明度
- `handle_label_stroke` (JSFunc): 手柄标签描边
- `handle_label_stroke_opacity` (Union[Numeric, JSFunc]): 手柄标签描边透明度
- `is_show_label` (bool): 是否显示标签
- `label_formatter` (JSFunc): 标签格式化
- `label_filter` (JSFunc): 标签过滤
- `label_direction` (str): 标签方向
- `label_spacing` (Numeric): 标签间距
- `label_align` (str): 标签对齐
- `label_font_size` (Union[Numeric, JSFunc]): 标签字号
- `label_font_family` (JSFunc): 标签字体
- `label_font_weight` (Union[Numeric, JSFunc]): 标签字重
- `label_stroke` (JSFunc): 标签描边
- `label_stroke_opacity` (Union[Numeric, JSFunc]): 标签描边透明度
- `is_show_indicator` (bool): 是否显示指示器
- `indicator_formatter` (JSFunc): 指示器格式化
- `indicator_label_font_size` (Union[Numeric, JSFunc]): 指示器标签字号
- `indicator_label_font_family` (JSFunc): 指示器标签字体
- `indicator_label_font_weight` (Union[Numeric, JSFunc]): 指示器标签字重
- `indicator_label_stroke` (JSFunc): 指示器标签描边
- `indicator_label_stroke_opacity` (Union[Numeric, JSFunc]): 指示器标签描边透明度
- `indicator_background_fill` (JSFunc): 指示器背景填充
- `indicator_background_fill_opacity` (Union[Numeric, JSFunc]): 指示器背景填充透明度
- `indicator_background_stroke` (JSFunc): 指示器背景描边
- `indicator_background_stroke_opacity` (Union[Numeric, JSFunc]): 指示器背景描边透明度
- `title_opts` (LegendTitleOpts): 标题配置
- `layout_opts` (LegendLayoutOpts): 布局配置

---

## LegendCategoryCfgOpts

分类图例配置。

**参数：**
- `position` (str): 位置
- `item_marker` (JSFunc): 标记样式
- `item_marker_fill` (JSFunc): 标记填充
- `item_marker_fill_opacity` (Union[Numeric, JSFunc]): 标记填充透明度
- `item_marker_stroke` (JSFunc): 标记描边
- `item_marker_stroke_opacity` (Union[Numeric, JSFunc]): 标记描边透明度
- `item_label_text` (JSFunc): 标签文本
- `item_label_font_size` (Union[Numeric, JSFunc]): 标签字号
- `item_label_font_family` (JSFunc): 标签字体
- `item_label_font_weight` (Union[Numeric, JSFunc]): 标签字重
- `item_label_fill` (JSFunc): 标签颜色
- `item_label_fill_opacity` (Union[Numeric, JSFunc]): 标签透明度
- `item_label_stroke` (JSFunc): 标签描边
- `item_label_stroke_opacity` (Union[Numeric, JSFunc]): 标签描边透明度
- `item_value_text` (JSFunc): 值文本
- `item_value_font_size` (Union[Numeric, JSFunc]): 值字号
- `item_value_font_family` (JSFunc): 值字体
- `item_value_font_weight` (Union[Numeric, JSFunc]): 值字重
- `item_value_fill` (JSFunc): 值颜色
- `item_value_fill_opacity` (Union[Numeric, JSFunc]): 值透明度
- `item_value_stroke` (JSFunc): 值描边
- `item_value_stroke_opacity` (Union[Numeric, JSFunc]): 值描边透明度
- `item_span` (Union[Numeric, Sequence[Numeric]]): 项跨度
- `item_spacing` (Union[Numeric, Sequence[Numeric]]): 项间距
- `item_background_fill` (str): 项背景填充
- `item_background_fill_opacity` (Numeric): 项背景填充透明度
- `nav_effect` (JSFunc): 导航效果
- `nav_duration` (Numeric): 导航持续时间
- `nav_orientation` (str): 导航方向
- `nav_default_page` (Numeric): 默认页
- `is_nav_loop` (bool): 是否循环导航
- `nav_page_num_fill` (str): 页码填充
- `nav_page_num_font_size` (Numeric): 页码字号
- `nav_page_num_opacity` (Numeric): 页码透明度
- `nav_page_num_stroke` (str): 页码描边
- `nav_page_num_stroke_opacity` (Numeric): 页码描边透明度
- `nav_button_fill` (str): 按钮填充
- `nav_button_opacity` (Numeric): 按钮透明度
- `nav_button_stroke` (str): 按钮描边
- `nav_button_stroke_opacity` (Numeric): 按钮描边透明度
- `nav_formatter` (JSFunc): 导航格式化
- `title_opts` (LegendTitleOpts): 标题配置
- `layout_opts` (LegendLayoutOpts): 布局配置

---

## LegendTitleOpts

图例标题配置。

**参数：**
- `title` (Union[bool, str]): 标题内容
- `title_spacing` (Union[Numeric, Sequence[Numeric]]): 标题间距
- `title_inset` (Union[Numeric, Sequence[Numeric]]): 标题内边距
- `title_position` (str): 标题位置
- `title_font_size` (Numeric): 标签字号
- `title_font_family` (str): 标题字体
- `title_font_weight` (Numeric): 标签字重
- `title_fill` (str): 标题颜色
- `title_fill_opacity` (Numeric): 标题透明度
- `title_stroke` (str): 标题描边
- `title_stroke_opacity` (Numeric): 标题描边透明度

---

## LegendLayoutOpts

图例布局配置。

**参数：**
- `cols` (Numeric): 列数
- `col_padding` (Numeric): 列间距
- `row_padding` (Numeric): 行间距
- `max_rows` (Numeric): 最大行数
- `max_cols` (Numeric): 最大列数
- `justify_content` (str): 内容对齐
- `align_items` (str): 项目对齐
- `flex_direction` (str): 弹性方向

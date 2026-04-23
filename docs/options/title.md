# 标题 Options

标题 Options 控制图表标题的显示和样式。

## TitleOpts

标题配置。

**参数：**
- `size` (Numeric): 标题大小
- `title` (str): 标题文本
- `subtitle` (str): 副标题文本
- `align` (str): 对齐方式
- `spacing` (Numeric): 间距
- `title_font_size` (Numeric): 标题字号
- `title_font_family` (str): 标题字体
- `title_font_weight` (Numeric): 标签字重
- `title_fill` (JSFunc): 标题颜色
- `title_fill_opacity` (Union[Numeric, JSFunc]): 标题填充透明度
- `title_stroke` (JSFunc): 标题描边
- `title_line_width` (Union[Numeric, JSFunc]): 标题线宽
- `title_stroke_opacity` (Union[Numeric, JSFunc]): 标题描边透明度
- `subtitle_font_size` (Numeric): 副标题字号
- `subtitle_font_family` (Numeric): 副标题字体
- `subtitle_font_weight` (Numeric): 副标题字重
- `subtitle_fill` (JSFunc): 副标题颜色
- `subtitle_fill_opacity` (Union[Numeric, JSFunc]): 副标题填充透明度
- `subtitle_stroke` (JSFunc): 副标题描边
- `subtitle_line_width` (Union[Numeric, JSFunc]): 副标题线宽
- `subtitle_stroke_opacity` (Union[Numeric, JSFunc]): 副标题描边透明度

**示例：**
```python
from pyantv import options as opts

chart.set_title(title_opts=opts.TitleOpts(
    title="销售数据趋势",
    subtitle="2023年度",
    align="center",
    title_font_size=20,
    title_fill="#333333"
))
```

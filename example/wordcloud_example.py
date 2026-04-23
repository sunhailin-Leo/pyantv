from pyantv import options as opts
from pyantv.charts import Wordcloud


c = (
    Wordcloud(render_opts=opts.RenderOpts(is_auto_fit=True, padding_top=40))
    .set_data(
        data=opts.FetchDataOpts(
            value="https://assets.antv.antgroup.com/g2/philosophy-word.json",
        )
    )
    .set_encode(color_field="text")
    .set_scale(
        color_scale_opts={"palette": "viridis"}, size_scale_opts={"range": [6, 20]}
    )
    .set_wordcloud_layout(
        sprial="rectangular",
        font_size=[20, 100],
    )
    .render("wordcloud_example.html")
)

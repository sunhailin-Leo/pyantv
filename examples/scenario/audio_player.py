"""
音频播放器可视化
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#audio-player
"""
from pyantv import options as opts
from pyantv.charts import Interval

import random
random.seed(42)
data = [{"freq": i, "amplitude": random.uniform(10, 80)} for i in range(32)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="freq", y_field_name="amplitude", color_field="amplitude")
    .set_global_options(
        title_opts=opts.TitleOpts(title="音频播放器可视化"),
    )
)
chart.render("audio_player.html")

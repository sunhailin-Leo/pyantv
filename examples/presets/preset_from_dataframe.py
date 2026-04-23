"""DataFrame 快捷出图示例。"""
import pandas as pd

from pyantv import Line
from pyantv.presets import with_dark_theme, with_auto_fit

df = pd.DataFrame({
    "year": ["2020", "2021", "2022", "2023", "2024"],
    "users": [1200, 1800, 2500, 3200, 4100],
})

chart = Line.from_dataframe(df).set_title("用户增长趋势")
with_dark_theme(chart)
with_auto_fit(chart)
chart.render("preset_from_dataframe.html")

from pyantv import options as opts
from pyantv.charts import Point

point = (
    Point()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://gw.alipayobjects.com/os/basement_prod/6b4aa721-b039-49b9-99d8-540b3f87d339.json",
        ),
    )
    .set_encode(x_field_name="height", y_field_name="weight", color_field="gender")
)
point.render("point_example.html")

# RepeatMatrix

## 概述

重复矩阵（RepeatMatrix）组合图表。

基于 G2 的 `repeatMatrix` 复合视图，对一组字段两两组合
生成 N×M 的散点矩阵，常用于多维数据的相关性快速探索
（散点图矩阵 / SPLOM）。

## 配置项

- **set_repeat_matrix_encode(x_field_name, y_field_name)**: 指定行列字段集合，传入 `Sequence[str]` 自动展开为矩阵
- **set_repeat_matrix_children(children)**: 设置每个矩阵格内复用的子图表（通常为 `Point`）

## 示例

```python
from pyantv import RepeatMatrix, Point

cell = (
    Point()
    .set_data(data=[...])
)

matrix = (
    RepeatMatrix()
    .set_repeat_matrix_encode(
        x_field_name=["sepal_length", "sepal_width", "petal_length"],
        y_field_name=["sepal_length", "sepal_width", "petal_length"],
    )
    .set_repeat_matrix_children(children=[cell.get_options()])
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

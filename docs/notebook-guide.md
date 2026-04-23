# Notebook 使用指南

pyantv 提供了深度集成的 Jupyter Notebook 支持，让你在 Jupyter Notebook、JupyterLab、Google Colab 和 VS Code Notebook 中直接内联渲染图表，无需任何额外代码。

## 安装

```bash
pip install pyantv[notebook]
```

或者单独安装：

```bash
pip install pyantv ipython>=7.0
```

## 基本用法

在 Jupyter Notebook 中使用 pyantv 非常简单：

```python
from pyantv import Line

# 创建图表
data = [
    {"x": "A", "y": 10},
    {"x": "B", "y": 20},
    {"x": "C", "y": 15},
]

chart = Line().set_data(data).set_encode(x_field_name="x", y_field_name="y")

# 在 cell 中直接显示图表（无需调用 render()）
chart
```

图表会自动在 notebook 中渲染为交互式可视化。

## 全局配置

使用 `notebook_config()` 函数可以全局配置 notebook 中图表的渲染参数：

```python
from pyantv.render.notebook import notebook_config

# 配置宽度、高度和主题
notebook_config(width="80%", height="400px", theme="dark")

# 之后创建的所有图表都会使用这些配置
chart = Line().set_data(data).set_encode(x_field_name="x", y_field_name="y")
chart  # 将以 80% 宽度、400px 高度、暗色主题渲染
```

### 配置参数

- **width**: 图表宽度，默认 "100%"
- **height**: 图表高度，默认 "400px"
- **theme**: 主题，可选 "default" 或 "dark"，默认 "default"

## Google Colab 使用

pyantv 完美支持 Google Colab。只需：

1. 在 Colab 中安装 pyantv：
   ```python
   !pip install pyantv[notebook]
   ```

2. 创建并显示图表：
   ```python
   from pyantv import Line
   chart = Line().set_data(data).set_encode(x_field_name="x", y_field_name="y")
   chart
   ```

你可以直接在 Colab 中打开我们的 [quickstart.ipynb](https://colab.research.google.com/github/sunhailin-Leo/pyantv/blob/main/notebooks/quickstart.ipynb) 快速开始。

## Binder 使用

Binder 让你可以在浏览器中直接运行 Jupyter Notebook，无需本地安装。

点击 Binder badge 即可启动：

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sunhailin-Leo/pyantv/main?labpath=notebooks/quickstart.ipynb)

Binder 会：
1. 克隆 pyantv 仓库
2. 安装所有依赖
3. 启动 Jupyter Lab
4. 打开指定的 notebook

## VS Code Notebook 使用

VS Code 也支持 Jupyter Notebook，使用方法与 Jupyter Notebook 完全相同：

1. 安装 Python 和 Jupyter 扩展
2. 创建 `.ipynb` 文件
3. 使用 pyantv 创建图表并直接显示

## 自动生成 Notebook

如果你有 `example/` 目录下的 Python 示例文件，可以使用 `scripts/gen_notebooks.py` 自动生成 notebook：

```bash
# 生成所有 example 的 notebook
python scripts/gen_notebooks.py --write

# 检查现有 notebook 是否与 example 同步
python scripts/gen_notebooks.py --check

# 只生成指定的 example
python scripts/gen_notebooks.py --write --example example/line_example.py

# 显示详细输出
python scripts/gen_notebooks.py --write --verbose
```

## 常见问题

### Q: 图表在 notebook 中不显示？

A: 确保你安装了 `ipython>=7.0`：
```bash
pip install --upgrade ipython
```

### Q: 如何调整图表大小？

A: 使用 `notebook_config()` 全局配置，或创建图表后调用 `set_options()`：
```python
from pyantv.render.notebook import notebook_config
notebook_config(width="80%", height="500px")
```

### Q: 可以在 notebook 中导出图表吗？

A: 可以。在 notebook 中渲染后，右键图表即可保存为图片。或者使用 `chart.render("output.html")` 导出为 HTML 文件。

### Q: 支持哪些 notebook 环境？

A: 支持：
- Jupyter Notebook
- JupyterLab
- Google Colab
- VS Code Notebook
- Binder

### Q: 图表在 notebook 中是静态的吗？

A: 不是。pyantv 图表是交互式的，支持缩放、平移、悬停提示等功能。

## 示例 Notebook

查看完整的示例：
- [quickstart.ipynb](https://github.com/sunhailin-Leo/pyantv/blob/main/notebooks/quickstart.ipynb) - 快速入门
- [all_charts.ipynb](https://github.com/sunhailin-Leo/pyantv/blob/main/notebooks/all_charts.ipynb) - 所有图表类型展示

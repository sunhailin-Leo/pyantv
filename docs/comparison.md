# pyantv vs pyecharts vs py-vchart

本文档从多个维度对比 pyantv、pyecharts 和 py-vchart 三个 Python 数据可视化库，帮助开发者选择适合的工具。

## API 设计

| 维度 | pyantv | pyecharts | py-vchart |
|------|--------|-----------|-----------|
| 设计理念 | 链式调用，类似 pyecharts，但基于 AntV G2 语法 | 链式调用，配置项丰富 | 函数式 API，更接近 VChart 原生语法 |
| 学习曲线 | 中等，熟悉 AntV G2 或 pyecharts 的开发者容易上手 | 中等，配置项较多但文档完善 | 较低，API 更简洁直接 |
| 代码示例 | `Line().set_data(data).set_encode(x_field_name="x", y_field_name="y")` | `Line().add_xaxis(x_data).add_yaxis(y_data)` | `Line(data, x="x", y="y")` |
| 类型提示 | 完整的类型注解，IDE 支持良好 | 部分类型注解 | 完整的类型注解 |

## 图表覆盖

| 维度 | pyantv | pyecharts | py-vchart |
|------|--------|-----------|-----------|
| 基础图表 | Line, Area, Bar (Interval), Point, Pie, Heatmap 等 | Line, Bar, Pie, Scatter, Radar 等 | Line, Bar, Pie, Scatter, Area 等 |
| 高级图表 | Sankey, Treemap, Chord, ForceGraph, WordCloud, Gauge, Liquid 等 | Graph, Tree, Map, 3D 图表等 | Sankey, Treemap, Graph 等 |
| 3D 图表 | Point3D, Line3D, Interval3D（基于 WebGL） | 丰富的 3D 图表（3D Bar, 3D Line, 3D Scatter 等） | 支持 3D 图表（有限） |
| 图表数量 | 44 种图表类型（8 大分类） | 50+ 种图表类型 | 20+ 种图表类型 |
| 组合图表 | 支持 View、Facet、Space 等组合方式 | 支持 Grid、Page、Tab 等组合 | 支持组合视图 |

## 性能

| 维度 | pyantv | pyecharts | py-vchart |
|------|--------|-----------|-----------|
| 渲染引擎 | AntV G2（Canvas/SVG/WebGL） | ECharts（Canvas/SVG） | VChart（Canvas/SVG） |
| 大数据量 | 良好，G2 针对大数据优化 | 良好，ECharts 有数据降采样 | 良好，VChart 有性能优化 |
| 渲染速度 | 中等，依赖浏览器渲染 | 快，ECharts 渲染优化成熟 | 快，VChart 基于 VRender |
| 内存占用 | 中等 | 较低 | 较低 |
| 动画性能 | 流畅，G2 动画引擎强大 | 流畅，ECharts 动画丰富 | 流畅，VChart 动画优化 |

## 生态

| 维度 | pyantv | pyecharts | py-vchart |
|------|--------|-----------|-----------|
| 社区活跃度 | 较新，社区规模较小 | 成熟，社区活跃，贡献者众多 | 较新，社区活跃 |
| 文档完善度 | 文档和示例持续完善 | 文档非常完善，示例丰富 | 文档完善，示例丰富 |
| 插件系统 | 内置插件系统（渲染器切换、手绘风格、Lottie 动画） | 插件较少，主要通过配置扩展 | 插件系统较弱 |
| Web 框架集成 | 支持 Flask、Django、Sanic、Streamlit | 支持 Flask、Django、Sanic 等 | 支持主流 Web 框架 |
| Notebook 支持 | 支持 Jupyter Notebook、JupyterLab | 支持 Jupyter Notebook、JupyterLab | 支持 Jupyter Notebook、JupyterLab |

## 文档

| 维度 | pyantv | pyecharts | py-vchart |
|------|--------|-----------|-----------|
| 文档语言 | 中文、英文、日文 | 中文、英文 | 中文、英文 |
| 示例数量 | 440+ 个完整示例（位于 `examples/`） | 500+ 个示例 | 200+ 个示例 |
| API 文档 | 完整的 API 参考文档 | 完整的 API 参考文档 | 完整的 API 参考文档 |
| 教程质量 | 快速开始、API 参考、高级特性 | 入门教程、进阶教程、最佳实践 | 入门教程、API 参考 |
| 社区支持 | GitHub Issues、Discussions | GitHub Issues、Gitter、论坛 | GitHub Issues、Discussions |

## License

| 维度 | pyantv | pyecharts | py-vchart |
|------|--------|-----------|-----------|
| 开源协议 | MIT License | MIT License | MIT License |
| 商业使用 | 允许，无限制 | 允许，无限制 | 允许，无限制 |
| 修改与分发 | 允许，需保留版权声明 | 允许，需保留版权声明 | 允许，需保留版权声明 |
| 专利授权 | 无明确专利授权 | 无明确专利授权 | 无明确专利授权 |

## 总结

- **pyantv**：适合需要 AntV G2 强大可视化能力的场景，提供链式调用 API、丰富的图表类型和插件系统，适合数据分析和交互式可视化需求。
- **pyecharts**：成熟稳定，图表类型丰富，生态完善，适合需要快速生成各类图表的场景，社区支持强大。
- **py-vchart**：API 简洁，基于 VChart 的现代化设计，适合需要轻量级、高性能可视化的场景，文档和示例完善。

选择建议：
- 如果需要 AntV G2 的强大功能和丰富的交互能力，选择 **pyantv**
- 如果需要成熟稳定的解决方案和丰富的图表类型，选择 **pyecharts**
- 如果需要简洁的 API 和现代化的可视化设计，选择 **py-vchart**

> Last updated: 2026-04-23

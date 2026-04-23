# 🐍 pyantv 示例画廊

基于 [AntV G2 v5](https://g2.antv.antgroup.com/) 的 Python 可视化库 **pyantv** 的完整示例集合。

## 📊 概览

共包含 **440+ 个示例**，覆盖 G2 官方文档的所有示例分类：

| 分类 | 说明 | 示例数 |
|------|------|--------|
| `general/` | 基础图表（折线、面积、柱形、饼图、散点等） | 200+ |
| `annotation/` | 数据标注（文本、线、区间、图形、连接） | 15 |
| `component/` | 组件（坐标轴、图例、提示、标签、动画等） | 50+ |
| `composite/` | 空间复合（分面、重复矩阵、空间布局） | 15 |
| `tree/` | 树图（矩形树图、打包图、火焰图） | 6 |
| `network/` | 关系图（桑基图、弦图、力导向图） | 4 |
| `map/` | 地图（行政地图、航班图、地铁图等） | 7 |
| `interaction/` | 交互（事件、刷选、数形交互） | 20+ |
| `advanced/` | 高级功能（洞察标注、叙事、排序、单元可视化） | 30+ |
| `threed/` | 3D 图表（散点、折线、柱形、曲面） | 15 |
| `fun/` | 趣味可视化（花瓣图、2.5D 柱形等） | 5 |
| `scenario/` | 场景可视化（股票K线、心率监测等） | 10 |
| `style/` | 样式（主题、手绘、纹理、渲染器等） | 23 |

## 🚀 快速开始

### 1. 安装依赖

```bash
cd pyantv
pip install -e .
```

### 2. 运行单个示例

```bash
python examples/general/line/basic_line.py
# 生成 basic_line.html，用浏览器打开即可查看
```

### 3. 生成画廊页面

```bash
# 方式一：使用 Makefile
cd examples && make generate

# 方式二：直接运行 Python 脚本
python examples/generate_gallery.py
```

生成完成后，用浏览器打开 `examples/index.html` 即可浏览所有 440+ 个示例。

### 4. 启动本地服务器浏览

```bash
# 方式一：使用 Makefile（推荐）
cd examples && make serve

# 方式二：指定端口
cd examples && make serve PORT=3000

# 方式三：手动启动
cd examples && python -m http.server 8080
# 然后访问 http://localhost:8080
```

## 🛠️ Makefile 命令

在 `examples/` 目录下执行：

```bash
make generate        # 重新生成画廊（运行所有示例 + 生成 index.html）
make serve           # 启动本地 HTTP 服务器浏览画廊（默认端口 8080）
make serve PORT=3000 # 指定端口
make clean           # 清理生成的 HTML 文件（_output/ 和 index.html）
make open            # 用浏览器打开画廊页面
make help            # 显示帮助信息
```

## 📁 目录结构

```
examples/
├── index.html              # 画廊页面（自动生成）
├── generate_gallery.py     # 画廊生成脚本
├── Makefile                # 便捷操作命令
├── README.md               # 本文件
├── _output/                # 渲染输出目录（自动生成）
├── general/                # 基础图表
│   ├── line/               # 折线图
│   ├── area/               # 面积图
│   ├── interval/           # 条形图/柱形图
│   ├── pie/                # 饼图
│   ├── point/              # 散点图
│   └── ...
├── annotation/             # 数据标注
├── component/              # 组件
├── composite/              # 空间复合
├── tree/                   # 树图
├── network/                # 关系图
├── map/                    # 地图
├── interaction/            # 交互
├── advanced/               # 高级功能
├── threed/                 # 3D 图表
├── fun/                    # 趣味可视化
├── scenario/               # 场景可视化
└── style/                  # 样式
```

## 📖 参考

- [pyantv 项目](https://github.com/sunhailin-Leo/pyantv)
- [AntV G2 官方文档](https://g2.antv.antgroup.com/)
- [G2 官方示例](https://g2.antv.antgroup.com/examples)

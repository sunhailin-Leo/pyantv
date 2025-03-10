<h1 align="center">pyantv</h1>
<p align="center">
    <em>Python ❤️ AntV = pyantv</em>
</p>
<p align="center">
    <a href="https://github.com/sunhailin-Leo/pyantv/actions">
        <img src="https://github.com/sunhailin-Leo/pyantv/actions/workflows/python-app.yml/badge.svg" alt="Github Actions Status">
    </a>
    <a href="https://codecov.io/gh/sunhailin-Leo/pyantv">
        <img src="https://codecov.io/gh/sunhailin-Leo/pyantv/branch/master/graph/badge.svg" alt="Codecov">
    </a>
</p>
<p align="center">
    <a href="https://github.com/sunhailin-Leo/pyantv/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

[中文 README](README.md) | [English README](README.en.md) | [日本語（にほんご）README](README.jp.md)

## 📣 简介

[AntV](https://github.com/antvis) 是蚂蚁集团推出的一套数据可视化解决方案，专注于 Web 数据可视化领域。它基于它基于可视化语法库 AntV Design 和渲染引擎 G 进行封装，在满足数据呈现的同时，还支持面向叙事场景的动画编排、丰富的交互能力和定制化的图表风格，简单易用的配置大大降低了用户的学习成本。而 Python 是一门富有表达力的语言，非常适合用于数据处理、AI 等场景。当数据分析，建模遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts)、[py-vchart](https://github.com/VisActor/py-vchart) 和 [py-antv](https://github.com/sunhailin-Leo/pyantv) 诞生了。

## ✨ 特性

* [pyecharts](https://github.com/pyecharts/pyecharts) like 的 API 设计，使用如丝滑般流畅，支持链式调用
* 囊括了 AntV G2 的大部分图表（后续兼容 AntV G2 的更多图表以及 AntV 生态的其他图表）
* 支持主流 Notebook 环境，Jupyter Notebook、JupyterLab
* 可轻松集成至 Flask，Sanic，Django 等主流 Web 框架 (**Coming soon...**)
* 高度灵活的配置项，可轻松搭配出精美的图表
* 详细的文档和示例，帮助开发者更快的上手项目

## 🔰 安装

**pip 安装**
```shell
# 安装
$ pip install pyantv -U
```

**源码安装**
```shell
# 源码安装
$ git clone https://github.com/sunhailin-Leo/pyantv
$ cd pyantv
$ pip install -r requirements.txt
$ python setup.py install
```

## ⛏ 代码质量

### 单元测试

```shell
$ pip install -r test/requirements.txt
$ make
```

### 集成测试

使用 Github Actions 持续集成环境。

### 代码规范

使用 [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) 以及 [pylint](https://www.pylint.org/) 提升代码质量。

## 😉 Author

pyantv 主要由以下几位开发者开发维护

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

## 💡 贡献

期待能有更多的开发者参与到 pyantv 的开发中来，我们会保证尽快 Reivew PR 并且及时回复。但提交 PR 请确保

1. 通过所有单元测试，如若是新功能，请为其新增单元测试
2. 遵守开发规范，使用 black 以及 isort 格式化代码（$ pip install -r requirements-dev.txt）
3. 如若需要，请更新相对应的文档

我们也非常欢迎开发者能为 pyantv 提供更多的示例，共同来完善文档，(文档在准备中...)

## 📃 License

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)
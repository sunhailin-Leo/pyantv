<p align="center">
    <em>Python ❤️ AntV = pyantv</em>
</p>

<p align="center">
    <a href="https://github.com/sunhailin-Leo/pyantv/actions">
        <img src="https://github.com/sunhailin-Leo/pyantv/actions/workflows/python-app.yml/badge.svg" alt="GitHub Actions Status">
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

<img src="https://gw.alipayobjects.com/zos/antfincdn/R8sN%24GNdh6/language.svg" width="18"> [Chinese README](README.md) | [English README](README.en.md) | [Japanese README](README.jp.md)

## 📣 Announcement

[AntV](https://github.com/antvis), initiated by Ant Group and open-sourced starting in 2017, reimagines data visualization by embedding the theory of graphical grammar into the JavaScript language. In response to rigid chart libraries that force a trade-off between flexibility and usability, we have categorized data visualization techniques into four series: 2, 6, 7, and 8, which respectively represent statistical analysis, graph analysis, geographical analysis, and unstructured data visualization. We have expanded these capabilities across different levels, including chart libraries, R&D tools, and AI-powered intelligent visualization.

Python, with its expressive power, is well-suited for data processing and AI scenarios. When data analysis and modeling meet data visualization, projects like [pyecharts](https://github.com/pyecharts/pyecharts), [py-vchart](https://github.com/VisActor/py-vchart), and [py-antv](https://github.com/sunhailin-Leo/pyantv) were born.

## ✨ Features

* API design inspired by [pyecharts](https://github.com/pyecharts/pyecharts), providing a smooth and fluent interface that supports chain calls.
* Includes most of the charts from AntV G2 (with plans to support more AntV G2 charts and other charts in the AntV ecosystem).
* Supports mainstream Notebook environments such as Jupyter Notebook and JupyterLab.
* Can be easily integrated into popular Web frameworks like Flask, Sanic, Django (**Coming soon...**).
* Highly flexible configuration options allow for the creation of beautiful charts.
* Detailed documentation and examples help developers get up to speed quickly.

## 🔰 Installation

**pip installation**

```shell
# 安装
$ pip install pyantv -U
```

**Source Code Installation**

```shell
# Source code installation
$ git clone https://github.com/sunhailin-Leo/pyantv 
$ cd pyantv 
$ pip install -r requirements.txt 
$ python setup.py install
```

## ⛏ Code Quality

### Unit Testing

```shell
$ pip install -r test/requirements.txt
$ make
```

### Integration Testing

Uses GitHub Actions for continuous integration.

### Code Standards

Uses [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/), and [pylint](https://www.pylint.org/) to enhance code quality.

## Authors

pyantv is primarily developed and maintained by the following developers:

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

## Contributions

We welcome more developers to contribute to pyantv. We will ensure PRs are reviewed promptly and replies are timely. However, please ensure the following when submitting a PR:

1. Pass all unit tests; if adding new features, include corresponding unit tests.
2. Follow development standards and format code using black and isort (`$ pip install -r requirements-dev.txt`).
3. Update relevant documentation if necessary.

We also welcome developers to provide more examples to improve the documentation (documentation is in preparation).

## License

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)

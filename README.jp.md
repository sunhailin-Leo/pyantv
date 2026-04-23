<h1 align="center">pyantv</h1>
<p align="center">
    <em>Python ❤️ AntV = pyantv</em>
</p>
<p align="center">
    <a href="https://github.com/sunhailin-Leo/pyantv/actions/workflows/python-app.yml">
        <img src="https://github.com/sunhailin-Leo/pyantv/actions/workflows/python-app.yml/badge.svg" alt="CI Status">
    </a>
    <a href="https://github.com/sunhailin-Leo/pyantv/actions/workflows/docs-deploy.yml">
        <img src="https://github.com/sunhailin-Leo/pyantv/actions/workflows/docs-deploy.yml/badge.svg" alt="Docs Deploy Status">
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
    <a href="https://colab.research.google.com/github/sunhailin-Leo/pyantv/blob/main/notebooks/quickstart.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
    </a>
    <a href="https://mybinder.org/v2/gh/sunhailin-Leo/pyantv/main?labpath=notebooks/quickstart.ipynb">
        <img src="https://mybinder.org/badge_logo.svg" alt="Binder">
    </a>
</p>

[中国語 README](README.md) | [英語 README](README.en.md) | [日本語 README](README.jp.md)


## 📣 紹介

[AntV](https://github.com/antvis) はアリババグループが提供するデータ可視化ソリューションで、Web データ可視化分野に焦点を当てています。これは、可視化文法ライブラリ AntV Design とレンダリングエンジン G を基にしており、データ表示だけでなく、ナラティブシーン向けのアニメーション編成、豊富なインタラクション能力、カスタマイズ可能なチャートスタイルもサポートしています。シンプルで使いやすい設定により、ユーザーの学習コストを大幅に削減します。一方、Python は表現力豊かな言語であり、データ処理や AI などのシナリオに非常に適しています。データ分析やモデリングがデータ可視化と出会うとき、[pyecharts](https://github.com/pyecharts/pyecharts)、[py-vchart](https://github.com/VisActor/py-vchart) そして [py-antv](https://github.com/sunhailin-Leo/pyantv) が誕生しました。

## ✨ 特徴

* [pyecharts](https://github.com/pyecharts/pyecharts) のような API 設計で、スムーズに使用でき、チェーン呼び出しをサポート
* AntV G2 の大部分のチャートを含み、将来的には AntV G2 の他のチャートや AntV エコシステムの他のチャートにも対応予定
* Jupyter Notebook、JupyterLab などの主流のノートブック環境をサポート
* Flask、Sanic、Django、Streamlit などの主流の Web フレームワークに簡単に統合可能
* 3D チャートをサポート（Point3D、Line3D、Interval3D）
* 組み込みプラグインシステム：レンダラー切替（Canvas/SVG/WebGL）、手描きスタイル（Rough）、Lottie アニメーション
* pandas DataFrame / numpy ndarray をデータソースとして直接使用可能
* アノテーションシステム：参照線、領域アノテーション、テキストアノテーション
* チャートエクスポート：PNG 画像としてエクスポート可能（Playwright ベース）
* 入力バリデーション：無効なパラメータが渡された場合に明確なエラーメッセージを表示
* 高度に柔軟な設定項目で、美しいチャートを簡単に作成可能
* 詳細なドキュメントと例があり、開発者がプロジェクトを迅速に習得できるよう支援（[オンラインドキュメント](https://sunhailin-Leo.github.io/pyantv)）
* 🆕 **クイックチャート作成**：`from_data()` / `from_dataframe()` で一行でチャートを作成、エンコーディングフィールドを自動推論
* 🆕 **イベントシステム**：90+ の G2 イベント定数 + `set_events()` Pythonic API でインタラクションを簡単にバインド
* 🆕 **プリセットシステム**：31 のすぐに使えるプリセット関数（テーマ、アニメーション、レイアウト、座標系、インタラクション、データ変換、フォーマッター）
* 🆕 **インタラクションプリセット**：`with_element_highlight()`、`with_brush_filter()`、`with_fisheye()` で一行でインタラクションを有効化
* 🆕 **データ変換プリセット**：`with_stack()`、`with_normalize()`、`with_sort_by()` で一行でデータ変換を適用
* 🆕 **カスタムテーマ**：テック風、ビジネス風、フレッシュ風の 3 つの内蔵テーマ + データフォーマット関数
* 🆕 **ショートカットメソッド**：`set_title()`、`set_padding()`、`set_size()` で一般的な設定を簡素化
* 🆕 **高度なチャートラッパー**：Funnel（ファネル）、WaterFall（ウォーターフォール）、Bullet（バレット）チャートをすぐに利用可能

### 📊 チャートギャラリー

![Gallery Preview](docs/assets/gallery_preview.png)

## 🔰 インストール

**pip インストール**
```shell
# インストール
$ pip install pyantv -U
```

**ソースコードからのインストール（uv 推奨）**
```shell
$ git clone https://github.com/sunhailin-Leo/pyantv
$ cd pyantv

# 推奨：uv を使用（CI と同じ構成、lock ファイルを自動管理）
$ make uv-install

# または：pip フォールバック（PEP 517 編集インストール）
$ pip install -e '.[dev,test,all]'
```

> Sprint 62 以降、pyantv は `pyproject.toml` を依存関係の唯一のソースとして使用しています。Sprint 72 以降、バージョン番号は `setuptools-scm` と git tag から自動的に派生されるため、手動でメンテナンスする必要はありません。

## ⛏ コード品質

### 単体テスト

```shell
$ pip install -e '.[test]'
$ make test          # 全単体テスト + カバレッジ
$ make lint          # flake8 コードチェック
$ make check         # lint + test の組み合わせ
```

### 統合テスト

Github Actions 持続的インテグレーション環境を使用。

## 🚀 クイックスタート

### 基本的な折れ線グラフ

```python
from pyantv import Line

line = (
    Line()
    .set_data(data=[
        {"year": "2020", "value": 3},
        {"year": "2021", "value": 4},
        {"year": "2022", "value": 3.5},
        {"year": "2023", "value": 5},
    ])
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(width=640, height=480, is_auto_fit=True)
)
line.render("line_chart.html")
```

### クイックチャート作成（from_data / from_dataframe）

```python
from pyantv import Line

# 一行でチャートを作成
chart = Line.from_data(
    data=[{"year": "2020", "value": 3}, {"year": "2021", "value": 4}],
    x_field_name="year",
    y_field_name="value",
)
chart.render("quick_line.html")
```

```python
import pandas as pd
from pyantv import Line

df = pd.DataFrame({"year": ["2020", "2021", "2022"], "value": [3, 4, 5]})

# x/y エンコーディングフィールドを自動推論
chart = Line.from_dataframe(df)
chart.render("line_from_dataframe.html")
```

### イベントバインディング

```python
from pyantv import Line
from pyantv.globals import ChartEvent

line = (
    Line()
    .set_data(data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}])
    .set_encode(x_field_name="x", y_field_name="y")
    .set_events({
        ChartEvent.ELEMENT_CLICK: "(ev) => { console.log('clicked:', ev.data); }",
    })
)
line.render("event_bindling.html")
```

### プリセットテーマ

```python
from pyantv import Line
from pyantv.presets import with_dark_theme, with_auto_fit, with_smooth_animation

chart = Line.from_data(
    data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}],
    x_field_name="x", y_field_name="y",
)
with_dark_theme(chart)
with_auto_fit(chart)
with_smooth_animation(chart)
chart.render("preset_chart.html")
```

### 高度なチャートラッパー

```python
from pyantv import Funnel, WaterFall, Bullet

# ファネルチャート
funnel = (
    Funnel()
    .set_data(data=[
        {"stage": "閲覧", "value": 100},
        {"stage": "カート", "value": 60},
        {"stage": "注文", "value": 30},
    ])
    .set_encode(x_field_name="stage", y_field_name="value")
)
funnel.render("funnel.html")

# ウォーターフォールチャート
waterfall = (
    WaterFall()
    .set_data(data=[
        {"category": "収入", "value": 120},
        {"category": "支出", "value": -40},
        {"category": "利益", "value": 80},
    ])
    .set_encode(x_field_name="category", y_field_name="value")
)
waterfall.render("waterfall.html")
```

### pandas DataFrame データソース

```python
import pandas as pd
from pyantv import Line

df = pd.DataFrame({
    "year": ["2020", "2021", "2022", "2023"],
    "value": [3, 4, 3.5, 5],
})
line = Line().set_data(data=df).set_encode(x_field_name="year", y_field_name="value")
line.render("line_from_dataframe.html")
```

### 3D 散布図

```python
from pyantv import Point3D, options as opts

point3d = (
    Point3D()
    .set_data(data=[
        {"x": 1, "y": 2, "z": 3},
        {"x": 4, "y": 5, "z": 6},
    ])
    .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
    .set_coordinate(opts.CoordinateCartesian3DOpts())
)
point3d.render("point3d_chart.html")
```

### Web フレームワーク統合

**Flask**

```python
from flask import Flask
from pyantv import Line
from pyantv.web import make_response

app = Flask(__name__)

@app.route("/chart")
def chart_view():
    line = Line().set_data(data=[{"x": 1, "y": 2}]).set_encode(x_field_name="x", y_field_name="y")
    return make_response(line)
```

**Django**

```python
from django.http import HttpResponse
from pyantv import Line
from pyantv.web import render_chart_to_html

def chart_view(request):
    line = Line().set_data(data=[{"x": 1, "y": 2}]).set_encode(x_field_name="x", y_field_name="y")
    return HttpResponse(render_chart_to_html(line))
```

**Sanic**

```python
from sanic import Sanic
from sanic.response import html
from pyantv import Line
from pyantv.web import render_chart_to_html

app = Sanic("ChartApp")

@app.route("/chart")
async def chart_view(request):
    line = Line().set_data(data=[{"x": 1, "y": 2}]).set_encode(x_field_name="x", y_field_name="y")
    return html(render_chart_to_html(line))
```

### プラグインシステム

```python
from pyantv import Interval

# 手描きスタイル
chart = Interval().set_data(data=[...]).use_rough(roughness=2.0)

# レンダラー切替
chart = Interval().set_data(data=[...]).use_renderer("svg")
```

### アノテーションシステム

```python
from pyantv import Line, options as opts

line = (
    Line()
    .set_data(data=[
        {"month": "Jan", "value": 80},
        {"month": "Feb", "value": 120},
        {"month": "Mar", "value": 95},
    ])
    .set_encode(x_field_name="month", y_field_name="value")
    .set_annotations([
        opts.LineAnnotationOpts(y=100, text="目標線"),
        opts.RegionAnnotationOpts(x_start="Feb", x_end="Mar", fill="rgba(255,0,0,0.1)"),
    ])
)
line.render("annotation_chart.html")
```

### Streamlit 統合

```python
import streamlit as st
from pyantv import Line
from pyantv.web import st_pyantv

line = (
    Line()
    .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
    .set_encode(x_field_name="x", y_field_name="y")
)
st_pyantv(line, height=400)
```

### チャートエクスポート

```python
from pyantv import Line

line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")

# PNG 画像としてエクスポート（playwright が必要）
line.save_as_image("chart.png", width=1200, height=800)
```

> Playwright のインストールが必要：`pip install playwright && playwright install chromium`

> その他の例は [examples/](examples/) ディレクトリを参照してください（440+ の完全な例を含む）。

### コード規約

[flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) および [pylint](https://www.pylint.org/) を使用してコード品質を向上。

## 😉 作者

pyantv は主に以下の開発者によって開発・保守されています

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

## 💡 貢献

より多くの開発者が pyantv の開発に参加することを期待しています。私たちは PR をできるだけ早くレビューし、タイムリーに返信することをお約束します。ただし、PR を送る際には以下の点を確認してください：

1. すべての単体テストに合格すること。新機能の場合は、それに応じた新しい単体テストを追加すること
2. 開発規約に従い、black と isort を使用してコードをフォーマットすること（$ pip install -r requirements-dev.txt）
3. 必要に応じて、関連するドキュメントを更新すること

また、開発者が pyantv にさらに多くの例を提供することを大歓迎します。完全なドキュメントは [docs/](docs/) ディレクトリまたはオンラインドキュメントサイト <https://sunhailin-Leo.github.io/pyantv> をご参照ください。初めての貢献は [docs/good-first-issues.md](docs/good-first-issues.md) からお始めください。

## 📃 ライセンス

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)

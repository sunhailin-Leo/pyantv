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

[中国語 README](README.md) | [英語 README](README.en.md) | [日本語 README](README.jp.md)


## 📣 紹介

[AntV](https://github.com/antvis) はアリババグループが提供するデータ可視化ソリューションで、Web データ可視化分野に焦点を当てています。これは、可視化文法ライブラリ AntV Design とレンダリングエンジン G を基にしており、データ表示だけでなく、ナラティブシーン向けのアニメーション編成、豊富なインタラクション能力、カスタマイズ可能なチャートスタイルもサポートしています。シンプルで使いやすい設定により、ユーザーの学習コストを大幅に削減します。一方、Python は表現力豊かな言語であり、データ処理や AI などのシナリオに非常に適しています。データ分析やモデリングがデータ可視化と出会うとき、[pyecharts](https://github.com/pyecharts/pyecharts)、[py-vchart](https://github.com/VisActor/py-vchart) そして [py-antv](https://github.com/sunhailin-Leo/pyantv) が誕生しました。

## ✨ 特徴

* [pyecharts](https://github.com/pyecharts/pyecharts) のような API 設計で、スムーズに使用でき、チェーン呼び出しをサポート
* AntV G2 の大部分のチャートを含み、将来的には AntV G2 の他のチャートや AntV エコシステムの他のチャートにも対応予定
* Jupyter Notebook、JupyterLab などの主流のノートブック環境をサポート
* Flask、Sanic、Django などの主流の Web フレームワークに簡単に統合可能 (近日公開...)
* 高度に柔軟な設定項目で、美しいチャートを簡単に作成可能
* 詳細なドキュメントと例があり、開発者がプロジェクトを迅速に習得できるよう支援

## 🔰 インストール

**pip インストール**
```shell
# インストール
$ pip install pyantv -U
```

**ソースコードからのインストール**
```shell
# ソースコードからのインストール
$ git clone https://github.com/sunhailin-Leo/pyantv
$ cd pyantv
$ pip install -r requirements.txt
$ python setup.py install
```

## ⛏ コード品質

### 単体テスト

```shell
$ pip install -r test/requirements.txt
$ make
```

### 統合テスト

Github Actions 持続的インテグレーション環境を使用。

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

また、開発者が pyantv にさらに多くの例を提供し、共同でドキュメントを改善することを大歓迎します。（ドキュメント準備中...）

## 📃 ライセンス

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)

Title: Breast Cancer データセット解析アプリ
Category: Projects
Slug: project1

### 概要

scikit‑learn に付属する Breast Cancer データセットを用いた簡単なサンプルアプリです。

### アピールポイント

- データエンジニアリングのプロセス
- データ可視化（一部はインタラクティブ）
- Docker の知見（再現性＆簡単デプロイ）

### 起動方法

Docker 環境があれば、ワンライナーで起動できます。

```
docker compose up -d --build
```

起動後、http://localhost:8501 で確認できます。

### 主な使用ライブラリ

- streamlit
- plotly
- seaborn
- pandas
- scikit-learn
- lightgbm
- supertree

### 改善余地

- SHAP などでの可視化
- より大きなデータセットでの分析
- Dockerfile の USER 設定でセキュリティ強化

### ファイル

現在、リポジトリは公開していないため、zip ファイルをダウンロードし、解凍してください。

zip ファイルは[こちら]({static}cancer-streamlit-app.zip)

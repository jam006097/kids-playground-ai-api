---
title: kids-playground-ai-api
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.1"
app_file: app.py
pinned: false
---

# 口コミ要約AI API

## 概要

本プロジェクトは、「親子で遊ぼうナビ」アプリケーションにAIを活用した**口コミの自動要約機能**を提供するAPIです。Hugging Face SpacesとGradioを基盤として構築されており、ユーザーが施設の評判を素早く把握できるよう支援します。

## 主な機能

- **口コミの自動要約:** 施設の口コミテキストを受け取り、AIが分析して中立的な要約文を生成します。
- **パスワード認証:** 環境変数で設定されたパスワードにより、APIへのアクセスを保護します。
- **Gradio UI:** 開発・デバッグ用に、ブラウザから直接操作できるGradioのデモUIを提供します。

## 技術スタック

- **AIフレームワーク:** Hugging Face Transformers
- **APIフレームワーク:** Gradio
- **言語:** Python 3.12
- **開発環境:** Docker, Docker Compose
- **品質管理:** Ruff (Linter/Formatter), Mypy (Type Checker), pre-commit (Git Hooks)

---

## ローカル開発環境のセットアップ

本プロジェクトはDockerを用いて、OSに依存しない開発環境を構築します。

### 前提条件

- [Docker](https://www.docker.com/) および [Docker Compose](https://docs.docker.com/compose/) がインストールされ、起動していること。

### セットアップ手順

1.  **リポジトリのクローン:**
    ```bash
    git clone https://github.com/jam006097/kids-playground-ai-api.git
    cd kids-playground-ai-api
    ```

2.  **環境変数の設定:**
    `.env.example`ファイルをコピーして`.env`ファイルを作成し、後述の「環境変数」セクションを参考に内容を編集します。
    ```bash
    cp .env.example .env
    ```

3.  **Dockerコンテナのビルドと起動:**
    ```bash
    docker-compose up --build -d
    ```
    これにより、必要なライブラリがインストールされ、Gradioアプリケーションがコンテナ内で起動します。

4.  **`pre-commit`フックのインストール:**
    Gitコミット時にコード品質チェックを自動実行するため、`pre-commit`フックをインストールします。
    ```bash
    docker-compose exec api pre-commit install
    ```

---

## 環境変数

本アプリケーションは、`.env`ファイルまたは実行環境の環境変数から以下の設定を読み込みます。

| 変数名              | 説明                                                                                                                            | デフォルト値・例                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `GRADIO_PASSWORD`   | APIとGradioデモUIを保護するためのパスワード。設定しない場合、認証は無効になります。                                               | `your_strong_password_here`                    |
| `AI_MODEL_NAME`     | （オプション）要約に使用するHugging Faceモデルの名前。指定しない場合、コード内で定義されたデフォルトモデルが使用されます。         | `llm-jp/t5-small-japanese-finetuned-sum` |

---

## アプリケーションの実行とアクセス

`docker-compose up`を実行すると、APIサーバーが起動します。

- **GradioデモUI:** `http://localhost:7860`
  - ブラウザでアクセスすると、パスワード認証が求められます。`.env`で設定した`GRADIO_PASSWORD`を入力してください。

### APIの認証と利用

APIはパスワードで保護されています。クライアントからAPIを呼び出す際は、以下の情報が必要です。

- **エンドポイントURL:** `http://localhost:7860` （またはデプロイ先のURL）
- **ユーザー名:** `gemini` （固定）
- **パスワード:** `GRADIO_PASSWORD`で設定した値

クライアント（例: `gradio_client`）では、このユーザー名とパスワードを使って認証を行います。

---

## テストの実行

`pytest`を使用してテストを実行します。以下のコマンドで、コンテナ内のすべてのテストを実行できます。

```bash
docker-compose exec api pytest
```

## デプロイ

このアプリケーションは、Hugging Face Spacesへのデプロイを想定して構成されています。リポジトリをHugging Faceにプッシュすると、自動的にビルドとデプロイが実行されます。

本番環境では、Hugging Faceの**Repository secrets**に`GRADIO_PASSWORD`を設定して、APIを保護してください。

## ライセンス

本プロジェクトは **MIT License** の下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

# kids-playground-ai-api

## 概要

本プロジェクトは、「親子で遊ぼうナビ」アプリケーションにAIを活用した**口コミの自動要約機能**を提供するAI APIです。Hugging Face SpacesとGradioを基盤として構築されており、ユーザーが施設の評判を素早く把握できるよう支援します。

## 機能概要

*   **口コミの自動要約:** 施設の口コミをAIが分析し、「ポジティブな点」と「注意が必要な点」などをまとめた中立的な要約文を生成します。
*   **API提供:** Djangoアプリケーションから利用可能なAPIエンドポイントとして機能します。
*   **Gradio UI:** 開発・デバッグ用に、ブラウザから直接操作できるGradioのデモUIを提供します。

## 技術スタック

*   **AIフレームワーク:** Hugging Face Transformers
*   **APIフレームワーク:** Gradio
*   **言語:** Python 3.12
*   **開発環境:** Docker, Docker Compose
*   **品質管理:** Ruff (Linter/Formatter), Mypy (Type Checker), pre-commit (Git Hooks)

## 開発環境のセットアップ

本プロジェクトはDockerベースで構築されており、以下の手順で開発環境をセットアップできます。

### 前提条件

*   Docker Desktopがインストールされ、起動していること。

### 手順

1.  **リポジトリのクローン:**
    ```bash
    git clone https://github.com/jam006097/kids-playground-ai-api.git
    cd kids-playground-ai-api
    ```

2.  **環境変数の設定:**
    `.env.example`を参考に、`.env`ファイルを作成し、必要な環境変数を設定します。
    ```bash
    cp .env.example .env
    # 必要に応じて .env ファイルを編集
    ```

3.  **Docker環境の構築と起動:**
    ```bash
    docker-compose up --build -d
    ```
    これにより、必要な依存関係がインストールされ、Gradioアプリケーションがコンテナ内で起動します。

4.  **`pre-commit`フックのインストール:**
    Gitコミット時にコード品質チェックが自動で実行されるように、`pre-commit`フックをインストールします。
    ```bash
    docker-compose exec api bash
    pre-commit install
    exit
    ```

## アプリケーションへのアクセス

開発環境が起動したら、ブラウザから以下のURLでGradioのデモUIにアクセスできます。

*   **Gradio UI:** `http://localhost:7860`

## テストの実行

*(このセクションは、テストが実装された後に追記します。)*

## 貢献

貢献を歓迎します！コントリビューションガイドラインについては、別途ドキュメントを参照してください。

## ライセンス

*(このセクションは、ライセンスが決定された後に追記します。)*

## 連絡先

ご質問やご提案がありましたら、GitHub Issuesをご利用ください。

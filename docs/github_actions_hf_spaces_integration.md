## Genemicliと実践！GitHub ActionsでHugging Face SpacesへAIアプリを自動デプロイするガイド

AIモデルを使ったアプリケーション開発は、時に予期せぬ課題に直面します。しかし、`genemicli`のような強力なCLIアシスタントと連携することで、それらの課題を乗り越え、スムーズにプロジェクトを進めることができます。この記事では、私たちが`genemicli`と共に、GitHub ActionsとHugging Face Spacesを連携させ、AIアプリケーションを自動でデプロイするまでの道のりを、具体的な実装手順と問題解決のプロセスを交えながら解説します。

---

### 1. Hugging Face Spacesの準備

まず、Hugging Face Spacesで新しいSpaceを作成します。

*   Hugging Faceにログインし、「Spaces」タブから「Create new Space」を選択。
*   「Space name」を決め、「Gradio」SDKを選択します。
*   「Create Space」をクリック。

### 2. GitHubリポジトリの準備

あなたのAIアプリケーションのコードがGitHubリポジトリにあることを確認してください。

### 3. Hugging Faceアクセストークンの取得

GitHub ActionsからHugging Face Spacesにアクセスするために、アクセストークンが必要です。

*   Hugging Faceにログインし、右上のプロフィールアイコン → 「Settings」 → 「Access Tokens」へ。
*   「New token」をクリックし、`write`権限を持つトークンを作成し、コピーします。

### 4. GitHub Secretsへのトークン登録

コピーしたアクセストークンをGitHubリポジトリのSecretsに登録します。これは、セキュリティのためにコードに直接トークンを書き込まないための重要な手順です。

*   GitHubリポジトリの「Settings」→「Secrets and variables」→「Actions」へ。
*   「New repository secret」をクリックし、**Name**を `HF_TOKEN`、**Secret**にコピーしたトークンを貼り付けて登録します。
    *   **`genemicli`との連携:** `genemicli`は、この`HF_TOKEN`の登録方法を丁寧に案内してくれました。

### 5. GitHub Actionsワークフローの作成

GitHubリポジトリのルートに `.github/workflows/sync-to-space.yml` というファイルを作成し、以下の内容を記述します。このワークフローは、GitHubの`main`ブランチへのプッシュをトリガーにして、Spaceのコンテンツを自動で更新します。

```yaml
name: Sync to Hugging Face hub
on:
  push:
    branches: [main] # mainブランチへのプッシュをトリガー
  workflow_dispatch: # 手動実行も可能にする

jobs:
  sync-to-hub:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          lfs: true # LFSファイルがある場合
      - name: Push to hub
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }} # GitHub Secretsからトークンを取得
        run: |
          # Spaceのリモートを追加（YOUR_HF_USERNAMEとYOUR_SPACE_NAMEを置き換える）
          git remote add space https://YOUR_HF_USERNAME:${{ secrets.HF_TOKEN }}@huggingface.co/spaces/YOUR_HF_USERNAME/YOUR_SPACE_NAME
          # mainブランチをSpaceに強制プッシュ
          git push --force space main
```

**注意点:**

*   `YOUR_HF_USERNAME` と `YOUR_SPACE_NAME` は、あなたのHugging Faceのユーザー名とSpace名に置き換えてください。
*   `fetch-depth: 0` と `lfs: true` は、大きなモデルファイルなどを扱う場合に重要です。
    *   **`genemicli`との連携:** `genemicli`は、このワークフローの作成をサポートし、`YOUR_HF_USERNAME`と`YOUR_SPACE_NAME`を実際の値に置き換えるよう指示してくれました。

### 6. `README.md` の設定

Hugging Face Spacesは、`README.md`の先頭にあるメタデータブロックを読み込んでSpaceの設定を行います。あなたの`README.md`の先頭に以下の内容を追加してください。

```yaml
---
title: あなたのアプリのタイトル
emoji: ✨
colorFrom: "#FFD700" # 好みの色に
colorTo: "#FFA500"   # 好みの色に
sdk: gradio
sdk_version: "4.x.x" # requirements.txtのGradioバージョンに合わせる
app_file: app.py     # アプリケーションのエントリーポイントファイル
pinned: false
---
```

**注意点:**

*   `title`、`emoji`、`colorFrom`、`colorTo` は自由に設定してください。
*   `sdk_version` は `requirements.txt` に記載されているGradioのバージョンに合わせてください。
*   `app_file` は、あなたのGradioアプリケーションのメインファイル（例: `app.py` や `src/main.py` など）のパスを記述します。
    *   **`genemicli`との連携:** `genemicli`は、Spaceが画面表示されない問題に直面した際、この`README.md`のメタデータ設定が不足していることを特定し、必要な項目（`title`、`sdk`、`app_file`など）の追加を提案・適用してくれました。

### 7. アプリケーションのエントリーポイントの調整 (`app.py`の作成)

Hugging Face Spacesで`ModuleNotFoundError`が発生した場合、アプリケーションのエントリーポイントを調整する必要があります。これは、Pythonのモジュールパスの問題を解決するためです。

GitHubリポジトリのルートに `app.py` というファイルを作成し、以下の内容を記述します。

```python
import sys
sys.path.append('./src') # srcディレクトリをPythonのパスに追加
from ai_api.main import iface # src/ai_api/main.pyからifaceオブジェクトをインポート

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0") # Gradioアプリケーションを起動
```

*   **`genemicli`との連携:** `genemicli`は、Space上で`ModuleNotFoundError: No module named 'ai_api'`というエラーが発生した際、この`app.py`ラッパーファイルの作成を提案・実装してくれました。これにより、`src`ディレクトリ内のモジュールが正しく認識され、アプリケーションが起動できるようになりました。

### 8. デプロイの確認

これらの設定が完了したら、GitHubリポジリにコードをプッシュしてください。GitHub Actionsが自動的に実行され、Hugging Face Spaceにコードが同期されます。

Hugging Face Spaceのページにアクセスし、アプリケーションが正常に表示されるか確認しましょう。もし問題があれば、Spaceページの「Logs」タブでエラーメッセージを確認してください。

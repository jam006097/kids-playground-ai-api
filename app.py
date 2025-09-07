import os
import sys

from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# srcディレクトリをシステムパスに追加
# これにより、`python app.py` をプロジェクトルートから実行した際に、
# `ai_api` パッケージを正しく見つけられるようになります。
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from ai_api.main import iface  # noqa: E402

# 環境変数から認証情報を取得
auth_user = os.getenv("GRADIO_USERNAME", "gemini")
auth_password = os.getenv("GRADIO_PASSWORD")

# 認証情報が両方設定されている場合のみ、認証を有効にする
auth_credentials = None
if auth_user and auth_password:
    auth_credentials = (auth_user, auth_password)

# サーバーを起動
if __name__ == "__main__":
    # サーバーを起動
    iface.launch(server_name="0.0.0.0", auth=auth_credentials)

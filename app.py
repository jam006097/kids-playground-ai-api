import os
import sys

from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

sys.path.append("./src")
from ai_api.main import iface  # noqa: E402

# 環境変数から認証情報を取得
# gradioのauthの仕様上、ユーザ名は必須だが、今回はパスワードのみ使用する
# そのため、ユーザ名は固定
auth_user = "gemini"
auth_password = os.getenv("GRADIO_PASSWORD")

# 認証情報が両方設定されている場合のみ、認証を有効にする
auth_credentials = None
if auth_user and auth_password:
    auth_credentials = (auth_user, auth_password)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", auth=auth_credentials)

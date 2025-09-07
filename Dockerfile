# Python 3.12の軽量イメージをベースにする
FROM python:3.12-slim

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを作成・設定
WORKDIR /app

# 依存関係ファイルをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . .

# Gradioが使用するポートを公開
EXPOSE 7860

# コンテナ起動時にアプリケーションを実行
CMD ["python", "app.py"]

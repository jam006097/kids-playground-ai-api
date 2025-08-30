FROM python:3.12-slim-bookworm

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# PYTHONPATHにsrcディレクトリを追加し、モジュールを正しく見つけられるようにする
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

EXPOSE 7860

# アプリケーションをモジュールとして実行する
CMD ["python", "-m", "ai_api.main"]

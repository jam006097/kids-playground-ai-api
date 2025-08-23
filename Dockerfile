FROM python:3.12-slim-bookworm

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["python", "src/ai_api/main.py"]
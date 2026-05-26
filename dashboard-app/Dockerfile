FROM python:3.11-slim

WORKDIR /app

COPY dashboard-app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY dashboard-app/ .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]

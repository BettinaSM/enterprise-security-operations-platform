FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r dashboard-app/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "dashboard-app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

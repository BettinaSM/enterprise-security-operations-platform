FROM python:3.11-slim

WORKDIR /app

# ---------------------------
# SYSTEM DEPENDENCIES
# ---------------------------

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------
# COPY REQUIREMENTS FIRST
# ---------------------------

COPY dashboard-app/requirements.txt .

# ---------------------------
# INSTALL PYTHON DEPENDENCIES
# ---------------------------

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# ---------------------------
# COPY APPLICATION
# ---------------------------

COPY dashboard-app/ .

# ---------------------------
# CREATE REQUIRED DIRECTORIES
# ---------------------------

RUN mkdir -p \
    /app/database \
    /app/reports \
    /app/logs \
    /app/tmp \
    /app/inventory

# ---------------------------
# EXPOSE PORTS
# ---------------------------

EXPOSE 8501
EXPOSE 8000

# ---------------------------
# START STREAMLIT
# ---------------------------

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (optional, can be added if required)
# RUN apt-get update && apt-get install -y ...

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

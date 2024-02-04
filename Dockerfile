# Dockerfile
FROM python:3.8

WORKDIR /app

COPY src/ /app

RUN pip install pandas

CMD ["python", "main.py"]

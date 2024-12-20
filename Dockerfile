FROM python:3.11-alpine
WORKDIR /app
COPY app/ ./app
EXPOSE 8080
CMD ["python", "app/main.py"]

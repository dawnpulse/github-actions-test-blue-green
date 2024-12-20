FROM python:3.10-alpine
WORKDIR /app
COPY main.py test_main.py ./
RUN python test_main.py
CMD ["python", "main.py"]
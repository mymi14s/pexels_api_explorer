FROM python:3.10-slim

WORKDIR /app
COPY ./src /app
COPY ./requirements.txt /app
COPY ./README.md ../README.md

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

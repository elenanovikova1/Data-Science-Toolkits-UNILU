FROM python:3.9-slim
FROM tensorflow/tensorflow:2.14.0

WORKDIR /app

RUN python -m venv venv

ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY flask/ /app/

EXPOSE 5000

ENV NAME World

CMD ["python", "app.py"]
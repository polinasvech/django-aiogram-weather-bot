FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY bot-requirements.txt ./bot-requirements.txt
RUN pip install --upgrade pip  && \
    pip install --no-cache-dir -r bot-requirements.txt
COPY ./src .
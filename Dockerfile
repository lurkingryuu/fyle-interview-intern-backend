FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/

COPY . /app

ARG FLASK_APP=core/server.py

RUN flask db upgrade -d core/migrations/

EXPOSE $GUNICORN_PORT

CMD ["gunicorn", "-c", "./gunicorn_config.py", "core.server:app"]

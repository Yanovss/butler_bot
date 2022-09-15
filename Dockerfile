FROM python:alpine AS build-env
ADD . /app
WORKDIR ./app
RUN apk --no-cache add gcc musl-dev g++
RUN python -m venv venv
COPY requirements.txt .
RUN source /app/venv/bin/activate; pip install -r requirements.txt
FROM python:alpine
RUN addgroup -g 1000 butler && adduser -u 1000 -G butler -h /home/butler -s /bin/sh -D butler
RUN mkdir /app /database && chown -R butler:butler /app
WORKDIR /app
COPY --from=build-env /app/venv /app/venv
COPY . .
USER butler
ENV TZ=Europe/Belgrade \
FLASK_APP=app.py \
FLASK_DEBUG=False \
BOT_TOKEN='' \
URL=http://192.168.100.200/telegram/send \
DATABASE_URL=sqlite:////database/bot_data.db \
LD_LIBRARY_PATH=/app/venv/lib/ \
PYTHONPATH=/app/venv/lib/python3.10:/app/venv/lib/python3.10/site-packages:/usr/local/lib/python3.10:/usr/local/lib/python3.10/lib-dynload \
PYTHONHOME=/app/venv/lib/python3.10
ENTRYPOINT ["/usr/bin/python", " app.py"]


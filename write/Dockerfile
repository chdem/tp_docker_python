FROM python:3.12-alpine

WORKDIR /app

COPY write ./write
COPY common ./write/common

WORKDIR /app/write

CMD ["tail", "-f", "/dev/null"]
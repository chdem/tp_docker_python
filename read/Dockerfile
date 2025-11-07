FROM python:3.12-alpine

WORKDIR /app

COPY read ./read
COPY common ./read/common

WORKDIR /app/read

CMD ["tail", "-f", "/dev/null"]
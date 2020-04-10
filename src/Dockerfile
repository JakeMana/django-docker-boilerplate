FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk update && apk add --no-cache postgresql zlib jpeg git
RUN apk add --no-cache --virtual build-deps gcc python3-dev musl-dev postgresql-dev zlib-dev jpeg-dev libxml2-dev libxslt-dev libffi-dev openssl-dev libgcc git

RUN pip install --upgrade pip
RUN pip install setuptools wheel

RUN apk add --update npm

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
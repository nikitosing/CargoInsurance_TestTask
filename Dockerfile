FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV MODULE_NAME="server"

COPY ./requirements.txt /

COPY ./app /app

RUN pip install -r /requirements.txt
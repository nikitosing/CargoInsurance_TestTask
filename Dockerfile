FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# set path to our python api file
ENV MODULE_NAME="server"

# copy contents of project into docker
COPY ./requirements.txt /

COPY ./app /app


# install poetry
RUN pip install -r /requirements.txt

# disable virtualenv for peotry
#RUN poetry config virtualenvs.create false

# install dependencies
#RUN poetry install
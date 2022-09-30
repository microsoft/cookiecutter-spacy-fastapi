FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
ENV PORT 8080
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN spacy download {{cookiecutter.spacy_model}}

COPY ./app /app/app

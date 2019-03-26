FROM python:3.6
ENV PORT 8080
EXPOSE ${PORT}
WORKDIR /usr/src

COPY ./requirements/spacy.txt ./requirements/spacy.txt
RUN pip install -r requirements/spacy.txt

COPY ./requirements/base.txt ./requirements/base.txt
RUN pip install -r requirements/base.txt
COPY ./app ./app

COPY start.sh .

CMD ["bash", "start.sh"]

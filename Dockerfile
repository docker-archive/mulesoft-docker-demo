FROM python:3.6-alpine
WORKDIR /home/api

COPY ./app.py /home/api/
COPY ./requirements.txt /home/api/

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


FROM python:3.6-alpine
WORKDIR /home/api
COPY ./requirements.txt /home/api/
RUN pip install -r requirements.txt

COPY ./app.py /home/api/
COPY ./static/* /home/api/static/


ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


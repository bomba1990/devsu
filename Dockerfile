FROM python:3.6.2-alpine3.6
WORKDIR /code
ADD . /code

RUN pip install -r requirements.txt

EXPOSE 9001

CMD ["python", "app.py"]


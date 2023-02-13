FROM python:3.8-buster

WORKDIR /app

COPY . /app

# RUN pip3 install -r requirements.txt

RUN pip3 install --upgrade pip


RUN pip3 install kafka-python

WORKDIR /app/src/

CMD ["python3.8", "fake_crawler/fake_crawler.py"]


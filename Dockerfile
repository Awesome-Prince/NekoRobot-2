FROM python:3.8.5-slim-buster

WORKDIR /root/NekoRobot

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U -r requirements.txt

CMD ["python3","-m","NekoRobot"]

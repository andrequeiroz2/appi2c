FROM ubuntu:20.04

LABEL MAINTAINER andrequeiroz.com@gmail.com

COPY appi2c /app

RUN apt-get update && apt-get install python3 python3-pip -y 

RUN pip3 install -r /app/requirements.txt

ENV FLASK_APP=app.py

WORKDIR /app/appi2c

RUN cd /app/appi2c && flask populate-type && flask populate-icon

EXPOSE 5000

CMD ["flask","run","--host","0.0.0.0"]
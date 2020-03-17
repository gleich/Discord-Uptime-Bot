FROM python:3.7.7-alpine3.11

# Installing requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY ./uptime-bot .
RUN rm -rf ./uptime-bot/secrets



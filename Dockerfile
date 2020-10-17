FROM python:3.8-buster

RUN apt-get update && apt install build-essential -y --no-install-recommends

COPY requirements.txt /app/requirements.txt
RUN  pip install -r /app/requirements.txt

# Now copy in our code, and run it
COPY . /app

WORKDIR /app
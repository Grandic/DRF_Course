FROM python:3

WORKDIR /DRF

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

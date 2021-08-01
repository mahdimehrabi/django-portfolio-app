# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN apk update \
    && apk add zlib-dev jpeg-dev gcc python3-dev musl-dev 
RUN apk add sqlite

# create sqlite file
RUN touch /usr/src/app/db.sqlite3	

# install dependencies
RUN python3 -m pip install --upgrade pip
COPY ./requirements/_base.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

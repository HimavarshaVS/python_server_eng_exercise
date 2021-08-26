FROM python:3.8.10-buster
LABEL maintainer="Himavarsha"

# Creating folders, and files for a project:
COPY ./ /app
WORKDIR /app

RUN pip install -r requirements.txt


FROM python:3.8-alpine
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./lunch.py" ]

FROM python:3.10-alpine

COPY . /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

EXPOSE 8000:8000
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev && python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "uvicorn", "app.app:app", "--host", "0.0.0.0", "--reload" ]
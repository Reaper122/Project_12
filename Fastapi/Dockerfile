FROM python:3.10

WORKDIR /usr/app

COPY . /usr/app/

RUN pip install fastapi uvicorn

RUN pip install -r /usr/app/requirements.txt

EXPOSE 13001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "13001","--reload"]
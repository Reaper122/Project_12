FROM python:3.10

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /usr/app/

EXPOSE 8501

CMD streamlit run show2.py --server.port 8501
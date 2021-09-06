FROM python:3

ADD requirements.txt main.py Football_Transfers_Class.py Create_table.py insert_data.py top250-00-19.csv ./

RUN  set -xe\
&& apt-get update -y && apt-get install -y  python3-pip  && python3 -m pip  install  --upgrade pip && python3 -m  pip install -r requirements.txt

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0


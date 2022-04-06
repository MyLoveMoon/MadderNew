FROM python:3.9.1-buster

WORKDIR /root/uyebot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3.8","main.py"]

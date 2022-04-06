FROM python:3.9.1-buster


RUN pip install -r requirements.txt

CMD ["python3","main.py"]

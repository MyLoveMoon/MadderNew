FROM python:3.9.1-buster
RUN pip freeze > requirements.txt

CMD ["python3","main.py"]

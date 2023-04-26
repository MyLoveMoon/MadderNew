FROM python:3.9.1-buster
RUN pip freeze > requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
CMD ["python3","main.py"]

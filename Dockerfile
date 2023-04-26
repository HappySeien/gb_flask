FROM python:3.11.0-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache -r requirements.txt

COPY wsgi.py wsgi.py
COPY services ./services

EXPOSE 5000

CMD ["python3", "wsgi.py"]

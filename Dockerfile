FROM python:3.7-alpine

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD app.py /app/app.py

EXPOSE 5000 

CMD ["python3", "app.py"]

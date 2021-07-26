FROM python:3.8
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=5000
RUN apt-get update && \
    apt-get install -y python3-pip
RUN pip install flask
COPY app.py /opt/
EXPOSE 5000
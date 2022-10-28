FROM python:3.7
COPY . /main_app
WORKDIR /main_app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT main_app:app
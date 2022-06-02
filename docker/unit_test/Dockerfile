FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "manage.py", "test", "autocompany.api"]

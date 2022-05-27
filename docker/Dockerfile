FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

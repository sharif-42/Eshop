FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

# copy entrypoint.sh
COPY ./compose/local/django/entrypoint.sh /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY . /app/

# run entrypoint.sh
ENTRYPOINT ["/entrypoint"]

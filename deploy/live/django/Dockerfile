FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential libpq-dev git espeak ffmpeg \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*



# Requirements are installed here to ensure they will be cached.

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --force-reinstall git+https://github.com/benoitc/gunicorn.git@master
ADD ./src /app



ADD ./deploy/live/django/entrypoint.sh /app/entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE 'main.settings'

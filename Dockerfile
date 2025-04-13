FROM python:3.12-slim-bookworm

ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} wagtail && \
    useradd -u ${UID} -g wagtail -m wagtail

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000


RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \  
    gcc \       
    python3-dev \ 
 && rm -rf /var/lib/apt/lists/*

RUN pip install "gunicorn==20.0.4"

COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /app

COPY --chown=wagtail:wagtail . .

USER wagtail

RUN python manage.py collectstatic --noinput --clear

CMD set -xe; python manage.py migrate --noinput; gunicorn core.wsgi:application
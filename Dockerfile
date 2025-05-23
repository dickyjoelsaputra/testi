FROM python:3.12-slim-bookworm

ARG UID=1001
ARG GID=1001

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

RUN chown -R wagtail:wagtail /app && \
    find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \;

COPY --chown=wagtail:wagtail . .

USER wagtail

# Try collectstatic during build but continue if it fails
RUN python manage.py collectstatic --noinput || echo "Collectstatic failed, will retry during runtime"

CMD set -xe; \
    python manage.py migrate --noinput; \
    python manage.py collectstatic --noinput; \
    gunicorn core.wsgi:application

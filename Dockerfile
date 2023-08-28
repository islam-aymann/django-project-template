FROM python:3.10-slim as base

WORKDIR /tmp

# Export requirements
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG DEBIAN_FRONTEND=noninteractive

EXPOSE 8000

# General installs
RUN apt-get update && apt-get --no-install-recommends install -y git curl gettext


# Purge build dependencies
RUN rm -rf /var/lib/apt/lists/* && apt-get clean

# Add user
RUN addgroup --system django && adduser --system --ingroup django --home /app django
USER django

WORKDIR /app
ENV PATH=${PATH}:/app/.local/bin

# install requirements
COPY --from=base /tmp/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install --no-cache -r requirements.txt

COPY --chown=django:django ./pre_deploy.sh /pre_deploy.sh
COPY --chown=django:django . /app

RUN chmod +x /pre_deploy.sh

CMD ["gunicorn", "project_name.wsgi", "--bind", "0.0.0.0:8000", "--log-level", "debug", "--timeout", "30", "--worker-connections", "1000", "--access-logfile", "-", "--chdir", "/app"]


###############################################
# Base Image
###############################################
FROM python:3.11.3-buster as base

ENV APP_HOME="/app" \
#    PYTHONFAULTHANDLER=1 \
#    PYTHONUNBUFFERED=1 \
#    PYTHONPATH="/app/app" \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.4.2 \
    POETRY_HOME="/etc/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM base as builder

RUN apt update \
    && apt install --no-install-recommends -y curl \
    && apt clean

# RUN openssl version

# install poetry: respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sS https://install.python-poetry.org | python3 -

WORKDIR $APP_HOME

# install deps: no dev deps
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-dev --no-interaction

###############################################
# Development Image
###############################################
FROM base as dev

WORKDIR $APP_HOME

# copy poetry + venv
COPY --from=builder $POETRY_HOME $POETRY_HOME

# ENV PATH=$APP_HOME/.venv/bin:$PATH

# install deps: quicker as runtime deps are already installed
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-interaction

###############################################
# Production Image
###############################################
FROM base as prod

WORKDIR $APP_HOME

ENV PATH=$APP_HOME/.venv/bin:$PATH

# copy src
COPY app ./app
COPY db ./db
COPY scripts ./scripts
COPY logging.conf ./
# make log dir
RUN mkdir /app/log

RUN chmod +x -R scripts
ENTRYPOINT ["scripts/run.sh"]

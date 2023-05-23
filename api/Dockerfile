###############################################
# Base Image
###############################################
FROM python:3.11.3-buster as base

ENV APP_HOME="/app" \
#    PYTHONFAULTHANDLER=1 \
#    PYTHONUNBUFFERED=1 \
#    PYTHONPATH="/app/gpt_othello" \
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

###############################################
# Development Image
###############################################
FROM base as dev

WORKDIR $APP_HOME

# copy poetry
COPY --from=builder $POETRY_HOME $POETRY_HOME
# add .venv to path
ENV PATH=$APP_HOME/.venv/bin:$PATH

# install deps: quicker as runtime deps are already installed
COPY pyproject.toml poetry.lock ./
COPY gpt_othello ./gpt_othello
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

###############################################
# Production Image
###############################################
FROM base as prod

WORKDIR $APP_HOME

# copy src
COPY app ./app
COPY db ./db
COPY scripts ./scripts
COPY logging.conf ./
# make log dir
RUN mkdir /app/log

RUN chmod +x -R scripts
ENTRYPOINT ["scripts/run.sh"]

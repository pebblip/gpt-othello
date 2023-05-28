###############################################
# 開発環境
###############################################
FROM python:3.10.3-buster as dev

ENV APP_HOME="/app" \
    POETRY_VERSION=1.4.2 \
    POETRY_HOME="/etc/poetry" 

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt update \
    && apt install --no-install-recommends -y curl \
    && apt clean

RUN curl -sS https://install.python-poetry.org | python3 -

WORKDIR $APP_HOME

COPY pyproject.toml poetry.lock ./
COPY gpt_othello ./gpt_othello
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

###############################################
# 本番環境
###############################################
FROM public.ecr.aws/lambda/python:3.10 as prod

ENV APP_HOME="/app" \
    POETRY_VERSION=1.4.2 \
    POETRY_HOME="/etc/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sS https://install.python-poetry.org | python3 -

WORKDIR $APP_HOME

COPY pyproject.toml poetry.lock ./
COPY gpt_othello ./gpt_othello
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-dev

CMD ["gpt_othello.main.lambda_handler"]

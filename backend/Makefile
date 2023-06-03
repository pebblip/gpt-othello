.PHONY: help up down build rebuild attach format lint

define HELP
Usage:
  make [COMMAND]

Commands:
  up:			Docker起動
  down:			Docker停止
  build:		Dockerコンテナのビルド
  rebuild:		Dockerコンテナの再ビルド
  attach:		Dockerコンテナにアタッチ
  format:		コードのフォーマット
  lint:			コードの静的解析

endef
export HELP

help:
	@echo "$$HELP"

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

rebuild:
	docker-compose build --no-cache

attach:
	docker-compose exec api bash

format:
	docker-compose exec api poetry run isort gpt_othello
	docker-compose exec api poetry run black gpt_othello

lint:
	docker-compose exec api poetry run isort gpt_othello --profile=black --check
	docker-compose exec api poetry run black gpt_othello --check
	docker-compose exec api poetry run mypy gpt_othello
	docker-compose exec api poetry run flake8 gpt_othello --exclude lib

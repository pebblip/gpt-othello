:black_circle: GPT-OTHELLO バックエンドAPI :white_circle:
-------------------

GPTオセロのバックエンドAPIです。

## ローカル環境での実行方法

1. .env.defaultをコピーして.envファイルを作成する。

* 必要があれば、`API_PORT`を変更する。
* ChatGPTを利用する場合は、各自で取得したOpenAIのAPIキーを`OPEN_API_KEY`に設定する。

2. Dockerを立ち上げる

```
docker compose up -d
```

3. APIの起動を確認する。

以下のURLにアクセスしてAPI一覧が表示されればOK。

```
http://localhost:8000/api/docs
```

ここで、ポート番号8000は、.envファイルの`API_PORT`で設定した値。



:black_circle: GPT-OTHELLO フロントエンド :white_circle:
-------------------

GPTオセロのフロント（画面）です。

## ローカル環境での実行方法

1. .env.defaultをコピーして.env.localファイルを作成する。

必要があれば、`VITE_BASE_API_URL`の値（ http://localhost:8000/dev/api ）を変更する。
ポート番号8000はバックエンド側の.envファイルの`API_PORT`と合わせる。

2. 必要なパッケージインストールする。

```
yarn
```

3. 起動する。

```
yarn dev
```

以下のようなログが出力されればOK。
```
  VITE v4.3.8  ready in 340 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help

```

4. ゲームを開始する。

上記で表示されたURL（ http://localhost:3000/ ）にブラウザでアクセスする。


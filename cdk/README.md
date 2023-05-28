:black_circle: GPT-OTHELLO :white_circle:
----------------------------------------

# デプロイ手順

1. フロントエンドをビルドする。

```
cd frontend
yarn build
```

2. AWSにインフラ（Stack）を展開する。

```
cdk deploy --profile YOUR_PROFILE --all
```


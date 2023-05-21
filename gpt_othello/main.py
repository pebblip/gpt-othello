from typing import Optional

import openai
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Python"}


@app.get("/ping")
def ping():
    return {"echo": "pong"}


def foo():
    return {"foo": "bar"}


@app.get("/translate")
def read_item(q: Optional[str] = None):
    foo()

    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは日本語を英語に翻訳するアシスタントです。"},
            {"role": "user", "content": q},
        ],
    )

    return {"response": response.choices[0]["message"]["content"]}

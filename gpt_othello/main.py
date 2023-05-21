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


@app.get("/init")
def read_item(q: Optional[str] = None):
    openai.api_key = "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"

    # Completion APIを呼び出す
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="オセロの初期盤面を64個の数値配列として表現する。初期盤面は黒石と白石が4つだけ配置されている。0:空きマス、1:黒石、2:白石を表す。",
        max_tokens=200,
        temperature=0,
    )

    # APIのレスポンスから64個の数値配列を取得
    output = response.choices[0].text.strip().replace("\n", "")

    return {"response": output}


@app.get("/next")
def read_item(q: Optional[str] = None):
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """
             あなたはオセロの達人です。オセロの盤面を解析して、あなたにとって最適な手を選びます。あなたは常に後手です。
             オセロの盤面は左上のマスを0番目として、右下のマスを63番目とする数値の配列で表現します。
             オセロの盤面では、数値の1を黒石、数値の2を白石、数値の0を空白のマスを表します。
             ここで、オセロの左上とは、先手番から見て、左上のマスのことです。
             """,
            },
            {
                "role": "user",
                "content": "オセロの盤面が[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]です。あなたの次の手は？",
            },
        ],
    )

    print(response.choices[0]["message"]["content"])
    print(response)

    return {"response": response.choices[0]["message"]["content"]}

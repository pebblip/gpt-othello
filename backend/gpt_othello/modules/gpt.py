import json
import os

import openai

from .othello import Board

openai.api_key = os.getenv("OPENAI_API_KEY")


class GPT:
    def ask(self, board: Board, valids: list[tuple[int, int]]):
        string_board = "\n".join([" ".join(map(str, row)) for row in board])
        string_valids = ", ".join(map(str, valids))

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "あなたはオセロゲームの次の最善手を助言するオセロの達人です。",
                },
                {
                    "role": "user",
                    "content": f"""
                オセロの現在の盤面は以下の通りです。
                {string_board}
                ここで、黒石がおける全ての位置座標は以下の通りです。
                {string_valids}です。
                この中から、あなたが次に打つべき位置座標をJSON形式で返してください。
                JSONは以下のキーのみを含みます。
                position: 次に打つべき位置座標
                description: それが最善手である論理的で分かりやすい説明

                回答はJSON文字列だけでよいです。
                """,
                },
            ],
        )

        response = response["choices"][0]["message"]["content"]

        return json.loads(response)

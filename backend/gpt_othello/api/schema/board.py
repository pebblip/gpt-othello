from gpt_othello.modules.othello import GameStatus
from pydantic import BaseModel, Field


class Board(BaseModel):
    size: int = Field(..., title="盤面サイズ", description="盤面のサイズ", example="8")
    rows: list[list[int]] = Field(
        ..., title="盤面", description="2次元配列で表現したオセロ盤面。1:黒,-1:白", example="[[0, 0],[0, 1], [-1, 0], [0, 0]]"
    )
    valids: list[tuple[int, int]] = Field(
        ...,
        title="次に置き石可能な位置のリスト",
        description="左上を(0,0)都する座標のリスト",
        example="[(0, 0), (0, 1), (0, 2)]",
    )
    status: GameStatus = Field(..., title="盤面状態", description="0:続行中, 1:黒の勝ち,2:白の勝ち,3:引き分け", example="0")
    score: list[int, int] = Field(..., title="スコア", description="黒と白の石の数", example="[2, 2]")

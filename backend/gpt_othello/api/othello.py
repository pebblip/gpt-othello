from dataclasses import dataclass

from fastapi import APIRouter
from fastapi.param_functions import Body, Depends, Query

from gpt_othello.modules.othello import Board as BoardModel
from gpt_othello.modules.othello import Othello, Stone

from .schema import BoardResponse

router = APIRouter()

BOARD_SIZE = 8

BoardParameter = list[list[int]]


@dataclass
class InitParams:
    pass


@dataclass
class UserPlaceParams:
    x: int = Query(..., title="X座標", description="石を置くX座標", ge=0)
    y: int = Query(..., title="Y座標", description="石を置くY座標", ge=0)
    board: BoardParameter = Body(
        ...,
        title="盤面",
        description="2次元配列で表現した現在のオセロ盤面。1:黒,-1:白",
        example="""
        [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,-1,1,0,0,0],
         [0,0,0,1,-1,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
       """,
    )


@dataclass
class UserPassParams:
    board: BoardParameter = Body(
        ...,
        title="盤面",
        description="2次元配列で表現した現在のオセロ盤面。-1:黒,1:白",
        example="""
        [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,-1,1,0,0,0],
         [0,0,0,1,-1,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
       """,
    )


@dataclass
class AIPlaceParams:
    board: BoardParameter = Body(
        ...,
        title="盤面",
        description="2次元配列で表現した現在のオセロ盤面。-1:黒,1:白",
        example="""
        [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,-1,1,0,0,0],
         [0,0,0,1,-1,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
       """,
    )


def toRows(board: BoardModel):
    return [[int(stone) for stone in row] for row in board]


@router.get(
    "/start",
    response_model=BoardResponse,
    summary="ゲームの開始",
    description="このエンドポイントはオセロゲームを開始します。ゲーム状態が初期化され、初期盤面がレスポンスとして返されます。",
)
def start(
    q: InitParams = Depends(),
):
    othello = Othello(BOARD_SIZE)

    return BoardResponse(
        size=BOARD_SIZE,
        rows=toRows(othello.get_board()),
        valids=othello.get_valid_moves(Stone.BLACK),
        status=othello.is_game_ended(),
        score=othello.get_score(),
    )


@router.post(
    "/user/place",
    response_model=BoardResponse,
    summary="ユーザの石の配置",
    description="ユーザーが石を置く位置を指定してこのエンドポイントにリクエストを送信します。その位置に石を置いた後のゲーム盤面をレスポンスとして返します。",
)
def user_place(
    q: UserPlaceParams = Depends(),
):
    othello = Othello(BOARD_SIZE)
    othello.set_board(q.board)
    othello.place_human((q.x, q.y), Stone.BLACK)

    return BoardResponse(
        size=BOARD_SIZE,
        rows=toRows(othello.get_board()),
        valids=othello.get_valid_moves(Stone.BLACK),
        status=othello.is_game_ended(),
        score=othello.get_score(),
    )


@router.post(
    "/user/pass",
    response_model=BoardResponse,
    summary="ユーザのパス",
    description="ユーザーがパスを宣言してこのエンドポイントにリクエストを送信します。その後、AIが石を置く位置を計算し、その位置に石を置いた後のゲーム盤面をレスポンスとして返します。",
)
def user_pass(
    q: UserPassParams = Depends(),
):
    othello = Othello(BOARD_SIZE)
    othello.set_board(q.board)
    othello.place_computer(Stone.WHITE)

    return BoardResponse(
        size=BOARD_SIZE,
        rows=toRows(othello.get_board()),
        valids=othello.get_valid_moves(Stone.BLACK),
        status=othello.is_game_ended(),
        score=othello.get_score(),
    )


@router.post(
    "/ai/place",
    response_model=BoardResponse,
    summary="AIの石の配置",
    description="このエンドポイントを呼び出すと、AIが次に石を置く位置を計算し、その位置に石を置いた後のゲーム盤面がレスポンスとして返されます。",
)
def ai_place(
    q: AIPlaceParams = Depends(),
):
    othello = Othello(BOARD_SIZE)
    othello.set_board(q.board)
    othello.place_computer(Stone.WHITE)
    return BoardResponse(
        size=BOARD_SIZE,
        rows=toRows(othello.get_board()),
        valids=othello.get_valid_moves(Stone.BLACK),
        status=othello.is_game_ended(),
        score=othello.get_score(),
    )

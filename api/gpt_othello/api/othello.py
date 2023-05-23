from dataclasses import dataclass

from fastapi import APIRouter
from fastapi.param_functions import Body, Depends, Query
from gpt_othello.modules.othello import STONE, Othello

from .schema import Board

router = APIRouter()

BOARD_SIZE = 8


@dataclass
class InitParams:
    pass


@dataclass
class NextParams:
    x: int = Query(..., title="X座標", description="石を置くX座標", ge=0)
    y: int = Query(..., title="Y座標", description="石を置くY座標", ge=0)
    board: list[list[int]] = Body(
        ...,
        title="盤面",
        description="2次元配列で表現したオセロ盤面。1:黒,-1:白",
        example="[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]",
    )


@router.get("/init", response_model=Board, summary="オセロの初期盤面の取得")
def init(
    q: InitParams = Depends(),
):
    """
    オセロの初期盤面を取得する
    """
    othello = Othello(BOARD_SIZE)

    return Board(rows=othello.get_board(), valids=othello.get_valid_moves(STONE.BLACK), status=othello.is_game_ended())


@router.post("/next", response_model=Board, summary="オセロの次の盤面の取得")
def next(
    q: NextParams = Depends(),
):
    othello = Othello(BOARD_SIZE)
    othello.set_board(q.board)
    othello.place_human((q.x, q.y), STONE.BLACK)
    othello.place_computer(STONE.WHITE)
    return Board(rows=othello.get_board(), valids=othello.get_valid_moves(STONE.BLACK), status=othello.is_game_ended())

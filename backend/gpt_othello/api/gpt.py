from dataclasses import dataclass

from fastapi import APIRouter
from fastapi.param_functions import Body, Depends

from gpt_othello.modules.gpt import GPT
from gpt_othello.modules.othello import Othello, Stone

from .schema import GptAnswerResponse

router = APIRouter()

BOARD_SIZE = 8


@dataclass
class AskParams:
    board: list[list[int]] = Body(
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


@router.post(
    "/gpt/ask",
    response_model=GptAnswerResponse,
    summary="ChatGPTに次の手を尋ねる",
    description="ChatGPTに次の手を尋ね、最善手を返します。",
)
def start(
    q: AskParams = Depends(),
):
    othello = Othello(BOARD_SIZE)
    othello.set_board(q.board)

    gpt = GPT()

    gpt.ask(othello.get_board(), othello.get_valid_moves(Stone.BLACK))

    answer = gpt.ask(othello.get_board(), othello.get_valid_moves(Stone.BLACK))

    return GptAnswerResponse(position=answer["position"], answer=answer["description"])

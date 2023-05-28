from enum import IntEnum

import numpy as np

from ..lib.MCTS import MCTS
from ..lib.othello.OthelloGame import OthelloGame
from ..lib.othello.pytorch.NNet import NNetWrapper as NNet
from ..lib.utils import dotdict

Position = tuple[int, int]


class STONE(IntEnum):
    BLACK = -1
    WHITE = +1


class Player(IntEnum):
    HUMAN = -1
    COMPUTER = +1


class GameStatus(IntEnum):
    NOT_ENDED = 0
    HUMAN_WIN = 1
    COMPUTER_WIN = 2
    DRAW = 3


class Othello:
    def __init__(self, size: int):
        self.size = size
        self.game = OthelloGame(size)
        self.board = self.game.getInitBoard()
        self.computer = self._init_computer()

    def set_board(self, board: list):
        initial_board = np.array(board)
        self.board = self.game.setInitBoard(initial_board)

    def get_board(self) -> list[list[STONE]]:
        return self.board.tolist()

    def get_valid_moves(self, stone: STONE) -> list[Position]:
        valids = self.game.getValidMoves(self.board, stone).tolist()
        valid_moves = [(int(i / self.game.n), int(i % self.game.n)) for i in range(len(valids)) if valids[i] == 1]
        # [8,0]はパスを表す
        return [] if valid_moves == [(self.size, 0)] else valid_moves

    def place_human(self, position: Position, stone: STONE):
        action = self.game.n * position[0] + position[1]
        valids = self.game.getValidMoves(self.board, Player.HUMAN)
        if valids[action] == 0:
            assert valids[action] > 0
        self.board, _ = self.game.getNextState(self.board, Player.HUMAN, action)

    def place_computer(self, stone: STONE):
        action = self.computer(self.game.getCanonicalForm(self.board, Player.COMPUTER))
        self.board, _ = self.game.getNextState(self.board, Player.COMPUTER, action)

    def get_score(self) -> tuple[int, int]:
        human_score = len([cell for cell in self.board.flatten() if cell == STONE.BLACK])
        computer_score = len([cell for cell in self.board.flatten() if cell == STONE.WHITE])
        return (human_score, computer_score)

    def is_game_ended(self) -> GameStatus:
        ended = self.game.getGameEnded(self.board, Player.HUMAN) * Player.HUMAN
        match ended:
            case Player.HUMAN:
                return GameStatus.HUMAN_WIN
            case Player.COMPUTER:
                return GameStatus.COMPUTER_WIN
            case 0:
                return GameStatus.NOT_ENDED
            case _:
                return GameStatus.DRAW

    def _init_computer(self):
        n1 = NNet(self.game)
        n1.load_checkpoint("/app/gpt_othello/lib/pretrained_models/othello/pytorch/", "8x8_100checkpoints_best.pth.tar")
        args1 = dotdict({"numMCTSSims": 50, "cpuct": 1.0})
        mcts1 = MCTS(self.game, n1, args1)
        n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
        return n1p

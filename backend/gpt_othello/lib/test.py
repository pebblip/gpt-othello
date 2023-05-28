import numpy as np

from MCTS import MCTS
from othello.OthelloGame import OthelloGame
from othello.OthelloPlayers import HumanOthelloPlayer
from othello.pytorch.NNet import NNetWrapper as NNet
from utils import *


def main():
    game = OthelloGame(8)

    board = game.getInitBoard()

    player1 = HumanOthelloPlayer(game).play

    n1 = NNet(game)
    n1.load_checkpoint("./pretrained_models/othello/pytorch/", "8x8_100checkpoints_best.pth.tar")
    args1 = dotdict({"numMCTSSims": 50, "cpuct": 1.0})
    mcts1 = MCTS(game, n1, args1)
    n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

    player2 = n1p

    players = [player2, None, player1]
    curPlayer = 1

    initial_board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )  # define the initial board state

    board = game.setInitBoard(initial_board)  # set th

    valid = game.getValidMoves(board, curPlayer)

    for i in range(len(valid)):
        if valid[i]:
            print("[", int(i / game.n), int(i % game.n), end="] ")

    # game.display(board)

    # action = players[curPlayer + 1](game.getCanonicalForm(board, curPlayer))

    #    valids = game.getValidMoves(game.getCanonicalForm(board, curPlayer), 1)

    #    if valids[action] == 0:
    #        assert valids[action] > 0

    #    game.getNextState(board, curPlayer, action)

    print("hoge")


#   game.getNextState(board, curPlayer, action)


if __name__ == "__main__":
    main()

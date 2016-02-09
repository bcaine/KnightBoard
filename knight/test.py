"""
Tests for each level of Cruise's Knight Board Challenge
"""

from board import Board
from mover import Mover


def test_level(level, file_path):
    assert level in range(1, 6)
    return {
        1: level1,
        2: level2,
        3: level3,
        4: level4,
        5: level5
    }[level](file_path)

def level1(file_path):

    board = Board(file_path, 8)
    moves = [(1, 3), (2, 1), (4, 2), (8, 8)]
    mover = Mover(board)
    mover.move(moves, display=True)

def level2(file_path):
    start = (1, 1)
    end = (6, 6)

    # Set starting point
    board = Board(file_path, 8)    
    board.set_knight_location(start)
    
    mover = Mover(board)
    path = mover.find_path(start, end)
    print path
    mover.move(path, display=True)

def level3(file_path):
    start = (1, 1)
    end = (6, 6)

    # Set starting point
    board = Board(file_path, 8)
    board.set_knight_location(start)

    mover = Mover(board)
    path = mover.find_shortest_path((1, 1), (6, 6))
    print path
    mover.move(path, display=True)

def level4(board):
    pass

def level5(board):
    pass

    

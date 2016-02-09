"""
Solution to Cruise's Knight Board Challenge.

"""

__author__ = "Ben Caine"
__email__ = "Bcaine0@gmail.com"
__date__ = "2/08/16"


import argparse
from board import Board
from mover import Mover

def main():
    parser = argparse.ArgumentParser(
        description="Solution to Cruise's Knight Board Challenge")

    parser.add_argument(
        '-p', '--path', type=str, help='Path to Board', required=True)
    parser.add_argument(
        '-l', '--level', type=int, help='Level 1-5', required=True)

    args = parser.parse_args()

    file_path = args.path
    level = args.level

    board = Board(file_path, level)

    if level == 1:
        level1(board)
    elif level == 2:
        level2(board)
    elif level == 3:
        level3(board)
    elif level == 4:
        level4(board)
    elif level == 5:
        level5(board)
    else:
        print "Please provide a level from 1-5"

def level1(board):
    moves = [(1, 3), (2, 1), (4, 2), (8, 8)]
    mover = Mover(board)
    mover.move(moves, display=True)

def level2(board):
    start = (1, 1)
    end = (6, 6)

    # Set starting point
    board.set_knight_location(start)
    
    mover = Mover(board)
    path = mover.find_path(start, end)
    print path
    mover.move(path, display=True)

def level3(board):
    start = (1, 1)
    end = (6, 6)

    # Set starting point
    board.set_knight_location(start)

    mover = Mover(board)
    path = mover.find_shortest_path((1, 1), (6, 6))
    print path
    mover.move(path, display=True)

def level4(board):
    pass

def level5(board):
    pass

if __name__ == "__main__":
    main()

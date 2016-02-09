"""
Solution to Cruise's Knight Board Challenge.

"""

__author__ = "Ben Caine"
__email__ = "Bcaine0@gmail.com"
__date__ = "2/08/16"


import argparse
from board import Board

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

    # Test each level
    level1(board)
    level2(board)


def level1(board):
    moves = [(1, 3), (2, 1), (4, 2), (8, 8)]
    board.perform_moves(moves, display=True)

def level2(board):
    print board.move((1,1), (6, 6))

def level3(board):
    print board.move((1,1), (6, 6), shortest=True)
    

if __name__ == "__main__":
    main()

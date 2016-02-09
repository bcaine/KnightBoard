"""
Solution to Cruise's Knight Board Challenge.

"""

__author__ = "Ben Caine"
__email__ = "Bcaine0@gmail.com"
__date__ = "2/08/16"


import argparse
from board import Board
from mover import Mover
from test import test_level

def main():
    parser = argparse.ArgumentParser(
        description="Solution to Cruise's Knight Board Challenge")

    parser.add_argument(
        '-p', '--path', type=str, help='Path to Board', required=True)
    parser.add_argument(
        '-l', '--level', type=int, help='Level 1-5', required=True)

    args = parser.parse_args()

    # Get the two args
    file_path = args.path
    level = args.level

    # Run the test for this level
    test_level(level, file_path)
    

if __name__ == "__main__":
    main()

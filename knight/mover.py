"""
A class handling any movement of the knight
"""
import networkx as nx
from board import Board


class Mover(object):

    def __init__(self, board):
        self.board = board
        self.graph = board.graph


    def move(self, moves, display=False):
        """
        Solution to Level 1
           Given a list of moves, this function moves the knight if valid.
           If the move is invalid, it reports that it is invaid and exits
           the function. 
           
           INPUT:
               moves: A location or Sequential List of locations (i, j) 
                      to move to.
               display: Whether to display each move
           RETURN: bool stating whether all moves were valid
        """
        if display:
            print self.board

        # Check whether moves is a list
        if type(moves) is not list:
            moves = [moves]

        # Do the first move independent of the valid checking
        # Because the first location is the start location
        valid = self.board.set_knight_location(moves[0])

        # For every other move, check that it is still valid
        # and display the board if desired
        for move in moves[1:]:
            valid = self.board.move_knight(self.board.current, move)
            if not valid:
                return False
            if display:
                print self.board
        return True

    
    def find_path(self, start, end):
        """Given a start and end, find a valid sequence of moves
           that the knight can take. This path may not be optimal
           INPUT:
               start: (i, j) starting location
               end: (i, j) ending location
           RETURN: list of moves
        """
        # Basic DFS with early stopping when match found
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next_node in set(self.graph.neighbors(vertex)) - set(path):
                if next_node == end:
                    return path + [next_node]
                else:
                    stack.append((next_node, path + [next_node]))
        return None
        

    def find_shortest_path(self, start, end):
        """Given a start and end, find the shortest valid sequence
           of moves that the knight can take.
           INPUT:
               start: (i, j) starting location
               end: (i, j) ending location
           RETURN: list of moves
        """
        # Use NetworkX shortest path function to find the
        # shortest path in our graph
        # Note: If you would prefer me implement a shortest
        # path algorithm myself, please let me know and I'll
        # resubmit with one ASAP. Shouldn't be too hard.
        return nx.shortest_path(self.graph, start, end)

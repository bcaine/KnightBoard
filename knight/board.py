"""
A representation of our knight board.
"""
import networkx as nx

class Board(object):

    def __init__(self, file_path, dimension):
        self.file_path = file_path
        self.board = None
        self.graph = nx.MultiGraph()
        self.dims = dimension

        # Current start, end, and current
        self.start = None
        self.end = None
        self.current = None

        # Read in the board
        self._init_board()
        self._init_graph()


    def set_knight_location(self, location):
        self.move_knight(self.current, location, check_valid=False)

    def move_knight(self, start, goal, check_valid=True):
        """Move your knight from its current location to a new location"""

        # Edges only exist between valid moves
        if check_valid and not self.graph.has_edge(start, goal):
            print "Move from: {} to: {} is invalid.".format(start, goal)
            return False
        
        # If it is valid, move the knight
        (old_x, old_y) = start
        (new_x, new_y) = goal
        
        self.board[old_x][old_y] = '.'
        self.board[new_x][new_y] = 'K'

        self.current = goal

        # Move was valid and performed
        return True
            

    def _init_board(self):
        """Reads in the board data from the filepath given to __init__"""
        f = open(self.file_path)
        # Read the board into a list of lists
        board = [row.split(" ") for row in f.read().split("\n")]
        # Get rid of any whitespace rows
        board = [row for row in board if len(row) == self.dims]

        # Quick checks to make sure its the correct dimensions
        assert len(board) == self.dims
        assert all([len(row) == self.dims for row in board])

        self.board = board
        
        # Find start and end locations if there are any
        self.start = self._find("S")
        self.end = self._find("E")

        if self.start:
            self.current = self.start
            self.board[self.current[0]][self.current[1]] = 'K'


    def _init_graph(self):
        """Creates a NetworkX graph of all valid moves"""
        assert self.board is not None

        for i in range(0, self.dims):
            for j in range(0, self.dims):
                pos = (i, j)
                # Get value of board at this location
                data = self.board[i][j]
                
                self.graph.add_node(pos, value=data)
                for move in self._generate_valid_moves(pos):
                    self.graph.add_edge(pos, move)

    def _get_weight(self, data):
        """Given data from the node, we calculate the weight of the edge"""
        pass

    def _generate_valid_moves(self, position):
        """Given a position, return all valid moves"""
        x, y = position

        xlim = self.dims - 1
        ylim = self.dims - 1

        moves = []

        # Range of our search neighborhood
        xmin = max(x-2, 0)
        xmax = min(x+3, xlim)
        
        ymin = max(y-2, 0)
        ymax = min(y+3, ylim)
        
        for i in range(xmin, xmax):
            for j in range(ymin, ymax):
                # Distance away has to be 3
                if abs(x-i) + abs(y-j) != 3:
                    continue

                moves.append((i, j))
        return moves

    
    def _find(self, value):
        """Find the first matching value on the board"""
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == value:
                    return (i, j)
        return None
        

    def __str__(self):
        """Overwritten __str__ class so print displays the board"""
        string = ''
        for row in self.board:
            string += ' '.join(row) + '\n'
        return string

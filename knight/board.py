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
        self.previous_value = '.'

        # Read in the board
        self._init_board()
        self._init_graph()


    def set_knight_location(self, location):
        if self.current:
            self.move_knight(self.current, location, check_valid=False)
        else:
            self.current = location
            (x, y) = location
            self.board[x][y] = "K"

    def move_knight(self, start, goal, check_valid=True):
        """Move your knight from its current location to a new location"""
        # Edges only exist between valid moves
        if check_valid and not self.graph.has_edge(start, goal):
            print "Move from: {} to: {} is invalid.".format(start, goal)
            return False
        
        # If it is valid, move the knight
        (old_x, old_y) = start
        (new_x, new_y) = goal

        # Goofy hack to let us show all past knight locations
        prev_val = self.board[old_x][old_y]
        
        self.board[old_x][old_y] = self.previous_value
        self.board[new_x][new_y] = 'K'
        self.previous_value = prev_val
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
        start = self._find("S")
        end = self._find("E")

        self.start = start[0] if start else None
        self.end = end[0] if end else None

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

                # If the node is not a [R]ock or a [B]arrier
                print data
                if data not in ["R", "B"]:
                    self.graph.add_node(pos, value=data)
                    
                for move in self._generate_valid_moves(pos):
                    if self._is_valid_path(pos, move):
                        weight = self._get_node_weight(move)
                        self.graph.add_edge(pos, move, weight=weight)

        # Get the two [T]eleport nodes and swap them.
        teleport = self._find('T')
        if len(teleport) == 2:
            t1, t2 = teleport
            # Create a mapping to eachother to implement teleport
            mapping = {t1: t2, t2: t1}
            # Apply said mapping
            self.graph = nx.relabel_nodes(self.graph, mapping)


    def _get_node_weight(self, data):
        """Return node weight if [W]ater or [L]ava, otherwise default to 1"""
        return {"W": 2, "L": 5}.get(data, 1)


    def _is_valid_path(self, start, end):
        """Checks if a path has no obstructions"""
        x, y = start
        end_x, end_y = end
        
        x_dir = end_x - x
        y_dir = end_y - y

        # We know we only move a total of 3 spaces, so we can figure
        # out exactly what moves are required to get from start to finish

        # If we move two spaces in the x direction, check that
        if abs(x_dir) > abs(y_dir):
            direction = -1 if x_dir < 0 else 1
            # Check first position
            x += direction
            if self._is_obstructed_location((x, y)):
                return False
            # Check second position
            x += direction
            if self._is_obstructed_location((x, y)):
                return False

        # Otherwise check two moves in the y direction
        else:
            direction = -1 if y_dir < 0 else 1
            # Check first position
            y += direction
            if self._is_obstructed_location((x, y)):
                return False
            y += direction
            if self._is_obstructed_location((x, y)):
                return False
        # Otherwise it's a safe path
        return True


    def _is_obstructed_location(self, location):
        """Returns whether or not a location is obstructed"""
        x, y = location
        return self.board[x][y] == "B"
        
        
    def _get_edge_weight(self, data):
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

                # Add additional constraints that prevent edges

                moves.append((i, j))
        return moves

    
    def _find(self, value):
        """Find the first matching value on the board"""
        found = []
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == value:
                    found.append((i, j))
        return found
        

    def __str__(self):
        """Overwritten __str__ class so print displays the board"""
        string = ''
        for row in self.board:
            string += ' '.join(row) + '\n'
        return string

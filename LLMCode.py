import math

class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = len(board)  # Size of the board (n x n)
        self.subgrid_size = int(math.sqrt(self.size))  # Size of the subgrids (k x k)

    def is_valid(self, row, col, num):
        # Check if 'num' is not in the current row
        if num in self.board[row]:
            return False
        
        # Check if 'num' is not in the current column
        for i in range(self.size):
            if self.board[i][col] == num:
                return False
        
        # Check if 'num' is not in the current subgrid
        subgrid_row_start = (row // self.subgrid_size) * self.subgrid_size
        subgrid_col_start = (col // self.subgrid_size) * self.subgrid_size

        for i in range(subgrid_row_start, subgrid_row_start + self.subgrid_size):
            for j in range(subgrid_col_start, subgrid_col_start + self.subgrid_size):
                if self.board[i][j] == num:
                    return False
        
        return True

    def find_empty(self):
        # Find an empty cell in the Sudoku grid (denoted by 0)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        empty = self.find_empty()

        if not empty:
            return True  # Puzzle solved

        row, col = empty

        for num in range(1, self.size + 1):  # Try numbers 1 through n
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  # Reset the cell

        return False

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))

# Example usage:
# Define a 9x9 Sudoku puzzle (0 denotes an empty cell)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solver = SudokuSolver(board)
if solver.solve():
    solver.print_board()
else:
    print("No solution exists.")

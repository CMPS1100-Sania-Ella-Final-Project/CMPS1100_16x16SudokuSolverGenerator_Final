import unittest

# Implementation of the missing functions
def isValidSudoku(grid):
    invalid_cells = []

    # Check rows and columns for duplicates
    for i in range(16):
        row_seen = set()
        col_seen = set()
        for j in range(16):
            # Check row
            if grid[i][j] != 0:
                if grid[i][j] in row_seen:
                    invalid_cells.append((i, j))
                row_seen.add(grid[i][j])
            # Check column
            if grid[j][i] != 0:
                if grid[j][i] in col_seen:
                    invalid_cells.append((j, i))
                col_seen.add(grid[j][i])

    # Check subgrids for duplicates
    for box_row in range(0, 16, 4):
        for box_col in range(0, 16, 4):
            seen = set()
            for i in range(4):
                for j in range(4):
                    val = grid[box_row + i][box_col + j]
                    if val != 0:
                        if val in seen:
                            invalid_cells.append((box_row + i, box_col + j))
                        seen.add(val)

    return invalid_cells

def isSafe(grid, row, col, num):
    # Check for the number in the same row
    for x in range(16):
        if grid[row][x] == num:
            return False

    # Check for the number in the same column
    for x in range(16):
        if grid[x][col] == num:
            return False

    # Check for the number in the corresponding 4x4 subgrid
    start_row = (row // 4) * 4
    start_col = (col // 4) * 4
    for i in range(4):
        for j in range(4):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solveSudoku(grid):
    def find_empty_location():
        for i in range(16):
            for j in range(16):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def solve():
        loc = find_empty_location()
        if not loc:
            return True
        row, col = loc

        for num in range(1, 17):
            if isSafe(grid, row, col, num):
                grid[row][col] = num
                if solve():
                    return True
                grid[row][col] = 0

        return False

    solve()

class TestSudokuSolver(unittest.TestCase):

    def test_is_valid_sudoku(self):
        # Invalid grid (row conflict)
        invalid_grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 8, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 2, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 0, 0, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 7, 9, 0, 0, 0, 0, 0, 0, 0],
            # Duplicate 5 in this row
            [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        invalid_cells = isValidSudoku(invalid_grid)
        self.assertIn((9, 15), invalid_cells)  # Duplicate 5 in row 9

    def test_is_safe(self):
        grid = [[0] * 16 for _ in range(16)]  # Empty grid
        grid[0][0] = 5

        # Unsafe due to row conflict
        self.assertFalse(isSafe(grid, 0, 1, 5))

        # Unsafe due to column conflict
        self.assertFalse(isSafe(grid, 1, 0, 5))

        # Safe placement
        self.assertTrue(isSafe(grid, 1, 1, 5))

    def test_solve_sudoku(self):
        # Partially filled valid grid
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 8, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 2, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 0, 0, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 7, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        solveSudoku(grid)
        self.assertTrue(isValidSudoku(grid))  # Ensure grid is solved and valid

if __name__ == "__main__":
    unittest.main(exit=False)

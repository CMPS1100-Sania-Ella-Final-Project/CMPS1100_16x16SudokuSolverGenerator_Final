#this is our test suite
import LOGIC_16SudokuSolver
import Sudoku_Examples
def isValidSudoku():
    grid = []
    invalid_cells = []  # List to track invalid entries

    # Check if the grid is valid
    for row in range(16):
        for col in range(16):
            num = grid[row][col]
            if num != 0:  # Only check non-empty cells
                grid[row][col] = 0  # Temporarily remove the number
                if not LOGIC_16SudokuSolver.isSafe(grid, row, col, num):
                    invalid_cells.append((row, col))
                grid[row][col] = num  # Restore the number

    return invalid_cells

def testing(grid):
    if not isValidSudoku(grid):
        print('The given Sudoku has invalid numbers.')
    else: 
        if (LOGIC_16SudokuSolver.solveSudoku(grid, 0, 0)):
            LOGIC_16SudokuSolver.printing(grid)
        else:
            print('no solution exists.')

#works
testing(Sudoku_Examples.puzzle)
print('----')
testing(Sudoku_Examples.puzzle1)
print('----')
testing(Sudoku_Examples.puzzle2)
print('----')
testing(Sudoku_Examples.puzzle3)
print('----')

testing(Sudoku_Examples.puzzle5)
print('----')
testing(Sudoku_Examples.puzzle6)
print('----')
testing(Sudoku_Examples.puzzle7)
print('----')
testing(Sudoku_Examples.puzzle8)
print('----')
testing(Sudoku_Examples.puzzle4)

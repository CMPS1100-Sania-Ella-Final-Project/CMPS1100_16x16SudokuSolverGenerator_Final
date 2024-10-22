#import random

import random


def generate_sudoku(remove_count=40):
    # Generate a completed Sudoku grid
    def fill_grid(grid):
        numbers = list(range(1, 10))
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(grid, i, j, num):
                            grid[i][j] = num
                            if fill_grid(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True

    def is_valid(grid, row, col, num):
        # Check row
        if num in grid[row]:
            return False
        # Check column
        if num in [grid[i][col] for i in range(9)]:
            return False
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    # Initialize empty 9x9 grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    
    # Fill the grid
    fill_grid(grid)
    
    # Create a copy of the filled grid
    puzzle = [row[:] for row in grid]
    
    # Remove numbers to create the puzzle
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells[:remove_count]:
        puzzle[i][j] = 0
    
    return puzzle, grid

# Generate a Sudoku puzzle
puzzle, solution = generate_sudoku()

# Print the puzzle
print("Sudoku Puzzle:")
for row in puzzle:
    print(row)

print("\nSolution:")
for row in solution:
    print(row)

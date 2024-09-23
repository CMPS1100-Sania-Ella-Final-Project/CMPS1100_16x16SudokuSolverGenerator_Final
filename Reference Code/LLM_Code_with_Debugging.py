# N is the size of the 2D matrix N*N
N = 16

# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(f'{arr[i][j]:2}', end=" ")  # Print with better formatting (2-width for numbers)
        print()

# Checks whether it will be legal to assign num to the given row, col
def isSafe(grid, row, col, num):
    # Check if the number is in the current row
    for x in range(N):
        if grid[row][x] == num:
            return False

    # Check if the number is in the current column
    for x in range(N):
        if grid[x][col] == num:
            return False

    # Check if the number is in the 4x4 subgrid
    startRow = row - row % 4
    startCol = col - col % 4
    for i in range(4):
        for j in range(4):
            if grid[i + startRow][j + startCol] == num:
                return False

    return True

# Takes a partially filled-in grid and attempts to assign values to all
# unassigned locations in such a way to meet the requirements for Sudoku solution.
def solveSudoku(grid, row, col):
    # Base case: if we have reached the end of the last row, puzzle is solved
    if row == N:
        return True

    # If column value becomes N, move to the next row and reset column to 0
    if col == N:
        return solveSudoku(grid, row + 1, 0)

    # Skip the cells that are already filled
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)

    # Try placing numbers 1 to N in the cell and backtrack if needed
    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num

            # Print debug statement to trace progress
            print(f"Placing {num} at ({row}, {col})")

            if solveSudoku(grid, row, col + 1):
                return True

        # Backtrack by resetting the cell
        grid[row][col] = 0
        print(f"Backtracking from ({row}, {col})")

    # If no number works, return False (backtrack)
    return False

# Driver Code

# Sample 16x16 Sudoku puzzle with 0 representing unassigned cells
grid = [[0, 5, 0, 0, 0, 0, 11, 10, 16, 12, 3, 14, 0, 2, 6, 0],
        [13, 8, 9, 0, 16, 0, 0, 0, 0, 4, 10, 6, 11, 0, 14, 7],
        [0, 0, 14, 0, 2, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 11, 16, 0, 6, 0, 14, 2, 13, 9, 7, 0, 15, 0, 0],
        [0, 4, 13, 14, 0, 9, 0, 5, 0, 0, 15, 0, 10, 12, 0, 8],
        [0, 16, 2, 0, 0, 0, 1, 6, 0, 5, 0, 0, 15, 0, 7, 15],
        [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 8, 9, 0, 6, 0, 2],
        [6, 0, 8, 0, 0, 0, 3, 15, 0, 11, 13, 16, 0, 5, 0, 1],
        [16, 0, 4, 8, 0, 0, 0, 11, 0, 7, 1, 0, 12, 0, 5, 0,],
        [2, 12, 0, 7, 0, 16, 0, 3, 0, 0, 11, 5, 13, 0, 0, 0],
        [15, 0, 3, 1, 5, 0, 8, 7, 0, 2, 4, 13, 0, 0, 9, 11],
        [11, 9, 0, 6, 0, 4, 14, 0, 12, 10, 0, 15, 7, 8, 0, 3],
        [12, 0, 1, 0, 7, 10, 5, 0, 15, 8, 0, 4, 0, 0, 0, 9],
        [14, 2, 0, 0, 15, 1, 6, 0, 5, 3, 7, 0, 0, 0, 0, 0],
        [0, 0, 15, 4, 14, 0, 12, 0, 0, 16, 6, 0, 0, 0, 3, 5],
        [7, 0, 0, 0, 13, 0, 16, 0, 0, 9, 0, 0, 14, 0, 0, 15]]

# Attempt to solve the puzzle
if solveSudoku(grid, 0, 0):
    printing(grid)
else:
    print("No solution exists")
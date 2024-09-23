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
grid = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 13, 0, 0, 9, 0],
        [0, 4, 0, 0, 8, 0, 7, 11, 5, 0, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 15, 9, 0, 1, 10, 8, 6, 0, 0, 11],
        [0, 8, 10, 0, 0, 12, 0, 0, 0, 4, 0, 14, 7, 0, 0, 16],
        [6, 0, 3, 7, 0, 15, 14, 0, 0, 0, 4, 0, 0, 16, 0, 0],
        [0, 15, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0],
        [0, 0, 4, 0, 11, 0, 3, 7, 0, 6, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 11, 0, 0, 12, 0, 0, 10, 5, 15, 0, 0, 3, 8],
        [0, 0, 12, 0, 1, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
        [0, 1, 14, 4, 0, 0, 0, 0, 12, 0, 11, 0, 0, 0, 0, 6],
        [0, 0, 8, 15, 0, 0, 13, 2, 0, 0, 0, 0, 0, 0, 7, 3],
        [11, 0, 2, 0, 12, 0, 0, 0, 1, 8, 15, 7, 4, 0, 0, 9],
        [0, 0, 0, 0, 0, 6, 0, 0, 0, 14, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 12, 16, 0, 0, 15, 0, 0, 2, 4, 14, 13, 0, 0],
        [3, 16, 15, 0, 0, 2, 0, 0, 0, 9, 0, 12, 0, 0, 0, 7],
        [0, 2, 9, 8, 4, 0, 0, 0, 0, 0, 7, 1, 0, 0, 16, 0]]

# Attempt to solve the puzzle
if solveSudoku(grid, 0, 0):
    printing(grid)
else:
    print("No solution exists")

# N is the size of the 2D matrix   N*N
N = 16
import random

# A utility function to print grid
def printing(arr):
    N = len(arr)  # Assuming it's a square grid (NxN)
    subgrid_size = int(N ** 0.5)  # 4x4 subgrid for a 16x16 grid

    for i in range(N):
        # Add a horizontal line between subgrids
        if i % subgrid_size == 0 and i != 0:
            print("--" * (N + subgrid_size - 1))  # Extra dashes for subgrid separation

        for j in range(N):
            # Add a vertical space between subgrids
            if j % subgrid_size == 0 and j != 0:
                print("|", end=" ")

            print(arr[i][j], end=" ")
        
        print()  # Move to the next line after each row


#Function to confirm input is a valid sudoku
def isValidSudoku(entries):
    grid = []
    invalid_cells = []  # List to track invalid entries

    # Convert entries to a 2D list
    for row in entries:
        grid_row = []
        for entry in row:
            try:
                value = int(entry.get()) if entry.get() != "" else 0
                grid_row.append(value)
            except ValueError:
                grid_row.append(0)  # Treat empty cells as 0
        grid.append(grid_row)
    
    # Check if the grid is valid
    for row in range(16):
        for col in range(16):
            num = grid[row][col]
            if num != 0:  # Only check non-empty cells
                grid[row][col] = 0
                if not isSafe(grid, row, col, num):
                    invalid_cells.append((row, col))
            grid[row][col] = num

    return invalid_cells

# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):
    
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(16):
        if grid[row][x] == num:
            return False

    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(16):
        if grid[x][col] == num:
            return False

    # Check if we find the same num in
    # the particular 4*4 matrix,
    # we return false
    startRow = row - row % 4
    startCol = col - col % 4
    for i in range(4):
        for j in range(4):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):
  
    # Check if we have reached the 15th
    # row and 16th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
       
        return True
      
    # Check if column value  becomes 16 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0

    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    
    for num in range(1, N + 1, 1):
      
        # Check if it is safe to place
        # the num (1-16)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(grid, row, col, num):
          
            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num

            # Checking for next possibility with next
            # column
            if solveSudoku(grid, row, col + 1):
                return True

        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False

def generate_sudoku(remove_count=120):
    # Generate a completed Sudoku grid
    def fill_grid(grid):
        numbers = list(range(1, 17))
        for i in range(16):
            for j in range(16):
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
        if num in [grid[i][col] for i in range(16)]:
            return False
        # Check 4x4 box
        box_row, box_col = 4 * (row // 4), 4 * (col // 4)
        for i in range(box_row, box_row + 4):
            for j in range(box_col, box_col + 4):
                if grid[i][j] == num:
                    return False
        return True

    # Initialize empty 16x16 grid
    grid = [[0 for _ in range(16)] for _ in range(16)]
    
    # Fill the grid
    fill_grid(grid)
    
    # Create a copy of the filled grid
    puzzle = [row[:] for row in grid]
    
    # Remove numbers to create the puzzle
    cells = [(i, j) for i in range(16) for j in range(16)]
    random.shuffle(cells)
    for i, j in cells[:remove_count]:
        puzzle[i][j] = 0
    
    return puzzle, grid
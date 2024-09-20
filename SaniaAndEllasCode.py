
# N is the size of the 2D matrix   N*N
N = 16

# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()

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
    # the particular 3*3 matrix,
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
  
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True
      
    # Check if column value  becomes 9 ,
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
        # the num (1-9)  in the
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

# Driver Code

# 0 means unassigned cells
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

if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution  exists ")
# N is the size of the 2D matrix   N*N
N = 16

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

# Driver Code

# 0 means unassigned cells
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
        [7, 0, 0, 0, 13, 0, 16, 0, 0, 9, 0, 0, 14, 0, 0, 15]
        ]

if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution exists ")



# Driver Code
# 0 means unassigned cells

if __name__ == "__main__": #starts automatically when run directly
    print("Welcome to the 16x16 Sudoku Solver!")
    
    # Take the user input grid
    grid = user_input_sudoku()

    print("\nHere is the Sudoku puzzle you entered:")
    printing(grid)

    # Check if the input grid is a valid Sudoku puzzle
    if isValidSudoku(grid):
        print("\nSolving the Sudoku puzzle...\n")
        if solveSudoku(grid, 0, 0):
            print("Solved Sudoku grid:")
            printing(grid)
        else:
            print("This Sudoku puzzle cannot be solved.")
    else:
        print("The input Sudoku puzzle is not valid.")

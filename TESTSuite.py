#This is the test suite for SaniaAndEllasCode
import SaniaAndEllasCode
import Sudoku_Examples
if (SaniaAndEllasCode.solveSudoku(Sudoku_Examples.puzzle1, 0, 0)):
    SaniaAndEllasCode.printing(Sudoku_Examples.puzzle1)
else:
    print("no solution exists ")

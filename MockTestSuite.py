
import unittest
from unittest.mock import patch
import SaniaAndEllasCode
import Sudoku_Examples

class TestSudokuGUI(unittest.TestCase):

    @patch('builtins.input', side_effect=["Sudoku_Examples.puzzle", "Sudoku_Examples.puzzle1"])
    def test_sudoku_solution(self, mock_input):
        # Test solving the first puzzle
        grid = eval(mock_input())  # Simulating user input for the puzzle
        result = SaniaAndEllasCode.solveSudoku(grid, 0, 0)
        self.assertTrue(result, "Sudoku solver should find a solution.")
        
        # Test solving the second puzzle
        grid = eval(mock_input())  # Simulating user input for another puzzle
        result = SaniaAndEllasCode.solveSudoku(grid, 0, 0)
        self.assertTrue(result, "Sudoku solver should find a solution.")

if __name__ == "__main__":
    unittest.main()

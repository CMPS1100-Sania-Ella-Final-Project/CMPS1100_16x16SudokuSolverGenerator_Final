import unittest
import subprocess
import sys

class TestSudokuSolver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the environment before running tests."""
        cls.script_path = 'LOGIC_16SudokuSolver.py'  # Ensure this path is correct.

    def test_program_runs(self):
        """Test if the program runs without crashing."""
        try:
            result = subprocess.run(
                [sys.executable, self.script_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            self.assertEqual(result.returncode, 0, f"Program exited with error: {result.stderr}")
        except Exception as e:
            self.fail(f"Failed to execute the script: {e}")

    def test_output_functionality(self):
        """Test the output of the solver."""
        try:
            from LOGIC_16SudokuSolver import solveSudoku  # Correct function name

            # Test case: An example 16x16 Sudoku puzzle input
            test_input = [
                [0, 0, 0, 0, 2, 0, 0, 6, 0, 0, 0, 3, 0, 0, 0, 0],
                # Add the rest of your Sudoku grid here
            ]
            # Add the expected solved Sudoku grid
            expected_output = [
                [1, 2, 3, 4, 2, 5, 7, 6, 9, 8, 10, 3, 11, 12, 13, 14],
                # Complete expected solved grid
            ]

            result = solveSudoku(test_input)
            self.assertEqual(result, expected_output, "Solver output is incorrect.")
        except ImportError:
            self.fail("The function 'solveSudoku' could not be imported. Check the script structure.")
        except Exception as e:
            self.fail(f"Output functionality test failed: {e}")

    def test_sudoku_solver_correctness(self):
        """Test for logic correctness (e.g., all rows, columns, and sub-grids are valid)."""
        from LOGIC_16SudokuSolver import solveSudoku  # Correct function name

        def is_valid_sudoku(grid):
            """Helper function to validate a solved Sudoku grid."""
            size = len(grid)
            block_size = int(size**0.5)

            def check_unique(values):
                """Check if all values are unique ignoring zeros."""
                nums = [v for v in values if v != 0]
                return len(nums) == len(set(nums))

            # Validate rows and columns
            for i in range(size):
                if not check_unique(grid[i]) or not check_unique([grid[j][i] for j in range(size)]):
                    return False

            # Validate sub-grids
            for row in range(0, size, block_size):
                for col in range(0, size, block_size):
                    block = [
                        grid[r][c]
                        for r in range(row, row + block_size)
                        for c in range(col, col + block_size)
                    ]
                    if not check_unique(block):
                        return False
            return True

        # Example 16x16 Sudoku puzzle
        test_input = [
            [0, 0, 0, 0, 2, 0, 0, 6, 0, 0, 0, 3, 0, 0, 0, 0],
            # Add the rest of the grid
        ]
        solved_grid = solveSudoku(test_input)
        self.assertTrue(is_valid_sudoku(solved_grid), "Solved grid is not a valid Sudoku.")

if __name__ == "__main__":
    unittest.main()

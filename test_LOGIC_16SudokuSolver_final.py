import unittest
import subprocess
import sys

class TestSudokuSolver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the environment before running tests
        cls.script_path = 'LOGIC_16SudokuSolver.py'  # Ensure this path is correct.

    def test_program_runs(self):
        # Test if the program runs without crashing
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

    def test_sudoku_puzzles(self):
        # Test the solver with three different Sudoku puzzles
        from LOGIC_16SudokuSolver import solveSudoku  # Import the solver function

        # Define Sudoku test cases
        test_cases = [
            {
                "name": "Easy Puzzle",
                "input": [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ],
                "expected": [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]
            },
            {
                "name": "Medium Puzzle",
                "input": [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 3, 0, 8, 5],
                    [0, 0, 1, 0, 2, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 7, 0, 0, 0],
                    [0, 0, 4, 0, 0, 0, 1, 0, 0],
                    [0, 9, 0, 0, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 7, 3],
                    [0, 0, 2, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 4, 0, 0, 0, 9]
                ],
                "expected": [
                    [9, 8, 7, 6, 5, 4, 3, 2, 1],
                    [4, 2, 6, 1, 7, 3, 9, 8, 5],
                    [3, 5, 1, 9, 2, 8, 7, 4, 6],
                    [1, 6, 8, 5, 3, 7, 2, 9, 4],
                    [7, 4, 9, 2, 8, 6, 1, 5, 3],
                    [2, 9, 5, 4, 1, 3, 8, 6, 7],
                    [5, 1, 3, 8, 6, 2, 4, 7, 9],
                    [6, 7, 2, 3, 9, 4, 5, 1, 8],
                    [8, 3, 4, 7, 5, 9, 6, 2, 1]
                ]
            },
            {
                "name": "Hard Puzzle",
                "input": [
                    [8, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 6, 0, 0, 0, 0, 0],
                    [0, 7, 0, 0, 9, 0, 2, 0, 0],
                    [0, 5, 0, 0, 0, 7, 0, 0, 0],
                    [0, 0, 0, 0, 4, 5, 7, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 3, 0],
                    [0, 0, 1, 0, 0, 0, 0, 6, 8],
                    [0, 0, 8, 5, 0, 0, 0, 1, 0],
                    [0, 9, 0, 0, 0, 0, 4, 0, 0]
                ],
                "expected": [
                    [8, 1, 2, 7, 5, 3, 6, 4, 9],
                    [9, 4, 3, 6, 8, 2, 1, 7, 5],
                    [6, 7, 5, 4, 9, 1, 2, 8, 3],
                    [1, 5, 4, 2, 3, 7, 8, 9, 6],
                    [3, 6, 9, 8, 4, 5, 7, 2, 1],
                    [7, 2, 8, 1, 6, 9, 5, 3, 4],
                    [5, 3, 1, 9, 7, 4, 6, 8, 2],
                    [4, 8, 6, 5, 2, 9, 3, 1, 7],
                    [2, 9, 7, 3, 1, 8, 4, 6, 5]
                ]
            }
        ]

        for case in test_cases:
            with self.subTest(case["name"]):
                result = solveSudoku(case["input"], 0, 0)  # Assuming function takes input and start position
                self.assertEqual(result, case["expected"], f"Failed for {case['name']}")

if __name__ == "__main__":
    unittest.main()

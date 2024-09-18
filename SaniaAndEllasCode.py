#This is where I will be writing the code for our Midterm

def check_sudoku_parameters(sudoku):
    N = len(sudoku)
    if not all(len(row) == N for row in sudoku):
        raise ValueError("Sudoku must be a square matrix.")
    if math.isqrt(N) ** 2 != N:
        return ValueError("Sudoku must be a square of squares.")
    valid_numbers = set(range(1, N + 1))
    for row in sudoku:
        for value in row:
            if value not in valid_numbers:
                return ValueError(f"Invalid number {value} found in Sudoku.")
    else: return True





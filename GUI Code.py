#GUI Code
import tkinter
import customtkinter
import LOGIC_16SudokuSolver


#solver Screen
# Function to validate input (only digits 1-16 or empty input allowed)
def validate_input(value_if_allowed):
    if value_if_allowed == "" or (value_if_allowed.isdigit() and 1 <= int(value_if_allowed) <= 16):
        return True
    return False

#global variable to hold reference to current v. new frame
grid_frame = None
#function to create & display grid
def create_grid():
    global grid_frame

    #clear any existing grid
    if grid_frame is not None:
        grid_frame.destroy()

    # Create a new frame for the Sudoku grid
    grid_frame = customtkinter.CTkFrame(app, width=800, height=800)
    grid_frame.pack(pady=20)

    # Validation command for entries
    validate_command = app.register(validate_input)

    # Store the entries in a 2D list
    entries = []

    for row in range(16):
        row_entries = []
        for col in range(16):
            # Determine the background color for the 4x4 subgrids
            bg_color = "#fee1e8" if (row // 4 + col // 4) % 2 == 0 else "#ffffb5"

            # Create a frame for each cell to handle coloring
            cell_frame = tkinter.Frame(grid_frame, width=40, height=40, bg=bg_color)
            cell_frame.grid(row=row, column=col, padx=1, pady=1)

            # Create an entry inside the frame
            entry = customtkinter.CTkEntry(
                cell_frame, 
                width=40, height=40, 
                justify="center", 
                font=("Arial", 12),
                validate="key", 
                validatecommand=(validate_command, "%P"),
                fg_color=bg_color
            )
            entry.pack(expand=True, fill="both")
            
            row_entries.append(entry)
        entries.append(row_entries)


    # Add a submit button below the grid
    submit_button = customtkinter.CTkButton(grid_frame, text="Submit", command=lambda: process_grid(entries))
    submit_button.grid(row=16, column=0, columnspan=16, pady=10)

    return entries

# Function to process the grid and validate user input
def process_grid(entries):
    invalid_cells = LOGIC_16SudokuSolver.isValidSudoku(entries)
    if invalid_cells:
        # Display an error message
        error_message = "Invalid entries detected at positions: " + ", ".join([f"({row+1}, {col+1})" for row, col in invalid_cells])
        error_label = customtkinter.CTkLabel(app, text=error_message, fg_color="red")
        error_label.pack(pady=10)
    else:
        grid = []
        for row in entries:
            grid_row = []
            for entry in row:
                try:
                    value = int(entry.get())
                    grid_row.append(value)
                except ValueError:
                    grid_row.append(0)  # Treat empty cells as 0
            grid.append(grid_row)
        
        if LOGIC_16SudokuSolver.solveSudoku(grid, 0, 0):
            # If the Sudoku is solved, update the entries with the solution
            for i in range(16):
                for j in range(16):
                    entries[i][j].delete(0, 'end')  # Clear the entry
                    entries[i][j].insert(0, str(grid[i][j]))  # Insert the solved value
            print("Sudoku solved!")
        else:
            print("No solution exists.")


#Puzzle Screen
def create_puzzle():
    entries=create_grid()
    # Generate a Sudoku puzzle and its solution
    puzzle, solution = LOGIC_16SudokuSolver.generate_sudoku()
    
    # Update the entry widgets with the new puzzle
    for i in range(16):
        for j in range(16):
            entries[i][j].delete(0, 'end')  # Clear the current entry
            if puzzle[i][j] != 0:
                entries[i][j].insert(0, str(puzzle[i][j]))  # Insert the new puzzle value
                entries[i][j].configure(state='disabled')
            else:
                entries[i][j].insert(0, '')  # Empty cell (value is 0)
    
    # Return the solution for later use (in case you need it for solving)
    LOGIC_16SudokuSolver.printing(solution)
    return solution



#system settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#app frame

app = customtkinter.CTk()
app.geometry("1350x900")
app.title("16x16 Sudokus!")
app.configure(bg_color="#d4f0f0")        
        
#UI elements introduced
title = customtkinter.CTkLabel(app, text="Welcome to our 16x16 Sudoku App! Are you looking for a new puzzle or a solution to one you have?")
selection_frame = customtkinter.CTkFrame(app, width=600, height=40)
selection_frame.pack_propagate(False)
select_solver = customtkinter.CTkButton(selection_frame, text="Sudoku Solver", command=create_grid)
select_puzzle = customtkinter.CTkButton(selection_frame, text="Sudoku Puzzle", command=create_puzzle)
title.pack()
selection_frame.pack(pady=10)
select_solver.pack(side="left", padx=50)
select_puzzle.pack(side="right", padx=50)
#driver
app.mainloop()
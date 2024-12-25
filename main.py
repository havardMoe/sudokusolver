import tkinter as tk
import numpy as np

def display_sudoku(grid):
    """
    Displays the Sudoku grid in a Tkinter pop-up window.

    Args:
        grid (np.ndarray): A 9x9 Sudoku grid.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Sudoku Solver")

    # Define the grid size
    for i in range(9):
        for j in range(9):
            # Create a label for each cell
            cell_value = grid[i, j] if grid[i, j] != 0 else ""
            label = tk.Label(root, text=cell_value, borderwidth=1, relief="solid", width=2, height=1, font=("Arial", 24))
            label.grid(row=i, column=j, padx=5, pady=5)

    # Run the application
    root.mainloop()

def check_valid_grid(grid):
    """
    Checks if a Sudoku grid is valid according to the rules:
    1. No duplicate numbers in any row.
    2. No duplicate numbers in any column.
    3. No duplicate numbers in any 3x3 sub-grid.

    Args:
        grid (np.ndarray): A 9x9 Sudoku grid.

    Returns:
        bool: True if the grid is valid, False otherwise.
    """
    def is_valid_row(grid):
        """Checks if each row in the grid is valid."""
        for row in grid:
            if not is_valid_unit(row):
                return False
        return True

    def is_valid_column(grid):
        """Checks if each column in the grid is valid."""
        for col in grid.T:  # Transpose the grid to iterate over columns as rows
            if not is_valid_unit(col):
                return False
        return True

    def is_valid_subgrid(grid):
        """Checks if each 3x3 sub-grid in the grid is valid."""
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                sub_grid = grid[box_row:box_row + 3, box_col:box_col + 3].flatten()
                if not is_valid_unit(sub_grid):
                    return False
        return True

    def is_valid_unit(unit):
        """Helper function to check if a row, column, or sub-grid is valid."""
        unit = unit[unit != 0]  # Remove empty cells
        return len(unit) == len(set(unit))  # Check for duplicates

    # Validate rows, columns, and sub-grids
    return is_valid_row(grid) and is_valid_column(grid) and is_valid_subgrid(grid)

if __name__ == "__main__":
    # Valid Sudoku grid
    sudoku_grid = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ])

    # Invalid grid (duplicate in a sub-grid)
    invalid_grid = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 5],  # Duplicate 5 in the bottom-right sub-grid
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ])

    print(check_valid_grid(sudoku_grid))  # Output: True
    print(check_valid_grid(invalid_grid))  # Output: False
    display_sudoku(sudoku_grid)

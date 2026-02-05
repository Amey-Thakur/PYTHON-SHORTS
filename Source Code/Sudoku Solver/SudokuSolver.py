"""
File: SudokuSolver.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a graphical Sudoku Solver using a backtracking 
    algorithm. It provides a Tkinter-based interface for grid entry and 
    demonstrates recursive constraint satisfaction for solving 9x9 puzzles.

Complexity Analysis:
    - Time Complexity: O(9^(n*n)) where n=9, essentially constant but 
      exponential in the number of empty cells in the worst case.
    - Space Complexity: O(n*n) for the grid and the recursion stack.

Logic:
    1. Backtracking Algorithm: Find an empty cell.
    2. Try digits 1-9. Check if the digit is valid in the current row, 
       column, and 3x3 subgrid.
    3. If valid, recursively try to solve the rest of the board.
    4. If no digits work, backtrack by resetting the cell and trying 
       the next digit in the previous recursive call.
    5. GUI: Maps user inputs to the grid, triggers solve, and updates display.
"""

import tkinter as tk
from tkinter import messagebox
from typing import List, Optional


class SudokuService:
    """
    A service class providing backtracking logic for solving Sudoku puzzles.
    """

    @staticmethod
    def is_valid(grid: List[List[int]], row: int, col: int, num: int) -> bool:
        """Checks if placing 'num' at grid[row][col] is valid."""
        # Check row
        for x in range(9):
            if grid[row][x] == num:
                return False

        # Check column
        for x in range(9):
            if grid[x][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def find_empty(self, grid: List[List[int]]) -> Optional[tuple]:
        """Finds the next empty cell (0) in the grid."""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return None

    def solve(self, grid: List[List[int]]) -> bool:
        """Solves the Sudoku grid using backtracking."""
        empty = self.find_empty(grid)
        if not empty:
            return True  # Puzzle solved

        row, col = empty
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.solve(grid):
                    return True
                grid[row][col] = 0  # Backtrack

        return False


class SudokuAppGUI:
    """
    Tkinter GUI for the Sudoku Solver.
    """

    def __init__(self, service: SudokuService):
        self.service = service
        self.window = tk.Tk()
        self.window.title("Scholarly Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self._build_grid()
        self._build_buttons()

    def _build_grid(self):
        """Constructs the 9x9 entry grid with subgrid styling."""
        container = tk.Frame(self.window, padx=10, pady=10)
        container.pack()

        for r in range(9):
            for c in range(9):
                # Add highlighting for 3x3 blocks
                padx = (2, 0) if c % 3 == 0 and c != 0 else (0, 0)
                pady = (2, 0) if r % 3 == 0 and r != 0 else (0, 0)
                
                entry = tk.Entry(container, width=3, font=('Arial', 18, 'bold'), 
                                justify='center', bd=1, relief="solid")
                entry.grid(row=r, column=c, padx=padx, pady=pady)
                self.cells[r][c] = entry

    def _build_buttons(self):
        """Adds control buttons."""
        btn_frame = tk.Frame(self.window, pady=10)
        btn_frame.pack()

        tk.Button(btn_frame, text="Solve Puzzle", command=self._solve, 
                  bg="#4CAF50", fg="white", font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear Grid", command=self._clear, 
                  font=('Arial', 10)).pack(side=tk.LEFT, padx=5)

    def _get_grid(self) -> List[List[int]]:
        """Parses inputs from the UI into a nested list."""
        grid = []
        for r in range(9):
            row = []
            for c in range(9):
                val = self.cells[r][c].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def _set_grid(self, grid: List[List[int]]):
        """Updates the UI with values from the grid."""
        for r in range(9):
            for c in range(9):
                self.cells[r][c].delete(0, tk.END)
                if grid[r][c] != 0:
                    self.cells[r][c].insert(0, str(grid[r][c]))

    def _solve(self):
        """Triggers the solve process."""
        try:
            grid = self._get_grid()
            if self.service.solve(grid):
                self._set_grid(grid)
            else:
                messagebox.showerror("Error", "No solution exists for this puzzle!")
        except ValueError:
            messagebox.showerror("Error", "Please enter digits 1-9 only.")

    def _clear(self):
        """Resets the grid."""
        for r in range(9):
            for c in range(9):
                self.cells[r][c].delete(0, tk.END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    service = SudokuService()
    app = SudokuAppGUI(service)
    app.run()

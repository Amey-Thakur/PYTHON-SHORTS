"""
File: GameOfLife.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements Conway's Game of Life, a cellular automaton. 
    It demonstrates emergent behavior from simple local rules applied to 
    a 2D grid of "live" and "dead" cells.

Complexity Analysis:
    - Time Complexity: O(G * W * H) where G is generations, W is width, H is height.
    - Space Complexity: O(W * H) to store the grid and its next state.

Rules:
    1. Any live cell with fewer than two live neighbors dies (underpopulation).
    2. Any live cell with two or three live neighbors lives on.
    3. Any live cell with more than three live neighbors dies (overpopulation).
    4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
"""

import time
import os
from typing import List


class GameOfLifeService:
    """
    A service class for local rule-based cellular automata (Game of Life).
    """

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, r: int, c: int, val: int):
        """Sets the state of a specific cell."""
        if 0 <= r < self.rows and 0 <= c < self.cols:
            self.grid[r][c] = val

    def get_neighbors(self, r: int, c: int) -> int:
        """Counts the number of live neighbors for a cell."""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nr, nc = r + i, c + j
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    count += self.grid[nr][nc]
        return count

    def next_generation(self):
        """Computes the next state of the grid according to Conway's rules."""
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.get_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if neighbors in [2, 3]:
                        new_grid[r][c] = 1
                else:
                    if neighbors == 3:
                        new_grid[r][c] = 1
        self.grid = new_grid

    def render_frame(self) -> str:
        """Returns a string representation of the current grid."""
        output = []
        for row in self.grid:
            output.append(" ".join(["■" if cell else "." for cell in row]))
        return "\n".join(output)


def main():
    """
    Demonstrates the Game of Life evolution.
    """
    print("--- Conway's Game of Life Service Demo ---")
    
    rows, cols = 15, 30
    service = GameOfLifeService(rows, cols)
    
    # Initialize with a "Glider" pattern
    glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    for r, c in glider:
        service.set_cell(r, c, 1)
        
    # Initialize with a "Blinker" pattern
    blinker = [(10, 10), (10, 11), (10, 12)]
    for r, c in blinker:
        service.set_cell(r, c, 1)

    generations = 10
    print(f"Evolving for {generations} generations...")
    
    output_log = []
    for g in range(generations):
        frame = f"\nGeneration {g}:\n" + service.render_frame()
        print(frame)
        output_log.append(frame)
        service.next_generation()
        # time.sleep(0.3) # Slow down for terminal visibility if running interactively
        
    print("\n--- Evolution Complete ---")


if __name__ == "__main__":
    main()

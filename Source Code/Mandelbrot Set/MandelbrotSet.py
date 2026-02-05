"""
File: MandelbrotSet.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Mandelbrot Set visualization using iterative 
    complexity analysis. It maps complex plane coordinates to escape-time 
    values and generates a numerical representation of the famous fractal.

Complexity Analysis:
    - Time Complexity: O(width * height * max_iter) where each pixel is 
      iteratively processed up to a maximum depth.
    - Space Complexity: O(width * height) to store the escape-time grid.

Logic:
    1. Define a region in the complex plane (Real and Imaginary axes).
    2. For each point c = x + iy:
       a. Initialize z = 0.
       b. Iteratively apply z = z^2 + c.
       c. Check if |z| > 2 (divergence).
       d. Record the iteration count at which z escapes or max_iter is reached.
    3. Generate a textual or image-based representation of the resulting values.
"""

from typing import List


class MandelbrotService:
    """
    A service class for generating Mandelbrot set escape-time data.
    """

    def __init__(self, width: int = 80, height: int = 40, max_iter: int = 100):
        self.width = width
        self.height = height
        self.max_iter = max_iter

    def compute(self, x_min: float, x_max: float, y_min: float, y_max: float) -> List[List[int]]:
        """
        Computes the escape-time values for a grid on the complex plane.
        """
        grid = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                # Map pixel to complex plane
                c = complex(
                    x_min + (w / self.width) * (x_max - x_min),
                    y_min + (h / self.height) * (y_max - y_min)
                )
                
                z = 0j
                iteration = 0
                while abs(z) <= 2 and iteration < self.max_iter:
                    z = z*z + c
                    iteration += 1
                row.append(iteration)
            grid.append(row)
        return grid

    def render_ascii(self, grid: List[List[int]]) -> str:
        """
        Renders the Mandelbrot grid as ASCII art for terminal output.
        """
        chars = "@%#*+=-:. "
        output = []
        for row in grid:
            line = "".join(chars[min(int(val / self.max_iter * (len(chars)-1)), len(chars)-1)] for val in row)
            output.append(line)
        return "\n".join(output)


def main():
    """
    Demonstrates the Mandelbrot Set calculation.
    """
    print("--- Mandelbrot Set Visualization Service Demo ---")
    
    # Standard view of the Mandelbrot Set
    width, height = 80, 40
    service = MandelbrotService(width, height, max_iter=50)
    
    print(f"Computing Mandelbrot Set (Dimensions: {width}x{height}, Max Iterations: {service.max_iter})...")
    
    # Boundary: Real [-2.0, 0.5], Imaginary [-1.0, 1.0]
    grid = service.compute(-2.0, 0.5, -1.0, 1.0)
    
    print("\nVisual Representation (ASCII Mapping):")
    print(service.render_ascii(grid))
    
    print("\nCorner Data Samples (Iteration Counts):")
    print(f"  Top-Left: {grid[0][0]}")
    print(f"  Center: {grid[height//2][width//2]}")
    print(f"  Bottom-Right: {grid[-1][-1]}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

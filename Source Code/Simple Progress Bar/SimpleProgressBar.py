"""
File: SimpleProgressBar.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a terminal-based progress bar utility. It utilizes 
    carriage return escape sequences to perform in-place buffer updates, 
    providing a non-intrusive visual representation of iterative task 
    completion states within a command-line interface.

Complexity Analysis:
    - Time Complexity: O(1) for each update operation.
    - Space Complexity: O(1) auxiliary space, as it manages a fixed-length 
      string buffer for the terminal display.

Logic:
    1. Calculate the completion ratio based on the current count and total.
    2. Determine the filled length of the progress bar using a predefined 
       maximum character width (e.g., 60 characters).
    3. Generate a string representation consisting of 'filled' symbols (=) 
       and 'empty' symbols (-).
    4. Construct a formatted output string containing the progress bar, 
       percentage, and optional suffixes.
    5. Write the string to sys.stdout followed by a carriage return (\r).
    6. Flush the output stream to ensure immediate terminal rendering without 
       advancing to a new line.
"""

import sys
import time
from typing import Optional


class ProgressBarService:
    """
    A service class for generating and managing terminal progress bars.
    """

    def __init__(self, total: int, bar_length: int = 60):
        """
        Initializes the progress bar service.
        
        Args:
            total: The total number of iterations or units of work.
            bar_length: The visual width of the progress bar in characters.
        """
        self.total = total
        self.bar_length = bar_length

    def update(self, current: int, suffix: str = "") -> None:
        """
        Calculates and renders the current progress state to the terminal.
        
        Args:
            current: The current iteration count.
            suffix: An optional string to append to the progress display.
        """
        # Ensure we don't divide by zero
        if self.total <= 0:
            return

        # Calculate the ratio and filled portion of the bar
        ratio = float(current) / float(self.total)
        filled_length = int(round(self.bar_length * ratio))
        percent = round(100.0 * ratio, 1)

        # Construct the progress bar string
        bar = '=' * filled_length + '-' * (self.bar_length - filled_length)

        # Write to stdout with carriage return for in-place updates
        # format: [==========] 100.0% ...suffix
        sys.stdout.write(f'[{bar}] {percent}% ...{suffix}\r')
        sys.stdout.flush()


def main():
    """
    Demonstrates the scholarly Simple Progress Bar implementation.
    """
    print("--- Simple Progress Bar Service Demo ---")
    
    total_steps = 10
    service = ProgressBarService(total=total_steps)
    
    # Simulate a time-consuming iterative task
    for i in range(total_steps + 1):
        service.update(i, suffix="Processing Output")
        time.sleep(0.1)  # Minimal sleep for demonstration performance
    
    print("\nTask Completion: Sequence Terminated.")


if __name__ == "__main__":
    main()

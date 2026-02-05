"""
File: StopWatch.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a terminal-based stopwatch utility utilizing 
    high-resolution time measurement. It demonstrates epoch-based timing, 
    delta computation, and user-driven state transitions for measuring 
    elapsed durations with sub-second precision.

Complexity Analysis:
    - Time Complexity: O(1) for start/stop operations.
    - Space Complexity: O(1) auxiliary space for timestamp storage.

Logic:
    1. Initialize the stopwatch in a stopped state.
    2. On start command, record the current epoch time as the start timestamp.
    3. On stop command, record the current epoch time as the end timestamp.
    4. Calculate elapsed time as the difference between end and start timestamps.
    5. Format and display the elapsed duration with configurable precision.
    6. Support lap recording and reset functionality for extended use cases.
"""

import time
from typing import List, Optional


class StopWatchService:
    """
    A service class for high-precision elapsed time measurement.
    """

    def __init__(self, precision: int = 2):
        """
        Initializes the stopwatch service.
        
        Args:
            precision: Decimal places for elapsed time display.
        """
        self.precision = precision
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.laps: List[float] = []
        self.is_running: bool = False

    def start(self) -> None:
        """
        Starts the stopwatch by recording the current epoch time.
        """
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            print("Stopwatch Started.")

    def stop(self) -> float:
        """
        Stops the stopwatch and calculates elapsed time.
        
        Returns:
            The elapsed time in seconds.
        """
        if self.is_running:
            self.end_time = time.time()
            self.is_running = False
            elapsed = self.end_time - self.start_time
            print(f"Stopwatch Stopped.")
            print(f"Elapsed Time: {round(elapsed, self.precision)} seconds")
            return elapsed
        return 0.0

    def lap(self) -> float:
        """
        Records a lap time without stopping the stopwatch.
        
        Returns:
            The current lap time in seconds.
        """
        if self.is_running and self.start_time:
            lap_time = time.time() - self.start_time
            self.laps.append(lap_time)
            print(f"Lap {len(self.laps)}: {round(lap_time, self.precision)} seconds")
            return lap_time
        return 0.0

    def reset(self) -> None:
        """
        Resets the stopwatch to its initial state.
        """
        self.start_time = None
        self.end_time = None
        self.laps.clear()
        self.is_running = False
        print("Stopwatch Reset.")


def main():
    """
    Demonstrates the scholarly Stop Watch implementation.
    """
    print("--- Stop Watch Service Demo ---")
    print()
    
    service = StopWatchService(precision=2)
    
    # Start the stopwatch
    service.start()
    
    # Simulate some work with lap recordings
    time.sleep(0.5)
    service.lap()
    
    time.sleep(0.3)
    service.lap()
    
    time.sleep(0.2)
    
    # Stop and get total elapsed time
    total = service.stop()
    
    print()
    print(f"Total Laps Recorded: {len(service.laps)}")
    print(f"Final Elapsed Time: {round(total, 2)} seconds")
    print("Demo Complete.")


if __name__ == "__main__":
    main()

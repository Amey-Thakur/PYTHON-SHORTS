"""
File: Timer.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a countdown timer with configurable duration and 
    display format. It demonstrates time manipulation, in-place terminal 
    updates using carriage return, and modular arithmetic for time conversion.

Complexity Analysis:
    - Time Complexity: O(t) where t is the countdown duration in seconds.
    - Space Complexity: O(1) constant space usage.

Logic:
    1. Accept duration in seconds from user.
    2. Convert seconds to minutes:seconds format using divmod.
    3. Display countdown with in-place update using carriage return.
    4. Sleep for 1 second between updates.
    5. Signal completion when countdown reaches zero.
"""

import time
from typing import Callable, Optional


class TimerService:
    """
    A service class for countdown timer functionality.
    """

    def __init__(self, callback: Optional[Callable[[], None]] = None):
        """
        Initializes the timer service.
        
        Args:
            callback: Optional function to call when timer completes.
        """
        self.callback = callback
        self.is_running: bool = False
        self.remaining: int = 0

    def countdown(
        self,
        seconds: int,
        show_hours: bool = False,
        message: str = "Time Up!"
    ) -> None:
        """
        Runs a countdown timer.
        
        Args:
            seconds: Duration in seconds.
            show_hours: If True, display hours:minutes:seconds format.
            message: Message to display when timer completes.
        """
        if seconds <= 0:
            print("Duration must be positive.")
            return

        self.remaining = seconds
        self.is_running = True

        print(f"Starting countdown: {self._format_time(seconds, show_hours)}")

        while self.remaining > 0 and self.is_running:
            display = self._format_time(self.remaining, show_hours)
            print(f"\r{display}", end="", flush=True)
            time.sleep(1)
            self.remaining -= 1

        print(f"\r{message}{'':10}")
        self.is_running = False

        if self.callback:
            self.callback()

    def _format_time(self, seconds: int, show_hours: bool = False) -> str:
        """
        Formats seconds into a time string.
        
        Args:
            seconds: Number of seconds.
            show_hours: Whether to include hours.
            
        Returns:
            Formatted time string (HH:MM:SS or MM:SS).
        """
        if show_hours:
            hours, remainder = divmod(seconds, 3600)
            mins, secs = divmod(remainder, 60)
            return f"{hours:02d}:{mins:02d}:{secs:02d}"
        else:
            mins, secs = divmod(seconds, 60)
            return f"{mins:02d}:{secs:02d}"

    def stop(self) -> None:
        """Stops the running timer."""
        self.is_running = False

    @staticmethod
    def parse_time_string(time_str: str) -> int:
        """
        Parses a time string to seconds.
        
        Args:
            time_str: Time in format "MM:SS" or "HH:MM:SS" or just seconds.
            
        Returns:
            Total seconds.
        """
        parts = time_str.split(':')
        if len(parts) == 1:
            return int(parts[0])
        elif len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        elif len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        return 0


def main():
    """
    Demonstrates the scholarly Timer implementation.
    """
    print("--- Timer Service Demo ---\n")
    
    service = TimerService()
    
    # Demo with a short countdown
    demo_seconds = 5
    print(f"Demo: {demo_seconds} second countdown\n")
    
    service.countdown(demo_seconds, message="Timer Complete!")
    
    print("\n--- Demo Complete ---")
    print("\nUsage: Enter time in seconds or MM:SS format")


if __name__ == "__main__":
    main()
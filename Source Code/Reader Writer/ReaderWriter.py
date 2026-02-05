"""
File: ReaderWriter.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the classic Readers-Writers synchronization problem 
    using mutex-based locking. It demonstrates concurrent access to shared 
    resources where multiple readers can read simultaneously, but writers 
    require exclusive access to prevent data races and ensure consistency.

Complexity Analysis:
    - Time Complexity: O(1) for each read/write operation (excluding lock contention).
    - Space Complexity: O(1) auxiliary space for the shared state and lock.

Logic:
    1. Initialize a shared variable and a mutex lock for synchronization.
    2. Define a Reader function that acquires the lock, reads the shared data, 
       and releases the lock.
    3. Define a Writer function that acquires the lock, modifies the shared data, 
       and releases the lock.
    4. Spawn multiple threads randomly assigned as readers or writers.
    5. Use thread joining to ensure all operations complete before termination.
    6. The mutex ensures mutual exclusion, preventing concurrent write conflicts.
"""

import threading
import random
from typing import List


class ReaderWriterService:
    """
    A service class for demonstrating the Readers-Writers synchronization problem.
    """

    def __init__(self):
        self.shared_data: int = 0
        self.lock = threading.Lock()
        self.threads: List[threading.Thread] = []

    def read(self, reader_id: int) -> None:
        """
        Performs a read operation on the shared data.
        
        Args:
            reader_id: Identifier for the reader thread.
        """
        print(f"Reader {reader_id}: Attempting to acquire lock...")
        self.lock.acquire()
        try:
            print(f"Reader {reader_id}: Lock acquired. Reading shared data: {self.shared_data}")
        finally:
            self.lock.release()
            print(f"Reader {reader_id}: Lock released.")

    def write(self, writer_id: int) -> None:
        """
        Performs a write operation on the shared data.
        
        Args:
            writer_id: Identifier for the writer thread.
        """
        print(f"Writer {writer_id}: Attempting to acquire lock...")
        self.lock.acquire()
        try:
            self.shared_data += 1
            print(f"Writer {writer_id}: Lock acquired. Updated shared data to: {self.shared_data}")
        finally:
            self.lock.release()
            print(f"Writer {writer_id}: Lock released.")

    def execute(self, iterations: int = 10) -> None:
        """
        Executes a series of random read/write operations.
        
        Args:
            iterations: Number of threads to spawn.
        """
        print(f"--- Reader-Writer Service Demo ---")
        print(f"Initial Shared Data: {self.shared_data}")
        print(f"Total Iterations: {iterations}")
        print()

        for i in range(iterations):
            if random.randint(0, 100) > 50:
                thread = threading.Thread(target=self.read, args=(i,))
            else:
                thread = threading.Thread(target=self.write, args=(i,))
            self.threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in self.threads:
            thread.join()

        print()
        print(f"Final Shared Data: {self.shared_data}")
        print("Execution Complete: All threads terminated.")


def main():
    """
    Demonstrates the scholarly Reader-Writer implementation.
    """
    service = ReaderWriterService()
    service.execute(iterations=10)


if __name__ == "__main__":
    main()

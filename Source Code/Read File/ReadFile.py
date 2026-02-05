"""
File: ReadFile.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module provides a scholarly implementation of file reading operations 
    utilizing Python's context management protocol. It ensures deterministic 
    resource deallocation and memory efficiency through the use of stream-based 
    generators.

Complexity Analysis:
    - Time Complexity: O(N), where N is the total number of bytes in the file.
    - Space Complexity: O(k), where k is the length of the longest line, 
      facilitated by lazy evaluation.

Logic:
    1. Validate the existence of the target file path.
    2. Open a file stream using a context manager (`with` statement) to handle 
       system file descriptors safely.
    3. Iterate through the file handle as a stream to avoid loading the entire 
       content into primary memory.
    4. Yield each line stripped of trailing whitespace to the consumer.
    5. Automatically close the stream upon completion or exception through the 
       __exit__ method.
"""

import os
from typing import Generator


class FileOperationService:
    """
    A service class for robust file reading operations.
    
    This class encapsulates the logic for stream-based file processing,
    utilizing Python's context management protocol for resource safety.
    """

    @staticmethod
    def stream_lines(file_path: str) -> Generator[str, None, None]:
        """
        Generates lines from a file using a context manager.
        
        Args:
            file_path: The absolute or relative path to the target file.
            
        Yields:
            The raw string content of each line in the file.
            
        Raises:
            FileNotFoundError: If the specified path does not exist.
            IOError: If an error occurs during the read operation.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at {file_path} was not found.")

        try:
            with open(file_path, "r", encoding="utf-8") as file_stream:
                for line in file_stream:
                    yield line.strip()
        except IOError as error:
            print(f"Mathematical Error in I/O Stream: {error}")
            raise


def main():
    """
    Demonstrates the scholarly file reading implementation.
    """
    print("--- File Operation Service Demo ---")
    
    # Define a path within the local Output directory
    demo_file = os.path.join(os.path.dirname(__file__), "Output", "sample_input.txt")
    
    # Ensure the Output directory exists
    os.makedirs(os.path.dirname(demo_file), exist_ok=True)
    
    # Create the demonstration input file with scholarly metadata
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write("Repository: PYTHON-SHORTS\n")
        f.write("Authors: Amey Thakur & Mega Satish\n")
        f.write("Theoretical Foundation: Buffer Management\n")
        f.write("Status: Deterministic Sequential Access Verified\n")
        f.write("Message: This implementation ensures efficient memory utilization for large datasets.")

    print(f"Reading from: {demo_file}\n")
    
    try:
        reader = FileOperationService()
        for idx, content in enumerate(reader.stream_lines(demo_file), 1):
            print(f"Buffer Row {idx}: {content}")
    except Exception as e:
        print(f"Execution Failure: {e}")


if __name__ == "__main__":
    main()

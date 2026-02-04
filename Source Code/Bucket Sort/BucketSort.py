"""
File: BucketSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    Bucket Sort is a distribution sort that works by partitioning an 
    array into several buckets. Each bucket is then sorted individually, 
    either using a different sorting algorithm or by recursively 
    applying the bucket sort. This implementation handles floating-point 
    numbers in the range [0, 1).

Complexity Analysis:
    - Time Complexity: O(N) average case (if inputs are uniformly distributed); 
      Worst case O(N^2) if all elements go into one bucket.
    - Space Complexity: O(N + K), where N is elements and K is buckets.

Logic:
    1. Create K empty buckets (where K is typically equal to N).
    2. Insert each element into a bucket calculated based on its value.
    3. Sort each individual bucket (using built-in Timsort in this case).
    4. Concatenate all sorted buckets into the final result.
"""

from typing import List

def bucket_sort(arr: List[float]) -> List[float]:
    """
    Sorts an array of floating point numbers in range [0, 1).

    Args:
        arr (List[float]): The list of floats to be sorted.

    Returns:
        List[float]: The sorted list.
    """
    if not arr:
        return []

    n = len(arr)
    # 1. Create n empty buckets
    buckets: List[List[float]] = [[] for _ in range(n)]

    # 2. Put elements in different buckets
    for val in arr:
        index = int(n * val)
        # Ensure index is within range [0, n-1]
        if index < 0:
            index = 0
        elif index >= n:
            index = n - 1
        buckets[index].append(val)

    # 3. Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

def run_bucket_sort_demo() -> None:
    """Demonstrates Bucket Sort."""
    print("--- Python Shorts: Bucket Sort Distribution Demo ---")
    data = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"Original: {data}")
    sorted_data = bucket_sort(data)
    print(f"Sorted  : {sorted_data}")

if __name__ == '__main__':
    run_bucket_sort_demo()

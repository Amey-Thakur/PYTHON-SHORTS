"""
File: KnapsackProblem.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the 0/1 Knapsack Problem using Dynamic Programming. 
    It solves the classic optimization problem of selecting items with given 
    weights and values to maximize total value without exceeding a weight limit.

Complexity Analysis:
    - Time Complexity: O(n * W) where n is number of items and W is capacity.
    - Space Complexity: O(n * W) for the DP table (can be optimized to O(W)).

Logic:
    1. Create a 2D DP table of size (n+1) x (capacity+1).
    2. Iterate through each item and each possible weight capacity.
    3. If item weight <= current capacity:
       Take max of (value with item + value of remaining capacity, value without item).
    4. Else, take the value without the item.
    5. Trace back through the table to identify which items were selected.
"""

from typing import List, Tuple, Dict


class KnapsackService:
    """
    A service class for solving the 0/1 Knapsack optimization problem.
    """

    def solve(self, weights: List[int], values: List[int], capacity: int) -> Dict:
        """
        Solves the 0/1 Knapsack problem.
        
        Args:
            weights: List of weights of items.
            values: List of values of items.
            capacity: Maximum weight capacity of the knapsack.
            
        Returns:
            Dictionary containing max_value and indices of selected items.
        """
        n = len(weights)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]

        # Backtrack to find selected items
        selected_indices = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                selected_indices.append(i-1)
                w -= weights[i-1]

        return {
            "max_value": dp[n][capacity],
            "selected_indices": selected_indices[::-1],
            "total_weight": capacity - w
        }


def main():
    """
    Demonstrates the 0/1 Knapsack Problem implementation.
    """
    print("--- 0/1 Knapsack Problem Service Demo ---")
    
    # Sample items: (Value, Weight)
    items = [
        {"name": "Laptop", "value": 1000, "weight": 3},
        {"name": "Camera", "value": 500, "weight": 1},
        {"name": "Phone", "value": 700, "weight": 1},
        {"name": "Watch", "value": 200, "weight": 1}
    ]
    
    capacity = 4
    weights = [item["weight"] for item in items]
    values = [item["value"] for item in items]
    
    service = KnapsackService()
    result = service.solve(weights, values, capacity)
    
    print(f"Knapsack Capacity: {capacity}kg")
    print("\nItems Available:")
    for i, item in enumerate(items):
        print(f"  {i}. {item['name']} (Value: ${item['value']}, Weight: {item['weight']}kg)")
        
    print(f"\nOptimization Result:")
    print(f"  Maximum Value: ${result['max_value']}")
    print(f"  Total Weight Used: {result['total_weight']}kg")
    print(f"  Selected Items:")
    for idx in result['selected_indices']:
        print(f"    - {items[idx]['name']}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

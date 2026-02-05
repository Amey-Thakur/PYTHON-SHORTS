"""
File: MonteCarloSimulation.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Monte Carlo Simulation for estimating the 
    mathematical constant Pi (π). It demonstrates probabilistic sampling 
    and the law of large numbers through random coordinate projection.

Complexity Analysis:
    - Time Complexity: O(n) where n is the number of random samples.
    - Space Complexity: O(1) as it only tracks counters for hits and trials.

Logic:
    1. Define a unit square [0, 1] x [0, 1] containing a quadrant of a unit circle.
    2. Generate N random points (x, y) within the square.
    3. Check if the point lies within the circle: x^2 + y^2 <= 1.
    4. The ratio of points inside the circle to total points approaches π/4.
    5. Estimate π = 4 * (Hits / Total).
"""

import random
from typing import Tuple, Dict


class MonteCarloPiService:
    """
    A service class for performing Monte Carlo simulations to estimate Pi.
    """

    def __init__(self, samples: int = 100000):
        self.samples = samples

    def estimate_pi(self) -> Dict[str, float]:
        """
        Executes the simulation and returns statistical results.
        """
        hits = 0
        for _ in range(self.samples):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            
            if x**2 + y**2 <= 1:
                hits += 1
        
        estimated_pi = 4 * (hits / self.samples)
        error = abs(estimated_pi - 3.141592653589793)
        
        return {
            "samples": self.samples,
            "hits": hits,
            "estimated_pi": estimated_pi,
            "error": error
        }


def main():
    """
    Demonstrates the Monte Carlo Pi estimation.
    """
    print("--- Monte Carlo Simulation Service Demo ---")
    
    sample_sizes = [1000, 10000, 100000, 1000000]
    
    print(f"{'Samples':<12} | {'Estimated Pi':<15} | {'Error':<15}")
    print("-" * 45)
    
    for size in sample_sizes:
        service = MonteCarloPiService(size)
        result = service.estimate_pi()
        print(f"{result['samples']:<12} | {result['estimated_pi']:<15.6f} | {result['error']:<15.8f}")
        
    print("\nObservation: As the sample size increases, the error generally decreases (Law of Large Numbers).")
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

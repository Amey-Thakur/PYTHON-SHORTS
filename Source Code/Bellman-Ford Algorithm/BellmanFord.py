"""
File: BellmanFord.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Bellman-Ford Algorithm for finding the shortest 
    paths from a single source vertex to all other vertices in a weighted 
    digraph. Unlike Dijkstra's, it supports negative edge weights and 
    detects negative weight cycles.

Complexity Analysis:
    - Time Complexity: O(V * E) where V is the number of vertices and E is edges.
    - Space Complexity: O(V) to store the distances and predecessors.

Logic:
    1. Initialize distances from source to all vertices as infinity, source as 0.
    2. Relax all edges |V| - 1 times. For an edge (u, v) with weight w, if 
       dist(u) + w < dist(v), then dist(v) = dist(u) + w.
    3. Final Check: Relax all edges one more time. If any distance can still 
       be reduced, a negative weight cycle exists.
    4. Reconstruct the shortest path using a predecessor mapping.
"""

from typing import List, Dict, Tuple, Optional, Union


class BellmanFordService:
    """
    A service class for computing shortest paths using the Bellman-Ford algorithm.
    """

    def __init__(self, vertices: int):
        self.V = vertices
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, u: int, v: int, w: int) -> None:
        """Adds a directed edge from u to v with weight w."""
        self.edges.append((u, v, w))

    def compute_shortest_path(self, src: int) -> Dict[str, Union[Dict[int, float], Dict[int, Optional[int]], bool]]:
        """
        Computes shortest paths from source.
        
        Returns:
            Dictionary containing distances, predecessors, and cycle detection status.
        """
        distances = {i: float('inf') for i in range(self.V)}
        predecessors = {i: None for i in range(self.V)}
        distances[src] = 0

        # Relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    predecessors[v] = u

        # Check for negative weight cycles
        has_cycle = False
        for u, v, w in self.edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                has_cycle = True
                break

        return {
            "distances": distances,
            "predecessors": predecessors,
            "has_negative_cycle": has_cycle
        }

    def get_path(self, predecessors: Dict[int, Optional[int]], target: int) -> List[int]:
        """Reconstructs the path to a target vertex."""
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = predecessors[current]
        return path[::-1]


def main():
    """
    Demonstrates the Bellman-Ford Algorithm implementation.
    """
    print("--- Bellman-Ford Algorithm Service Demo ---")
    
    # Case 1: Standard Graph
    V = 5
    service = BellmanFordService(V)
    service.add_edge(0, 1, -1)
    service.add_edge(0, 2, 4)
    service.add_edge(1, 2, 3)
    service.add_edge(1, 3, 2)
    service.add_edge(1, 4, 2)
    service.add_edge(3, 2, 5)
    service.add_edge(3, 1, 1)
    service.add_edge(4, 3, -3)

    print(f"Graph with {V} vertices and {len(service.edges)} edges initialized.")
    result = service.compute_shortest_path(0)

    if result["has_negative_cycle"]:
        print("Error: Graph contains a negative weight cycle!")
    else:
        print("\nShortest Distances from Source (Node 0):")
        for node, dist in result["distances"].items():
            path = service.get_path(result["predecessors"], node)
            print(f"  Node {node}: Distance = {dist}, Path = {' -> '.join(map(str, path))}")

    # Case 2: Negative Cycle Detection
    print("\n--- Negative Cycle Test ---")
    cycle_service = BellmanFordService(3)
    cycle_service.add_edge(0, 1, 1)
    cycle_service.add_edge(1, 2, -1)
    cycle_service.add_edge(2, 0, -1)  # Cycle: 0->1->2->0 weight = 1 + -1 + -1 = -1
    
    cycle_result = cycle_service.compute_shortest_path(0)
    if cycle_result["has_negative_cycle"]:
        print("Success: Negative weight cycle correctly detected.")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

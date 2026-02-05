"""
File: DijkstraAlgorithm.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements Dijkstra's Algorithm for finding the shortest paths 
    between nodes in a weighted graph with non-negative edge weights. 
    It demonstrates the use of a priority queue for greedy optimization.

Complexity Analysis:
    - Time Complexity: O((V + E) log V) with a binary heap priority queue.
    - Space Complexity: O(V + E) to store the adjacency list and distances.

Logic:
    1. Initialize distances to all nodes as infinity, start node as 0.
    2. Use a priority queue to always explore the node with the smallest 
       known distance.
    3. For the current node, relax all outgoing edges: if a shorter path is 
       found, update the distance and push to the priority queue.
    4. Maintain a mapping of predecessors to reconstruct the shortest path.
"""

import heapq
from typing import Dict, List, Tuple, Optional


class DijkstraService:
    """
    A service class for computing shortest paths using Dijkstra's Algorithm.
    """

    def __init__(self):
        """Initializes an empty graph."""
        self.adjacency_list: Dict[int, List[Tuple[int, int]]] = {}

    def add_edge(self, u: int, v: int, weight: int) -> None:
        """
        Adds an undirected edge with a weight.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def compute_shortest_path(self, start: int, end: int) -> Tuple[Optional[List[int]], int]:
        """
        Computes the shortest path and distance between two nodes.
        
        Returns:
            Tuple of (Path as list of nodes, Total distance).
        """
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start] = 0
        
        priority_queue = [(0, start)]
        predecessors = {node: None for node in self.adjacency_list}
        
        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)
            
            if current_distance > distances[u]:
                continue
                
            if u == end:
                break
                
            for v, weight in self.adjacency_list.get(u, []):
                distance = current_distance + weight
                
                if distance < distances[v]:
                    distances[v] = distance
                    predecessors[v] = u
                    heapq.heappush(priority_queue, (distance, v))
                    
        return self._reconstruct_path(predecessors, start, end), distances[end]

    def _reconstruct_path(self, predecessors: Dict[int, Optional[int]], start: int, end: int) -> Optional[List[int]]:
        """Reconstructs the path from start to end."""
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]
            if current == start:
                path.append(start)
                break
        
        if not path or path[-1] != start:
            return None
            
        return path[::-1]


def main():
    """
    Demonstrates the Dijkstra's Algorithm implementation.
    """
    print("--- Dijkstra's Algorithm Service Demo ---")
    
    service = DijkstraService()
    edges = [
        (0, 1, 4), (0, 7, 8),
        (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 8, 2), (2, 5, 4),
        (3, 4, 9), (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1), (6, 8, 6),
        (7, 8, 7)
    ]
    
    for u, v, w in edges:
        service.add_edge(u, v, w)
        
    start_node = 0
    end_node = 4
    
    print(f"Finding shortest path from node {start_node} to {end_node}...")
    path, distance = service.compute_shortest_path(start_node, end_node)
    
    if path:
        print(f"Path Found: {' -> '.join(map(str, path))}")
        print(f"Total Distance: {distance}")
    else:
        print("No path found.")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

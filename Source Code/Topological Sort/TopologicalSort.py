"""
File: TopologicalSort.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements Topological Sort using Depth-First Search (DFS) 
    on a Directed Acyclic Graph (DAG). Topological ordering is essential for 
    task scheduling, dependency resolution, and compilation order determination.

Complexity Analysis:
    - Time Complexity: O(V + E) where V = vertices, E = edges.
    - Space Complexity: O(V) for the visited array and recursion stack.

Logic:
    1. Build adjacency list representation of the directed graph.
    2. Perform DFS from each unvisited vertex.
    3. After visiting all neighbors, push current vertex to front of result.
    4. The resulting order satisfies all edge constraints (u before v for edge u→v).
    5. Only valid for DAGs; cycles make topological sort impossible.
"""

from typing import List, Dict, Set, Optional


class TopologicalSortService:
    """
    A service class for performing topological sort on directed graphs.
    """

    def __init__(self):
        """Initializes an empty graph."""
        self.adjacency_list: Dict[int, List[int]] = {}
        self.vertex_count: int = 0

    def add_vertex(self, vertex: int) -> None:
        """
        Adds a vertex to the graph.
        
        Args:
            vertex: The vertex identifier.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertex_count += 1

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        Adds a directed edge from one vertex to another.
        
        Args:
            from_vertex: Source vertex.
            to_vertex: Destination vertex.
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adjacency_list[from_vertex].append(to_vertex)

    def sort(self) -> Optional[List[int]]:
        """
        Performs topological sort using DFS.
        
        Returns:
            List of vertices in topological order, or None if cycle detected.
        """
        visited: Set[int] = set()
        rec_stack: Set[int] = set()  # For cycle detection
        result: List[int] = []

        def dfs(vertex: int) -> bool:
            """Recursive DFS helper. Returns False if cycle detected."""
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor in rec_stack:
                    return False  # Cycle detected
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False

            rec_stack.remove(vertex)
            result.insert(0, vertex)
            return True

        for vertex in self.adjacency_list:
            if vertex not in visited:
                if not dfs(vertex):
                    return None  # Graph has a cycle

        return result

    def print_graph(self) -> None:
        """Prints the adjacency list representation of the graph."""
        print("Graph Adjacency List:")
        for vertex, neighbors in self.adjacency_list.items():
            neighbor_str = ' -> '.join(map(str, neighbors)) if neighbors else '(no outgoing edges)'
            print(f"  {vertex} -> {neighbor_str}")


def main():
    """
    Demonstrates the scholarly Topological Sort implementation.
    """
    print("--- Topological Sort Service Demo ---\n")

    service = TopologicalSortService()

    # Build sample DAG (task dependencies)
    edges = [
        (5, 2), (5, 0),
        (4, 0), (4, 1),
        (2, 3), (3, 1)
    ]

    print("Adding edges:")
    for u, v in edges:
        print(f"  {u} -> {v}")
        service.add_edge(u, v)

    print()
    service.print_graph()

    print("\nTopological Sort Result:")
    result = service.sort()

    if result:
        print(f"  Order: {' -> '.join(map(str, result))}")
        print("\nInterpretation: Tasks should be executed in this order")
        print("to satisfy all dependencies.")
    else:
        print("  Error: Graph contains a cycle (not a DAG)")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

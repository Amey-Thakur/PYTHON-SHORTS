"""
File: Graph.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of a Graph data structure using Adjacency Lists. 
    This module supports directed and undirected edges, weighted connections, 
    and fundamental traversal algorithms (Breadth-First Search and 
    Depth-First Search) within a discrete mathematical framework.

Mathematical Logic:
    A Graph G is defined as an ordered pair (V, E), where V is a set of 
    vertices and E ⊆ V × V is a set of edges. This implementation models 
    G using an Adjacency List representation, optimizing for sparse structures.
"""

from typing import Dict, List, Set, Optional, Any
from collections import deque

class Vertex:
    """Represents a discrete node within a graph structure."""
    def __init__(self, key: Any):
        self.key = key
        self.neighbors: Dict['Vertex', float] = {}

    def add_neighbor(self, neighbor: 'Vertex', weight: float = 0):
        """Establishes a weighted edge from this vertex to a neighbor."""
        self.neighbors[neighbor] = weight

    def get_connections(self) -> List['Vertex']:
        """Returns all adjacent vertices."""
        return list(self.neighbors.keys())

    def get_weight(self, neighbor: 'Vertex') -> Optional[float]:
        """Returns the weight of the edge to a specific neighbor."""
        return self.neighbors.get(neighbor)

    def __str__(self) -> str:
        return f"{self.key} -> {[x.key for x in self.neighbors]}"

class Graph:
    """Scholarly implementation of a Graph data structure $G = (V, E)$."""
    def __init__(self, directed: bool = True):
        self.vertices: Dict[Any, Vertex] = {}
        self.directed = directed

    def add_vertex(self, key: Any) -> Vertex:
        """Adds a vertex to the graph if it does not exist."""
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)
        return self.vertices[key]

    def add_edge(self, u: Any, v: Any, weight: float = 0):
        """Adds a weighted edge between two vertices."""
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        
        self.vertices[u].add_neighbor(self.vertices[v], weight)
        if not self.directed:
            self.vertices[v].add_neighbor(self.vertices[u], weight)

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        """Retrieves a vertex by its key identifier."""
        return self.vertices.get(key)

    def bfs(self, start_key: Any) -> List[Any]:
        """Performs a Breadth-First Search traversal."""
        start_node = self.get_vertex(start_key)
        if not start_node:
            return []
        
        visited: Set[Vertex] = {start_node}
        queue = deque([start_node])
        order = []
        
        while queue:
            curr = queue.popleft()
            order.append(curr.key)
            for neighbor in curr.get_connections():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start_key: Any) -> List[Any]:
        """Performs a Depth-First Search traversal (iterative)."""
        start_node = self.get_vertex(start_key)
        if not start_node:
            return []
        
        visited: Set[Vertex] = set()
        stack = [start_node]
        order = []
        
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                order.append(curr.key)
                # Push neighbors in reverse to maintain deterministic order
                for neighbor in reversed(curr.get_connections()):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def __iter__(self):
        return iter(self.vertices.values())

def run_graph_demo():
    """Execution demo with complex topological test vectors."""
    print("--- Python Shorts: Discrete Topology & Graph Theory ---")
    
    # Construct a directed weighted graph
    g = Graph(directed=True)
    edges = [('A', 'B', 5), ('A', 'C', 3), ('B', 'C', 2), ('C', 'D', 4), ('D', 'A', 1)]
    
    print("\n[Action]: Constructing Directed Weighted Graph...")
    for u, v, w in edges:
        g.add_edge(u, v, w)
        print(f"Edge Created: ({u}) --[{w}]--> ({v})")
    
    print("\n[Traversal]: Breadth-First Search (BFS) starting from A:")
    print(f"Order: {g.bfs('A')}")
    
    print("\n[Traversal]: Depth-First Search (DFS) starting from A:")
    print(f"Order: {g.dfs('A')}")
    
    print("\n[Topology]: Connectivity and Weight Verification:")
    for v in g:
        for neighbor in v.get_connections():
            print(f"({v.key}, {neighbor.key}) @ Weight: {v.get_weight(neighbor)}")

if __name__ == "__main__":
    run_graph_demo()

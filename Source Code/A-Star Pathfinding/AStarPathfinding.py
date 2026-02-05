"""
File: AStarPathfinding.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: February 5, 2026
License: MIT License

Description:
    This module implements the A* (A-Star) Pathfinding algorithm. It is an 
    informed search algorithm that uses heuristics to find the shortest path 
    between nodes in a graph or grid.

Complexity Analysis:
    - Time Complexity: O(E) = O(b^d) where b is the branching factor and d is depth.
    - Space Complexity: O(V) = O(b^d) to store the frontier and explored nodes.

Logic:
    1. Maintain a priority queue (open set) of nodes to be explored.
    2. f(n) = g(n) + h(n), where g(n) is the cost from start and h(n) is the heuristic.
    3. Heuristic used: Manhattan Distance (for grid-based L1 movement).
    4. Iteratively explore the node with the lowest f(n).
    5. Reconstruct the path once the goal is reached.
"""

import heapq
from typing import List, Tuple, Dict, Set, Optional


class AStarService:
    """
    A service class for A* Pathfinding on a 2D grid.
    """

    def __init__(self, grid: List[List[int]]):
        """
        Initializes the A* service with a grid.
        
        Args:
            grid: 2D list where 0 is walkable and 1 is an obstacle.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def heuristic(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        """
        Manhattan distance heuristic.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Returns valid 4-way neighbors (Up, Down, Left, Right).
        """
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0:
                neighbors.append((x, y))
        return neighbors

    def search(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Performs the A* search.
        
        Returns:
            List of coordinates representing the path, or None if no path exists.
        """
        open_set = []
        heapq.heappush(open_set, (0, start))
        
        came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
        g_score: Dict[Tuple[int, int], int] = {start: 0}
        
        while open_set:
            current_f, current = heapq.heappop(open_set)
            
            if current == goal:
                return self._reconstruct_path(came_from, current)
                
            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
                    
        return None

    def _reconstruct_path(
        self, 
        came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]], 
        current: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Reconstructs the path from goal to start.
        """
        path = []
        while current in came_from:
            path.append(current)
            prev = came_from[current]
            if prev is None:
                break
            current = prev
        return path[::-1]

    def display_grid_with_path(self, path: List[Tuple[int, int]]) -> str:
        """
        Returns a string representation of the grid with the path marked.
        """
        path_set = set(path)
        output = []
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) == path[0]:
                    row_str += "S "
                elif (r, c) == path[-1]:
                    row_str += "G "
                elif (r, c) in path_set:
                    row_str += "* "
                elif self.grid[r][c] == 1:
                    row_str += "# "
                else:
                    row_str += ". "
            output.append(row_str)
        return "\n".join(output)


def main():
    """
    Demonstrates the A* Pathfinding implementation.
    """
    print("--- A* Pathfinding Service Demo ---")
    
    # 0 = Path, 1 = Wall
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    service = AStarService(grid)
    path = service.search(start, goal)
    
    if path:
        print(f"Path Found (Length: {len(path)}):")
        print(service.display_grid_with_path(path))
        print("\nCoordinates:")
        print(" -> ".join(map(str, path)))
    else:
        print("No path found.")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

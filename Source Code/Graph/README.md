# Graph (Discrete Topology)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python Graph.py
```

## 1. Definition
A **Graph** is a non-linear data structure consisting of a set of vertices (or nodes) $V$ and a set of edges $E$ that connect pairs of vertices. This scholarly implementation utilizes **Adjacency Lists** to represent the topological relationships, providing efficiency for sparse graphs.

## 2. Mathematical Explanation
A graph $G$ is formally defined as an ordered pair:

$$
G = (V, E)
$$

Where:
- $V = \{v_1, v_2, \dots, v_n\}$ is the set of **Vertices**.
- $E \subseteq \{(u, v) \mid u, v \in V\}$ is the set of **Edges**.

### Weighted Directed Graphs
In this implementation, edges can be **Directed** (one-way) or **Undirected** (two-way), and may carry a scalar **Weight** $w(u, v)$ representing distance, cost, or capacity.

## 3. Computer Science Theory
- **Adjacency List Representation**: Stores each vertex as a key mapped to a list of its neighbors. This optimizes space for graphs where $|E| \ll |V|^2$.
- **Traversal Algorithms**:
    - **BFS (Breadth-First Search)**: Explores nodes layer by layer using a FIFO queue, guaranteed to find the shortest path in unweighted graphs.
    - **DFS (Depth-First Search)**: Explores as far as possible along each branch before backtracking, utilizing a LIFO stack.
- **Complexity**:
    - **Time Complexity**: $O(V + E)$ for both BFS and DFS.
    - **Space Complexity**: $O(V + E)$ to store the adjacency list and traversal state.

## 4. Python Implementation Logic
- **Object-Oriented Design**: Encapsulates $Vertex$ and $Graph$ as discrete entities, allowing for easy expansion (e.g., adding Dijkstra's or A* algorithms).
- **Atomic Operations**: Supports dynamic vertex and edge insertion with automatic handling of boundary conditions.

## 5. Visual Representation

### Topological Mapping & Logic Verification
![Graph Demo](Demo.png)

```mermaid
graph TD
    subgraph AdjacencyMapping ["Adjacency List Data Structure"]
        direction LR
        V1["Vertex A"] --- L1["[B:5, C:3]"]
        V2["Vertex B"] --- L2["[C:2]"]
        V3["Vertex C"] --- L3["[D:4]"]
        V4["Vertex D"] --- L4["[A:1]"]
    end
```

```mermaid
graph LR
    subgraph Topology ["Topological Graph View"]
        A["A"] -- 5 --> B["B"]
        A -- 3 --> C["C"]
        B -- 2 --> C
        C -- 4 --> D["D"]
        D -- 1 --> A
    end
```

```mermaid
flowchart TD
    Start["Start Traversal"] --> Type{"Method?"}
    Type -- BFS --> Queue["Use FIFO Queue"]
    Queue --> B1["Visit Start Node"]
    B1 --> B2["Enqueue Neighbors"]
    B2 --> B3["Pop & Mark Visited"]
    B3 --> B4{"Queue Empty?"}
    B4 -- No --> B2
    B4 -- Yes --> End["Finish"]

    Type -- DFS --> Stack["Use LIFO Stack"]
    Stack --> D1["Push Start Node"]
    D1 --> D2["Pop & Visit"]
    D2 --> D3["Push Neighbors"]
    D3 --> D4{"Stack Empty?"}
    D4 -- No --> D2
    D4 -- Yes --> End
```

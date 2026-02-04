# Doubly Linked List (Bidirectional Sequences)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python DoublyLinkedList.py
```

## 1. Definition
A **Doubly Linked List (DLL)** is a linear data structure where each element (node) contains a data field and two reference fields (pointers): one pointing to the previous node and another to the next node in the sequence. This bidirectional structure allows for efficient traversal in both directions.

## 2. Mathematical Explanation
A Doubly Linked List can be formalized as a set of nodes $V$ and a set of bidirectional relations $E$. Each node $n_i \in V$ is a tuple:

$$
n_i = (prev_i, data_i, next_i)
$$

Where:
- $prev_i$ refers to $n_{i-1}$ (or $\emptyset$ if $i=0$).
- $next_i$ refers to $n_{i+1}$ (or $\emptyset$ if $i=n$).
- The sequence maintains a total ordering from **Head** ($n_0$) to **Tail** ($n_n$).

## 3. Computer Science Theory
- **Memory Management**: Unlike contiguous arrays, list nodes are allocated dynamically in heap memory. The overhead of storing two pointers per node is traded for flexibility in dynamic sizing.
- **Pointer Integrity**: All mutation operations (Insert/Delete) must preserve the consistency of both `next` and `prev` pointers across adjacent nodes to avoid memory leaks or "broken" chains.
- **Complexity**:
    - **Time Complexity**: 
        - Access/Search: $O(n)$
        - Insertion/Deletion at ends: $O(1)$ (with Tail pointer)
        - Insertion/Deletion in middle: $O(n)$
    - **Space Complexity**: $O(n)$ proportional to the number of nodes.

## 4. Python Implementation Logic
- **Bidirectional Encapsulation**: Employs Head and Tail pointers to ensure terminal operations are constant-time $O(1)$.
- **In-place Reversal**: Implements a memory-efficient reversal algorithm that swaps pointers without duplicating node objects.
- **Iteration Strategy**: All traversals are implemented iteratively to prevent exhaustion of the recursion stack in environments with high memory-to-node ratios.

## 5. Visual Representation

### 5.1 Bidirectional Logic Check
![Doubly Linked List Demo](Demo.png)

### 5.2 Validation Scenarios
| Case ID | Operation | Input | Expected Output | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | **Initialization** | N/A | Empty state, size 0 | Verifies object creation. |
| **TC-02** | **Append** | `10`, `20` | `[10, 20]` (Forward) | Verifies tail injection logic. |
| **TC-03** | **Prepend** | `5` | `[5, 10, 20]` | Verifies head injection logic. |
| **TC-04** | **Reversal** | N/A | `[20, 10, 5]` | Verifies 'prev' pointer integrity. |
| **TC-05** | **Removal** | `10` | `[5, 20]` | Verifies node excision logic. |

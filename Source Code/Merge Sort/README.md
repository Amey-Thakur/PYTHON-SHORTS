# Merge Sort (Divide and Conquer & Stable Sorting)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python MergeSort.py
```

## 1. Definition
**Merge Sort** is an efficient, stable, comparison-based sorting algorithm. Most implementations produce a stable sort, meaning that the relative order of equal elements is preserved in the sorted output. It is a quintessential example of the **Divide and Conquer** algorithmic paradigm.

## 2. Mathematical Explanation
Merge Sort relies on the recursive decomposition of a problem into smaller instances of the same problem.

### Recurrence Relation
For an input of size $n$, the time complexity $T(n)$ is defined as:

$$
T(n) = 2T(n/2) + O(n)
$$

By the **Master Theorem**, this recurrence belongs to Case 2, where $a=2, b=2, d=1$. Since $a=b^d$, the total complexity is:

$$
O(n \log n)
$$

### Stability and Merging
The stability is guaranteed in the merging step. When two equal elements are compared (one from the left sub-array and one from the right), the implementation prioritizes the element from the left sub-array:
`if left[i] <= right[j]: ...`

## 3. Computer Science Theory
- **Auxiliary Space**: Unlike Heap Sort or Quick Sort, standard Merge Sort requires $O(n)$ auxiliary space to store the merged sub-arrays.
- **Cache Local Performance**: Merge Sort has excellent cache locality during the sequential merge process, making it suitable for external sorting (large datasets stored on disk).
- **Complexity**:
    - **Time Complexity**: $O(n \log n)$ (Best, Average, and Worst case).
    - **Space Complexity**: $O(n)$.

## 4. Python Implementation Logic
- **Recursive Splitting**: Uses Python's slice notation `[:middle]` and `[middle:]` for clear sub-array creation.
- **Pointer-Based Merging**: Avoids $O(n)$ list removals by maintaining index pointers, ensuring the merge step remains strictly linear.

## 5. Visual Representation

### Divide and Conquer Flow
```mermaid
flowchart TD
    A["Start: sort(dataset)"] --> B{"len(dataset) <= 1?"}
    B -- "Yes" --> C["Return dataset"]
    B -- "No" --> D["middle = n // 2"]
    D --> E["left_half = sort(dataset[:middle])"]
    D --> F["right_half = sort(dataset[middle:])"]
    E --> G["merge(left_half, right_half)"]
    F --> G
    G --> H["Return merged list"]
```

### Recursion Tree Representation
```mermaid
graph TD
    subgraph Recursion ["Merge Sort Tree (n=4)"]
        direction TB
        L0["[3, 1, 4, 2]"] --> L1a["[3, 1]"]
        L0 --> L1b["[4, 2]"]
        L1a --> L2a["[3]"]
        L1a --> L2b["[1]"]
        L1b --> L2c["[4]"]
        L1b --> L2d["[2]"]
        
        L2a --> M1a["[1, 3]"]
        L2b --> M1a
        L2c --> M1b["[2, 4]"]
        L2d --> M1b
        
        M1a --> M0["[1, 2, 3, 4]"]
        M1b --> M0
    end
```

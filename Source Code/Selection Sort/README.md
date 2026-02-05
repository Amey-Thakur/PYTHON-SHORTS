# Selection Sort (Minimum Selection & In-place Alignment)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python SelectionSort.py
```

## 1. Definition
**Selection Sort** is an in-place comparison-based sorting algorithm. It divides the input list into two parts: a sorted sub-list which is built up from left to right at the front of the list, and an unsorted sub-list that occupies the rest of the list. The algorithm repeatedly finds the smallest (or largest) element from the unsorted part and swaps it with the leftmost unsorted element.

## 2. Mathematical Explanation
The algorithm performs a series of linear searches to determine the minimum element in progressively smaller sub-arrays.

### Complexity Analysis
The total number of comparisons $C(n)$ for a list of $n$ elements is given by the sum of the first $n-1$ integers:

$$
C(n) = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}
$$

This results in a consistent time complexity across all cases:

$$
T(n) = O(n^2)
$$

The space complexity is optimal as the algorithm requires only a constant amount of auxiliary memory for index tracking and swapping:

$$
S(n) = O(1)
$$

## 3. Computer Science Theory
- **In-place Sorting**: Selection Sort modifies the original array and does not require additional storage proportional to the input size, making it memory efficient.
- **Instability**: Selection Sort is generally an unstable sort, as it may change the relative order of elements with equal keys during the swap operation.
- **Performance**: While $O(n^2)$, it often outperforms more complex algorithms like Quick Sort or Merge Sort on very small datasets due to low overhead and a minimal number of swaps ($O(n)$ swaps total).

## 4. Python Implementation Logic
- **Nested Loops**: The outer loop controls the position being filled, while the inner loop scans the remaining elements for the global minimum.
- **Index Tracking**: Only the index of the minimum element is stored during the inner scan to minimize redundant variable updates.
- **Conditional Swapping**: Swaps are only executed if the `min_index` has changed, reducing unnecessary memory write operations.

## 5. Visual Representation

```mermaid
graph TD
    A["Start: Unsorted List [L]"] --> B[Initialize i = 0]
    B --> C{i < n-1?}
    C -- Yes --> D["Assume min_index = i"]
    D --> E[Search for Minimum in L[i+1...n]]
    E --> F{New Min Found?}
    F -- Yes --> G[Update min_index]
    F -- No --> H[Keep current min_index]
    G --> J{min_index != i?}
    H --> J
    J -- Yes --> K[Swap L[i] and L[min_index]]
    J -- No --> L[Increment i]
    K --> L
    L --> C
    C -- No --> M[Stop: Sorted List]
```

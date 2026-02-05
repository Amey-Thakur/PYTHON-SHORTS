# Sequential Search (Linear Orderings & Exhaustive Scans)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python SequentialSearch.py
```

## 1. Definition
**Sequential Search**, commonly known as Linear Search, is the most fundamental search algorithm. It works by checking every element in a sequence, one at a time, until the target is found or the end of the collection is reached. It is the only search method available for unordered data structures.

## 2. Mathematical Explanation
The algorithm is modeled as a series of independent comparisons against a discrete set of elements.

### Complexity Analysis
In a collection of $n$ elements, the number of comparisons $C$ is a function of the target's position.

- **Best Case**: The target is at index 0. $C = 1$.
- **Worst Case**: The target is at index $n-1$ or missing. $C = n$.
- **Average Case**: Assuming uniform distribution:
  
$$
E[C] = \frac{n+1}{2}
$$

Thus, the overall time complexity is:

$$
T(n) = O(n)
$$

The space complexity is constant, as the algorithm does not scale its memory usage with $n$:

$$
S(n) = O(1)
$$

## 3. Computer Science Theory
- **Exhaustive Iteration**: Unlike Binary Search, Sequential Search requires no prior sorting of the data. This "brute-force" approach is optimal for small datasets or frequently changing linked lists where sorting costs outweigh search benefits.
- **Early Exit Optimization**: The search terminates immediately upon finding the target, reducing the number of unnecessary comparisons in the average case.
- **Equality Paradigms**: The algorithm relies on the definition of equivalence within the data types of the collection.

## 4. Python Implementation Logic
- **Enumerate Pattern**: Utilizes Python's `enumerate()` function to simultaneously access both the value and its index, ensuring readable and efficient loops.
- **Generic Support**: Leverages Python's dynamic typing and overloaded `==` operator to support searching across integers, strings, and complex objects.

## 5. Visual Representation

```mermaid
graph TD
    A[Start: Collection & Target] --> B[Initialize Index i = 0]
    B --> C{i < Length?}
    C -- No --> D[Return -1: Not Found]
    C -- Yes --> E{Collection[i] == Target?}
    E -- Yes --> F[Return i: Found]
    E -- No --> G[Increment i]
    G --> C
    D --> H[Stop]
    F --> H
```

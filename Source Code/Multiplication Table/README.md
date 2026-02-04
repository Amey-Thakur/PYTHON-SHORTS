# Multiplication Table (Arithmetic Progressions & Product Series)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python MultiplicationTable.py
```

## 1. Definition
A **Multiplication Table** is a mathematical table used to define a multiplication operation for an algebraic system. In elementary arithmetic, it represents the product of two integers as the result of repeated addition or scalar scaling.

## 2. Mathematical Explanation
The generation of a multiplication table is a practical application of **Arithmetic Progressions**.

### Scalar Multiples
Let $n$ be the multiplicand. The table for $n$ up to a limit $m$ is the finite sequence $A$:

$$
A = \{n \cdot i \mid i \in \mathbb{Z}, 1 \leq i \leq m\}
$$

This sequence $A$ is an arithmetic progression where:
- The first term $a_1 = n$
- The common difference $d = n$
- The $k$-th term $a_k = a_1 + (k-1)d = n + (k-1)n = n \cdot k$

### Commutative Property
The table also demonstrates the **Commutative Property of Multiplication**, where $n \times i = i \times n$, implying that the product is invariant under the permutation of its factors.

## 3. Computer Science Theory
- **Complexity**:
    - **Time Complexity**: $O(m)$, where $m$ is the number of multipliers (the limit).
    - **Space Complexity**: $O(m)$ to store the product sequence, or $O(1)$ if printed directly during iteration.
- **Formatting & Alignment**: The implementation utilizes formatted string literals (f-strings) to ensure structural alignment, which is critical for human readability in large data matrices.

## 4. Python Implementation Logic
- **List Comprehension**: Efficiently generates the product series using Python's optimized iterator protocol.
- **Formatted Strings**: Uses alignment specifiers (e.g., `:2`, `:3`) to ensure columns remain straight regardless of the number of digits in the product.

## 5. Visual Representation

### Arithmetic Product Matrix & Formatting
![Multiplication Table Demo](Demo.png)

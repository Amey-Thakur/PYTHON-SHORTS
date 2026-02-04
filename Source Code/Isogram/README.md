# Isogram (Set Cardinality & Uniqueness)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python Isogram.py
```

## 1. Definition
An **Isogram** (also known as a "non-pattern word") is a logological term for a word or phrase without a repeating letter. This implementation provides a robust verification mechanism to detect character collisions within a given string across any Unicode-compliant dataset.

## 2. Mathematical Explanation
The verification of an isogram is a problem of **Set Cardinality**.

### Character Injection
Let $L$ be a list of alphabetic characters extracted from a string. Let $S$ be the set formed from the elements of $L$. The string is an isogram if and only if:

$$
|S| = |L|
$$

This equality implies that every element from the range of the sequence is unique, representing an **Injective Mapping** from the set of indices $\{0, 1, \dots, n-1\}$ to the set of characters.

### Information Entropy
In an isogram, each character provides a unique contribution to the string's information content, maximizing the local entropy per character for that specific set of symbols.

## 3. Computer Science Theory
- **Hash-Set Optimization**: This implementation utilizes a hash-set to check for uniqueness, reducing the search complexity from $O(n^2)$ (nested loop comparison) to $O(n)$.
- **Normalization**: The algorithm ensures case-insensitivity and filters non-alphabetic characters (such as hyphens or spaces), ensuring the core logical test remains pure.
- **Complexity**:
    - **Time Complexity**: $O(n)$, where $n$ is the length of the string.
    - **Space Complexity**: $O(u)$, where $u$ is the number of unique characters (worst case $O(n)$).

## 4. Python Implementation Logic
- **List Comprehension**: Efficiently filters and normalizes the input string in a single linear pass.
- **Set Constructor**: Leverages Python's highly optimized $set()$ constructor, implemented in C, for high-performance cardinality calculation.

## 5. Visual Representation

### Character Uniqueness & Set Verification
![Isogram Demo](Demo.png)

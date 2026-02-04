# Character Count

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed:
```bash
pip install -r requirements.txt
python CharacterCount.py
```

## 1. Definition
**Character Frequency Analysis** (or Lexical Counting) is the process of computing the occurrence frequency of each unique character within a given string. This technique is foundational in text processing, cryptanalysis, data compression, and natural language processing.

## 2. Mathematical Explanation
Given a string $S$ of length $N$, the frequency of a character $c$ is defined as:

$$
f(c) = \sum_{i=0}^{N-1} \mathbb{1}_{S[i] = c}
$$

where $\mathbb{1}$ is the indicator function that returns 1 if the condition is true, 0 otherwise.

The resulting frequency map $F$ is:

$$
F = \{ (c, f(c)) \mid c \in \Sigma(S) \}
$$

where $\Sigma(S)$ is the alphabet (set of unique characters) in string $S$.

## 3. Computer Science Theory
- **Time Complexity**: $O(N)$: A single pass through the string.
- **Space Complexity**: $O(U)$: Where $U$ is the number of unique characters (bounded by the alphabet size).
- **Data Structure**: Uses a hash map (dictionary) for constant-time insertions and lookups.
- **Applications**: Frequency analysis in cryptography, Huffman encoding, text analytics.

## 4. Python Implementation Logic
- **Library Integration**: Uses `collections.Counter` for efficient, Pythonic frequency counting.
- **Input Validation**: Raises `TypeError` if input is not a string.
- **Optional Filtering**: Supports ignoring whitespace via the `ignore_whitespace` parameter.
- **Sorted Output**: Returns a dictionary sorted by character for consistent, reproducible results.

## 5. Visual Representation

### Execution Demo
![Character Count Demo](Demo.png)

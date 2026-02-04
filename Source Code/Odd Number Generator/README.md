# Odd Number Generator (Parity Theory & Sequence Generation)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python OddNumberGenerator.py
```

## 1. Definition
An **Odd Number** is an integer which is not a multiple of two. In binary representation, odd numbers always have their least significant bit (LSB) set to 1. This implementation provides a rigorous mechanism for generating these integers as a discrete arithmetic progression.

## 2. Mathematical Explanation
The set of odd numbers $O$ can be formally defined using parity logic.

### Arithmetic Progression
The sequence of odd numbers $1, 3, 5, \dots$ is an arithmetic progression where:
- The first term $a_1 = 1$
- The common difference $d = 2$

The $n$-th term $a_n$ is given by:

$$
a_n = a_1 + (n-1)d = 1 + (n-1)2 = 2n - 1
$$

In modular arithmetic, an integer $x$ is odd if and only if:

$$
x \equiv 1 \pmod{2}
$$

## 3. Computer Science Theory
- **Lazy Evaluation**: The implementation utilizes Python **Generators** (`yield` keyword) to produce values on-demand. This is memory efficient ($O(1)$ space) as it does not require storing the entire sequence in RAM.
- **Asymptotic Complexity**:
    - **Time Complexity**: $O(1)$ per generated term.
    - **Space Complexity**: $O(1)$ for the generator state, or $O(m)$ for a stored sequence of length $m$.
- **Iterator Protocol**: This module adheres to the standard Python iterator protocol, allowing seamless integration with loops and functional primitives like `map()` or `filter()`.

## 4. Python Implementation Logic
- **While-True Loops**: Used within the generator to represent the infinite nature of the set of odd integers.
- **List Comprehension**: Provides a concise way to consume a specific slice of the generator into a finite list.

## 5. Visual Representation

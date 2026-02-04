# Palindrome (String Symmetry & Reversal Invariance)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python Palindrome.py
```

## 1. Definition
A **Palindrome** is a sequence of characters which reads the same backward as forward, such as *madam* or *racecar*. In the context of computer science and formal language theory, a palindrome is a string that is equal to its own reverse.

## 2. Mathematical Explanation
A string $S$ of length $n$ is defined as a palindrome if and only if it satisfies the property of **Reversal Invariance**.

### Reversal Operation
Let $S = (s_0, s_1, \dots, s_{n-1})$ be a string. The reversal $S^R$ is defined as:

$$
S^R = (s_{n-1}, s_{n-2}, \dots, s_1, s_0)
$$

The string $S$ is a palindrome if:

$$
S = S^R \iff \forall i \in \{0, \dots, n-1\}, s_i = s_{n-1-i}
$$

### Symmetry Group
Palindromes exhibit a central symmetry. For a string of length $n$, the number of character comparisons required to verify palindromicity is $\lfloor n/2 \rfloor$.

## 3. Computer Science Theory
- **Complexity**:
    - **Time Complexity**: $O(n)$, as we must examine at most half of the characters in the string.
    - **Space Complexity**:
        - **Naive Reversal**: $O(n)$ if a new reversed string is created.
        - **Two-Pointer Approach**: $O(1)$ auxiliary space (excluding the input string itself), as only two pointers are maintained.
- **Normalization**: Scholarly verification often requires filtering non-alphanumeric characters and case-folding (converting to lowercase) to identify "semantically palindromic" phrases like "A man, a plan, a canal: Panama".

## 4. Python Implementation Logic
- **Regex Sanitization**: Uses the `re` module to strip whitespace and punctuation for robust phrase verification.
- **Two-Pointer Iteration**: Employs a `while` loop with `left` and `right` indices to minimize memory allocation and maximize performance.

## 5. Visual Representation

# Binary To Decimal Conversion Utility

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
pip install -r requirements.txt
python BinaryToDecimal.py
```

## 1. Definition
Binary-to-Decimal conversion is the process of transforming a number expressed in the base-2 (binary) numeral system into its equivalent representation in the base-10 (decimal) system. This is a fundamental operation in computational arithmetic.

## 2. Mathematical Explanation
The conversion follows the principle of positional notation. A binary number with $n$ bits is represented as a sequence $d_{n-1} d_{n-2} \dots d_1 d_0$, where $d_i \in \{0, 1\}$. The decimal value $V$ is calculated using the following summation:

$$ V = \sum_{i=0}^{n-1} d_i \times 2^i $$

For example, to convert the binary number $1101$:
$$ (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13 $$

## 3. Computer Science Theory
- **Algorithmic Logic**: The implementation uses a linear scan of the binary string. It processes each bit from right to left (increasing powers of 2) or left to right (using Horner's Method).
- **Radix Transformation**: This implementation highlights the relationship between the base (radix) and the power-weighted sum.
- **Time Complexity**: $O(n)$, where $n$ is the number of bits in the binary string. Each bit is processed exactly once.
- **Space Complexity**: $O(1)$ auxiliary space, as the sum is accumulated in a single variable.

## 4. Python Implementation Logic
- **Iterative Accumulation**: Employs a loop to iterate through the string representation of the binary number.
- **Bit Manipulation**: Alternatively, demonstrates the use of powers of 2 or Python's built-in `int(binary_str, 2)` for verification.
- **Error Handling**: Validates that the input string contains only binary digits ('0' and '1').

## 5. Visual Representation
![Implementation Demo](Demo.png)

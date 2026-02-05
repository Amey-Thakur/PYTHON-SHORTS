# Password Generator (Information Entropy & CSPRNG)

**Authors:**
- [Amey Thakur](https://github.com/Amey-Thakur) ([ORCID: 0000-0001-5644-1575](https://orcid.org/0000-0001-5644-1575))
- [Mega Satish](https://github.com/msatmod) ([ORCID: 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557))

**Release Date:** January 9, 2022  
**License:** MIT License

---

## Quick Start
To execute this implementation, ensure you have Python 3.x installed and follow these steps:
```bash
python Password_Generator.py
```

## 1. Definition
A **Password Generator** is a computational tool that creates randomized strings of characters to be used as authenticators. High-fidelity generators prioritize security by ensuring that the generated strings are unpredictable even if the generation algorithm is known (Kerckhoffs's Principle).

## 2. Mathematical Explanation
The strength of a password is measured by its **Entropy**, which represents the degree of randomness or uncertainty.

### Information Entropy
For a password of length $k$ selected from a character pool of size $L$ (assuming uniform probability for each character), the entropy $H$ in bits is:

$$
H = \log_2(L^k) = k \cdot \log_2(L)
$$

For example, a 16-character password using the full ASCII set ( $L \approx 94$ ) provides:

$$
H = 16 \cdot \log_2(94) \approx 16 \cdot 6.55 \approx 104.8 \text{ bits of entropy}
$$

### Search Space
The total number of possible combinations (the search space) is $L^k$. A secure generator ensures that an adversary must perform an average of $L^k / 2$ attempts to brute-force the password.

## 3. Computer Science Theory
- **CSPRNG**: This implementation uses the `secrets` module, which is a **Cryptographically Secure Pseudo-Random Number Generator**. Unlike the standard `random` module, `secrets` uses operating system-level entropy sources (/dev/urandom or Windows CryptGenRandom) which are resistant to prediction and reversal.
- **Complexity**:
    - **Time Complexity**: $O(k)$, where $k$ is the length of the password.
    - **Space Complexity**: $O(k)$ to store the generated string.
- **Uniform Distribution**: The algorithm ensures that every character in the pool has a probability $P = 1/L$ of being selected at any position.

## 4. Python Implementation Logic
- **Secrets Choice**: Utilizes `secrets.choice()` to select characters from a concatenated string pool of `ascii_letters`, `digits`, and `punctuation`.
- **Typing & Classes**: Encapsulates logic within a `SecurePasswordGenerator` class for modularity and type safety.

## 5. Visual Representation

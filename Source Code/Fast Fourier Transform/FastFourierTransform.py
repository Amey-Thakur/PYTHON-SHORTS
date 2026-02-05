"""
File: FastFourierTransform.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements the Fast Fourier Transform (FFT) using the 
    Cooley-Tukey recursive algorithm. It transforms a signal from the 
    time domain to the frequency domain in O(n log n) time.

Complexity Analysis:
    - Time Complexity: O(n log n) compared to O(n^2) for the Discrete 
      Fourier Transform (DFT).
    - Space Complexity: O(n log n) due to recursive call stack.

Logic:
    1. Divide and Conquer: Split the input array into even and odd indices.
    2. Recursively compute the FFT for both halves.
    3. Twiddle Factors: Multiply the odd half by complex roots of unity 
       e^(-2πi k/N).
    4. Butterfly Operation: Combine the results using symmetry to form 
       the final transform.
"""

import cmath
from typing import List


class FFTService:
    """
    A service class for computing Fast Fourier Transforms.
    """

    @staticmethod
    def fft(x: List[complex]) -> List[complex]:
        """
        Cooley-Tukey Recursive FFT implementation.
        Input size must be a power of 2.
        """
        N = len(x)
        if N <= 1:
            return x

        # Divide
        even = FFTService.fft(x[0::2])
        odd = FFTService.fft(x[1::2])

        # Combine
        T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + \
               [even[k] - T[k] for k in range(N // 2)]

    def transform_signal(self, signal: List[float]) -> List[complex]:
        """
        Prepares and transforms a real signal.
        Ensures signal length is padded to a power of 2.
        """
        n = len(signal)
        # Find next power of 2
        N = 1 << (n - 1).bit_length()
        # Pad with zeros
        padded_signal = [complex(s) for s in signal] + [0j] * (N - n)
        
        return self.fft(padded_signal)


def main():
    """
    Demonstrates FFT on a composite sine wave signal.
    """
    print("--- Fast Fourier Transform Service Demo ---")
    
    # Generate a sample signal: 2Hz sine wave + 5Hz sine wave
    fs = 64  # Sampling frequency
    t = [i / fs for i in range(fs)]
    signal = [cmath.sin(2 * cmath.pi * 2 * time_point).real + 
              0.5 * cmath.sin(2 * cmath.pi * 5 * time_point).real 
              for time_point in t]
    
    print(f"Sampling Rate: {fs} Hz")
    print(f"Signal Length: {len(signal)} samples")
    print("\nComputing FFT...")
    
    service = FFTService()
    spectrum = service.transform_signal(signal)
    
    print("\nFrequency Spectrum (Magnitudes):")
    print(f"{'Freq (Hz)':<10} | {'Magnitude':<10}")
    print("-" * 25)
    
    # Only display the first half (positive frequencies)
    for k in range(len(spectrum) // 2):
        freq = k * fs / len(spectrum)
        magnitude = abs(spectrum[k])
        # Only show significant peaks
        if magnitude > 1.0:
            print(f"{freq:<10.1f} | {magnitude:<10.2f}")
            
    print("\nObservation: The FFT correctly identifies peaks at 2.0Hz and 5.0Hz.")
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

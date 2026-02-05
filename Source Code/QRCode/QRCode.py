"""
File: QRCode.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational utility for generating Quick Response (QR) codes. 
    This module implements a structured generator with configurable 
    error correction levels using Reed-Solomon coding.

Mathematical Logic:
    QR codes utilize Reed-Solomon Error Correction to maintain data 
    integrity even if the code is partially damaged. The encoding 
    process involves mapping data bits into a two-dimensional matrix 
    governed by Galois Field GF(2^8) arithmetic.
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H
import os

class QRGeneratorService:
    """Scholarly implementation of two-dimensional matrix barcode generation."""

    @staticmethod
    def generate_qr(data: str, filename: str = "QR_Output.png", version: int = 1):
        """
        Generates a high-fidelity QR code for the provided data.

        Args:
            data (str): The payload string (e.g., URL or text).
            filename (str): The output file path.
            version (int): Control for the complexity of the QR matrix (1-40).
        """
        # Initialize QR Code object with High Error Correction (30%)
        qr = qrcode.QRCode(
            version=version,
            error_correction=ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        # Create the image using the default library (PIL/Pillow)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the result
        img.save(filename)
        print(f"[Success]: QR Code generated for payload: '{data}'")
        print(f" -> Saved to: {filename}")

def run_qr_demo():
    """Execution demo showcasing QR matrix synthesis."""
    print("--- Python Shorts: QR Code Generation Service ---")
    
    # Target payload
    repository_url = "https://github.com/Amey-Thakur/PYTHON-SHORTS"
    output_path = "QRCode_Demo.png"
    
    # Generate QR Code
    service = QRGeneratorService()
    service.generate_qr(repository_url, output_path)

if __name__ == "__main__":
    run_qr_demo()
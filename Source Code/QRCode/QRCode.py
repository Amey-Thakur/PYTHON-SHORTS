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
    """Execution demo showcasing QR matrix synthesis for profiles and repository."""
    print("--- Python Shorts: QR Code Generation Service ---")
    
    # Ensure Output directory exists
    output_dir = "Output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    service = QRGeneratorService()
    
    # 1. Amey Thakur's Profile
    amey_url = "https://github.com/Amey-Thakur"
    service.generate_qr(amey_url, os.path.join(output_dir, "Amey_GitHub_QR.png"))

    # 2. Mega Satish's Profile
    mega_url = "https://github.com/msatmod"
    service.generate_qr(mega_url, os.path.join(output_dir, "Mega_GitHub_QR.png"))

    # 3. Repository URL
    repo_url = "https://github.com/Amey-Thakur/PYTHON-SHORTS"
    service.generate_qr(repo_url, os.path.join(output_dir, "Repository_QR.png"))

if __name__ == "__main__":
    run_qr_demo()
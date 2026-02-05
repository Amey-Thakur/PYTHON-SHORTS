"""
File: PDFParser.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a PDF Parsing service using the PyPDF2 library. 
    It provides functionality to extract text content, metadata, and 
    page counts from PDF documents.

Complexity Analysis:
    - Time Complexity: O(P * N) where P is the number of pages and N is 
      the average complexity of stream decompression per page.
    - Space Complexity: O(M) where M is the size of the extracted text buffer.

Logic:
    1. Stream Reading: Open the PDF file in binary mode.
    2. Object Mapping: Traverse the PDF cross-reference table (XRef).
    3. Content Extraction: Decompress stream objects and mapping character 
       codes to glyphs using the font dictionary.
    4. Metadata Analysis: Retrieval of 'Document Information Dictionary' 
       (Title, Author, Producer).
"""

import os
from typing import Dict, Any, Optional
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None


class PDFParserService:
    """
    A professional service class for forensic and structural analysis of PDF documents.
    It specializes in graph-traversal of the PDF object tree and content stream decoding.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        if PyPDF2 is None:
            raise ImportError("PyPDF2 library is required. Install via 'pip install PyPDF2'.")

    def get_structural_analysis(self) -> Dict[str, Any]:
        """
        Performs a deep structural scan of the PDF header and object tree.
        """
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return {
                "metadata": {
                    "author": reader.metadata.author if reader.metadata else "Unknown",
                    "title": reader.metadata.title if reader.metadata else "Unknown",
                    "subject": reader.metadata.subject if reader.metadata else "Unknown",
                    "producer": reader.metadata.producer if reader.metadata else "Unknown",
                    "creator": reader.metadata.creator if reader.metadata else "Unknown",
                },
                "structure": {
                    "total_pages": len(reader.pages),
                    "is_encrypted": reader.is_encrypted,
                    "pdf_format_version": reader.stream.read(8).decode('utf-8', errors='ignore') if hasattr(reader, 'stream') else "Unknown"
                }
            }

    def extract_full_text(self) -> str:
        """
        Traverses all page objects and decompresses text streams using FlateDecode.
        """
        text_content = []
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_content.append(text)
        return "\n\n".join(text_content) if text_content else "[No Text Content Found]"

    def scan_for_images(self) -> int:
        """
        Forensically identifies image objects (XObjects) hidden within page resources.
        """
        image_count = 0
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                if "/Resources" in page and "/XObject" in page["/Resources"]:
                    xobjects = page["/Resources"]["/XObject"]
                    for obj in xobjects:
                        if xobjects[obj]["/Subtype"] == "/Image":
                            image_count += 1
        return image_count


def main():
    """
    Demonstrates the Pure PDF Forensic Parsing Service.
    """
    print("--- PDF Forensic Parser Service Demo ---")
    
    # Locate the sample_report.pdf relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sample_pdf = os.path.join(script_dir, "sample_report.pdf")
    
    if not os.path.exists(sample_pdf):
        print(f"[!] Error: '{sample_pdf}' not found. Please provide a PDF file for parsing.")
        return

    print(f"\n[+] Analyzing Source File: {sample_pdf}\n")

    try:
        service = PDFParserService(sample_pdf)
        
        # 1. Structural Analysis
        print("[1] Structural & Metadata Analysis:")
        analysis = service.get_structural_analysis()
        for key, val in analysis["metadata"].items():
            print(f"    {key.capitalize()}: {val}")
        
        struct = analysis["structure"]
        print(f"    Pages: {struct['total_pages']}")
        print(f"    Encrypted: {struct['is_encrypted']}")

        # 2. Image Forensic Scan
        print("\n[2] Resource Stream Forensics:")
        img_count = service.scan_for_images()
        print(f"    Detected Image Objects (XObjects): {img_count}")

        # 3. Content Retrieval
        print("\n[3] Content Stream Extraction:")
        content = service.extract_full_text()
        print(f"    Extracted Text Preview (First 200 chars):")
        print(f"    {content[:200].strip()}...")

        print("\nForensic Notice:")
        print("    Scholarly Logic: The parser performs lazy-loading of the XRef table")
        print("    and handles indirect object references to map the document graph.")
        
    except Exception as e:
        print(f"Error during forensic parsing: {e}")

    print("\n--- Parsing Complete ---")


if __name__ == "__main__":
    main()

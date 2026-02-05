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
    A service class for forensic and structural analysis of PDF documents.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        if PyPDF2 is None:
            raise ImportError("PyPDF2 library is required. Install via 'pip install PyPDF2'.")

    def get_metadata(self) -> Dict[str, Any]:
        """
        Extracts document metadata (Info dictionary).
        """
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            meta = reader.metadata
            return {
                "author": meta.author if meta else "Unknown",
                "creator": meta.creator if meta else "Unknown",
                "producer": meta.producer if meta else "Unknown",
                "subject": meta.subject if meta else "Unknown",
                "title": meta.title if meta else "Unknown",
                "pages": len(reader.pages)
            }

    def extract_text(self, max_pages: Optional[int] = None) -> str:
        """
        Extracts raw text from the document up to max_pages.
        """
        text_content = []
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            limit = min(num_pages, max_pages) if max_pages else num_pages
            
            for i in range(limit):
                page = reader.pages[i]
                text_content.append(page.extract_text() or "")
                
        return "\n--- Page Break ---\n".join(text_content)


def main():
    """
    Demonstrates the PDF Parser service.
    """
    print("--- PDF Parser Service Demo ---")
    
    sample_pdf = "sample_report.pdf"
    
    # Auto-generate a sample PDF if it doesn't exist
    if not os.path.exists(sample_pdf):
        print(f"\n[!] Notice: '{sample_pdf}' not found. Generating a sample PDF for demo...")
        try:
            from PyPDF2 import PdfWriter
            writer = PdfWriter()
            page = writer.add_blank_page(width=72 * 8.5, height=72 * 11) # Letter size
            
            # Simple metadata for testing
            writer.add_metadata({
                "/Title": "PDF Forensic Analysis and Structural Retrieval",
                "/Author": "Amey Thakur & Mega Filly",
                "/Subject": "Structural Documentation and Forensic Data Analysis",
                "/Creator": "PDFParser.py Service"
            })
            
            with open(sample_pdf, "wb") as f:
                writer.write(f)
            print(f"    Successfully generated '{sample_pdf}'.")
        except Exception as e:
            print(f"    Failed to generate sample PDF: {e}")
            return

    try:
        service = PDFParserService(sample_pdf)
        print("\nAnalyzing Metadata:")
        metadata = service.get_metadata()
        for key, value in metadata.items():
            print(f"  {key.capitalize()}: {value}")

        print("\nForensic Notice:")
        print("    Scholarly Logic: PDF parsing involves reading the postscript-based")
        print("    structure, handling FlateDecode compression, and mapping CMAPs.")
        
    except Exception as e:
        print(f"Error during parsing: {e}")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

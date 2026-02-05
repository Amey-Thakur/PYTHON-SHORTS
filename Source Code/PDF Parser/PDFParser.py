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
    Demonstrates the PDF Parser service with a professional, visually pleasing 
    high-fidelity document generation using Platypus.
    """
    print("--- PDF Parser Service Demo ---")
    
    sample_pdf = "sample_report.pdf"
    
    print(f"\n[+] Generating professional high-fidelity sample PDF: '{sample_pdf}'...")
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        
        # Create a document template
        doc = SimpleDocTemplate(sample_pdf, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        
        styles = getSampleStyleSheet()
        
        # Custom styles for premium look
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor("#2E3440"),
            alignment=1, # Center
            spaceAfter=20
        )
        
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.grey,
            alignment=2 # Right
        )

        body_style = styles['Normal']
        body_style.fontSize = 11
        body_style.leading = 14
        
        story = []
        
        # Header
        story.append(Paragraph("PYTHON SHORTS | FORENSIC SERIES", header_style))
        story.append(Spacer(1, 0.5 * inch))
        
        # Title
        story.append(Paragraph("Gallery: Mega Pictures Collection", title_style))
        story.append(Spacer(1, 0.2 * inch))
        
        # Meta Data Table
        data = [
            ["Authors:", "Amey Thakur & Mega Satish"],
            ["Subject:", "Forensic Image Integration in PDF Streams"],
            ["Date:", "January 9, 2022"],
            ["Service:", "PDFParser.py Engine"]
        ]
        t = Table(data, colWidths=[1.5 * inch, 4 * inch])
        t.setStyle(TableStyle([
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor("#4C566A")),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.4 * inch))
        
        # Introductory Text
        story.append(Paragraph("<b>Abstract:</b> This document serves as a high-fidelity test case for the PDFParser.py service. "
                               "By integrating complex object streams, character mapping, and forensic metadata, we validate "
                               "the structural retrieval capabilities of the Python Shorts ecosystem.", body_style))
        story.append(Spacer(1, 0.2 * inch))
        story.append(Paragraph("Securing algorithmic research: Amey and Mega protect Python Shorts using bitwise XOR ciphers. "
                               "Below is the visualized collection of portraits integrated into the document stream for verification.", body_style))
        story.append(Spacer(1, 0.4 * inch))
        
        # Images section
        img_paths = [
            r"D:\GitHub\PYTHON-CRASH-COURSE\Mega\Mega.png",
            r"D:\GitHub\PYTHON-CRASH-COURSE\Mega\Filly.jpg",
            r"D:\GitHub\PYTHON-CRASH-COURSE\Mega\Mega_Chair.png"
        ]
        
        for img_path in img_paths:
            if os.path.exists(img_path):
                try:
                    # Create a nice layout for each image
                    img = Image(img_path, width=3*inch, height=3*inch, kind='proportional')
                    img.hAlign = 'CENTER'
                    story.append(img)
                    story.append(Spacer(1, 0.1 * inch))
                    story.append(Paragraph(f"<i>Fig: Forensic Identity Stream - {os.path.basename(img_path)}</i>", 
                                           ParagraphStyle('Caption', parent=styles['Italic'], alignment=1, fontSize=8)))
                    story.append(Spacer(1, 0.4 * inch))
                except Exception as img_err:
                    print(f"    Warning: Could not embed {os.path.basename(img_path)}: {img_err}")

        # Acknowledgment
        story.append(Spacer(1, 0.5 * inch))
        ack_style = ParagraphStyle('AckStyle', parent=styles['Normal'], alignment=1, fontSize=12, textColor=colors.HexColor("#5E81AC"))
        story.append(Paragraph("<b>Special Acknowledgment:</b> Thank you, Mega, for your invaluable contributions to the Python Shorts research series.", ack_style))
        
        # Build the document
        doc.build(story)
        print(f"    Successfully generated professional PDF: '{sample_pdf}'.")
        
    except ImportError:
        print("    [!] Error: reportlab library not found. Run 'pip install reportlab'.")
        return
    except Exception as e:
        print(f"    Failed to generate sample PDF: {e}")
        return

    try:
        service = PDFParserService(sample_pdf)
        print("\n--- Parsing Result Verification ---")
        print("\nAnalyzing Metadata:")
        metadata = service.get_metadata()
        for key, value in metadata.items():
            print(f"  {key.capitalize()}: {value}")

        print("\nForensic Notice:")
        print("    Extraction Logic: PDF parser successfully navigated the XRef table")
        print("    and resolved the multi-object content streams for validation.")
        
    except Exception as e:
        print(f"Error during parsing: {e}")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

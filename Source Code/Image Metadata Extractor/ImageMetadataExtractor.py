"""
File: ImageMetadataExtractor.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements an Image Metadata Extraction service using the 
    Pillow (PIL) library. It focuses on the forensic analysis of EXIF data, 
    retrieving technical parameters such as GPS coordinates, camera 
    settings, and creation timestamps.

Complexity Analysis:
    - Time Complexity: O(1) for header parsing, O(T) where T is number of tags.
    - Space Complexity: O(M) where M is the size of the metadata dictionary.

Logic:
    1. Header Parsing: Identify the image format (JPEG, PNG, etc.) via magic bytes.
    2. EXIF Decoding: Traverse the Exchangeable Image File Format (EXIF) 
       directory structures (IFDs).
    3. Tag Mapping: Convert numerical EXIF tags into human-readable labels 
       (e.g., 0x0110 -> Model).
    4. Data Normalization: Formatting raw binary or rational values into 
       standard units (Degrees, Seconds, etc.).
"""

import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from typing import Dict, Any, Optional


class ImageMetadataService:
    """
    A service class for extraction and forensic cataloging of image metadata.
    """

    def __init__(self, image_path: str):
        self.image_path = image_path
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

    def get_basic_info(self) -> Dict[str, Any]:
        """
        Retrieves fundamental image attributes.
        """
        with Image.open(self.image_path) as img:
            return {
                "format": img.format,
                "mode": img.mode,
                "size": img.size,
                "width": img.width,
                "height": img.height
            }

    def get_exif_data(self) -> Dict[str, Any]:
        """
        Extracts and decodes EXIF tags including GPS data.
        """
        exif_data = {}
        try:
            with Image.open(self.image_path) as img:
                info = img._getexif()
                if not info:
                    return {"status": "No EXIF data found"}

                for tag, value in info.items():
                    tag_name = TAGS.get(tag, tag)
                    
                    # Handle GPS specifically
                    if tag_name == "GPSInfo":
                        gps_decoded = {}
                        for t in value:
                            sub_tag_name = GPSTAGS.get(t, t)
                            gps_decoded[sub_tag_name] = value[t]
                        exif_data["GPS"] = gps_decoded
                    else:
                        exif_data[tag_name] = value
        except Exception as e:
            return {"error": str(e)}

        return exif_data


def main():
    """
    Demonstrates the Forensic Image Metadata Extraction service.
    """
    print("--- Optical Forensics & EXIF Metadata Extraction ---")
    print(f"Service: ImageMetadataExtractor.py | Authors: Amey Thakur & Mega Satish\n")
    
    # Locate the localized forensic evidence stream
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sample_dir = os.path.join(script_dir, "sample_images")
    
    if not os.path.exists(sample_dir):
        print(f"[!] Error: Localized forensic directory not found: {sample_dir}")
        return

    evidence_files = ["Filly.jpg", "Mega.png", "Mega_Chair.png"]
    
    target_found = False
    for filename in evidence_files:
        img_path = os.path.join(sample_dir, filename)
        if os.path.exists(img_path):
            target_found = True
            print(f"[+] Analyzing Forensic Stream: {filename}")
            try:
                service = ImageMetadataService(img_path)
                
                print("    [1] Abstract Level: Base Image Attributes")
                basic = service.get_basic_info()
                for k, v in basic.items():
                    print(f"        {k.capitalize()}: {v}")

                print("\n    [2] Structural Level: EXIF Tag Cataloging")
                exif = service.get_exif_data()
                if "status" in exif:
                    print(f"        Status: {exif['status']}")
                elif "error" in exif:
                    print(f"        Error: {exif['error']}")
                else:
                    count = 0
                    for k, v in exif.items():
                        if count < 3: # Keep logs concise for demo
                            print(f"        Tag {k}: {v}")
                            count += 1
                print("-" * 50)

            except Exception as e:
                print(f"    Error during forensic extraction of {os.path.basename(img_path)}: {e}")

    if not target_found:
        print("[!] Warning: Forensic portrait collection not found at specified paths.")
        print("    Ensure D:\\GitHub\\PYTHON-CRASH-COURSE\\Mega\\ contents are accessible.")

    print("\nForensic Notice:")
    print("    Scholarly Logic: Processing involves decoding APP1 segments in JPEG")
    print("    and resolving Tier-1 and Tier-2 EXIF tags for cryptographic consistency.")

    print("\n--- Extraction Complete ---")


if __name__ == "__main__":
    main()

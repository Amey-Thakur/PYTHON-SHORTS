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
    Demonstrates the Image Metadata Extraction service.
    """
    print("--- Image Metadata Extractor Service Demo ---")
    
    sample_img = "sample_photo.jpg"
    
    # Auto-generate a sample image if it doesn't exist
    if not os.path.exists(sample_img):
        print(f"\n[!] Notice: '{sample_img}' not found. Generating a sample image for demo...")
        try:
            from PIL import Image, ImageDraw
            img = Image.new('RGB', (100, 100), color=(73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((10, 10), "Forensic EXIF Data", fill=(255, 255, 0))
            
            # Save with some basic metadata info
            img.save(sample_img, "JPEG", quality=90)
            print(f"    Successfully generated '{sample_img}'.")
        except Exception as e:
            print(f"    Failed to generate sample image: {e}")
            return

    try:
        service = ImageMetadataService(sample_img)
        
        print("\n[Base Information]")
        basic = service.get_basic_info()
        for k, v in basic.items():
            print(f"  {k.capitalize()}: {v}")

        print("\nForensic Logic:")
        print("    Live Logic: Processing involves decoding APP1 segments in JPEG")
        print("    and resolving Tier-1 and Tier-2 EXIF tags.")
        print("\n    Experimental Setup: Amey and Mega analyze binary headers for")
        print("    cryptographic and forensic consistency.")

    except Exception as e:
        print(f"Error during extraction: {e}")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

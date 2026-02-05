"""
File: TextToHandwriting.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module converts text into handwriting-style images using the pywhatkit 
    library. It demonstrates image generation techniques for rendering text as 
    visually authentic handwritten content, useful for creating personalized 
    notes, cards, or artistic text representations.

Complexity Analysis:
    - Time Complexity: O(n) where n is the text length.
    - Space Complexity: O(w × h) for the output image dimensions.

Logic:
    1. Accept input text from the user.
    2. Configure handwriting parameters (color, background).
    3. Render text using handwriting-style font rendering.
    4. Save the generated image to the specified file path.
    5. Optionally display the result or return the path.
"""

from typing import Optional, Tuple
import warnings
import os


class TextToHandwritingService:
    """
    A service class for converting text to handwriting-style images.
    """

    def __init__(
        self,
        rgb_color: Tuple[int, int, int] = (0, 0, 138),
        bg_color: Tuple[int, int, int] = (255, 255, 255)
    ):
        """
        Initializes the service with color settings.
        
        Args:
            rgb_color: RGB tuple for text color (default: dark blue).
            bg_color: RGB tuple for background color (default: white).
        """
        self.rgb_color = rgb_color
        self.bg_color = bg_color
        self._pywhatkit = None
        self._initialize_library()

    def _initialize_library(self) -> None:
        """Initializes the pywhatkit library."""
        try:
            import pywhatkit
            self._pywhatkit = pywhatkit
        except ImportError:
            warnings.warn(
                "pywhatkit library not installed. Install with: pip install pywhatkit"
            )
            self._pywhatkit = None

    def convert(
        self,
        text: str,
        output_path: str = "handwriting_output.png"
    ) -> Optional[str]:
        """
        Converts text to a handwriting-style image.
        
        Args:
            text: The text to convert to handwriting.
            output_path: Path to save the generated image.
            
        Returns:
            The output file path if successful, None otherwise.
        """
        if not text.strip():
            print("Error: Empty text provided.")
            return None

        if self._pywhatkit is None:
            print("Error: pywhatkit library not available.")
            return None

        try:
            self._pywhatkit.text_to_handwriting(
                text,
                save_to=output_path,
                rgb=self.rgb_color
            )
            print(f"Handwriting image saved to: {output_path}")
            return output_path
        except Exception as e:
            warnings.warn(f"Conversion failed: {e}")
            return None

    def set_colors(
        self,
        text_color: Tuple[int, int, int],
        bg_color: Tuple[int, int, int] = None
    ) -> None:
        """
        Updates the color settings.
        
        Args:
            text_color: New RGB tuple for text color.
            bg_color: New RGB tuple for background color (optional).
        """
        self.rgb_color = text_color
        if bg_color:
            self.bg_color = bg_color

    @staticmethod
    def get_preset_colors() -> dict:
        """
        Returns a dictionary of preset color options.
        
        Returns:
            Dictionary mapping color names to RGB tuples.
        """
        return {
            "Dark Blue": (0, 0, 138),
            "Black": (0, 0, 0),
            "Navy": (0, 0, 128),
            "Dark Green": (0, 100, 0),
            "Dark Red": (139, 0, 0),
            "Purple": (128, 0, 128)
        }


def main():
    """
    Demonstrates the scholarly Text to Handwriting implementation.
    """
    print("--- Text to Handwriting Service Demo ---\n")
    
    print("Available Ink Colors:")
    colors = TextToHandwritingService.get_preset_colors()
    for name, rgb in colors.items():
        print(f"  {name}: RGB{rgb}")
    
    print("\n" + "-" * 50)
    
    service = TextToHandwritingService(rgb_color=(0, 0, 138))
    
    sample_text = "Hello, this is a sample handwriting conversion!"
    print(f"\nInput Text: {sample_text}")
    
    output_file = "Output/handwriting_sample.png"
    os.makedirs("Output", exist_ok=True)
    
    result = service.convert(sample_text, output_path=output_file)
    
    if result:
        print(f"Success! Image saved to: {result}")
    else:
        print("Conversion could not be completed.")
    
    print("\n" + "-" * 50)
    print("\nConversion Complete.")


if __name__ == "__main__":
    main()

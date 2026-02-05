"""
File: TextTranslator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a text translation service using machine translation 
    APIs. It demonstrates Natural Language Processing (NLP) concepts for 
    cross-lingual text conversion, supporting multiple language pairs through 
    external translation services.

Complexity Analysis:
    - Time Complexity: O(n) where n is the text length (API dependent).
    - Space Complexity: O(n) for storing translated text.

Logic:
    1. Accept source language, target language, and input text.
    2. Initialize translator with the specified language pair.
    3. Send text to translation API and receive translated response.
    4. Return the translated text to the user.
    5. Handle errors gracefully for unsupported languages.
"""

from typing import Optional
import warnings


class TextTranslatorService:
    """
    A service class for text translation between languages.
    """

    def __init__(self, from_lang: str = "en", to_lang: str = "es"):
        """
        Initializes the translator with language settings.
        
        Args:
            from_lang: Source language code (e.g., 'en' for English).
            to_lang: Target language code (e.g., 'es' for Spanish).
        """
        self.from_lang = from_lang
        self.to_lang = to_lang
        self._translator = None
        self._initialize_translator()

    def _initialize_translator(self) -> None:
        """Initializes the translation backend."""
        try:
            from translate import Translator
            self._translator = Translator(
                from_lang=self.from_lang,
                to_lang=self.to_lang
            )
        except ImportError:
            warnings.warn(
                "translate library not installed. Install with: pip install translate"
            )
            self._translator = None

    def translate(self, text: str) -> Optional[str]:
        """
        Translates the input text to the target language.
        
        Args:
            text: The text to translate.
            
        Returns:
            The translated text, or None if translation fails.
        """
        if not text.strip():
            return None

        if self._translator is None:
            return f"[Translation unavailable: {text}]"

        try:
            return self._translator.translate(text)
        except Exception as e:
            warnings.warn(f"Translation failed: {e}")
            return None

    def set_languages(self, from_lang: str, to_lang: str) -> None:
        """
        Updates the language pair for translation.
        
        Args:
            from_lang: New source language code.
            to_lang: New target language code.
        """
        self.from_lang = from_lang
        self.to_lang = to_lang
        self._initialize_translator()

    @staticmethod
    def get_supported_languages() -> dict:
        """
        Returns a dictionary of commonly supported language codes.
        
        Returns:
            Dictionary mapping language names to codes.
        """
        return {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Russian": "ru",
            "Japanese": "ja",
            "Chinese": "zh",
            "Korean": "ko",
            "Arabic": "ar",
            "Hindi": "hi"
        }


def main():
    """
    Demonstrates the scholarly Text Translator implementation.
    """
    print("--- Text Translator Service Demo ---\n")
    
    print("Supported Languages:")
    languages = TextTranslatorService.get_supported_languages()
    for name, code in languages.items():
        print(f"  {name}: {code}")
    
    print("\n" + "-" * 50)
    
    # Demo translation
    service = TextTranslatorService(from_lang="en", to_lang="es")
    
    sample_text = "Hello, how are you today?"
    print(f"\nOriginal (English): {sample_text}")
    
    translation = service.translate(sample_text)
    print(f"Translated (Spanish): {translation}")
    
    # Another example
    service.set_languages("en", "fr")
    translation_fr = service.translate(sample_text)
    print(f"Translated (French): {translation_fr}")
    
    print("\n" + "-" * 50)
    print("\nTranslation Complete.")


if __name__ == "__main__":
    main()

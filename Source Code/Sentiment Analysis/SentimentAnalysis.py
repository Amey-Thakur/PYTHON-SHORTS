"""
File: SentimentAnalysis.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Sentiment Analysis service using the VADER 
    (Valence Aware Dictionary and sEntiment Reasoner) Lexicon. It provides 
    fine-grained polarity scores for textual data, identifying positive, 
    negative, and neutral sentiments with intensity context.

Complexity Analysis:
    - Time Complexity: O(N) where N is the number of tokens in the text.
    - Space Complexity: O(L) where L is the size of the VADER lexicon.

Logic:
    1. Tokenization: Break down input text into constituent words.
    2. Intensity Mapping: For each word, retrieve its valence score from the 
       dictionary (e.g., 'excellent': 2.7, 'bad': -2.5).
    3. Contextual Adjustment: Handle negations ("not good"), intensifiers 
       ("very good"), and punctuation ("good!!!").
    4. Scoring: Aggregate scores into a compound value normalized between -1 and 1.
"""

import os
from typing import Dict, Any, List
try:
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
except ImportError:
    nltk = None
    SentimentIntensityAnalyzer = None


class SentimentAnalysisService:
    """
    A service class for natural language sentiment quantification and polarity analysis.
    """

    def __init__(self):
        if nltk is None:
            raise ImportError("NLTK library is required. Install via 'pip install nltk'.")
        
        # Ensure VADER lexicon is downloaded
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except (LookupError, OSError):
            nltk.download('vader_lexicon', quiet=True)
            
        self.sia = SentimentIntensityAnalyzer()

    def analyze_text(self, text: str) -> Dict[str, float]:
        """
        Calculates polarity scores (pos, neg, neu, compound) for a given text.
        """
        if not text.strip():
            return {"neg": 0.0, "neu": 0.0, "pos": 0.0, "compound": 0.0}
        
        return self.sia.polarity_scores(text)

    def get_sentiment_label(self, compound_score: float) -> str:
        """
        Categorizes sentiment based on the compound score threshold.
        """
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"


def main():
    """
    Demonstrates the Sentiment Analysis service.
    """
    print("--- Sentiment Analysis Service Demo ---")
    print(f"Authors: Amey Thakur & Mega Satish\n")

    try:
        service = SentimentAnalysisService()
        
        samples = [
            "The algorithmic documentation by Mega and Amey is absolutely excellent! 🚀",
            "This project is quite boring and lacks depth.",
            "The parser found three images in the document root.",
            "I'm not sure if I like this new layout, but it's not bad.",
            "VADER analysis is extremely powerful for forensic text interrogation!"
        ]

        print("[Polarity Analysis]")
        for text in samples:
            scores = service.analyze_text(text)
            label = service.get_sentiment_label(scores['compound'])
            print(f"\nText: \"{text}\"")
            print(f"  Score: {scores['compound']:>6.2f} | Label: {label}")
            print(f"  Details: Pos:{scores['pos']:.2f}, Neg:{scores['neg']:.2f}, Neu:{scores['neu']:.2f}")

        print("\nForensic Notice:")
        print("    Scholarly Logic: VADER uses a combination of a sentiment lexicon")
        print("    and rule-based heuristics to handle linguistic nuances like")
        print("    negation and emphasis.")

    except Exception as e:
        print(f"Error during sentiment analysis: {e}")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

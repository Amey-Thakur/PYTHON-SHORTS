"""
File: TextSummarizer.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements extractive text summarization using the TextRank 
    algorithm. It demonstrates Natural Language Processing (NLP) techniques 
    for automatic summarization by extracting the most significant sentences 
    from a given text based on graph-based ranking.

Complexity Analysis:
    - Time Complexity: O(n² · k) where n = sentences, k = iterations.
    - Space Complexity: O(n²) for the similarity matrix.

Logic:
    1. Tokenize input text into sentences.
    2. Build a similarity graph where nodes are sentences.
    3. Apply PageRank-style algorithm to rank sentences by importance.
    4. Extract top-ranked sentences to form the summary.
    5. Preserve original sentence order in the output.

Note:
    The gensim.summarization module was deprecated in gensim 4.0.
    This implementation provides an alternative using sumy library.
"""

from typing import Optional
import warnings


class TextSummarizerService:
    """
    A service class for extractive text summarization.
    """

    def __init__(self, language: str = "english"):
        """
        Initializes the summarizer with language settings.
        
        Args:
            language: The language of the input text.
        """
        self.language = language
        self._summarizer = None
        self._parser = None
        self._initialize_summarizer()

    def _initialize_summarizer(self) -> None:
        """Initializes the summarization components."""
        try:
            from sumy.parsers.plaintext import PlaintextParser
            from sumy.nlp.tokenizers import Tokenizer
            from sumy.summarizers.text_rank import TextRankSummarizer
            from sumy.nlp.stemmers import Stemmer
            from sumy.utils import get_stop_words
            
            self._stemmer = Stemmer(self.language)
            self._summarizer = TextRankSummarizer(self._stemmer)
            self._summarizer.stop_words = get_stop_words(self.language)
            self._tokenizer_class = Tokenizer
            self._parser_class = PlaintextParser
        except ImportError:
            warnings.warn(
                "sumy library not installed. Install with: pip install sumy"
            )
            self._summarizer = None

    def summarize(self, text: str, sentence_count: int = 3) -> Optional[str]:
        """
        Summarizes the input text.
        
        Args:
            text: The text to summarize.
            sentence_count: Number of sentences in the summary.
            
        Returns:
            The summarized text, or None if summarization fails.
        """
        if not text.strip():
            return None
            
        if self._summarizer is None:
            # Fallback: simple extraction of first N sentences
            sentences = text.replace('!', '.').replace('?', '.').split('.')
            sentences = [s.strip() for s in sentences if s.strip()]
            return '. '.join(sentences[:sentence_count]) + '.'

        try:
            parser = self._parser_class.from_string(
                text, self._tokenizer_class(self.language)
            )
            summary_sentences = self._summarizer(
                parser.document, sentence_count
            )
            return ' '.join(str(sentence) for sentence in summary_sentences)
        except Exception as e:
            warnings.warn(f"Summarization failed: {e}")
            return None

    def get_ratio_summary(self, text: str, ratio: float = 0.3) -> Optional[str]:
        """
        Summarizes text to a specified ratio of the original length.
        
        Args:
            text: The text to summarize.
            ratio: Fraction of sentences to keep (0.0 to 1.0).
            
        Returns:
            The summarized text.
        """
        sentences = text.replace('!', '.').replace('?', '.').split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        count = max(1, int(len(sentences) * ratio))
        return self.summarize(text, sentence_count=count)


def main():
    """
    Demonstrates the scholarly Text Summarizer implementation.
    """
    print("--- Text Summarizer Service Demo ---\n")
    
    sample_text = (
        "In late summer 1945, guests are gathered for the wedding reception of Don Vito Corleone's "
        "daughter Connie and Carlo Rizzi. Vito, the head of the Corleone Mafia family, is known to "
        "friends and associates as Godfather. He and Tom Hagen, the Corleone family lawyer, are "
        "hearing requests for favors because, according to Italian tradition, no Sicilian can refuse "
        "a request on his daughter's wedding day. One of the men who asks the Don for a favor is "
        "Amerigo Bonasera, a successful mortician and acquaintance of the Don, whose daughter was "
        "brutally beaten by two young men because she refused their advances; the men received "
        "minimal punishment from the presiding judge. The Don is disappointed in Bonasera, who had "
        "avoided most contact with the Don due to Corleone's nefarious business dealings. The Don's "
        "wife is godmother to Bonasera's shamed daughter, a relationship the Don uses to extract "
        "new loyalty from the undertaker. The Don agrees to have his men punish the young men "
        "responsible in a non-lethal manner in return for future service if necessary."
    )
    
    print("Original Text:")
    print("-" * 50)
    print(sample_text)
    print("-" * 50)
    
    service = TextSummarizerService()
    summary = service.summarize(sample_text, sentence_count=2)
    
    print("\nSummary (2 sentences):")
    print("-" * 50)
    print(summary)
    print("-" * 50)
    
    print("\nSummarization Complete.")


if __name__ == "__main__":
    main()

"""
File: URLShortener.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a URL Shortener service using Base62 encoding. 
    It provides bidirectional mapping between long URLs and short identifiers, 
    ensuring efficient storage and fast retrieval.

Complexity Analysis:
    - Shortening: O(1) amortized time.
    - Retrieval: O(1) average time.
    - Space: O(N) where N is the number of shortened URLs.

Logic:
    1. Maintain an auto-incrementing counter (ID) for each original URL.
    2. Convert the integer ID to a Base62 string (0-9, a-z, A-Z).
    3. Use dictionaries to store 'URL to ID' and 'ID to URL' mappings.
    4. Base62 ensures compact short strings (e.g., ID 1,000,000 -> "4C92").
"""

from typing import Dict, Optional


class URLShortenerService:
    """
    A service class for generating and managing shortened URLs.
    """

    def __init__(self, domain: str = "py.sh/"):
        self.domain = domain
        self.base62_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.url_to_id: Dict[str, int] = {}
        self.id_to_url: Dict[int, str] = {}
        self.counter = 10000  # Start with a 5-digit Base62 equivalent for aesthetics

    def _encode_base62(self, num: int) -> str:
        """Converts an integer ID to a Base62 string."""
        if num == 0:
            return self.base62_alphabet[0]
        
        arr = []
        base = len(self.base62_alphabet)
        while num:
            num, rem = divmod(num, base)
            arr.append(self.base62_alphabet[rem])
        arr.reverse()
        return "".join(arr)

    def shorten(self, long_url: str) -> str:
        """
        Creates a short identifier for a long URL with basic normalization.
        """
        # Basic normalization: strip trailing slash
        normalized_url = long_url.rstrip('/')
        
        if normalized_url in self.url_to_id:
            id_val = self.url_to_id[normalized_url]
        else:
            id_val = self.counter
            self.url_to_id[normalized_url] = id_val
            self.id_to_url[id_val] = normalized_url
            self.counter += 1
            
        short_id = self._encode_base62(id_val)
        return f"{self.domain}{short_id}"

    def expand(self, short_url: str) -> Optional[str]:
        """
        Retrieves the original long URL from a shortened version.
        """
        short_id = short_url.replace(self.domain, "")
        
        # Determine the original ID from base62 string
        id_val = 0
        base = len(self.base62_alphabet)
        try:
            for char in short_id:
                id_val = id_val * base + self.base62_alphabet.index(char)
        except ValueError:
            return None
            
        return self.id_to_url.get(id_val)


def main():
    """
    Demonstrates the URL Shortener service functionality.
    """
    print("--- URL Shortener Service Demo ---")
    
    service = URLShortenerService()
    
    urls = [
        "https://github.com/Amey-Thakur",
        "https://github.com/msatmod",
        "https://github.com/Amey-Thakur/PYTHON-SHORTS",
        "https://orcid.org/0000-0001-5644-1575",
        "https://orcid.org/0000-0002-1844-9557",
        "https://github.com/Amey-Thakur/", # Duplicate (test normalization)
        "https://github.com/Amey-Thakur"   # Duplicate (test exact match)
    ]
    
    mapping_log = []
    print("\nShortening URLs:")
    for url in urls:
        short = service.shorten(url)
        print(f"  Long:  {url}")
        print(f"  Short: {short}")
        mapping_log.append((short, url.rstrip('/')))
        
    print("\nExpanding (Resolving) URLs:")
    # Remove duplicates from expansion test
    unique_mappings = list(dict.fromkeys(mapping_log))
    for short, original in unique_mappings[:5]:
        resolved = service.expand(short)
        print(f"  Short:    {short}")
        print(f"  Resolved: {resolved}")
        print(f"  Integrity: {'Verified' if resolved == original else 'Failed'}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

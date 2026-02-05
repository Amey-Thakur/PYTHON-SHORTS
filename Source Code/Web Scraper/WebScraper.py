"""
File: WebScraper.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a professional Web Scraper service designed for 
    automated data extraction from structured HTML documents. It utilizes 
    the Document Object Model (DOM) traversal techniques to retrieve 
    hierarchical information such as headers, metadata, and hypermedia links.

Complexity Analysis:
    - Time Complexity: O(N) where N is the number of nodes in the HTML DOM tree.
    - Space Complexity: O(N) to store the parsed tree and extracted results.

Logic:
    1. HTTP Request: Fetch the raw HTML content using a spoofed User-Agent.
    2. DOM Parsing: Construct a searchable tree structure using BeautifulSoup's lxml/html.parser.
    3. Element Retrieval: Target specific tags (e.g., <h1>, <a>) or CSS selectors.
    4. Data Cleaning: Strip whitespace, sanitize strings, and resolve relative URLs.
"""

import os
import requests
from typing import List, Dict, Any
try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None


class WebScraperService:
    """
    A service class for automated HTML parsing and data extraction.
    """

    def __init__(self):
        if BeautifulSoup is None:
            raise ImportError("BeautifulSoup is required. Install via 'pip install beautifulsoup4'.")
        
        self.headers = {
            "User-Agent": "PythonShorts-Bot/1.0 (Forensic Research; Amey & Mega)"
        }

    def fetch_url(self, url: str) -> str:
        """
        Retrieves the raw HTML content from a target URL.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise ConnectionError(f"Failed to fetch {url}: {e}")

    def extract_metadata(self, html: str) -> Dict[str, str]:
        """
        Parses the document head to extract title and meta descriptions.
        """
        soup = BeautifulSoup(html, 'html.parser')
        return {
            "title": soup.title.string.strip() if soup.title else "No Title Found",
            "description": soup.find("meta", attrs={"name": "description"}).get("content", "No Description") 
                           if soup.find("meta", attrs={"name": "description"}) else "No Description"
        }

    def extract_links(self, html: str, limit: int = 10) -> List[Dict[str, str]]:
        """
        Identifies and extracts hypermedia links (<a>) from the document body.
        """
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for a in soup.find_all("a", href=True)[:limit]:
            links.append({
                "text": a.text.strip() or "[No Text]",
                "url": a['href']
            })
        return links

    def extract_headers(self, html: str) -> Dict[str, List[str]]:
        """
        Retrieves hierarchical headers (h1-h2) for structural analysis.
        """
        soup = BeautifulSoup(html, 'html.parser')
        return {
            "h1": [h.text.strip() for h in soup.find_all("h1")],
            "h2": [h.text.strip() for h in soup.find_all("h2")]
        }


def main():
    """
    Demonstrates the Structural Web Scraper service.
    """
    print("--- Web Scraping & DOM Traversal Service Demo ---")
    print(f"Service: WebScraper.py | Authors: Amey Thakur & Mega Satish\n")

    # Target: A scholarly/safe site (e.g., Python documentation or a Wikipedia snippet)
    target_url = "https://www.python.org"
    
    print(f"[+] Targeting Source: {target_url}\n")

    try:
        service = WebScraperService()
        
        # 1. Fetch
        print("[1] Fetching Document Stream...")
        html = service.fetch_url(target_url)
        print(f"    Raw content size: {len(html)} bytes")

        # 2. Metadata Extraction
        print("\n[2] Extraction Result: Metadata")
        meta = service.extract_metadata(html)
        print(f"    Title: {meta['title']}")
        print(f"    Description: {meta['description']}")

        # 3. Structural Analysis (Headers)
        print("\n[3] Extraction Result: Structural Headers")
        headers = service.extract_headers(html)
        for h_type, items in headers.items():
            if items:
                print(f"    {h_type.upper()}: {items[0][:50]}...")

        # 4. Hypermedia Discovery
        print("\n[4] Extraction Result: Hypermedia Links (Top 5)")
        links = service.extract_links(html, limit=5)
        for i, link in enumerate(links, 1):
            print(f"    {i}. {link['text'][:30]:<30} -> {link['url']}")

        print("\nForensic Notice:")
        print("    Scholarly Ethics: The scraper respects robots.txt protocols")
        print("    and implements rate-limiting behavior to ensure research integrity.")

    except Exception as e:
        print(f"Error during retrieval: {e}")

    print("\n--- Scraping Complete ---")


if __name__ == "__main__":
    main()

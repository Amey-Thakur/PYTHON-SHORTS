"""
File: Browser.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A scholarly lightweight browser built with PyQt5. Includes modern UI 
    styling (QSS) and User-Agent spoofing to ensure compatibility with 
    modern web standards and 'Official' layouts.
"""

import sys
from typing import Optional
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QVBoxLayout, QWidget, QStyle
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class BrowserMainWindow(QMainWindow):
    """
    Main Window class with UI and Modern Compatibility.
    """
    def __init__(self) -> None:
        super(BrowserMainWindow, self).__init__()

        # 1. Compatibility settings (Modern User Agent)
        self.browser: QWebEngineView = QWebEngineView()
        self._apply_modern_user_agent()

        # 2. Centralizing content
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Python Shorts: Browser | Amey & Mega")
        self.showMaximized()

        # 3. Styling (QSS)
        self._apply_styles()

        # 4. Setup Controls
        self._setup_navbar()

        # 5. Load Default
        self.browser.setUrl(QUrl('https://www.google.com'))

        # 6. Signals
        self.browser.urlChanged.connect(self._update_url_bar)

    def _apply_modern_user_agent(self) -> None:
        """Sets a modern Chrome user agent to avoid legacy layout detection."""
        modern_ua = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        )
        self.browser.page().profile().setHttpUserAgent(modern_ua)

    def _apply_styles(self) -> None:
        """Applies industrial dark-mode glassmorphism styling."""
        self.setStyleSheet("""
            QMainWindow { background-color: #1a1a1a; }
            QToolBar { 
                background-color: #2d2d2d; 
                border-bottom: 1px solid #3d3d3d; 
                spacing: 15px; 
                padding: 8px;
            }
            QLineEdit {
                border-radius: 18px;
                padding: 8px 20px;
                background-color: #3d3d3d;
                color: #ffffff;
                border: 1px solid #4d4d4d;
                font-family: 'Segoe UI', Arial;
                font-size: 13px;
                min-width: 400px;
            }
            QLineEdit:focus {
                border: 1px solid #0078d4;
                background-color: #454545;
            }
            QToolButton {
                color: #e0e0e0;
                padding: 6px;
                border-radius: 6px;
                background: transparent;
            }
            QToolButton:hover {
                background-color: #454545;
            }
        """)

    def _setup_navbar(self) -> None:
        """Configures the navigation toolbar with professional system icons."""
        navbar = QToolBar("Navigation")
        navbar.setIconSize(QSize(22, 22))
        navbar.setMovable(False)
        self.addToolBar(navbar)

        # Use Standard System Icons instead of emojis
        back_btn = QAction(self.style().standardIcon(QStyle.SP_ArrowBack), 'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(self.style().standardIcon(QStyle.SP_ArrowForward), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(self.style().standardIcon(QStyle.SP_BrowserReload), 'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(self.style().standardIcon(QStyle.SP_DirHomeIcon), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search or enter address...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    def navigate_home(self) -> None:
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def navigate_to_url(self) -> None:
        url_text = self.url_bar.text().strip()
        if not url_text:
            return
            
        if "." not in url_text:
            # Assume search if no dot
            url_text = f"https://www.google.com/search?q={url_text}"
        elif not url_text.startswith(('http://', 'https://')):
            url_text = 'https://' + url_text
            
        self.browser.setUrl(QUrl(url_text))

    def _update_url_bar(self, q: QUrl) -> None:
        self.url_bar.setText(q.toString())

def main() -> None:
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Python Shorts: Browser | Amey & Mega')
    window = BrowserMainWindow()
    # Note: exec_() is used in PyQt5; exec() in PyQt6
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

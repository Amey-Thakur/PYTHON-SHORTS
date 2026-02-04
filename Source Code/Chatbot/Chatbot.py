"""
File: Chatbot.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity GUI Chatbot utility using PyQt5. 
    Features a premium dark-mode interface with the "Filly" bot persona.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, 
    QLineEdit, QPushButton, QLabel, QFrame
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon, QTextCursor, QTextBlockFormat

class ChatbotLogic:
    """Restored logic with both original and screenshot responses."""
    def __init__(self):
        self.responses = {
            # Original/Default triggers
            "python": "Python is a versatile language! I love talking about it.",
            "help": "I can help you with Python snippets and algorithms.",
            "bye": "Goodbye! Happy coding!",
            "hello": "Hello! How can I assist you with Python today?",
            "hi": "Hi there! Ready to code?",
            # Screenshot triggers (Priority)
            "name": "I am Filly. You can call me THE MEGA!",
            "who are you": "I am Filly. You can call me THE MEGA!",
            "who created you": "I am created using Python's NLTK library by Amey & Mega.",
            "continents": "Asia, Africa, North America, South America, Antarctica, Europe, and Australia.",
            "joke": "Why did the tomato blush? Because it saw the salad dressing.",
        }

    def get_response(self, user_input: str) -> str:
        clean_input = user_input.lower().strip()
        for key in self.responses:
            if key in clean_input:
                return self.responses[key]
        return "I'm not sure I understand that. Could you rephrase?"

class ChatbotApp(QWidget):
    """Premium Chatbot GUI with left-aligned messages."""
    def __init__(self):
        super().__init__()
        self.bot_logic = ChatbotLogic()
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("Python Shorts: Chatbot | Amey & Mega")
        self.setFixedSize(450, 650)
        self.setStyleSheet("background-color: #121212;")

        # Main Layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(15)

        # 1. Chat Display Area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFrameStyle(QFrame.NoFrame)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                border: 1px solid #2a2a2a;
                border-radius: 15px;
                padding: 15px;
                color: #e0e0e0;
                font-size: 15px;
            }
            QScrollBar:vertical {
                border: none;
                background: #1a1a1a;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #3a3a3c;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        self.layout.addWidget(self.chat_display)

        # 2. Input Area
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type a message...")
        self.input_field.setFixedHeight(45)
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #2a2a2a;
                border: none;
                border-radius: 22px;
                padding-left: 15px;
                padding-right: 15px;
                color: #ffffff;
                font-size: 14px;
            }
        """)
        self.input_field.returnPressed.connect(self.handle_send)

        self.send_btn = QPushButton("Send")
        self.send_btn.setFixedSize(85, 45)
        self.send_btn.setStyleSheet("""
            QPushButton {
                background-color: #007aff;
                color: white;
                border-radius: 22px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #0063cc; }
            QPushButton:pressed { background-color: #0051a8; }
        """)
        self.send_btn.clicked.connect(self.handle_send)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_btn)
        
        self.layout.addLayout(input_layout)
        self.setLayout(self.layout)

        # Initial Message from Filly
        self.add_bot_message("Hi! I am Filly. How can I assist you today?")

    def handle_send(self):
        text = self.input_field.text().strip()
        if text:
            self.add_user_message(text)
            self.input_field.clear()
            response = self.bot_logic.get_response(text)
            self.add_bot_message(response)

    def add_user_message(self, message):
        # User message: RIGHT-aligned using Qt-native QTextBlockFormat
        cursor = self.chat_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        # Set right alignment for this block
        block_format = QTextBlockFormat()
        block_format.setAlignment(Qt.AlignRight)
        cursor.insertBlock(block_format)
        
        # Insert the formatted message
        cursor.insertHtml(
            f"<span style='color: #af52de; font-size: 16px;'>👤 </span>"
            f"<span style='color: #af52de; font-weight: bold; font-size: 16px;'>You:</span><br>"
            f"<span style='color: #00ddff; font-size: 15px;'>{message}</span>"
        )
        
        # Add spacing
        cursor.insertBlock()
        self._scroll_to_bottom()


    def add_bot_message(self, message):
        # Bot message: LEFT-aligned using Qt-native QTextBlockFormat
        cursor = self.chat_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        # Set left alignment for this block
        block_format = QTextBlockFormat()
        block_format.setAlignment(Qt.AlignLeft)
        cursor.insertBlock(block_format)
        
        # Insert the formatted message
        cursor.insertHtml(
            f"<span style='color: #ffffff; font-size: 16px;'>🤖 </span>"
            f"<span style='color: #ff9f0a; font-weight: bold; font-size: 16px;'>Filly:</span><br>"
            f"<span style='color: #ff9f0a; font-size: 15px;'>{message}</span>"
        )
        
        # Add spacing
        cursor.insertBlock()
        self._scroll_to_bottom()

    def _scroll_to_bottom(self):
        scrollbar = self.chat_display.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

def main():
    app = QApplication(sys.argv)
    
    # Set default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    gui = ChatbotApp()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
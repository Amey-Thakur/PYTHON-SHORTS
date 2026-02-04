"""
File: Calculator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A professional, high-fidelity modern calculator application built with PyQt5. 
    It features a sophisticated dark-themed user interface with circular 
    buttons and responsive arithmetic logic.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    """
    High-Fidelity GUI Calculator with Modern Aesthetics.
    Matches the scholarly visual standard for Python Shorts.
    """
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("Python Shorts: Calculator")
        self.setFixedSize(350, 520)
        
        # General Widget Styling
        self.setStyleSheet("background-color: #0b0b0b;")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 30, 20, 20)
        layout.setSpacing(15)

        # Display Area
        self.display = QLineEdit()
        self.display.setFixedSize(310, 80)
        self.display.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.display.setReadOnly(True)
        self.display.setText("0")
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #121212;
                color: #ffffff;
                border: none;
                font-size: 48px;
                padding-right: 10px;
                font-family: 'Segoe UI', Arial;
            }
        """)
        layout.addWidget(self.display)

        # Button Grid
        grid = QGridLayout()
        grid.setSpacing(12)

        # Button Style Templates
        style_num = """
            QPushButton {
                background-color: #2b2b2b;
                color: white;
                border-radius: 35px;
                font-size: 24px;
                font-weight: bold;
                min-width: 70px;
                min-height: 70px;
            }
            QPushButton:hover { background-color: #3d3d3d; }
            QPushButton:pressed { background-color: #505050; }
        """
        style_op = """
            QPushButton {
                background-color: #ff9f0a;
                color: white;
                border-radius: 35px;
                font-size: 26px;
                font-weight: bold;
                min-width: 70px;
                min-height: 70px;
            }
            QPushButton:hover { background-color: #ffb13d; }
            QPushButton:pressed { background-color: #cc7f08; }
        """
        style_spec = """
            QPushButton {
                background-color: #a5a5a5;
                color: black;
                border-radius: 35px;
                font-size: 22px;
                font-weight: bold;
                min-width: 70px;
                min-height: 70px;
            }
            QPushButton:hover { background-color: #d4d4d4; }
            QPushButton:pressed { background-color: #8e8e8e; }
        """
        style_zero = """
            QPushButton {
                background-color: #2b2b2b;
                color: white;
                border-radius: 35px;
                font-size: 24px;
                font-weight: bold;
                min-height: 70px;
                padding-left: 25px;
                text-align: left;
            }
            QPushButton:hover { background-color: #3d3d3d; }
            QPushButton:pressed { background-color: #505050; }
        """

        # Row 1: Special Operators
        self._add_btn(grid, "C", 0, 0, style_spec)
        self._add_btn(grid, "DEL", 0, 1, style_spec)
        self._add_btn(grid, "%", 0, 2, style_spec)
        self._add_btn(grid, "/", 0, 3, style_op)

        # Row 2: 7-8-9-*
        self._add_btn(grid, "7", 1, 0, style_num)
        self._add_btn(grid, "8", 1, 1, style_num)
        self._add_btn(grid, "9", 1, 2, style_num)
        self._add_btn(grid, "*", 1, 3, style_op)

        # Row 3: 4-5-6--
        self._add_btn(grid, "4", 2, 0, style_num)
        self._add_btn(grid, "5", 2, 1, style_num)
        self._add_btn(grid, "6", 2, 2, style_num)
        self._add_btn(grid, "-", 2, 3, style_op)

        # Row 4: 1-2-3-+
        self._add_btn(grid, "1", 3, 0, style_num)
        self._add_btn(grid, "2", 3, 1, style_num)
        self._add_btn(grid, "3", 3, 2, style_num)
        self._add_btn(grid, "+", 3, 3, style_op)

        # Row 5: 0 - . - =
        zero_btn = QPushButton("0")
        zero_btn.setStyleSheet(style_zero)
        zero_btn.clicked.connect(self._on_click)
        grid.addWidget(zero_btn, 4, 0, 1, 2) # Spans 2 columns

        self._add_btn(grid, ".", 4, 2, style_num)
        self._add_btn(grid, "=", 4, 3, style_op)

        layout.addLayout(grid)
        self.setLayout(layout)

    def _add_btn(self, grid, text, r, c, style):
        btn = QPushButton(text)
        btn.setStyleSheet(style)
        btn.clicked.connect(self._on_click)
        grid.addWidget(btn, r, c)

    def _on_click(self) -> None:
        sender = self.sender()
        if not sender: return
        text = sender.text()
        current = self.display.text()

        if text == "C":
            self.display.setText("0")
        elif text == "DEL":
            if len(current) > 1:
                self.display.setText(current[:-1])
            else:
                self.display.setText("0")
        elif text == "=":
            try:
                # Replace visual operators with Python logic
                expr = current.replace("x", "*").replace("%", "/100")
                result = str(eval(expr))
                # Format to avoid long decimals
                if "." in result and len(result) > 10:
                    result = format(float(result), ".6f").rstrip("0").rstrip(".")
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            if current == "0" and text != ".":
                self.display.setText(text)
            else:
                self.display.setText(current + text)

def main() -> None:
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
File: Calculator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A professional, modern calculator application built with PyQt5. 
    It supports basic arithmetic operations and features a high-fidelity 
    dark-themed user interface.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    """
    Standard GUI Calculator with Modern Aesthetics.
    """
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("Python Shorts: Calculator | Amey & Mega")
        self.setFixedSize(320, 450)
        
        # UI Styling (Dark Theme)
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; }
            QLineEdit {
                background-color: #252526;
                color: #ffffff;
                border: none;
                padding: 15px;
                font-size: 26px;
                margin-bottom: 10px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #333333;
                color: #e0e0e0;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                min-height: 50px;
            }
            QPushButton:hover { background-color: #444444; }
            QPushButton#action { background-color: #0078d4; }
            QPushButton#action:hover { background-color: #0086f0; }
            QPushButton#equal { background-color: #107c10; }
            QPushButton#equal:hover { background-color: #108e10; }
        """)

        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3, 'action'),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3, 'action'),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3, 'action'),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2, 'equal'), ('+', 3, 3, 'action'),
        ]

        for btn_text, r, c, *extra in buttons:
            button = QPushButton(btn_text)
            if extra:
                button.setObjectName(extra[0])
            button.clicked.connect(self._on_click)
            grid.addWidget(button, r, c)

        layout.addLayout(grid)
        self.setLayout(layout)

    def _on_click(self) -> None:
        sender = self.sender()
        if not sender:
            return
            
        text = sender.text() # type: ignore

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                # Security Note: eval is used here for a simple calculator script, 
                # but should be restricted in production environments.
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

def main() -> None:
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
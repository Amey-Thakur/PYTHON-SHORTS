"""
File: Calendar.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity calendar application built with PyQt5. It features 
    a modern dark-mode interface and allows users to browse dates with 
    professional styling.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
)
from PyQt5.QtCore import Qt, QDate

class CalendarApp(QWidget):
    """
    Modern Calendar Application with Scholarly Aesthetics.
    """
    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("Python Shorts: Calendar | Amey & Mega")
        self.setFixedSize(400, 450)
        
        # UI Styling (Dark Theme)
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #ffffff; }
            QCalendarWidget QWidget { alternate-background-color: #252526; }
            QCalendarWidget QAbstractItemView:enabled {
                color: #e0e0e0;
                background-color: #1e1e1e;
                selection-background-color: #0078d4;
                selection-color: #ffffff;
            }
            QCalendarWidget QToolButton {
                background-color: #333333;
                color: #ffffff;
                border-radius: 4px;
                margin: 5px;
            }
            QCalendarWidget QMenu { background-color: #252526; }
            QCalendarWidget QSpinBox { background-color: #252526; color: #ffffff; }
            QLabel { font-size: 16px; margin: 10px; }
        """)

        layout = QVBoxLayout()
        
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.selectionChanged.connect(self._show_date)
        layout.addWidget(self.calendar)

        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignCenter)
        self._show_date() # Set initial date text
        layout.addWidget(self.label)

        self.setLayout(layout)

    def _show_date(self) -> None:
        date: QDate = self.calendar.selectedDate()
        self.label.setText(f"Selected Date: {date.toString('MMMM d, yyyy')}")

def main() -> None:
    app = QApplication(sys.argv)
    cal = CalendarApp()
    cal.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
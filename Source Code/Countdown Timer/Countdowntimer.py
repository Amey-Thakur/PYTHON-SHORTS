"""
File: Countdowntimer.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity premium countdown timer implemented in PyQt5. Features 
    advanced custom painting for a dynamic circular progress indicator, 
    glassmorphic UI elements, and precise temporal synchronization.
"""

import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QHBoxLayout, QGraphicsDropShadowEffect, QFrame
)
from PyQt5.QtCore import QTimer, Qt, QRectF, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QAntialiasing

class CircularProgressBar(QWidget):
    """Custom circular progress indicator with high-precision rendering."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0
        self._max = 100
        self.setMinimumSize(220, 220)

    @pyqtProperty(float)
    def value(self): return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.update()

    def set_max(self, m):
        self._max = m
        self.update()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        thickness = 12
        margin = 15
        rect = QRectF(margin, margin, width - 2*margin, height - 2*margin)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Background track
        painter.setPen(QPen(QColor("#161b22"), thickness))
        painter.drawEllipse(rect)

        # Active progress arc
        if self._max > 0:
            angle = -360 * (self._value / self._max)
            grad = QPen(QColor("#58a6ff"), thickness)
            grad.setCapStyle(Qt.RoundCap)
            painter.setPen(grad)
            painter.drawArc(rect, 90 * 16, int(angle * 16))

class PremiumTimer(QWidget):
    """High-fidelity Countdown Timer with Glassmorphic Interface."""
    def __init__(self) -> None:
        super().__init__()
        self.total_seconds = 0
        self.seconds_left = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("Python Shorts: Precision Chronometer")
        self.setFixedSize(400, 450)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        # Main Container with Glassmorphism
        self.container = QFrame(self)
        self.container.setGeometry(10, 10, 380, 430)
        self.container.setStyleSheet("""
            QFrame {
                background-color: rgba(13, 17, 23, 0.95);
                border: 1px solid #30363d;
                border-radius: 24px;
            }
            QLabel { color: #8b949e; border: none; background: transparent; }
            QLineEdit {
                background-color: #161b22;
                color: #58a6ff;
                border: 2px solid #30363d;
                padding: 10px;
                font-size: 18px;
                border-radius: 12px;
                font-weight: bold;
            }
            QLineEdit:focus { border: 2px solid #58a6ff; }
            QPushButton {
                background-color: #238636;
                color: #ffffff;
                border: none;
                padding: 12px;
                border-radius: 12px;
                font-size: 14px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover { background-color: #2ea043; }
            QPushButton#closeBtn {
                background-color: transparent;
                color: #484f58;
                font-size: 20px;
                min-width: 30px;
            }
            QPushButton#closeBtn:hover { color: #f85149; }
            QPushButton#resetBtn { background-color: #30363d; color: #c9d1d9; }
            QPushButton#resetBtn:hover { background-color: #363c44; }
        """)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 5)
        self.container.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(30, 20, 30, 30)
        layout.setSpacing(20)

        # Header
        header = QHBoxLayout()
        title = QLabel("CHRONOMETER")
        title.setFont(QFont("Arial", 10, QFont.Bold))
        header.addWidget(title)
        
        close_btn = QPushButton("×")
        close_btn.setObjectName("closeBtn")
        close_btn.clicked.connect(self.close)
        header.addWidget(close_btn, 0, Qt.AlignRight)
        layout.addLayout(header)

        # Progress Indicator
        self.progress_ring = CircularProgressBar()
        layout.addWidget(self.progress_ring, 0, Qt.AlignCenter)

        # Time Display Overlay (Centered in Ring)
        self.time_display = QLabel("00:00", self.progress_ring)
        self.time_display.setGeometry(0, 0, 220, 220)
        self.time_display.setAlignment(Qt.AlignCenter)
        self.time_display.setStyleSheet("font-size: 48px; color: #ffffff; font-weight: 300;")

        # Controls
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Interval (seconds)...")
        self.input_field.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.input_field)

        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("INITIATE")
        self.start_btn.clicked.connect(self._start_timer)
        btn_layout.addWidget(self.start_btn)

        self.reset_btn = QPushButton("RESET")
        self.reset_btn.setObjectName("resetBtn")
        self.reset_btn.clicked.connect(self._reset_timer)
        btn_layout.addWidget(self.reset_btn)
        layout.addLayout(btn_layout)

    def _start_timer(self) -> None:
        try:
            val = self.input_field.text().strip()
            if not val: return
            self.total_seconds = int(val)
            self.seconds_left = self.total_seconds
            if self.seconds_left <= 0: raise ValueError
            
            self.progress_ring.set_max(self.total_seconds)
            self.progress_ring.value = self.total_seconds
            
            self.input_field.setEnabled(False)
            self.start_btn.setEnabled(False)
            self.timer.start(1000)
            self._update_ui()
            print(f"[Timer Started]: {self.total_seconds} seconds")
        except ValueError:
            self.time_display.setText("ERROR")

    def _reset_timer(self) -> None:
        self.timer.stop()
        self.seconds_left = 0
        self.progress_ring.value = 0
        self.time_display.setText("00:00")
        self.input_field.setEnabled(True)
        self.start_btn.setEnabled(True)
        self.input_field.clear()
        print("[Timer Reset]")

    def _tick(self) -> None:
        if self.seconds_left > 0:
            self.seconds_left -= 1
            self.progress_ring.value = self.seconds_left
            self._update_ui()
        else:
            self.timer.stop()
            self.time_display.setText("EXP")
            self.input_field.setEnabled(True)
            self.start_btn.setEnabled(True)
            print("[Timer Expired]")

    def _update_ui(self) -> None:
        mins, secs = divmod(self.seconds_left, 60)
        self.time_display.setText(f"{mins:02d}:{secs:02d}")

    # Allow dragging
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

from PyQt5.QtCore import QPoint

def main():
    app = QApplication(sys.argv)
    window = PremiumTimer()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
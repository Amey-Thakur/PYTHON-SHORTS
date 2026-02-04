"""
File: Calendar.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License
"""

import sys
import calendar
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
    QLabel, QPushButton, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QColor, QPainter, QLinearGradient

class WheelPicker(QScrollArea):
    """
    Custom Scroller Widget mimicking the Apple iOS Wheel Picker.
    """
    selected = pyqtSignal(int)

    def __init__(self, items, item_height=50, visible_count=5):
        super().__init__()
        self.items = list(items)  # Ensure it's a list
        self.item_height = item_height
        self.visible_count = visible_count
        self.selected_index = 0
        self._initializing = True  # Flag to prevent signals during init
        
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("background: transparent; border: none;")
        self.setFocusPolicy(Qt.StrongFocus)  # Enable keyboard focus
        
        self.content = QWidget()
        self.content.setStyleSheet("background: transparent;")
        self.layout = QVBoxLayout(self.content)
        # Margin = 1 item height on each side so centered item aligns with selection
        padding = (visible_count // 2) * item_height
        self.layout.setContentsMargins(0, padding, 0, padding)
        self.layout.setSpacing(0)
        
        self.labels = []
        for text in items:
            lbl = QLabel(str(text))
            lbl.setFixedHeight(item_height)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: #444444; font-size: 18px; font-weight: bold;")
            self.layout.addWidget(lbl)
            self.labels.append(lbl)
            
        self.setWidget(self.content)
        self.setFixedHeight(item_height * visible_count)
        
        self.verticalScrollBar().valueChanged.connect(self._on_scroll)
        
        # Snapping timer
        self.snap_timer = QTimer()
        self.snap_timer.setSingleShot(True)
        self.snap_timer.timeout.connect(self._snap_to_closest)

    def _on_scroll(self, value):
        if not self.labels:
            return
        center_y = value + (self.height() / 2)
        
        for i, lbl in enumerate(self.labels):
            # Use geometry from layout since y() may not be ready
            lbl_y = self.layout.itemAt(i).geometry().y() if self.layout.itemAt(i) else 0
            lbl_center = lbl_y + (self.item_height / 2)
            dist = abs(center_y - lbl_center)
            
            # Visual effect: Scale and fade based on distance from center
            max_dist = self.height() / 2
            if dist < max_dist:
                ratio = 1 - (dist / max_dist)
                size = 18 + int(12 * ratio)
                opacity = int(100 + 155 * ratio)
                color = f"rgba(255, 159, 10, {opacity})" if dist < self.item_height/2 else f"rgba(255, 255, 255, {opacity})"
                lbl.setStyleSheet(f"color: {color}; font-size: {size}px; font-weight: bold;")
            else:
                lbl.setStyleSheet("color: #444444; font-size: 18px; font-weight: bold;")

        self.snap_timer.start(100) # Restart snap timer on scroll

    def _snap_to_closest(self):
        val = self.verticalScrollBar().value()
        # More precise index calculation
        idx = int(round(val / self.item_height))
        idx = max(0, min(idx, len(self.items) - 1))  # Clamp to valid range
        self.selected_index = idx
        
        target_val = idx * self.item_height
        
        # Only animate if difference is significant
        if abs(val - target_val) > 2:
            self.animation = QPropertyAnimation(self.verticalScrollBar(), b"value")
            self.animation.setDuration(150)
            self.animation.setStartValue(val)
            self.animation.setEndValue(target_val)
            self.animation.setEasingCurve(QEasingCurve.OutCubic)
            self.animation.start()
        else:
            self.verticalScrollBar().setValue(target_val)
        self.selected_index = idx
        
        # Only emit if not during initialization
        if not self._initializing:
            self.selected.emit(idx)

    def set_index(self, idx):
        # Defer the scrolling until the widget is shown
        QTimer.singleShot(100, lambda: self._do_set_index(idx))

    def _do_set_index(self, idx):
        idx = max(0, min(idx, len(self.items) - 1))
        self.verticalScrollBar().setValue(idx * self.item_height)
        self.selected_index = idx
        self._initializing = False  # Done initializing

    def get_selected_value(self):
        """Returns the currently selected item value."""
        if 0 <= self.selected_index < len(self.items):
            return self.items[self.selected_index]
        return self.items[0] if self.items else None

    def keyPressEvent(self, event):
        """Handle keyboard navigation."""
        if event.key() == Qt.Key_Up:
            new_idx = max(0, self.selected_index - 1)
            self.verticalScrollBar().setValue(new_idx * self.item_height)
            self.selected_index = new_idx
            self.selected.emit(new_idx)
        elif event.key() == Qt.Key_Down:
            new_idx = min(len(self.items) - 1, self.selected_index + 1)
            self.verticalScrollBar().setValue(new_idx * self.item_height)
            self.selected_index = new_idx
            self.selected.emit(new_idx)
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        """Improved wheel event for smoother scrolling."""
        delta = event.angleDelta().y()
        if delta > 0:
            new_idx = max(0, self.selected_index - 1)
        else:
            new_idx = min(len(self.items) - 1, self.selected_index + 1)
        self.verticalScrollBar().setValue(new_idx * self.item_height)
        self.selected_index = new_idx
        self.selected.emit(new_idx)
        event.accept()

class CalendarApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("Python Shorts: Calendar | Amey & Mega")
        self.setFixedSize(480, 680)
        self.setStyleSheet("background-color: #000000; color: white; font-family: 'Segoe UI', Arial;")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)

        # 1. Header with Pickers
        picker_layout = QHBoxLayout()
        
        self.month_picker = WheelPicker(calendar.month_name[1:], item_height=40, visible_count=3)
        self.month_picker.selected.connect(self._on_month_selected)
        self.month_picker.set_index(self.current_month - 1)
        
        years = list(range(1975, 2101))  # 1975 to 2100
        self.years_list = years
        self.year_picker = WheelPicker(years, item_height=40, visible_count=3)
        self.year_picker.selected.connect(self._on_year_selected)  # Pass index directly
        # Find current year index
        current_year_idx = years.index(self.current_year) if self.current_year in years else 51
        self.year_picker.set_index(current_year_idx)

        picker_layout.addWidget(self.month_picker)
        picker_layout.addWidget(self.year_picker)
        self.main_layout.addLayout(picker_layout)

        # 2. Weekday Headers
        self.weekdays_grid = QGridLayout()
        self.weekdays_grid.setSpacing(10)
        for col, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
            lbl = QLabel(day)
            lbl.setStyleSheet("color: #ff9f0a; font-weight: bold; font-size: 16px;")
            lbl.setAlignment(Qt.AlignCenter)
            self.weekdays_grid.addWidget(lbl, 0, col)
        self.main_layout.addLayout(self.weekdays_grid)

        # 3. Days Grid
        self.grid_container = QWidget()
        self.grid = QGridLayout(self.grid_container)
        self.grid.setSpacing(10)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.grid_container)

        # 4. Selection Footer
        self.selection_label = QLabel("Designed by Amey & Mega")
        self.selection_label.setStyleSheet("color: #8e8e93; font-size: 14px; margin-top: 10px;")
        self.selection_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.selection_label)

        self._update_calendar()
        self.setLayout(self.main_layout)

    def _update_calendar(self) -> None:
        while self.grid.count():
            child = self.grid.takeAt(0)
            if child.widget(): child.widget().deleteLater()

        month_days = calendar.monthcalendar(self.current_year, self.current_month)
        self.day_style = "QPushButton { background-color: #1c1c1e; color: white; border-radius: 12px; font-size: 18px; min-width: 50px; min-height: 50px; border: none; } QPushButton:hover { background-color: #2c2c2e; border: 1px solid #ff9f0a; }"
        self.selected_style = "QPushButton { background-color: #ff9f0a; color: black; border-radius: 12px; font-size: 18px; min-width: 50px; min-height: 50px; border: none; font-weight: bold; }"
        
        today = datetime.now()
        self.day_buttons = {}  # Track buttons by day number
        
        for row, week in enumerate(month_days):
            for col, day in enumerate(week):
                if day != 0:
                    btn = QPushButton(str(day))
                    btn.setStyleSheet(self.day_style)
                    # Highlight today with orange border
                    if day == today.day and self.current_month == today.month and self.current_year == today.year:
                         btn.setStyleSheet(self.day_style + "border: 1px solid #ff9f0a; color: #ff9f0a;")
                    btn.clicked.connect(lambda checked, d=day, b=btn: self._on_day_clicked(d, b))
                    self.day_buttons[day] = btn
                    self.grid.addWidget(btn, row, col)

    def _on_day_clicked(self, day: int, btn: QPushButton) -> None:
        # Reset all buttons to default style
        for d, button in self.day_buttons.items():
            button.setStyleSheet(self.day_style)
        
        # Highlight clicked button with solid orange
        btn.setStyleSheet(self.selected_style)
        
        # Update footer label
        selected_date = datetime(self.current_year, self.current_month, day)
        self.selection_label.setText(selected_date.strftime("%A, %B %d, %Y"))
        self.selection_label.setStyleSheet("color: #ff9f0a; font-size: 18px; font-weight: bold;")

    def _on_month_selected(self, idx):
        # Get the actual value from the picker to ensure sync
        if 0 <= idx < 12:
            self.current_month = idx + 1
            self._update_calendar()

    def _on_year_selected(self, idx):
        if 0 <= idx < len(self.years_list):
            self.current_year = self.years_list[idx]
            self._update_calendar()

def main() -> None:
    app = QApplication(sys.argv)
    cal = CalendarApp()
    cal.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

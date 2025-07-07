from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QLabel,
    QStackedWidget,
)

import sys


class BasePage(QWidget):
    """Base class for all pages with common functionality"""

    def __init__(self, title):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.title = QLabel(f"<h1>{title}</h1>")
        self.layout.addWidget(self.title)

    def addContent(self, content):
        """Add content to the page"""
        self.layout.addWidget(content)

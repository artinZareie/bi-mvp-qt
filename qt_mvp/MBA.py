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

from BasePage import BasePage

import sys


class MBA(BasePage):
    def __init__(self):
        super().__init__("Market Basket Analysis")

        content = QLabel("This page currently contains bullshit.")

        self.addContent(content)

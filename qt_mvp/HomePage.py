from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

import sys

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Intelligent ERP MVP")

        self.button = QPushButton("Smash me!")

        self.button.clicked.connect(
            lambda checked: print("Full of cum")
        )

        self.setCentralWidget(self.button)
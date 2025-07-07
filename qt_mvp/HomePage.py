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
from MBA import MBA
from SeasonalTrendAnalysis import SeasonalTrendAnalysis

import sys

SIDEBAR_STYLESHIT = """
QListWidget {
    border: none;
    font-size: 14px;
}
QListWidget::item {
    padding: 10px;
    border-bottom: 1px solid;
}
"""

SIDEBAR_MENU_ITEMS = [
    ("Market Basket Analysis", "market_basket", MBA),
    ("Seasonal Trend Analysis", "seasonal_trend", SeasonalTrendAnalysis),
]


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Intelligent ERP MVP")

        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self._create_sidebar()
        self._create_main_content()

        self.main_layout.addWidget(self.sidebar, 1)
        self.main_layout.addWidget(self.main_content, 4)

        self.setCentralWidget(self.main_widget)

    def _create_sidebar(self):
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(300)
        self.sidebar.setStyleSheet(SIDEBAR_STYLESHIT)

        self.menu_items = SIDEBAR_MENU_ITEMS

        for text, icon_name, _ in self.menu_items:
            item = QListWidgetItem(text)
            item.setData(Qt.UserRole, icon_name)
            self.sidebar.addItem(item)

        self.sidebar.currentRowChanged.connect(self._change_page)

    def _create_main_content(self):
        self.main_content = QStackedWidget()

        self.pages = {}

        for _, icon_name, page in SIDEBAR_MENU_ITEMS:
            page = page()
            self.pages[icon_name] = page
            self.main_content.addWidget(page)

        self.sidebar.setCurrentRow(0)
        self.main_content.setCurrentIndex(0)

    def _change_page(self, index):
        if 0 <= index < len(self.menu_items):
            page_name = self.menu_items[index][1]
            page_index = list(self.pages.keys()).index(page_name)
        self.main_content.setCurrentIndex(page_index)

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
    ("Market Basket Analysis", "market_basket"),
    ("Seasonal Trend Analysis", "seasonal_trend"),
    ("Dashboard", "dashboard"),
    ("Reports", "reports"),
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

        for text, icon in self.menu_items:
            item = QListWidgetItem(text)
            item.setData(Qt.UserRole, icon)
            self.sidebar.addItem(item)

        self.sidebar.currentRowChanged.connect(self._change_page)

    def _create_main_content(self):
        self.main_content = QStackedWidget()

        self.pages = {}

        market_basket_page = QWidget()
        market_basket_layout = QVBoxLayout()
        market_basket_layout.addWidget(QLabel("<h1>Market Basket Analysis</h1>"))
        market_basket_layout.addWidget(
            QLabel("This page will contain market basket analysis tools.")
        )
        market_basket_page.setLayout(market_basket_layout)
        self.pages["market_basket"] = market_basket_page

        seasonal_trend_page = QWidget()
        seasonal_trend_layout = QVBoxLayout()
        seasonal_trend_layout.addWidget(QLabel("<h1>Seasonal Trend Analysis</h1>"))
        seasonal_trend_layout.addWidget(
            QLabel("This page will contain seasonal trend analysis tools.")
        )
        seasonal_trend_page.setLayout(seasonal_trend_layout)
        self.pages["seasonal_trend"] = seasonal_trend_page

        dashboard_page = QWidget()
        dashboard_layout = QVBoxLayout()
        dashboard_layout.addWidget(QLabel("<h1>Dashboard</h1>"))
        dashboard_layout.addWidget(
            QLabel("This is the main dashboard with key metrics.")
        )
        dashboard_page.setLayout(dashboard_layout)
        self.pages["dashboard"] = dashboard_page

        reports_page = QWidget()
        reports_layout = QVBoxLayout()
        reports_layout.addWidget(QLabel("<h1>Reports</h1>"))
        reports_layout.addWidget(QLabel("This page will contain various reports."))
        reports_page.setLayout(reports_layout)
        self.pages["reports"] = reports_page

        for page_name, page_widget in self.pages.items():
            self.main_content.addWidget(page_widget)

        self.sidebar.setCurrentRow(2)

    def _change_page(self, index):
        if 0 <= index < len(self.menu_items):
            page_name = self.menu_items[index][1]
            page_index = list(self.pages.keys()).index(page_name)
        self.main_content.setCurrentIndex(page_index)

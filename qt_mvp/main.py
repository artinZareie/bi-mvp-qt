from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from HomePage import *

import sys


# Entry point of the program
def main():
    print("Willkommen")

    app = QApplication(sys.argv)

    main_window = HomePage()
    main_window.showMaximized()

    app.exec()


if __name__ == "__main__":
    main()

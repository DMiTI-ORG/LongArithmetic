from LongArithmetic.app import App
from PyQt6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = App()
    application.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import QWidget


class Screen(QWidget):
    def __init__(self, class_name):
        super().__init__()
        self.ui = class_name
        self.ui.setupUi(self)
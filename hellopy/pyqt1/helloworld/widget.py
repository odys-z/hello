# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget

from anclient import Anclient

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.bDialog.clicked.connect(self.onDialog)

    @Slot()
    def onDialog(self, check):
        print(self.ui.bDialog)
        print(check)
        x = Anclient()
        ip = self.ui.txtIP.text()
        print(self.ui.txtIP, ip)
        x.ping(self.ui.txtIP.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

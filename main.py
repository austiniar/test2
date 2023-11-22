import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QWidget


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circle_coords = None
        self.init_ui()
        self.show()

    def init_ui(self):
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.circle_coords = [random.randrange(0, 500) for i in range(2)]
        self.repaint()

    def paintEvent(self, event):
        if self.circle_coords:
            painter = QPainter(self)
            painter.begin(self)

            diameter = random.randrange(10, 401)
            painter.setPen(QPen(QColor(0, 0, 0), 5))
            painter.setBrush(QBrush(QColor(255, 255, 0)))
            painter.drawEllipse(*self.circle_coords, diameter, diameter)

            painter.end()
            self.circle_coords = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    sys.exit(app.exec())

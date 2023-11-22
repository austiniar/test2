import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic.properties import QtCore, QtGui
from pyqt5_plugins.examplebutton import QtWidgets


class Ui_Circles(object):
    def setupUi(self, Circles):
        Circles.setObjectName("Circles")
        Circles.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Circles.sizePolicy().hasHeightForWidth())
        Circles.setSizePolicy(sizePolicy)
        Circles.setMinimumSize(QSize(600, 600))
        Circles.setMaximumSize(QSize(600, 600))
        self.pushButton = QtWidgets.QPushButton(Circles)
        self.pushButton.setGeometry(QRect(170, 230, 261, 91))
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Circles)
        QMetaObject.connectSlotsByName(Circles)

    def retranslateUi(self, Circles):
        _translate = QCoreApplication.translate
        Circles.setWindowTitle(_translate("Circles", "Form"))
        self.pushButton.setText(_translate("Circles", "Нарисовать случайный круг"))


class Circles(QWidget, Ui_Circles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            painter.setBrush(QBrush(QColor(*(random.randrange(0, 256) for i in range(3)))))
            painter.drawEllipse(*self.circle_coords, diameter, diameter)

            painter.end()
            self.circle_coords = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    sys.exit(app.exec())

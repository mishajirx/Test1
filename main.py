import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QMainWindow
from random import randint


class PaintFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.q = 10
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.change_flag)

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое, 
    # например, при создании формы

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()

    def change_flag(self):
        self.flag = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(int(self.q)):
            x = randint(0, 600)
            y = randint(0, 800)
            r = randint(0, 200)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PaintFlag()
    ex.show()
    sys.exit(app.exec())

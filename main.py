import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QMainWindow
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 220, 150))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Press"))


class PaintFlag(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.q = 10
        # uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setupUi(self)
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
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            x = randint(0, 600)
            y = randint(0, 800)
            r = randint(0, 200)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PaintFlag()
    ex.show()
    sys.exit(app.exec())

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_MainWindow
from triangle import Ui_TriangleWindow
from rectangle import Ui_RectangleWindow
from parallelogram import Ui_ParallelogramWindow

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def open_triangle():
    global Triangle
    Triangle = QtWidgets.QMainWindow()
    ui = Ui_TriangleWindow()
    ui.setupUi(Triangle)
    MainWindow.close()
    Triangle.show()

    def open_main():
        Triangle.close()
        MainWindow.show()

    ui.pushButton.clicked.connect(open_main)
def open_rectangle():
    global Rectangle
    Rectangle = QtWidgets.QMainWindow()
    ui = Ui_RectangleWindow()
    ui.setupUi(Rectangle)
    MainWindow.close()
    Rectangle.show()

    def open_main():
        Rectangle.close()
        MainWindow.show()

    ui.pushButton.clicked.connect(open_main)
def open_parallelogram():
    global Parallelogram
    Parallelogram = QtWidgets.QMainWindow()
    ui = Ui_ParallelogramWindow()
    ui.setupUi(Parallelogram)
    MainWindow.close()
    Parallelogram.show()

    def open_main():
        Parallelogram.close()
        MainWindow.show()

    ui.pushButton.clicked.connect(open_main)

ui.pushButton_3.clicked.connect(open_parallelogram)
ui.pushButton_2.clicked.connect(open_triangle)
ui.pushButton.clicked.connect(open_rectangle)
sys.exit(app.exec_())

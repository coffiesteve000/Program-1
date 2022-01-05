from PyQt6 import QtCore, QtGui, QtWidgets, uic
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    MainWindow = uic.loadUi("Main.ui")
    MainWindow.showMaximized()
    MainWindow.show()
    df=app.exec()
    sys.exit(df)
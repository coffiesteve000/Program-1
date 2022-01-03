from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6 import QtCore, QtGui, QtWidgets
from addCustomer import Ui_widget
from __init__ import CustomerDb

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 563)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 591, 511))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(113)
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(500, 530, 101, 24))
        self.addButton.setStyleSheet("color: rgb(255, 255, 255);\n"
            "background-color: rgb(0, 0, 255);\n"
            "selection-color: rgb(15, 15, 255);")
        self.addButton.setObjectName("addButton")
        
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(300, 530, 101, 24))
        self.refreshButton.setStyleSheet("color: rgb(255, 255, 255);\n"
            "background-color: rgb(0, 0, 255);\n"
            "selection-color: rgb(15, 15, 255);")
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.load_customer_details)
        self.addButton.clicked.connect(self.call_add_customer_widget)

        #start method on load
        self.load_customer_details()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def load_customer_details(self):
        Customerdb = CustomerDb() # instance of the class
        customer_details = Customerdb.return_all_data() # data from database
        self.tableWidget.setRowCount(0) # first set the row count of the tablke to zero
        # Now loop thru the customer_details and insert into database
        for row_number, row_Data in enumerate(customer_details):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_Data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def call_add_customer_widget(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_widget()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Service"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Cost"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.addButton.setText(_translate("Form", "Add Customer"))
        self.refreshButton.setText(_translate("Form", "Refresh List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

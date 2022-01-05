from PyQt6 import QtCore, QtGui, QtWidgets, uic
import sys
from link import CustomerDB
from PyQt6.QtWidgets import QMessageBox
import re
class Ui_MainWindow:
    def __init__(self) -> None:
        self.CustomerDb = CustomerDB() # Initialize db
    
    def load_customer_details(self):
        Customer_details = self.CustomerDb.return_all()
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(Customer_details):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def set_date(self):
        from datetime import date
        today = date.today()
        self.dateEdit.setDate(today)

    def insert_data(self):
        """Add data to database
        
        Keyword arguments:
        Return -- Return success or unsuccess.
        """
        
        Customerdb = CustomerDB()
        name = self.nameEdit.text().strip()
        contact = self.contactEdit.text().strip()
        service = self.serviceEdit.toPlainText().strip()
        cost = self.costEdit.text().strip()
        date = self.dateEdit.text().strip()
        all_inputs = [name, contact, service, cost, date]
        each_value = any([self.is_input_empty_or_not(each_input) for each_input in all_inputs])
        
        if each_value:
            self.error_message_color()
            self.label.setText("Provide all data")
            return
        else: pass

        response = Customerdb.insert_into_db(name, contact, service, cost, date)
        if response == "Added Successfully":
            self.success_message_color()
            self.set_fields_empty()
            self.load_customer_details()
            self.label.setText(response)

    def is_input_empty_or_not(self,each_input):
        """Check whether the all the input the user provided are not empty
        
        Keyword arguments:
        each_input -- Each values in the list inputs.
        Return: Return a match of search. Whether the results contains empty spaces or empty.
        """
        return re.search("^\s*$", each_input)

    def set_fields_empty(self):
        self.nameEdit.setText("")
        self.contactEdit.setText("")
        self.serviceEdit.setPlaceholderText("Enter Service Details here")
        self.costEdit.setText("")


    def cancel(self):
        if True:
            mes = QMessageBox.question(QMessageBox(), 
                        'Confirm', 'Are you sure you want to exit? Save all data in the input field if there is any before exit ', 
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if mes == QMessageBox.StandardButton.Yes:
                # sys.exit()
                self.set_fields_empty()
            else:
                return
            
    def error_message_color(self):
        self.label.setStyleSheet("color: rgb(170, 0, 0);")
        
    def success_message_color(self):
        self.label.setStyleSheet("color: rgb(0, 170, 0);")
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    MainWindow = uic.loadUi("Main.ui")
    # start method
    MainWindow.load_customer_details()
    MainWindow.set_date()
    # MainWindow.tableWidget.setItem(1,5,QtWidgets.QTableWidgetItem(data))

    # click events
    MainWindow.saveButton.clicked.connect(MainWindow.insert_data)
    MainWindow.cancelButton.clicked.connect(MainWindow.cancel)

    #----------- Validators --------------#
    onlyfloat = QtGui.QDoubleValidator()
    onlyInt = QtGui.QIntValidator()
    MainWindow.contactEdit.setValidator(onlyInt)
    MainWindow.costEdit.setValidator(onlyfloat)
    #----------- Validators End--------------#
    MainWindow.showMaximized()
    MainWindow.show()
    df=app.exec()
    sys.exit(df)
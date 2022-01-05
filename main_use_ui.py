from PyQt6 import QtGui, QtWidgets, uic
import sys
from link import CustomerDB
from PyQt6.QtWidgets import QMessageBox
import re
CustomerDb = CustomerDB() # Initialize db
class setupUi:
    def load_customer_details():
        Customer_details = CustomerDb.return_all()
        MainWindow.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(Customer_details):
            MainWindow.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                MainWindow.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def set_date():
        from datetime import date
        today = date.today()
        MainWindow.dateEdit.setDate(today)

    def insert_data():
        """Add data to database
        
        Keyword arguments:
        Return -- Return success or unsuccess.
        """
        
        Customerdb = CustomerDB()
        name = MainWindow.nameEdit.text().strip()
        contact = MainWindow.contactEdit.text().strip()
        service = MainWindow.serviceEdit.toPlainText().strip()
        cost = MainWindow.costEdit.text().strip()
        date = MainWindow.dateEdit.text().strip()
        all_inputs = [name, contact, service, cost, date]
        each_value = any([setupUi.is_input_empty_or_not(each_input) for each_input in all_inputs])
        
        if each_value:
            setupUi.error_message_color()
            MainWindow.label.setText("Provide all data")
            return
        else: pass

        response = Customerdb.insert_into_db(name, contact, service, cost, date)
        if response == "Added Successfully":
            setupUi.success_message_color()
            setupUi.set_fields_empty()
            setupUi.load_customer_details()
            MainWindow.label.setText(response)

    def is_input_empty_or_not(each_input):
        """Check whether the all the input the user provided are not empty
        
        Keyword arguments:
        each_input -- Each values in the list inputs.
        Return: Return a match of search. Whether the results contains empty spaces or empty.
        """
        return re.search("^\s*$", each_input)

    def set_fields_empty():
        MainWindow.nameEdit.setText("")
        MainWindow.contactEdit.setText("")
        MainWindow.serviceEdit.setPlaceholderText("Enter Service Details here")
        MainWindow.costEdit.setText("")


    def cancel():
        if True:
            mes = QMessageBox.question(QMessageBox(), 
                        'Confirm', 'Are you sure you want to exit? Save all data in the input field if there is any before exit ', 
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if mes == QMessageBox.StandardButton.Yes:
                # sys.exit()
                setupUi.set_fields_empty()
            else:
                return
            
    def error_message_color():
        MainWindow.label.setStyleSheet("color: rgb(170, 0, 0);")
        
    def success_message_color():
        MainWindow.label.setStyleSheet("color: rgb(0, 170, 0);")
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    MainWindow = uic.loadUi("Main.ui")
    # start method
    setupUi.load_customer_details()
    setupUi.set_date()
    # MainWindow.tableWidget.setItem(1,5,QtWidgets.QTableWidgetItem(data))

    # click events
    MainWindow.saveButton.clicked.connect(setupUi.insert_data)
    MainWindow.cancelButton.clicked.connect(setupUi.cancel)

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
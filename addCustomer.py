from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sys
from __init__ import CustomerDb


class Ui_widget(object):


    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(500, 415)
        widget.setStyleSheet("")
        self.saveButton = QtWidgets.QPushButton(widget)
        self.saveButton.setGeometry(QtCore.QRect(120, 350, 91, 41))
        self.saveButton.setMouseTracking(True)
        self.saveButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(widget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setGeometry(QtCore.QRect(260, 350, 91, 41))
        self.cancelButton.setMouseTracking(True)
        self.cancelButton.setStyleSheet("background-color: rgb(255, 21, 0);\n"
"font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.cancelButton.setObjectName("cancelButton")

        self.cancelButton.clicked.connect(self.close_window)

        self.layoutWidget = QtWidgets.QWidget(widget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 40, 301, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.name = QtWidgets.QLabel(self.layoutWidget)
        self.name.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.name.setObjectName("name")
        self.nameLayout.addWidget(self.name)
        self.nameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.nameLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.nameLayout)
        self.contactLayout = QtWidgets.QHBoxLayout()
        self.contactLayout.setObjectName("contactLayout")
        self.contact = QtWidgets.QLabel(self.layoutWidget)
        self.contact.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.contact.setObjectName("contact")
        self.contactLayout.addWidget(self.contact)
        self.contactEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.contactEdit.setObjectName("contactEdit")
        self.contactLayout.addWidget(self.contactEdit)
        self.verticalLayout.addLayout(self.contactLayout)
        self.serviceLayout = QtWidgets.QHBoxLayout()
        self.serviceLayout.setObjectName("serviceLayout")
        self.service = QtWidgets.QLabel(self.layoutWidget)
        self.service.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.service.setObjectName("service")
        self.serviceLayout.addWidget(self.service)
        self.serviceEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.serviceEdit.setObjectName("serviceEdit")
        self.serviceLayout.addWidget(self.serviceEdit)
        self.verticalLayout.addLayout(self.serviceLayout)
        self.costLayout = QtWidgets.QHBoxLayout()
        self.costLayout.setObjectName("costLayout")
        self.cost = QtWidgets.QLabel(self.layoutWidget)
        self.cost.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.cost.setObjectName("cost")
        self.costLayout.addWidget(self.cost)
        self.costEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.costEdit.setObjectName("costEdit")
        self.costLayout.addWidget(self.costEdit)
        self.verticalLayout.addLayout(self.costLayout)
        self.dateLayout = QtWidgets.QHBoxLayout()
        self.dateLayout.setObjectName("dateLayout")
        self.date = QtWidgets.QLabel(self.layoutWidget)
        self.date.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.date.setObjectName("date")
        self.dateLayout.addWidget(self.date)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.dateLayout)
        # click events
        self.saveButton.clicked.connect(self.save_data_to_db)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def save_data_to_db(self):
        """This method Sends the customer details to the database
        """
        Customerdb = CustomerDb() # instance of the class
        name = self.nameEdit.text().strip()
        contact = self.contactEdit.text().strip()
        service = self.serviceEdit.text().strip()
        cost = self.costEdit.text().strip()
        date = self.dateEdit.text().strip()
        all_inputs = [name, contact, service, cost, date]
        for each_value in all_inputs:
            if each_value == "":
                print("Provide all data")# You can add a label to the UI to show this response message
                return
            elif all_inputs[3] :
                try: 
                    contact = int(all_inputs[1])
                    cost = int(all_inputs[3])
                except Exception:
                    print("The cost price or Contact must be a number") # You can add a label to the UI to show this response message
                    return 
            else: pass
        
        response = Customerdb.insert_data_to_database(name, contact, service, cost, date)
        print(response) # You can add a label to the UI to show this response message
        if response =="added successfully":
            self.set_fields_empty()

            
    def set_fields_empty(self):
        self.nameEdit.setText("")
        self.contactEdit.setText("")
        self.serviceEdit.setText("")
        self.costEdit.setText("")
    
    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Add Customer"))
        self.saveButton.setText(_translate("widget", "Save"))
        self.cancelButton.setText(_translate("widget", "Cancel"))
        self.name.setText(_translate("widget", "Name"))
        self.contact.setText(_translate("widget", "Contact"))
        self.service.setText(_translate("widget", "Service"))
        self.cost.setText(_translate("widget", "Cost"))
        self.date.setText(_translate("widget", "Date"))

    def close_window(self):
        """Use to close dialog window
        """
        # YOU MUST USE A DIALOG BOX ELSE THE WHOLE UI WILL CLOSE. YOU CAN UNCOMMENT BELOW IF YOU WISH
        # if True:
        #     mes = QMessageBox.question(QMessageBox(), 
        #                 'Confirm', 'Are you sure you want to exit?. Save all data in the input field if there is any before exit ', 
        #                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        #     if mes == QMessageBox.StandardButton.Yes:
        #         sys.exit()
        #     else:
        #         return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())

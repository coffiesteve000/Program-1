from PyQt6 import QtCore, QtGui, QtWidgets
from link import CustomerDB
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 517, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setLineWidth(7)
        self.frame.setMidLineWidth(4)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 16777215, 16777215))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(589, 29, 341, 621))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 400, 321, 201))
        self.widget_2.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(60, 80, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(20, 10, 311, 351))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("border-color: rgb(85, 0, 255);\n"
"gridline-color: rgb(85, 255, 255);")
        self.widget.setObjectName("widget")
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setGeometry(QtCore.QRect(40, 310, 80, 41))
        self.saveButton.setMouseTracking(True)
        self.saveButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setGeometry(QtCore.QRect(180, 310, 80, 41))
        self.cancelButton.setMouseTracking(True)
        self.cancelButton.setStyleSheet("background-color: rgb(255, 21, 0);\n"
"font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.cancelButton.setObjectName("cancelButton")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 290, 281))
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
        self.dateEdit.setDisplayFormat("d/M/yyyy")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.dateLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        # start method
        self.load_customer_details()
        self.set_date()
        # self.tableWidget.setItem(1,5,QtWidgets.QTableWidgetItem(data))

        # click events
        self.saveButton.clicked.connect(self.insert_data)
        self.cancelButton.clicked.connect(self.cancel)
        
        #----------- Validators --------------#
        onlyfloat = QtGui.QDoubleValidator()
        onlyInt = QtGui.QIntValidator()
        self.contactEdit.setValidator(onlyInt)
        self.costEdit.setValidator(onlyfloat)
        #----------- Validators End--------------#
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def load_customer_details(self):
        CustomerDb = CustomerDB()
        Customer_details = CustomerDb.return_all()
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
        Customerdb = CustomerDB()
        name = self.nameEdit.text().strip()
        contact = self.contactEdit.text().strip()
        service = self.serviceEdit.text().strip()
        cost = self.costEdit.text().strip()
        date = self.dateEdit.text().strip()
        all_inputs = [name, contact, service, cost, date]
        for each_value in all_inputs:
            if each_value == "":
                self.label.setText("Provide all data")
                return
            elif all_inputs[3] :
                try: 
                    contact = int(all_inputs[1])
                    # cost = int(all_inputs[3])
                except Exception:
                    self.label.setText("Contact must be a number")
                    return
                try: 
                    # contact = int(all_inputs[1])
                    cost = int(all_inputs[3])
                except Exception:
                    self.label.setText("Cost must be a number")
                    return
                    '''
            elif all_inputs[3] :
                try: 
                    # contact = int(all_inputs[1])
                    cost = int(all_inputs[3])
                except Exception:
                    print("Cost must be a number") # You can add a label to the UI to show this response message
                    self.label.setText("Cost must be a number")
                    return
                    ''' 
            else: pass

        response = Customerdb.insert_into_db(name, contact, service, cost, date)
        if response == "Added Successfully":
            self.set_fields_empty()
            self.load_customer_details()
            self.label.setText(response)



    def set_fields_empty(self):
        self.nameEdit.setText("")
        self.contactEdit.setText("")
        self.serviceEdit.setText("")
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Service"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cost"))
        self.saveButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.saveButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">bd=0</span></p></body></html>"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.cancelButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.cancelButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">bd=0</span></p></body></html>"))
        self.cancelButton.setText(_translate("MainWindow", "Clear"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.contact.setText(_translate("MainWindow", "Contact"))
        self.service.setText(_translate("MainWindow", "Service"))
        self.cost.setText(_translate("MainWindow", "Cost"))
        self.date.setText(_translate("MainWindow", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

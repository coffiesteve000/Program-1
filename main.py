from PyQt6 import QtCore, QtGui, QtWidgets
from link import CustomerDB
from PyQt6.QtWidgets import QMessageBox
import re



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow.resize(898, 602)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dockWidget = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget.setMaximumSize(QtCore.QSize(300, 524287))
        self.dockWidget.setAutoFillBackground(False)
        self.dockWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dockWidget.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.dockWidgetContents_2)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                  "gridline-color: rgb(85, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 30))
        self.cancelButton.setMouseTracking(True)
        self.cancelButton.setStyleSheet("background-color: rgb(255, 21, 0);\n"
                                        "font: 9pt \"Arial Rounded MT Bold\";\n"
                                        "color: rgb(255, 255, 255);")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 30))
        self.saveButton.setMouseTracking(True)
        self.saveButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                      "font: 9pt \"Arial Rounded MT Bold\";\n"
                                      "color: rgb(255, 255, 255);")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.serviceLayout = QtWidgets.QHBoxLayout()
        self.serviceLayout.setObjectName("serviceLayout")
        self.service = QtWidgets.QLabel(self.widget)
        self.service.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.service.setObjectName("service")
        self.serviceLayout.addWidget(self.service, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.serviceEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.serviceEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.serviceEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.serviceEdit.setOverwriteMode(True)
        self.serviceEdit.setCenterOnScroll(True)
        self.serviceEdit.setObjectName("serviceEdit")
        self.serviceLayout.addWidget(self.serviceEdit, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridLayout_2.addLayout(self.serviceLayout, 4, 0, 1, 1)
        self.costLayout = QtWidgets.QHBoxLayout()
        self.costLayout.setObjectName("costLayout")
        self.cost = QtWidgets.QLabel(self.widget)
        self.cost.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.cost.setObjectName("cost")
        self.costLayout.addWidget(self.cost)
        self.costEdit = QtWidgets.QLineEdit(self.widget)
        self.costEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.costEdit.setObjectName("costEdit")
        self.costLayout.addWidget(self.costEdit)
        self.gridLayout_2.addLayout(self.costLayout, 2, 0, 1, 1)
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.name.setObjectName("name")
        self.nameLayout.addWidget(self.name)
        self.nameEdit = QtWidgets.QLineEdit(self.widget)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.nameLayout.addWidget(self.nameEdit)
        self.gridLayout_2.addLayout(self.nameLayout, 0, 0, 1, 1)
        self.contactLayout = QtWidgets.QHBoxLayout()
        self.contactLayout.setObjectName("contactLayout")
        self.contact = QtWidgets.QLabel(self.widget)
        self.contact.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.contact.setObjectName("contact")
        self.contactLayout.addWidget(self.contact)
        self.contactEdit = QtWidgets.QLineEdit(self.widget)
        self.contactEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.contactEdit.setObjectName("contactEdit")
        self.contactLayout.addWidget(self.contactEdit)
        self.gridLayout_2.addLayout(self.contactLayout, 1, 0, 1, 1)
        self.dateLayout = QtWidgets.QHBoxLayout()
        self.dateLayout.setObjectName("dateLayout")
        self.date = QtWidgets.QLabel(self.widget)
        self.date.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.date.setObjectName("date")
        self.dateLayout.addWidget(self.date)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEdit.setCurrentSection(
            QtWidgets.QDateTimeEdit.Section.DaySection)
        self.dateEdit.setDisplayFormat("d/M/yyyy")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setObjectName("dateEdit")
        self.dateLayout.addWidget(self.dateEdit)
        self.gridLayout_2.addLayout(self.dateLayout, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        # self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        self.gridLayout_6.addWidget(self.dockWidget, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_3.setLineWidth(0)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 3)
        self.dockWidget_2 = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget_2.setAutoFillBackground(False)
        self.dockWidget_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.dockWidget_2.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_4.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(
            self.label_4, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        self.gridLayout_6.addWidget(self.dockWidget_2, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExport_Data = QtGui.QAction(MainWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionExit_App = QtGui.QAction(MainWindow)
        self.actionExit_App.setObjectName("actionExit_App")
        self.actionView_All = QtGui.QAction(MainWindow)
        self.actionView_All.setObjectName("actionView_All")
        self.menuFile.addAction(self.actionExport_Data)
        self.menuFile.addAction(self.actionExit_App)
        self.menuView.addAction(self.actionView_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
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
        self.serviceEdit
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
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.label_2.setText(_translate(
            "MainWindow", "ENTER BOOK LISTING DETAILS"))
        self.cancelButton.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.cancelButton.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">bd=0</span></p></body></html>"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.saveButton.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.saveButton.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">bd=0</span></p></body></html>"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.service.setText(_translate("MainWindow", "Service"))
        self.serviceEdit.setPlaceholderText(_translate(
            "MainWindow", "Enter Service Details here"))
        self.cost.setText(_translate("MainWindow", "Cost     "))
        self.name.setText(_translate("MainWindow", "Name   "))
        self.contact.setText(_translate("MainWindow", "Contact"))
        self.date.setText(_translate("MainWindow", "Date    "))
        self.label_3.setText(_translate("MainWindow", "BOOK LISTING SYSTEM"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Service"))
        self.label_4.setText(_translate("MainWindow", "ALL RECORDS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionExport_Data.setText(_translate("MainWindow", "Export Data"))
        self.actionExit_App.setText(_translate("MainWindow", "Exit App"))
        self.actionView_All.setText(_translate("MainWindow", "View All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

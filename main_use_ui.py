from PyQt6 import QtGui, QtWidgets, uic
import sys
from PyQt6.QtCore import QFileInfo
from link import CustomerDB
from PyQt6.QtWidgets import QMessageBox, QFileDialog
import re
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import pandas as pd
CustomerDb = CustomerDB() # instance of db
class setupUi:
    def load_customer_details():
        Customer_details = CustomerDb.return_all()
        MainWindow.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(Customer_details):
            MainWindow.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                Data = QtWidgets.QTableWidgetItem(str(data))
                
                if column_number in set((0,2,3)): # aligning text in column 1,3 and 4
                    Data.setTextAlignment(10)
                else:
                    Data.setTextAlignment(0)
                
                MainWindow.tableWidget.setItem(row_number,column_number,Data)
                

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

    def error_message_color():
        MainWindow.label.setStyleSheet("color: rgb(170, 0, 0);")
        
    def success_message_color():
        MainWindow.label.setStyleSheet("color: rgb(0, 170, 0);")

    def cancel():
        if True:
            mes = QMessageBox.question(QMessageBox(), 
                        'Confirm', 'Are you sure you want to exit? Save all data in the input field if there is any before exit ', 
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if mes == QMessageBox.StandardButton.Yes:
                setupUi.set_fields_empty()
            else:
                return

    def exit_app():
        if True:
            mes = QMessageBox.warning(QMessageBox(), 
                        'Confirm', 'Are you sure you want to exit? Save all data in the input field if there is any before exit ', 
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if mes == QMessageBox.StandardButton.Yes:
                sys.exit()
            else:
                return

    """ PRINTING
    def print_file():
        # printer = QPrinter(QPrinter.HighResolution) #attribute error
        dialog = QPrintDialog() # QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.Accepted:
            MainWindow.tableWidget.print_(dialog.printer())

        else:
            pass
    
    
    def print_preview_dialog():
        # printer = QPrinter(QPrinter.HighResolution) #attribute error
        previewDialog = QPrintPreviewDialog() # QPrintPreviewDialog(printer)
        previewDialog.paintRequested.connect(setupUi.print_preview)
        previewDialog.exec()



    def print_preview(printer):
        MainWindow.tableWidget.print_(dialog.printer()) #attribute error when using print_preview_dialog
    """
    def export_file():
        path,pt= QFileDialog.getSaveFileName(None,"Save File", None, "PDF files (.pdf);;All Files(*)") #QFileInfo().suffix()
        print(path),print(pt)
        if path != "":
            if pt == "PDF files (.pdf)":
                if QFileInfo(path).suffix() == "":
                    path += ".pdf"
                    """ NORMAL FILE_SAVING METHOD
                    file = open(path,'w')
                    text = MainWindow.serviceEdit.toPlainText()
                    file.write(text)
                    file.close()
                    """
                    """
                    printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                    printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                    printer.setOutputFileName(path)
                    # MainWindow.serviceEdit.document().print(printer) # or without document()
                    # MainWindow.tableWidget.document().print(printer) 
                    document = QtGui.QTextDocument(MainWindow.tableWidget)
                    print(document.toPlainText())
                    document.print(printer)
                    """
    def export_excel():
        setupUi.success_message_color()
        MainWindow.label.setText("Exporting to excel...")

        try:

            columnHeaders = []

            # create column headers
            for h in range(MainWindow.tableWidget.model().columnCount()):
                columnHeaders.append(MainWindow.tableWidget.horizontalHeaderItem(h).text())

            df = pd.DataFrame(columns = columnHeaders)

            # create dataframe
            for row in range(MainWindow.tableWidget.model().rowCount()):
                for col in range(MainWindow.tableWidget.model().columnCount()):
                    df.at[row,columnHeaders[col]] = MainWindow.tableWidget.item(row,col).text()

            path,pt= QFileDialog.getSaveFileName(None,"Export File", None, "Excel Workbook (.xlsx);;All Files(*)")
            if QFileInfo(path).suffix() == "": path += ".xlsx"
            df.to_excel(path,index=False)

            setupUi.success_message_color()
            MainWindow.label.setText("Exported Successfully")


            mes = QMessageBox.information(QMessageBox(), 
                        'Success', 'File exported successfully', 
                        QMessageBox.StandardButton.Ok)

        except Exception:

            setupUi.error_message_color()
            MainWindow.label.setText("Export Unsuccessful")

            mes = QMessageBox.critical(QMessageBox(), 
                        'Error', 'Error exporting file', 
                        QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Ok)
            if mes == QMessageBox.StandardButton.Retry:
                setupUi.export_excel()
            else: return



            # PDF EXPORT
    def export_pdf():
        print("Exporting to PDF")

                        
                    
                    
                    
                    
                

    





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
    MainWindow.exitAction.triggered.connect(setupUi.exit_app)
    MainWindow.printAction.triggered.connect(setupUi.print_file)
    # MainWindow.actionPrint_Preview.triggered.connect(setupUi.print_preview_dialog)  #attribute error
    MainWindow.exportAction.triggered.connect(setupUi.export_excel)

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
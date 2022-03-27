# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\FEXMOVA\proyectos PYTHON\gestionsoriana\ALTAPEDIDOS.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import time
from datetime import date, datetime
import dateutil.parser as dp
#from popups import errornumeros


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 60, 20, 201))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 60, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 120, 110, 22))
        self.dateEdit.setMinimumDate(QtCore.QDate(2017, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.BOTONPRUEBA1 = QtWidgets.QPushButton(self.centralwidget)
        self.BOTONPRUEBA1.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.BOTONPRUEBA1.setObjectName("BOTONPRUEBA1")
        self.BOTONPRUEBA2 = QtWidgets.QPushButton(self.centralwidget)
        self.BOTONPRUEBA2.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.BOTONPRUEBA2.setObjectName("BOTONPRUEBA2")
        self.BOTONPRUEBA3 = QtWidgets.QPushButton(self.centralwidget)
        self.BOTONPRUEBA3.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.BOTONPRUEBA3.setObjectName("BOTONPRUEBA3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#botones de pruebas
        self.BOTONPRUEBA1.clicked.connect(self.validacionnumeros)
        
#botones de pruebas     
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ALTA DE PEDIDOS"))
        self.label_2.setText(_translate("MainWindow", "Nímero Pedido"))
        self.label_3.setText(_translate("MainWindow", "Tienda"))
        self.label_4.setText(_translate("MainWindow", "Cotización (Excel)"))
        self.label_5.setText(_translate("MainWindow", "Pedido (PDF)"))
        self.label_6.setText(_translate("MainWindow", "Inicio Embarque"))
        self.label_7.setText(_translate("MainWindow", "Fin Embarque"))
        self.label_8.setText(_translate("MainWindow", "Fecha Pedido"))
        self.BOTONPRUEBA1.setText(_translate("MainWindow", "PRUEBA 1"))
        self.BOTONPRUEBA2.setText(_translate("MainWindow", "PRUEBA 2"))
        self.BOTONPRUEBA3.setText(_translate("MainWindow", "PRUEBA 3"))

    

    #obtener ruta del archivo
    def obtenerruta(self):
        ruta = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File','','Files (*.png *.pdf *.jpg)')
        return(ruta[0])


        
    def validacionnumeros(self):
        a=self.lineEdit.text()
        print(a)
        try:
            b=int(a)
            return(b)
        except:
            errornumeros()
            return()
            
           

    def fechapedido(self):
        day=self.dateEdit.dateTime().toString("dd")
        month=self.dateEdit.dateTime().toString("MM")
        year=self.dateEdit.dateTime().toString("yyyy")
        s='-'
        vectordate=year+s+month+s+day
        conversion=fechaatimestmp(vectordate)
        print(conversion)
        return(conversion)
    
    def fechainicioembarque(self):
        day=self.dateEdit2.dateTime().toString("dd")
        month=self.dateEdit2.dateTime().toString("MM")
        year=self.dateEdit2.dateTime().toString("yyyy")
        s='-'
        vectordate=year+s+month+s+day
        conversion=fechaatimestmp(vectordate)
        return(conversion)
    
    def fechafinembarque(self):
        day=self.dateEdit3.dateTime().toString("dd")
        month=self.dateEdit3.dateTime().toString("MM")
        year=self.dateEdit3.dateTime().toString("yyyy")
        s='-'
        vectordate=year+s+month+s+day
        conversion=fechaatimestmp(vectordate)
        return(conversion)
        
        
def fechaatimestmp(fecha):
        #formato de concatenacion para fecha a Timestamp
        vectortime=fecha+"T00:00:00.000Z"
        utc_dt = datetime.strptime(vectortime, '%Y-%m-%dT%H:%M:%S.%fZ')
        # Convert UTC datetime to seconds since the Epoch
        conversion = int((utc_dt - datetime(1970, 1, 1)).total_seconds())        
        return(conversion)

def errornumeros():
        msg=QMessageBox()
        msg.setWindowTitle("ERROR DE FORMATO")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sólo se permiten números en PEDIDO y TIENDA")
        x=msg.exec_()
        return()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
   
    sys.exit(app.exec_())

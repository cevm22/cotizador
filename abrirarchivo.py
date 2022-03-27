import logging
import sqlite3
import os
import shutil
import time
import subprocess
from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 80)
        MainWindow.setMinimumSize(QtCore.QSize(557, 52))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listaCB = QtWidgets.QComboBox(self.centralwidget)
        self.listaCB.setGeometry(QtCore.QRect(170, 50, 251, 22))
        self.listaCB.setObjectName("listaCB")
        self.abrir = QtWidgets.QPushButton(self.centralwidget)
        self.abrir.setGeometry(QtCore.QRect(450, 10, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.abrir.setFont(font)
        self.abrir.setObjectName("abrir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.abrir.setText(_translate("MainWindow", "ABRIR \n"
"Archivo"))
        self.label.setText(_translate("MainWindow", "ESCOGER ARCHIVO ------>"))
        self.label_2.setText(_translate("MainWindow", "Archivos del pedido  ---->"))
        self.label_3.setText(_translate("MainWindow", "Carpeta del pedido"))
        self.abrir.clicked.connect(self.abrirtemporal)

    def llenarCB_archivos(self):
        #pedido=str('1-0')
        pedido=self.tomarinfo()
        self.label_3.setText(str(pedido))
        b = os.getcwd()  # obtener la ruta exacta del archivo
        documentacion='DOCUMENTACION'
        a = os.listdir(b +'\\' +documentacion+'\\'+pedido)  # obtener lo que hay dentro de la carpeta
        print(b)
        for i in range(len(a)):
            self.listaCB.addItem(a[i])
        return ()

    def abrirtemporal(self):
        pedido = self.tomarinfo()
        try:
            a=str(self.listaCB.currentText())
            rutascript = os.getcwd()
            carpeta = "DOCUMENTACION"
            origen=rutascript+'\\'+carpeta+'\\'+pedido+'\\'+a
            print(origen)
            print(path.exists(origen))
            # copiar archivo
            trashes="trashes"
            timestamp=str(int(time.mktime(time.localtime())))
            rutacopia=rutascript+'\\'+trashes+'\\'+timestamp+'---'+a
            print(rutacopia)
            shutil.copyfile(origen, rutacopia)
            #abrir archivo temporal
            os.startfile(rutacopia)
            print("listo")
            sys.exit()

        except IOError:
            print("NO EXISTE ARCHIVO")
            mensajeerror()
        return ()

    def tomarinfo(self):
        print("TOMANDO INFORMACIÓN")
        print("*************************")
        temporal = ""
        SUBCAT = "items.db"
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT = """SELECT item
                    from pasar
                    where ID = 1
                    """
            print("INTENTO")
            cursor.execute(SELECT)
            record = cursor.fetchone()

            temporal = record[0]

            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                #self.llenarinfopedido(str(temporal),tempcantidad)
                return(str(temporal))


        return ()
    def carpetatrashes(self):
        archivo = path.exists('trashes')
        if archivo == True:
            print("existe el archivo trashes")
        else:
            print("NO EXISTE.... creando archivo")
            os.mkdir('trashes')
        return ()
def mensajeerror():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR")
    msg.setIcon(QMessageBox.Information)
    msg.setText("NO SE ENCUENTRA ARCHIVO SELECCIONADO")
    x = msg.exec_()
    return()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.llenarCB_archivos()
    ui.carpetatrashes()
    sys.exit(app.exec_())

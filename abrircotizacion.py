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
    def abrirlistacotizacion(self):
        script = "HOME.py"
        subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        sys.exit()
        return ()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 52)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listaCB = QtWidgets.QComboBox(self.centralwidget)
        self.listaCB.setGeometry(QtCore.QRect(170, 20, 251, 22))
        self.listaCB.setObjectName("listaCB")
        self.abrir = QtWidgets.QPushButton(self.centralwidget)
        self.abrir.setGeometry(QtCore.QRect(450, 10, 81, 31))
        self.abrir.setObjectName("abrir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABRIR COTIZACIÓN MANUAL"))
        self.abrir.setText(_translate("MainWindow", "ABRIR"))
        self.label.setText(_translate("MainWindow", "ESCOGER COTIZACIÓN A ABRIR"))
        self.abrir.clicked.connect(self.abrirtemporal)

    def populateCB(self):
        print("llenarCB_SUBCAT")
        SUBCAT = "administrativo.db"
        self.listaCB.clear()
        # vectorsubcat = globals()["vectorsubcategoria"]

        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()

            SELECT = """SELECT numcotizacion from cotizaciones
                        """
            cursor.execute(SELECT)

            record = cursor.fetchall()
            for row in record:
                a = str(row[0])
                self.listaCB.addItem(a)
                # vectorsubcat.append(a)
                # print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                # print("Cerrando conexión de Base de Datos")
        return ()

    def carpetatrashes(self):
        archivo = path.exists('trashes')
        if archivo == True:
            print("existe el archivo trashes")
        else:
            print("NO EXISTE.... creando archivo")
            os.mkdir('trashes')
        return ()

    def abrirtemporal(self):
        try:
            a=str(self.listaCB.currentText())
            b=a+str('.xlsx')
            rutascript = os.getcwd()
            carpeta = "COTIZACIONES"
            origen=rutascript+'\\'+carpeta+'\\'+b
            print(origen)
            print(path.exists(origen))
            # copiar archivo
            trashes="trashes"
            timestamp=str(int(time.mktime(time.localtime())))
            rutacopia=rutascript+'\\'+trashes+'\\'+timestamp+'.xlsx'
            print(rutacopia)
            shutil.copyfile(origen, rutacopia)
            #abrir archivo temporal
            os.startfile(rutacopia)
            self.abrirlistacotizacion()
            print("listo")
        except IOError:
            print("NO EXISTE ARCHIVO")
            mensajeerror()
        return ()

def mensajeerror():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR")
    msg.setIcon(QMessageBox.Information)
    msg.setText("NO SE ENCUENTRA COTIZACION")
    x = msg.exec_()
    return()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.populateCB()
    ui.carpetatrashes()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime
from visor_cotizacion_1 import Ui_Dialog_visor_cotizador
from GESTORCOTIZACIONES_1_1 import *
from GESTORPEDIDOS_3 import *
from COTIZADOR_1_2_1 import *
from ALTAPEDIDOS_3 import *
import logging
import sqlite3
import json
import os
import subprocess
import shutil
import time
from os import path


class Ui_MainWindow(object):
    def gestorcot(self): #NO USAR
        self.window2=QtWidgets.QMainWindow() #ESTE ES EL FORM
        self.uid=Ui_Gestor_Cot()
        self.uid.setupUi_GESTORCOTIZACIONES(self.window2)
        self.uid.llenadogui()
        self.window2.show()
        MainWindow.close()
    def gestorped(self): #NO USAR
        self.window2=QtWidgets.QMainWindow() #ESTE ES EL FORM
        self.uid=Ui_Gestor_Pedidos()
        self.uid.setupUi(self.window2)
        self.uid.llenado()
        self.window2.show()
        MainWindow.close()
    def nuevacot(self): #NO USAR
        self.window2=QtWidgets.QMainWindow() #ESTE ES EL FORM
        self.uid=Ui_MainWindow_cotizador()
        self.uid.setupUi(self.window2)
        self.uid.bloquearbotones()
        self.uid.borrartodo()
        self.uid.borrartextedit()
        self.window2.show()
        MainWindow.close()

    def altaped(self): #NO USAR
        script = "ALTAPEDIDOS_3.py"
        # os.system(script)
        subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        sys.exit()
        return ()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gestorcotizaciones = QtWidgets.QPushButton(self.centralwidget)
        self.gestorcotizaciones.setGeometry(QtCore.QRect(50, 60, 101, 41))
        self.gestorcotizaciones.setObjectName("gestorcotizaciones")
        self.gestorpedidos = QtWidgets.QPushButton(self.centralwidget)
        self.gestorpedidos.setGeometry(QtCore.QRect(170, 60, 101, 41))
        self.gestorpedidos.setObjectName("gestorpedidos")
        self.nuevacotizacion = QtWidgets.QPushButton(self.centralwidget)
        self.nuevacotizacion.setGeometry(QtCore.QRect(50, 110, 101, 41))
        self.nuevacotizacion.setObjectName("nuevacotizacion")
        self.altapedido = QtWidgets.QPushButton(self.centralwidget)
        self.altapedido.setGeometry(QtCore.QRect(170, 110, 101, 41))
        self.altapedido.setObjectName("altapedido")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestor Fidget-Soriana"))
        self.gestorcotizaciones.setText(_translate("MainWindow", "Gestor de\n"
"Cotizaciones"))
        self.gestorpedidos.setText(_translate("MainWindow", "Gestor de\n"
"Pedidos"))
        self.nuevacotizacion.setText(_translate("MainWindow", "NUEVA \n"
"Cotización"))
        self.altapedido.setText(_translate("MainWindow", "ALTA de \n"
"Pedido"))
        self.label.setText(_translate("MainWindow", "HOME"))
        self.gestorcotizaciones.clicked.connect(self.gestorcot)
        self.gestorpedidos.clicked.connect(self.gestorped)
        self.nuevacotizacion.clicked.connect(self.nuevacot)
        self.altapedido.clicked.connect(self.altaped)

    def borrandoycreandodirectorio(self):
        archivo = path.exists('trashes')
        #print(archivo)
        if archivo == True:
            #print("existe el archivo trashes")
            a = os.getcwd()
            #shutil.rmtree(a + r'\trashes')
            #os.mkdir("trashes")
        else:
            print("NO EXISTE.... creando archivo")
            #os.mkdir('trashes')
        return ()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.borrandoycreandodirectorio()
    sys.exit(app.exec_())

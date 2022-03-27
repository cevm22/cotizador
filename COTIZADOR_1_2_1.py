from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
from pathlib import Path
from datetime import date, datetime
from Dialog import Ui_Dialog
from AM_1 import Ui_Dialog_AM
from SELECCIONAR_AM1 import Ui_Dialog_SELCCIONARMANUAL
from vaciadodeinfo import *
from sendingmails import *
from libreriaasana import *
from GESTORCOTIZACIONES_1_1 import *
import subprocess
import dateutil.parser as dp
import logging
import sqlite3
import json
import time
import sys
import datetime
import csv
import os

# +++++++++++++++++
# Varibles globales
# +++++++++++++++++
DBinfotiendas = "INFO.db"
vectorinfotienda = []
vectoritems = []
vectorinfoitems = []
VERIFICADOR = 0
fecha = datetime.date.today()
year = fecha.year
month = fecha.month
day = fecha.day
basedatos='administrativo.db'
cotizacion=''
seleccionartipoBD=''
# +++++++++++++++++
# Varibles globales
# +++++++++++++++++
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Enable logging


class Ui_MainWindow_cotizador(object):
    def salir(self):
        #MainWindow_COT.close()
        gestor()

    def setupUi(self, MainWindow_COT):

        MainWindow_COT.setObjectName("MainWindow_COT")
        MainWindow_COT.resize(772, 612)
        MainWindow_COT.setMinimumSize(QtCore.QSize(772, 612))
        MainWindow_COT.setMaximumSize(QtCore.QSize(772, 612))
        self.centralwidget = QtWidgets.QWidget(MainWindow_COT)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NUMTIENDA = QtWidgets.QLineEdit(self.centralwidget)
        self.NUMTIENDA.setGeometry(QtCore.QRect(60, 20, 31, 20))
        self.NUMTIENDA.setObjectName("NUMTIENDA")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.BUSCARINFOTIENDA = QtWidgets.QPushButton(self.centralwidget)
        self.BUSCARINFOTIENDA.setGeometry(QtCore.QRect(100, 10, 101, 41))
        self.BUSCARINFOTIENDA.setObjectName("BUSCARINFOTIENDA")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 0, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.fecha = QtWidgets.QLabel(self.centralwidget)
        self.fecha.setGeometry(QtCore.QRect(670, 30, 71, 21))
        self.fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.fecha.setObjectName("fecha")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 0, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Usuario = QtWidgets.QLabel(self.centralwidget)
        self.Usuario.setGeometry(QtCore.QRect(540, 30, 91, 21))
        self.Usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.Usuario.setObjectName("Usuario")
        self.FORMATO = QtWidgets.QLabel(self.centralwidget)
        self.FORMATO.setGeometry(QtCore.QRect(280, 10, 61, 16))
        self.FORMATO.setAlignment(QtCore.Qt.AlignCenter)
        self.FORMATO.setObjectName("FORMATO")
        self.ESTADO = QtWidgets.QLabel(self.centralwidget)
        self.ESTADO.setGeometry(QtCore.QRect(410, 10, 61, 16))
        self.ESTADO.setAlignment(QtCore.Qt.AlignCenter)
        self.ESTADO.setObjectName("ESTADO")
        self.DIRECCION = QtWidgets.QLabel(self.centralwidget)
        self.DIRECCION.setGeometry(QtCore.QRect(280, 30, 231, 16))
        self.DIRECCION.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.DIRECCION.setObjectName("DIRECCION")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 110, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.TITULOCOTIZACION = QtWidgets.QLineEdit(self.centralwidget)
        self.TITULOCOTIZACION.setGeometry(QtCore.QRect(120, 110, 371, 20))
        self.TITULOCOTIZACION.setMaxLength(70)
        self.TITULOCOTIZACION.setObjectName("TITULOCOTIZACION")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 130, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 140, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(10, 170, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(10, 190, 25, 19))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(10, 210, 25, 19))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(10, 230, 25, 19))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(10, 250, 25, 19))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(10, 270, 25, 19))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_7.setGeometry(QtCore.QRect(10, 290, 25, 19))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_8 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_8.setGeometry(QtCore.QRect(10, 310, 25, 19))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_9.setGeometry(QtCore.QRect(10, 330, 25, 19))
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_10.setGeometry(QtCore.QRect(10, 350, 25, 19))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_11.setGeometry(QtCore.QRect(10, 370, 25, 19))
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_12.setGeometry(QtCore.QRect(10, 390, 25, 19))
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_13 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_13.setGeometry(QtCore.QRect(10, 410, 25, 19))
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_14 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_14.setGeometry(QtCore.QRect(10, 430, 25, 19))
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_15 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_15.setGeometry(QtCore.QRect(10, 450, 25, 19))
        self.toolButton_15.setObjectName("toolButton_15")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(60, 140, 291, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.ITEMDESCRIPCION_1 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_1.setGeometry(QtCore.QRect(60, 170, 301, 16))
        self.ITEMDESCRIPCION_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_1.setObjectName("ITEMDESCRIPCION_1")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(380, 140, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.ITEMMODELO_1 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_1.setGeometry(QtCore.QRect(380, 170, 91, 16))
        self.ITEMMODELO_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_1.setObjectName("ITEMMODELO_1")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(500, 140, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.ITEMCANTIDAD_1 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_1.setGeometry(QtCore.QRect(500, 170, 51, 16))
        self.ITEMCANTIDAD_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_1.setObjectName("ITEMCANTIDAD_1")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(580, 140, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.ITEMUNIDAD_1 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_1.setGeometry(QtCore.QRect(580, 170, 51, 16))
        self.ITEMUNIDAD_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_1.setObjectName("ITEMUNIDAD_1")
        self.ITEM_SUBTOTAL_1 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_1.setGeometry(QtCore.QRect(670, 170, 51, 16))
        self.ITEM_SUBTOTAL_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_1.setObjectName("ITEM_SUBTOTAL_1")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(670, 140, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 460, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_3.setFont(font)
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ITEMCANTIDAD_2 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_2.setGeometry(QtCore.QRect(500, 190, 51, 16))
        self.ITEMCANTIDAD_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_2.setObjectName("ITEMCANTIDAD_2")
        self.ITEMUNIDAD_2 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_2.setGeometry(QtCore.QRect(580, 190, 51, 16))
        self.ITEMUNIDAD_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_2.setObjectName("ITEMUNIDAD_2")
        self.ITEMDESCRIPCION_2 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_2.setGeometry(QtCore.QRect(60, 190, 301, 16))
        self.ITEMDESCRIPCION_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_2.setObjectName("ITEMDESCRIPCION_2")
        self.ITEM_SUBTOTAL_2 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_2.setGeometry(QtCore.QRect(670, 190, 51, 16))
        self.ITEM_SUBTOTAL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_2.setObjectName("ITEM_SUBTOTAL_2")
        self.ITEMMODELO_2 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_2.setGeometry(QtCore.QRect(380, 190, 91, 16))
        self.ITEMMODELO_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_2.setObjectName("ITEMMODELO_2")
        self.ITEMCANTIDAD_3 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_3.setGeometry(QtCore.QRect(500, 210, 51, 16))
        self.ITEMCANTIDAD_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_3.setObjectName("ITEMCANTIDAD_3")
        self.ITEMUNIDAD_3 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_3.setGeometry(QtCore.QRect(580, 210, 51, 16))
        self.ITEMUNIDAD_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_3.setObjectName("ITEMUNIDAD_3")
        self.ITEMDESCRIPCION_3 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_3.setGeometry(QtCore.QRect(60, 210, 301, 16))
        self.ITEMDESCRIPCION_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_3.setObjectName("ITEMDESCRIPCION_3")
        self.ITEM_SUBTOTAL_3 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_3.setGeometry(QtCore.QRect(670, 210, 51, 16))
        self.ITEM_SUBTOTAL_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_3.setObjectName("ITEM_SUBTOTAL_3")
        self.ITEMMODELO_3 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_3.setGeometry(QtCore.QRect(380, 210, 91, 16))
        self.ITEMMODELO_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_3.setObjectName("ITEMMODELO_3")
        self.ITEMCANTIDAD_4 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_4.setGeometry(QtCore.QRect(500, 230, 51, 16))
        self.ITEMCANTIDAD_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_4.setObjectName("ITEMCANTIDAD_4")
        self.ITEMUNIDAD_4 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_4.setGeometry(QtCore.QRect(580, 230, 51, 16))
        self.ITEMUNIDAD_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_4.setObjectName("ITEMUNIDAD_4")
        self.ITEMDESCRIPCION_4 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_4.setGeometry(QtCore.QRect(60, 230, 301, 16))
        self.ITEMDESCRIPCION_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_4.setObjectName("ITEMDESCRIPCION_4")
        self.ITEM_SUBTOTAL_4 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_4.setGeometry(QtCore.QRect(670, 230, 51, 16))
        self.ITEM_SUBTOTAL_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_4.setObjectName("ITEM_SUBTOTAL_4")
        self.ITEMMODELO_4 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_4.setGeometry(QtCore.QRect(380, 230, 91, 16))
        self.ITEMMODELO_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_4.setObjectName("ITEMMODELO_4")
        self.ITEMCANTIDAD_5 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_5.setGeometry(QtCore.QRect(500, 250, 51, 16))
        self.ITEMCANTIDAD_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_5.setObjectName("ITEMCANTIDAD_5")
        self.ITEMUNIDAD_5 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_5.setGeometry(QtCore.QRect(580, 250, 51, 16))
        self.ITEMUNIDAD_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_5.setObjectName("ITEMUNIDAD_5")
        self.ITEMDESCRIPCION_5 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_5.setGeometry(QtCore.QRect(60, 250, 301, 16))
        self.ITEMDESCRIPCION_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_5.setObjectName("ITEMDESCRIPCION_5")
        self.ITEM_SUBTOTAL_5 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_5.setGeometry(QtCore.QRect(670, 250, 51, 16))
        self.ITEM_SUBTOTAL_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_5.setObjectName("ITEM_SUBTOTAL_5")
        self.ITEMMODELO_5 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_5.setGeometry(QtCore.QRect(380, 250, 91, 16))
        self.ITEMMODELO_5.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_5.setObjectName("ITEMMODELO_5")
        self.ITEMCANTIDAD_6 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_6.setGeometry(QtCore.QRect(500, 270, 51, 16))
        self.ITEMCANTIDAD_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_6.setObjectName("ITEMCANTIDAD_6")
        self.ITEMUNIDAD_6 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_6.setGeometry(QtCore.QRect(580, 270, 51, 16))
        self.ITEMUNIDAD_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_6.setObjectName("ITEMUNIDAD_6")
        self.ITEMDESCRIPCION_6 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_6.setGeometry(QtCore.QRect(60, 270, 301, 16))
        self.ITEMDESCRIPCION_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_6.setObjectName("ITEMDESCRIPCION_6")
        self.ITEM_SUBTOTAL_6 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_6.setGeometry(QtCore.QRect(670, 270, 51, 16))
        self.ITEM_SUBTOTAL_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_6.setObjectName("ITEM_SUBTOTAL_6")
        self.ITEMMODELO_6 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_6.setGeometry(QtCore.QRect(380, 270, 91, 16))
        self.ITEMMODELO_6.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_6.setObjectName("ITEMMODELO_6")
        self.ITEMCANTIDAD_7 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_7.setGeometry(QtCore.QRect(500, 290, 51, 16))
        self.ITEMCANTIDAD_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_7.setObjectName("ITEMCANTIDAD_7")
        self.ITEMUNIDAD_7 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_7.setGeometry(QtCore.QRect(580, 290, 51, 16))
        self.ITEMUNIDAD_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_7.setObjectName("ITEMUNIDAD_7")
        self.ITEMDESCRIPCION_7 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_7.setGeometry(QtCore.QRect(60, 290, 301, 16))
        self.ITEMDESCRIPCION_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_7.setObjectName("ITEMDESCRIPCION_7")
        self.ITEM_SUBTOTAL_7 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_7.setGeometry(QtCore.QRect(670, 290, 51, 16))
        self.ITEM_SUBTOTAL_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_7.setObjectName("ITEM_SUBTOTAL_7")
        self.ITEMMODELO_7 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_7.setGeometry(QtCore.QRect(380, 290, 91, 16))
        self.ITEMMODELO_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_7.setObjectName("ITEMMODELO_7")
        self.ITEMCANTIDAD_8 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_8.setGeometry(QtCore.QRect(500, 310, 51, 16))
        self.ITEMCANTIDAD_8.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_8.setObjectName("ITEMCANTIDAD_8")
        self.ITEMUNIDAD_8 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_8.setGeometry(QtCore.QRect(580, 310, 51, 16))
        self.ITEMUNIDAD_8.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_8.setObjectName("ITEMUNIDAD_8")
        self.ITEMDESCRIPCION_8 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_8.setGeometry(QtCore.QRect(60, 310, 301, 16))
        self.ITEMDESCRIPCION_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_8.setObjectName("ITEMDESCRIPCION_8")
        self.ITEM_SUBTOTAL_8 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_8.setGeometry(QtCore.QRect(670, 310, 51, 16))
        self.ITEM_SUBTOTAL_8.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_8.setObjectName("ITEM_SUBTOTAL_8")
        self.ITEMMODELO_8 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_8.setGeometry(QtCore.QRect(380, 310, 91, 16))
        self.ITEMMODELO_8.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_8.setObjectName("ITEMMODELO_8")
        self.ITEMCANTIDAD_9 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_9.setGeometry(QtCore.QRect(500, 330, 51, 16))
        self.ITEMCANTIDAD_9.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_9.setObjectName("ITEMCANTIDAD_9")
        self.ITEMUNIDAD_9 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_9.setGeometry(QtCore.QRect(580, 330, 51, 16))
        self.ITEMUNIDAD_9.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_9.setObjectName("ITEMUNIDAD_9")
        self.ITEMDESCRIPCION_9 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_9.setGeometry(QtCore.QRect(60, 330, 301, 16))
        self.ITEMDESCRIPCION_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_9.setObjectName("ITEMDESCRIPCION_9")
        self.ITEM_SUBTOTAL_9 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_9.setGeometry(QtCore.QRect(670, 330, 51, 16))
        self.ITEM_SUBTOTAL_9.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_9.setObjectName("ITEM_SUBTOTAL_9")
        self.ITEMMODELO_9 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_9.setGeometry(QtCore.QRect(380, 330, 91, 16))
        self.ITEMMODELO_9.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_9.setObjectName("ITEMMODELO_9")
        self.ITEMCANTIDAD_10 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_10.setGeometry(QtCore.QRect(500, 350, 51, 16))
        self.ITEMCANTIDAD_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_10.setObjectName("ITEMCANTIDAD_10")
        self.ITEMUNIDAD_10 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_10.setGeometry(QtCore.QRect(580, 350, 51, 16))
        self.ITEMUNIDAD_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_10.setObjectName("ITEMUNIDAD_10")
        self.ITEMDESCRIPCION_10 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_10.setGeometry(QtCore.QRect(60, 350, 301, 16))
        self.ITEMDESCRIPCION_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_10.setObjectName("ITEMDESCRIPCION_10")
        self.ITEM_SUBTOTAL_10 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_10.setGeometry(QtCore.QRect(670, 350, 51, 16))
        self.ITEM_SUBTOTAL_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_10.setObjectName("ITEM_SUBTOTAL_10")
        self.ITEMMODELO_10 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_10.setGeometry(QtCore.QRect(380, 350, 91, 16))
        self.ITEMMODELO_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_10.setObjectName("ITEMMODELO_10")
        self.ITEMCANTIDAD_11 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_11.setGeometry(QtCore.QRect(500, 370, 51, 16))
        self.ITEMCANTIDAD_11.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_11.setObjectName("ITEMCANTIDAD_11")
        self.ITEMUNIDAD_11 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_11.setGeometry(QtCore.QRect(580, 370, 51, 16))
        self.ITEMUNIDAD_11.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_11.setObjectName("ITEMUNIDAD_11")
        self.ITEMDESCRIPCION_11 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_11.setGeometry(QtCore.QRect(60, 370, 301, 16))
        self.ITEMDESCRIPCION_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_11.setObjectName("ITEMDESCRIPCION_11")
        self.ITEM_SUBTOTAL_11 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_11.setGeometry(QtCore.QRect(670, 370, 51, 16))
        self.ITEM_SUBTOTAL_11.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_11.setObjectName("ITEM_SUBTOTAL_11")
        self.ITEMMODELO_11 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_11.setGeometry(QtCore.QRect(380, 370, 91, 16))
        self.ITEMMODELO_11.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_11.setObjectName("ITEMMODELO_11")
        self.ITEMCANTIDAD_12 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_12.setGeometry(QtCore.QRect(500, 390, 51, 16))
        self.ITEMCANTIDAD_12.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_12.setObjectName("ITEMCANTIDAD_12")
        self.ITEMUNIDAD_12 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_12.setGeometry(QtCore.QRect(580, 390, 51, 16))
        self.ITEMUNIDAD_12.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_12.setObjectName("ITEMUNIDAD_12")
        self.ITEMDESCRIPCION_12 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_12.setGeometry(QtCore.QRect(60, 390, 301, 16))
        self.ITEMDESCRIPCION_12.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_12.setObjectName("ITEMDESCRIPCION_12")
        self.ITEM_SUBTOTAL_12 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_12.setGeometry(QtCore.QRect(670, 390, 51, 16))
        self.ITEM_SUBTOTAL_12.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_12.setObjectName("ITEM_SUBTOTAL_12")
        self.ITEMMODELO_12 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_12.setGeometry(QtCore.QRect(380, 390, 91, 16))
        self.ITEMMODELO_12.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_12.setObjectName("ITEMMODELO_12")
        self.ITEMCANTIDAD_13 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_13.setGeometry(QtCore.QRect(500, 410, 51, 16))
        self.ITEMCANTIDAD_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_13.setObjectName("ITEMCANTIDAD_13")
        self.ITEMUNIDAD_13 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_13.setGeometry(QtCore.QRect(580, 410, 51, 16))
        self.ITEMUNIDAD_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_13.setObjectName("ITEMUNIDAD_13")
        self.ITEMDESCRIPCION_13 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_13.setGeometry(QtCore.QRect(60, 410, 301, 16))
        self.ITEMDESCRIPCION_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_13.setObjectName("ITEMDESCRIPCION_13")
        self.ITEM_SUBTOTAL_13 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_13.setGeometry(QtCore.QRect(670, 410, 51, 16))
        self.ITEM_SUBTOTAL_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_13.setObjectName("ITEM_SUBTOTAL_13")
        self.ITEMMODELO_13 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_13.setGeometry(QtCore.QRect(380, 410, 91, 16))
        self.ITEMMODELO_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_13.setObjectName("ITEMMODELO_13")
        self.ITEMCANTIDAD_14 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_14.setGeometry(QtCore.QRect(500, 430, 51, 16))
        self.ITEMCANTIDAD_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_14.setObjectName("ITEMCANTIDAD_14")
        self.ITEMUNIDAD_14 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_14.setGeometry(QtCore.QRect(580, 430, 51, 16))
        self.ITEMUNIDAD_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_14.setObjectName("ITEMUNIDAD_14")
        self.ITEMDESCRIPCION_14 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_14.setGeometry(QtCore.QRect(60, 430, 301, 16))
        self.ITEMDESCRIPCION_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_14.setObjectName("ITEMDESCRIPCION_14")
        self.ITEM_SUBTOTAL_14 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_14.setGeometry(QtCore.QRect(670, 430, 51, 16))
        self.ITEM_SUBTOTAL_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_14.setObjectName("ITEM_SUBTOTAL_14")
        self.ITEMMODELO_14 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_14.setGeometry(QtCore.QRect(380, 430, 91, 16))
        self.ITEMMODELO_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_14.setObjectName("ITEMMODELO_14")
        self.ITEMCANTIDAD_15 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMCANTIDAD_15.setGeometry(QtCore.QRect(500, 450, 51, 16))
        self.ITEMCANTIDAD_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMCANTIDAD_15.setObjectName("ITEMCANTIDAD_15")
        self.ITEMUNIDAD_15 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMUNIDAD_15.setGeometry(QtCore.QRect(580, 450, 51, 16))
        self.ITEMUNIDAD_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMUNIDAD_15.setObjectName("ITEMUNIDAD_15")
        self.ITEMDESCRIPCION_15 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMDESCRIPCION_15.setGeometry(QtCore.QRect(60, 450, 301, 16))
        self.ITEMDESCRIPCION_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ITEMDESCRIPCION_15.setObjectName("ITEMDESCRIPCION_15")
        self.ITEM_SUBTOTAL_15 = QtWidgets.QLabel(self.centralwidget)
        self.ITEM_SUBTOTAL_15.setGeometry(QtCore.QRect(670, 450, 51, 16))
        self.ITEM_SUBTOTAL_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_SUBTOTAL_15.setObjectName("ITEM_SUBTOTAL_15")
        self.ITEMMODELO_15 = QtWidgets.QLabel(self.centralwidget)
        self.ITEMMODELO_15.setGeometry(QtCore.QRect(380, 450, 91, 16))
        self.ITEMMODELO_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEMMODELO_15.setObjectName("ITEMMODELO_15")
        self.MECANICO = QtWidgets.QPushButton(self.centralwidget)
        self.MECANICO.setGeometry(QtCore.QRect(0, 60, 91, 31))
        self.MECANICO.setObjectName("MECANICO")
        self.ELECTRICO = QtWidgets.QPushButton(self.centralwidget)
        self.ELECTRICO.setGeometry(QtCore.QRect(100, 60, 91, 31))
        self.ELECTRICO.setObjectName("ELECTRICO")
        self.SENSORES = QtWidgets.QPushButton(self.centralwidget)
        self.SENSORES.setGeometry(QtCore.QRect(200, 60, 91, 31))
        self.SENSORES.setObjectName("SENSORES")
        self.CONTROL = QtWidgets.QPushButton(self.centralwidget)
        self.CONTROL.setGeometry(QtCore.QRect(300, 60, 91, 31))
        self.CONTROL.setObjectName("CONTROL")
        self.ESPECIALES = QtWidgets.QPushButton(self.centralwidget)
        self.ESPECIALES.setGeometry(QtCore.QRect(400, 60, 91, 31))
        self.ESPECIALES.setObjectName("ESPECIALES")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(490, 60, 16, 81))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(500, 110, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.TE = QtWidgets.QLineEdit(self.centralwidget)
        self.TE.setGeometry(QtCore.QRect(600, 110, 31, 20))
        self.TE.setMaxLength(3)
        self.TE.setAlignment(QtCore.Qt.AlignCenter)
        self.TE.setObjectName("TE")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 111, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.AGREGARMANUAL = QtWidgets.QPushButton(self.centralwidget)
        self.AGREGARMANUAL.setGeometry(QtCore.QRect(510, 60, 111, 31))
        self.AGREGARMANUAL.setObjectName("AGREGARMANUAL")
        self.BUSCARMANUAL = QtWidgets.QPushButton(self.centralwidget)
        self.BUSCARMANUAL.setGeometry(QtCore.QRect(630, 60, 111, 31))
        self.BUSCARMANUAL.setObjectName("BUSCARMANUAL")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(520, 0, 16, 51))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 50, 781, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.GARANTIA = QtWidgets.QTextEdit(self.centralwidget)
        self.GARANTIA.setGeometry(QtCore.QRect(10, 500, 291, 61))
        self.GARANTIA.setObjectName("GARANTIA")
        self.COMENTARIOS = QtWidgets.QTextEdit(self.centralwidget)
        self.COMENTARIOS.setGeometry(QtCore.QRect(320, 500, 291, 61))
        self.COMENTARIOS.setObjectName("COMENTARIOS")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(620, 470, 20, 121))
        self.line_7.setMidLineWidth(4)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(650, 470, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(640, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.GUARDARYENVIAR = QtWidgets.QPushButton(self.centralwidget)
        self.GUARDARYENVIAR.setGeometry(QtCore.QRect(650, 520, 111, 51))
        self.GUARDARYENVIAR.setObjectName("GUARDARYENVIAR")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(320, 480, 291, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 480, 291, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 570, 511, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(0, 570, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        MainWindow_COT.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_COT)
        self.statusbar.setObjectName("statusbar")
        MainWindow_COT.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_COT)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_COT)

    def retranslateUi(self, MainWindow_COT):
        _translate = QtCore.QCoreApplication.translate

        MainWindow_COT.setWindowTitle(_translate("MainWindow_COT", "Cotizador Figet-Soriana. V1.0.191218"))
        self.label.setText(_translate("MainWindow_COT", "Tienda"))
        self.NUMTIENDA.setText(_translate("MainWindow_COT", "9999"))
        self.label_2.setText(_translate("MainWindow_COT", "Formato"))
        self.label_3.setText(_translate("MainWindow_COT", "Estado"))
        self.label_4.setText(_translate("MainWindow_COT", "Dirección"))
        self.BUSCARINFOTIENDA.setText(_translate("MainWindow_COT", "BUSCAR INFO"))
        self.label_5.setText(_translate("MainWindow_COT", "FECHA"))
        self.fecha.setText(_translate("MainWindow_COT", time.strftime("%D ", time.localtime())))
        self.label_7.setText(_translate("MainWindow_COT", "Resp. Cotizar"))
        self.Usuario.setText(_translate("MainWindow_COT", "Usuario apellido"))
        self.FORMATO.setText(_translate("MainWindow_COT", "ABC"))
        self.ESTADO.setText(_translate("MainWindow_COT", "ABC"))
        self.DIRECCION.setText(_translate("MainWindow_COT", "DIRECCIÓN COMPLETA DE LA TIENDA"))
        self.label_12.setText(_translate("MainWindow_COT", "Titulo Cotización =>"))
        self.TITULOCOTIZACION.setText(
            _translate("MainWindow_COT", "Aquí llevará el título de la cotización pendiente por enviar "))
        self.label_13.setText(_translate("MainWindow_COT", "#"))
        self.toolButton.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_2.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_3.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_4.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_5.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_6.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_7.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_8.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_9.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_10.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_11.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_12.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_13.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_14.setText(_translate("MainWindow_COT", "..."))
        self.toolButton_15.setText(_translate("MainWindow_COT", "..."))
        self.label_14.setText(_translate("MainWindow_COT", "Descripción"))
        self.ITEMDESCRIPCION_1.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.label_16.setText(_translate("MainWindow_COT", "Modelo"))
        self.ITEMMODELO_1.setText(_translate("MainWindow_COT", "123456789012345"))
        self.label_18.setText(_translate("MainWindow_COT", "Cantidad"))
        self.ITEMCANTIDAD_1.setText(_translate("MainWindow_COT", "12345678"))
        self.label_20.setText(_translate("MainWindow_COT", "Unidad"))
        self.ITEMUNIDAD_1.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEM_SUBTOTAL_1.setText(_translate("MainWindow_COT", "12345678"))
        self.label_23.setText(_translate("MainWindow_COT", "Precio"))
        self.ITEMCANTIDAD_2.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_2.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_2.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_2.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_2.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_3.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_3.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_3.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_3.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_3.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_4.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_4.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_4.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_4.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_4.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_5.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_5.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_5.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_5.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_5.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_6.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_6.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_6.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_6.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_6.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_7.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_7.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_7.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_7.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_7.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_8.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_8.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_8.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_8.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_8.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_9.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_9.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_9.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_9.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_9.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_10.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_10.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_10.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_10.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_10.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_11.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_11.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_11.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_11.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_11.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_12.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_12.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_12.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_12.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_12.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_13.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_13.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_13.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_13.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_13.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_14.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_14.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_14.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_14.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_14.setText(_translate("MainWindow_COT", "123456789012345"))
        self.ITEMCANTIDAD_15.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMUNIDAD_15.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMDESCRIPCION_15.setText(
            _translate("MainWindow_COT", "aquí va la descripción del item que se está cotizando 12"))
        self.ITEM_SUBTOTAL_15.setText(_translate("MainWindow_COT", "12345678"))
        self.ITEMMODELO_15.setText(_translate("MainWindow_COT", "123456789012345"))
        self.MECANICO.setText(_translate("MainWindow_COT", "MECANICO"))
        self.ELECTRICO.setText(_translate("MainWindow_COT", "ELECTRICO"))
        self.SENSORES.setText(_translate("MainWindow_COT", "SENSORES"))
        self.CONTROL.setText(_translate("MainWindow_COT", "CONTROL"))
        self.ESPECIALES.setText(_translate("MainWindow_COT", "ESPECIALES"))
        self.label_15.setText(_translate("MainWindow_COT", "Tiempo Entrega"))
        self.TE.setText(_translate("MainWindow_COT", "3"))
        self.comboBox.setItemText(0, _translate("MainWindow_COT", "DIAS"))
        self.comboBox.setItemText(1, _translate("MainWindow_COT", "SEMANAS"))
        self.AGREGARMANUAL.setText(_translate("MainWindow_COT", "Agregar Item Manual"))
        self.BUSCARMANUAL.setText(_translate("MainWindow_COT", "Buscar Item Manual"))
        self.GARANTIA.setHtml(_translate("MainWindow_COT",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.COMENTARIOS.setHtml(_translate("MainWindow_COT",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LAS REFACCIONES SE ENCUENTRAN SUJETOS SALVO PREVIA VENTA.   LOS TIEMPOS DE ENTREGA PUEDEN VARIAR DEBIDO A CONTINGENCIA COVID-19</p>\n"
                                            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_17.setText(_translate("MainWindow_COT", "SUBTOTAL"))
        self.label_19.setText(_translate("MainWindow_COT", "200,000.00"))
        self.GUARDARYENVIAR.setText(_translate("MainWindow_COT", "GUARDAR Y ENVIAR"))
        self.label_21.setText(_translate("MainWindow_COT", "COMENTARIOS"))
        self.label_22.setText(_translate("MainWindow_COT", "GARANTIAS"))
        self.label_24.setText(_translate("MainWindow_COT", "NOTAS EXTRAS"))

        # BOTONES#BOTONES#BOTONES#BOTONES
        self.BUSCARINFOTIENDA.clicked.connect(self.buscarinfo)
        # self.MECANICO.clicked.connect(self.AGREGARITEMS)
        self.GUARDARYENVIAR.clicked.connect(self.PRUEBAS)
        # self.CONTROL.clicked.connect(self.actualizar)
        self.MECANICO.clicked.connect(self.mecanico)
        self.ELECTRICO.clicked.connect(self.electrico)
        self.SENSORES.clicked.connect(self.sensores)
        self.CONTROL.clicked.connect(self.control)
        self.ESPECIALES.clicked.connect(self.especiales)
        self.toolButton.clicked.connect(self.borrarfila1)
        self.toolButton_2.clicked.connect(self.borrarfila2)
        self.toolButton_3.clicked.connect(self.borrarfila3)
        self.toolButton_4.clicked.connect(self.borrarfila4)
        self.toolButton_5.clicked.connect(self.borrarfila5)
        self.toolButton_6.clicked.connect(self.borrarfila6)
        self.toolButton_7.clicked.connect(self.borrarfila7)
        self.toolButton_8.clicked.connect(self.borrarfila8)
        self.toolButton_9.clicked.connect(self.borrarfila9)
        self.toolButton_10.clicked.connect(self.borrarfila10)
        self.toolButton_11.clicked.connect(self.borrarfila11)
        self.toolButton_12.clicked.connect(self.borrarfila12)
        self.toolButton_13.clicked.connect(self.borrarfila13)
        self.toolButton_14.clicked.connect(self.borrarfila14)
        self.toolButton_15.clicked.connect(self.borrarfila15)

        self.AGREGARMANUAL.clicked.connect(self.AGREGARITEMMANUAL)
        self.BUSCARMANUAL.clicked.connect(self.SELECCIONARITEMMANUAL)

    # BOTONES#BOTONES#BOTONES#BOTONES
    def PRUEBAS(self):

        a=self.VALIDACION()
        if a ==1:
            # NO HACER NADA
            return()
        if a==0:
            ##print("ACCCIONANDO FUNCIONES PARA GENERAR ")
            self.GENERARCOTIZACION()
            return()

        return ()

    def secuencia(self):
        #print("iniciando lastrow")
        basedatos = "administrativo.db"
        try:

            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            SELECT = """SELECT seq from sqlite_sequence
                       where name ='cotizaciones'
                       """
            cursor.execute(SELECT)
            record = cursor.fetchone()

            registros = record[0]
            cursor.close
            #print("ultimoo registro", registros)
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                return (registros)

    def VALIDACION(self):
        print("validando")
        tienda = (self.NUMTIENDA.text())
        titulo = (self.TITULOCOTIZACION.text())
        comentarios = (self.COMENTARIOS.toPlainText())
        te = (self.TE.text())
        notas = self.lineEdit.text()

        if tienda == "":
            mensaje = "FALTA INGRESAR NÚMERO DE TIENDA"
            error(mensaje)
            return(1)

        if titulo == "":
            mensaje = "FALTA INGRESAR TÍTULO A LA COTIZACIÓN"
            error(mensaje)
            return (1)

        if comentarios == "":
            mensaje = "FALTA INGRESAR COMENTARIOS"
            error(mensaje)
            return (1)

        if te == "":
            mensaje = "FALTA INGRESAR TIEMPO DE ENTREGA"
            error(mensaje)
            return (1)

        if notas == "":
            mensaje = "FALTA INGRESAR NOTAS EXTRAS EN DONDE SE RESUME LA COTIZACION"
            error(mensaje)
            return (1)
        return (0)

    def obtenerlistaitems(self):
        numsoriana = "S/C"
        LISTA = []
        vec = globals()["vectoritems"]
        largo = (len(vec))

        for i in range(largo):
            LISTA.append([numsoriana, (vec[i][0]), (vec[i][5]), (vec[i][1]), (vec[i][2]), (vec[i][4]), (vec[i][3])])
        return(LISTA)

    def GENERARCOTIZACION(self):
        # print("seccion de pruebas")
        # //////////////////////////////////
        # FECHA[0][1-3]
        fechaacortada = []
        fechaacortada.append(year)  # año
        fechaacortada.append(month)  # mes
        fechaacortada.append(day)  # dia
        # print(fechaacortada)
        # FECHA
        # //////////////////////////////////
        # //////////////////////////////////
        # NUMERO COTIZACIÓN [1]
        #sec = int(self.secuencia()) + 1
        #det = (self.NUMTIENDA.text())
        #numcot = det + "-" + str(day) + str(month) + str(year) + "-" + "CV" + "-" + str(sec)
        numcot = globals()['cotizacion']
        # NUMERO COTIZACIÓN
        # //////////////////////////////////
        # //////////////////////////////////
        # NUM DE TIENDA[2]
        INFOTIENDA = self.buscarinfo()
        det = INFOTIENDA[0]
        # print(det)
        # NUM DE TIENDA
        # //////////////////////////////////
        # //////////////////////////////////
        # DIRECCION TIENDA [3]
        DIRECCION = [INFOTIENDA[1], INFOTIENDA[2], INFOTIENDA[3]]
        # print(DIRECCION)
        # DIRECCION TIENDA
        # //////////////////////////////////
        # //////////////////////////////////
        # TE[4] notas[5] garantias[6]
        a = self.garantiasycomentarios()
        TE = a[4] + "-" + a[5]
        notas = a[3]
        garantias = a[2]
        # //////////////////////////////////
        # //////////////////////////////////
        # QUIEN COTIZA[7]
        nombre = "Asistente Electrónico"
        numero = 'PHONE NUMBER'
        correo = "EMAIL@EMAIL.COM"
        quiencotiza = [nombre, numero, correo]
        # QUIEN COTIZA[7]
        # //////////////////////////////////
        # //////////////////////////////////
        # TITULO[8]
        titulo = a[1]
        # print(titulo)
        # TITULO[8]
        # //////////////////////////////////
        # //////////////////////////////////
        # LISTA DE ITEMS [9]
        LISTA=self.obtenerlistaitems()
        #numsoriana = "S/C"
        #descripcion = "DESCRIPCION"
        #marca = "MARCA"
        #modelo = "MODELO"
        #cant = "1"
        #unidadmedida = "PIEZA"
        #precio = "100"
        #LISTA = []
        #LISTA.append([numsoriana, descripcion, marca, modelo, cant, unidadmedida, precio])
        # LISTA DE ITEMS [9]
        # //////////////////////////////////
        # //////////////////////////////////
        # NUMERO DE CELDAS [10]
        cantidaditems = len(LISTA)  # len(globals()["vectoritems"])
        # print(cantidaditems)
        celda = 20
        numcelda = []
        for i in range(cantidaditems):
            celda += 1
            z = str(celda)
            c = 'C' + z
            d = 'D' + z
            e = 'E' + z
            f = 'F' + z
            g = 'G' + z
            h = 'H' + z
            i = 'I' + z
            numcelda.append([c, d, e, f, g, h, i])
        #print(numcelda)
        # NUMERO DE CELDAS [10]
        # //////////////////////////////////
        VECTORDEINFORMACION = [fechaacortada, numcot, det, DIRECCION, TE, notas, garantias, quiencotiza, titulo, LISTA,
                               numcelda]
        # //////////////////////////////////
        # print("#########################################3")

        # //////////////////////////////////
        consecutivo = int(self.secuencia()) + 1
        HOY = int(time.mktime(time.localtime()))
        preciocliente = self.label_19.text()
        informacionitems = globals()["vectoritems"]
        largo = (len(informacionitems))
        ListaITEMS = []
        ListaCANTITEMS = []
        ListaUNIDAD = []

        for i in range(largo):
            ListaITEMS.append(informacionitems[i][1])
            ListaCANTITEMS.append(informacionitems[i][2])
            ListaUNIDAD.append(informacionitems[i][4])

        vectorBD = [consecutivo, numcot, det, titulo, "0", preciocliente,
                    "0", json.dumps(quiencotiza), a[4], a[5], a[3], "0", a[0], HOY,
                    json.dumps(ListaITEMS), json.dumps(ListaCANTITEMS), json.dumps(ListaUNIDAD), garantias]
        # //////////////////////////////////
        proc = subprocess.Popen(["python", "wait.py"])
        # print("#########################################3")
        self.guardarcotizacion(vectorBD)
        # print("#########################################3")
        teoria=llenarformato(VECTORDEINFORMACION)
        # print("#########################################3")
        self.enviarcorreo(det,numcot,titulo)
        proc.terminate()
        # print("#########################################3")
        print("GENERANDO TASK EN ASANA")
        #notasextras = str(self.lineEdit.text())
        #titulotask="Cotizacion: "+str(numcot)
        #publicacion=asana_task(str(titulotask), str(notasextras))
        #print(publicacion)
        # //////////////////////////////////
        mensaje="¡Cotización enviada!"
        error(mensaje)
        print("LISTO EL COTIZADOR")
        #exit()
        self.salir()

        return ()



    def enviarcorreo(self,det,numcot,titulo):#,vectorBD,VECTORDEINFORMACION,numcot,titulo):
        tienda=int(det)
        #ASUNTO
        asunto=str(titulo)#"Cotizacion FIDGET->"
        #CUERPO DEL CORREO
        body="""
        Se comparte cotización solicitada, favor de considerar los tiempos de entrega.
        
        saludos cordiales!
        """
        #VECTOR DESTINATARIOS
        fijo1='COMPY_EMAIL1@EMAIL.COM'
        fijo2='COMPY_EMAIL2@EMAIL.COM'
        fijo3='COMPY_EMAIL3@EMAIL.COM'

        if tienda==0:
            vectormails=self.vectorcorreos(tienda)
            vectormails.append(fijo1)#DESACTIVAR PARA QUE FUNCIONEN LOS CORREOS
        else:
            vectormails=self.vectorcorreos(tienda)
            vectormails.append(fijo1)#DESACTIVAR PARA QUE FUNCIONEN LOS CORREOS
            vectormails.append(fijo2)
            vectormails.append(fijo3)
            
        # print(vectormails)

        # enviarmail(vector,asunto,cuerpotexto,numcot)
        enviarmail(vectormails,asunto,body,numcot)

        return()

    def vectorcorreos(self,determinante):
        vectormails=[]
        rutabasedatos="SORIANAMAILS.db"
        try:
            sqliteConnection = sqlite3.connect(rutabasedatos)
            cursor = sqliteConnection.cursor()
            # print("Successfully Connected to SQLite")
            SELECT = """SELECT gerencia_mail, admin_mail, mtto_mail
                    FROM
                    mails
                    WHERE
                    tienda =?
                    """
            cursor.execute(SELECT,(determinante,))
            record = cursor.fetchall()

            vectormails.append(record[0][0])
            vectormails.append(record[0][1])
            vectormails.append(record[0][2])

            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                # print("Cerrando conexión de Base de Datos")
                if determinante==0:
                    asistente=["EMAIL@EMAIL.COM"]
                    return(asistente)                                
                return(vectormails) 

        return()


    def guardarcotizacion(self,vector):
        # print(vector)
        basedatos = 'administrativo.db'
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            # print("Successfully Connected to SQLite")
            vector_query = """ INSERT INTO 'cotizaciones'
             ('consecutivo','numcotizacion','numtienda','titulocotizacion',
             'costofidget','preciocliente','ganancia','elabora',
             'TEnum','TEDS','comentarios','estatus','motivo','timestampcreacion',
             'items','cantitems','unidad','garantias')
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            # guardar en base de datos
            cursor.execute(vector_query, vector)
            # actualizar base de datos
            sqliteConnection.commit()
            # print("Image and file inserted successfully as a BLOB into a table")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                # print("SE HA GUARDADO LA INFORMACION DE LA COTIZACION EN DATABASE")

        return()

    def calculosubtotal(self):
        listavector = vectoritems
        largo = len(listavector)
        costos = []
        for i in range(largo):
            multiplicar = (float(listavector[i][3])) * (float(listavector[i][2]))
            costos.append(multiplicar)
        sumatoria = str((sum(costos)))

        self.label_19.setText(sumatoria)
        return ()

    def AGREGARITEMS(self,seccion):
        limite = len(globals()["vectoritems"])
        if limite > 14:
            # print("HAS ALCANZADO EL LÍMITE")
            return ()
        Dialog = QtWidgets.QDialog()
        # enviar datos al form DIALOG
        self.m = seccion  # "HOLA desde el primero form"
        ui = Ui_Dialog(self.m)
        ui.setupUi(Dialog)
        ui.seleccionar(self.m)
        ui.inicio()
        Dialog.show()
        respuesta = Dialog.exec_()

        if respuesta == QtWidgets.QDialog.Accepted:
            # print("Boton aceptado")
            # comando de tomar en base de datos el dato guardado
            self.tomarinfo()
            self.actualizar()
            self.calculosubtotal()

        else:
            print("Boton cancelado")
        # print("respuesta")
        return ()

    def SELECCIONARITEMMANUAL(self):
        Dialog = QtWidgets.QDialog()
        # enviar datos al form DIALOG
        #self.m = seccion  # "HOLA desde el primero form"
        ui = Ui_Dialog_SELCCIONARMANUAL()
        ui.setupUi(Dialog)
        #ui.buttonBox.setEnabled(False)
        ui.SELECCIONAR_llenarCB_SUBCAT()
        Dialog.show()
        respuesta = Dialog.exec_()

        if respuesta == QtWidgets.QDialog.Accepted:
            # print("Boton aceptado")
            # comando de tomar en base de datos el dato guardado

            # print("guardando DESDE SELECCIONAR manual EL ITEM ")
            self.tomarinfo()
            self.actualizar()
            self.calculosubtotal()

        else:
            print("Boton cancelado")
        return()

    def AGREGARITEMMANUAL(self):
        Dialog = QtWidgets.QDialog()
        # enviar datos al form DIALOG
        ui = Ui_Dialog_AM()
        ui.setupUi(Dialog)
        ui.buttonBox.setEnabled(False)
        ui.GENERARID()#activando funciones de otra librería
        Dialog.show()
        respuesta = Dialog.exec_()

        if respuesta == QtWidgets.QDialog.Accepted:
            # print("Boton aceptado")
            # comando de tomar en base de datos el dato guardado
            cotizacion=globals()['cotizacion']
            ui.guardarITEMmanual(cotizacion)
            print("guardando desde cotizador")
            self.tomarinfo()
            self.actualizar()
            self.calculosubtotal()

        else:
            print("Boton cancelado")
        return()

    def tomarinfo(self):
        # print("TOMANDO INFORMACIÓN")
        # print("*************************")
        temporal = ""
        tempcantidad = ""
        tempDB=""
        SUBCAT = "items.db"
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT = """SELECT item, cantidad, DB
                    from pasar
                    where ID = 1
                    """
            # print("INTENTO")
            cursor.execute(SELECT)
            record = cursor.fetchone()

            temporal = record[0]
            tempcantidad = record[1]
            tempDB=record[2]
            # print(tempcantidad)
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                # print("INSTANCE")
                print(isinstance(tempcantidad, int))
                if isinstance(tempcantidad, int):
                    # print("es núm entero")
                    #self.agregar(temporal, tempcantidad)
                    self.seleccionarbasededatos(temporal, tempcantidad,tempDB)
                    return ()
                if isinstance(tempcantidad, float):
                    # print("es flotante")
                    #self.agregar(temporal, tempcantidad)
                    self.seleccionarbasededatos(temporal, tempcantidad, tempDB)
                    return ()
                else:
                    print("ERROR EN CANTIDAD ALV")

                # self.agregar(temporal,tempcantidad)
        return ()

    def seleccionarbasededatos(self, temporal, tempcantidad,tempDB):
        if tempDB=="AM":
            SEL = """SELECT descripcion, numfid, subtotal, medida, marca from AM where numfid = ? """
            self.agregar(temporal, tempcantidad, SEL)
            return()
        if tempDB=="MECANICO":
            #SEL = """SELECT descripcion, numfid, subtotal, medida, marca from mecanico where numfid = ? """
            ## print("mecanico")
            SEL=globals()['seleccionartipoBD']
            self.agregar(temporal, tempcantidad, SEL)
            return()
        if tempDB=="ELECTRICO":
            SEL=globals()['seleccionartipoBD']
            self.agregar(temporal, tempcantidad, SEL)
            return()
        if tempDB=="SENSORES":
            SEL=globals()['seleccionartipoBD']
            self.agregar(temporal, tempcantidad, SEL)
            return()
        if tempDB=="CONTROL":
            SEL=globals()['seleccionartipoBD']
            self.agregar(temporal, tempcantidad, SEL)
            return()
        if tempDB=="ESPECIALES":
            SEL=globals()['seleccionartipoBD']
            self.agregar(temporal, tempcantidad, SEL)
            return()

    def agregar(self, subcategoria, tempcantidad, SELBD):
        # print("*************************")
        # print("AGREGANDO ITEMS AL VECTOR")
        # vectorsimulador=['descripcion','modelo','cantidad','unidad','precio']
        vec = (globals()["vectoritems"])
        # print(vec)
        vector = []
        SUBCAT = "items.db"
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            #SELECT = """SELECT descripcion, numfid, subtotal, medida, marca from mecanico where numfid = ? """
            SELECT=SELBD
            cursor.execute(SELECT, (subcategoria,))
            record = cursor.fetchall()

            for row in record:
                vector.append(row[0])
                vector.append(row[1])
                vector.append(tempcantidad)
                vector.append(row[2])
                vector.append(row[3])
                vector.append(row[4])

            # print("VECTOR FORMADO")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                # print("AGREGANDO VECTOR GLOBAL")
                vec.append(vector)
                (globals()["vectoritems"]) = vec
                # print("Cerrando conexión de Base de Datos")
                # print(vec)
        return ()
# 0000000000000000000000000000000000000000
    def mecanico(self):
        seccion = "MECANICO"
        select=("""SELECT descripcion, numfid, subtotal, medida, marca from mecanico where numfid = ? """)
        globals()['seleccionartipoBD']=select
        self.AGREGARITEMS(seccion)
        return ()

    def electrico(self):
        seccion = "ELECTRICO"
        select = """SELECT descripcion, numfid, subtotal, medida, marca from electrico where numfid = ? """
        globals()['seleccionartipoBD'] = select
        self.AGREGARITEMS(seccion)
        return ()

    def sensores(self):
        seccion = "SENSORES"
        select = """SELECT descripcion, numfid, subtotal, medida, marca from sensores where numfid = ? """
        globals()['seleccionartipoBD'] = select
        self.AGREGARITEMS(seccion)
        return ()

    def control(self):
        seccion = "CONTROL"
        select = """SELECT descripcion, numfid, subtotal, medida, marca from control where numfid = ? """
        globals()['seleccionartipoBD'] = select
        self.AGREGARITEMS(seccion)
        return ()

    def especiales(self):
        seccion = "ESPECIALES"
        select = """SELECT descripcion, numfid, subtotal, medida, marca from especiales where numfid = ? """
        globals()['seleccionartipoBD'] = select
        self.AGREGARITEMS(seccion)
        return ()

    def actualizar(self):
        # print("*************************")
        vector = globals()["vectoritems"]
        longitudvector = len(globals()["vectoritems"])
        # print("longitud ->", longitudvector)
        # print("*************************")
        pag = int(0)
        a1 = 0
        a2 = 1
        a3 = 2
        a4 = 4
        a5 = 3

        # print(vector)
        if longitudvector == 0:
            print("no hay consultas")
            return ()
        if longitudvector > 0:
            pos = pag
            self.toolButton.setText(str(pos + 1))
            self.toolButton.setEnabled(1)
            self.ITEMDESCRIPCION_1.setText(str(vector[pos][a1]))
            self.ITEMMODELO_1.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_1.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_1.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_1.setText(str(vector[pos][a5]))
        if longitudvector > 1:
            pos = pag + 1
            self.toolButton_2.setText(str(pos + 1))
            self.toolButton_2.setEnabled(1)
            self.ITEMDESCRIPCION_2.setText(str(vector[pos][a1]))
            self.ITEMMODELO_2.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_2.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_2.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_2.setText(str(vector[pos][a5]))
        if longitudvector > 2:
            pos = pag + 2
            self.toolButton_3.setText(str(pos + 1))
            self.toolButton_3.setEnabled(1)
            self.ITEMDESCRIPCION_3.setText(str(vector[pos][a1]))
            self.ITEMMODELO_3.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_3.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_3.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_3.setText(str(vector[pos][a5]))
        if longitudvector > 3:
            pos = pag + 3
            self.toolButton_4.setText(str(pos + 1))
            self.toolButton_4.setEnabled(1)
            self.ITEMDESCRIPCION_4.setText(str(vector[pos][a1]))
            self.ITEMMODELO_4.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_4.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_4.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_4.setText(str(vector[pos][a5]))
        if longitudvector > 4:
            pos = pag + 4
            self.toolButton_5.setText(str(pos + 1))
            self.toolButton_5.setEnabled(1)
            self.ITEMDESCRIPCION_5.setText(str(vector[pos][a1]))
            self.ITEMMODELO_5.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_5.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_5.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_5.setText(str(vector[pos][a5]))
        if longitudvector > 5:
            pos = pag + 5
            self.toolButton_6.setText(str(pos + 1))
            self.toolButton_6.setEnabled(1)
            self.ITEMDESCRIPCION_6.setText(str(vector[pos][a1]))
            self.ITEMMODELO_6.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_6.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_6.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_6.setText(str(vector[pos][a5]))
        if longitudvector > 6:
            pos = pag + 6
            self.toolButton_7.setText(str(pos + 1))
            self.toolButton_7.setEnabled(1)
            self.ITEMDESCRIPCION_7.setText(str(vector[pos][a1]))
            self.ITEMMODELO_7.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_7.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_7.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_7.setText(str(vector[pos][a5]))
        if longitudvector > 7:
            pos = pag + 7
            self.toolButton_8.setText(str(pos + 1))
            self.toolButton_8.setEnabled(1)
            self.ITEMDESCRIPCION_8.setText(str(vector[pos][a1]))
            self.ITEMMODELO_8.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_8.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_8.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_8.setText(str(vector[pos][a5]))
        if longitudvector > 8:
            pos = pag + 8
            self.toolButton_9.setText(str(pos + 1))
            self.toolButton_9.setEnabled(1)
            self.ITEMDESCRIPCION_9.setText(str(vector[pos][a1]))
            self.ITEMMODELO_9.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_9.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_9.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_9.setText(str(vector[pos][a5]))
        if longitudvector > 9:
            pos = pag + 9
            self.toolButton_10.setText(str(pos + 1))
            self.toolButton_10.setEnabled(1)
            self.ITEMDESCRIPCION_10.setText(str(vector[pos][a1]))
            self.ITEMMODELO_10.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_10.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_10.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_10.setText(str(vector[pos][a5]))
        if longitudvector > 10:
            pos = pag + 10
            self.toolButton_11.setText(str(pos + 1))
            self.toolButton_11.setEnabled(1)
            self.ITEMDESCRIPCION_11.setText(str(vector[pos][a1]))
            self.ITEMMODELO_11.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_11.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_11.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_11.setText(str(vector[pos][a5]))
        if longitudvector > 11:
            pos = pag + 11
            self.toolButton_12.setText(str(pos + 1))
            self.toolButton_12.setEnabled(1)
            self.ITEMDESCRIPCION_12.setText(str(vector[pos][a1]))
            self.ITEMMODELO_12.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_12.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_12.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_12.setText(str(vector[pos][a5]))
        if longitudvector > 12:
            pos = pag + 12
            self.toolButton_13.setText(str(pos + 1))
            self.toolButton_13.setEnabled(1)
            self.ITEMDESCRIPCION_13.setText(str(vector[pos][a1]))
            self.ITEMMODELO_13.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_13.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_13.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_13.setText(str(vector[pos][a5]))
        if longitudvector > 13:
            pos = pag + 13
            self.toolButton_14.setText(str(pos + 1))
            self.toolButton_14.setEnabled(1)
            self.ITEMDESCRIPCION_14.setText(str(vector[pos][a1]))
            self.ITEMMODELO_14.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_14.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_14.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_14.setText(str(vector[pos][a5]))
        if longitudvector > 14:
            pos = pag + 14
            self.toolButton_15.setText(str(pos + 1))
            self.toolButton_15.setEnabled(1)
            self.ITEMDESCRIPCION_15.setText(str(vector[pos][a1]))
            self.ITEMMODELO_15.setText(str(vector[pos][a2]))
            self.ITEMCANTIDAD_15.setText(str(vector[pos][a3]))
            self.ITEMUNIDAD_15.setText(str(vector[pos][a4]))
            self.ITEM_SUBTOTAL_15.setText(str(vector[pos][a5]))

        return ()

    def borrarfila1(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[0]
        (globals()["vectoritems"]) = vec
        self.toolButton.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila2(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[1]
        (globals()["vectoritems"]) = vec
        self.toolButton_2.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila3(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[2]
        (globals()["vectoritems"]) = vec
        self.toolButton_3.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila4(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[3]
        (globals()["vectoritems"]) = vec
        self.toolButton_4.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila5(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[4]
        (globals()["vectoritems"]) = vec
        self.toolButton_5.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila6(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[5]
        (globals()["vectoritems"]) = vec
        self.toolButton_6.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila7(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[6]
        (globals()["vectoritems"]) = vec
        self.toolButton_7.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila8(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[7]
        (globals()["vectoritems"]) = vec
        self.toolButton_8.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila9(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[8]
        (globals()["vectoritems"]) = vec
        self.toolButton_9.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila10(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[9]
        (globals()["vectoritems"]) = vec
        self.toolButton_10.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila11(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[10]
        (globals()["vectoritems"]) = vec
        self.toolButton_11.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila12(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[11]
        (globals()["vectoritems"]) = vec
        self.toolButton_12.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila13(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[12]
        (globals()["vectoritems"]) = vec
        self.toolButton_13.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila14(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[13]
        (globals()["vectoritems"]) = vec
        self.toolButton_14.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrarfila15(self):
        self.borrartodo()
        vec = (globals()["vectoritems"])
        del vec[14]
        (globals()["vectoritems"]) = vec
        self.toolButton_15.setEnabled(0)
        self.actualizar()
        self.calculosubtotal()
        return ()

    def borrartodo(self):
        self.toolButton.setText("")
        self.toolButton.setEnabled(0)
        self.ITEMDESCRIPCION_1.setText("")
        self.ITEMMODELO_1.setText("")
        self.ITEMCANTIDAD_1.setText("")
        self.ITEMUNIDAD_1.setText("")
        self.ITEM_SUBTOTAL_1.setText("")

        self.toolButton_2.setText("")
        self.toolButton_2.setEnabled(0)
        self.ITEMDESCRIPCION_2.setText("")
        self.ITEMMODELO_2.setText("")
        self.ITEMCANTIDAD_2.setText("")
        self.ITEMUNIDAD_2.setText("")
        self.ITEM_SUBTOTAL_2.setText("")

        self.toolButton_3.setText("")
        self.toolButton_3.setEnabled(0)
        self.ITEMDESCRIPCION_3.setText("")
        self.ITEMMODELO_3.setText("")
        self.ITEMCANTIDAD_3.setText("")
        self.ITEMUNIDAD_3.setText("")
        self.ITEM_SUBTOTAL_3.setText("")

        self.toolButton_4.setText("")
        self.toolButton_4.setEnabled(0)
        self.ITEMDESCRIPCION_4.setText("")
        self.ITEMMODELO_4.setText("")
        self.ITEMCANTIDAD_4.setText("")
        self.ITEMUNIDAD_4.setText("")
        self.ITEM_SUBTOTAL_4.setText("")

        self.toolButton_5.setText("")
        self.toolButton_5.setEnabled(0)
        self.ITEMDESCRIPCION_5.setText("")
        self.ITEMMODELO_5.setText("")
        self.ITEMCANTIDAD_5.setText("")
        self.ITEMUNIDAD_5.setText("")
        self.ITEM_SUBTOTAL_5.setText("")

        self.toolButton_6.setText("")
        self.toolButton_6.setEnabled(0)
        self.ITEMDESCRIPCION_6.setText("")
        self.ITEMMODELO_6.setText("")
        self.ITEMCANTIDAD_6.setText("")
        self.ITEMUNIDAD_6.setText("")
        self.ITEM_SUBTOTAL_6.setText("")

        self.toolButton_7.setText("")
        self.toolButton_7.setEnabled(0)
        self.ITEMDESCRIPCION_7.setText("")
        self.ITEMMODELO_7.setText("")
        self.ITEMCANTIDAD_7.setText("")
        self.ITEMUNIDAD_7.setText("")
        self.ITEM_SUBTOTAL_7.setText("")

        self.toolButton_8.setText("")
        self.toolButton_8.setEnabled(0)
        self.ITEMDESCRIPCION_8.setText("")
        self.ITEMMODELO_8.setText("")
        self.ITEMCANTIDAD_8.setText("")
        self.ITEMUNIDAD_8.setText("")
        self.ITEM_SUBTOTAL_8.setText("")

        self.toolButton_9.setText("")
        self.toolButton_9.setEnabled(0)
        self.ITEMDESCRIPCION_9.setText("")
        self.ITEMMODELO_9.setText("")
        self.ITEMCANTIDAD_9.setText("")
        self.ITEMUNIDAD_9.setText("")
        self.ITEM_SUBTOTAL_9.setText("")

        self.toolButton_10.setText("")
        self.toolButton_10.setEnabled(0)
        self.ITEMDESCRIPCION_10.setText("")
        self.ITEMMODELO_10.setText("")
        self.ITEMCANTIDAD_10.setText("")
        self.ITEMUNIDAD_10.setText("")
        self.ITEM_SUBTOTAL_10.setText("")

        self.toolButton_11.setText("")
        self.toolButton_11.setEnabled(0)
        self.ITEMDESCRIPCION_11.setText("")
        self.ITEMMODELO_11.setText("")
        self.ITEMCANTIDAD_11.setText("")
        self.ITEMUNIDAD_11.setText("")
        self.ITEM_SUBTOTAL_11.setText("")

        self.toolButton_12.setText("")
        self.toolButton_12.setEnabled(0)
        self.ITEMDESCRIPCION_12.setText("")
        self.ITEMMODELO_12.setText("")
        self.ITEMCANTIDAD_12.setText("")
        self.ITEMUNIDAD_12.setText("")
        self.ITEM_SUBTOTAL_12.setText("")

        self.toolButton_13.setText("")
        self.toolButton_13.setEnabled(0)
        self.ITEMDESCRIPCION_13.setText("")
        self.ITEMMODELO_13.setText("")
        self.ITEMCANTIDAD_13.setText("")
        self.ITEMUNIDAD_13.setText("")
        self.ITEM_SUBTOTAL_13.setText("")

        self.toolButton_14.setText("")
        self.toolButton_14.setEnabled(0)
        self.ITEMDESCRIPCION_14.setText("")
        self.ITEMMODELO_14.setText("")
        self.ITEMCANTIDAD_14.setText("")
        self.ITEMUNIDAD_14.setText("")
        self.ITEM_SUBTOTAL_14.setText("")

        self.toolButton_15.setText("")
        self.toolButton_15.setEnabled(0)
        self.ITEMDESCRIPCION_15.setText("")
        self.ITEMMODELO_15.setText("")
        self.ITEMCANTIDAD_15.setText("")
        self.ITEMUNIDAD_15.setText("")
        self.ITEM_SUBTOTAL_15.setText("")
        return ()

    # FUNCION PARA OBTENER TEXTO DE GARANTIAS COMENTARIOS Y NOTAS EXTRAS
    def garantiasycomentarios(self):
        notasextras = self.lineEdit.text()
        titulo = self.TITULOCOTIZACION.text()
        garantia = self.GARANTIA.toPlainText()
        comentarios = (self.COMENTARIOS.toPlainText())#+notasextras
        TEDS = self.comboBox.currentText()
        TEcant = self.TE.text()
        timestampHOY = int(time.mktime(time.localtime()))

        vector = ["0", titulo, garantia, comentarios, TEDS, TEcant]
        return (vector)

    def buscarinfo(self):
        tienda = (self.NUMTIENDA.text())
        if tienda == "":
            mensaje = "FAVOR INGRESAR DETERMINANTE/NUMERO DE TIENDA"
            error(mensaje)
            return ()
        else:
            tienda = (self.NUMTIENDA.text())
            infotienda = consultar(int(tienda))
            globals()['vectorinfotienda'] = infotienda
            self.FORMATO.setText(infotienda[3])
            self.ESTADO.setText(infotienda[4])
            self.DIRECCION.setText(infotienda[7])
            vector = []
            vector = [tienda, infotienda[3], infotienda[4], infotienda[7]]
            sec = int(self.secuencia()) + 1
            det = (self.NUMTIENDA.text())
            numcot = det + "-" + str(day) + str(month) + str(year) + "-" + "V2" + "-" + str(sec)
            globals()['cotizacion'] = numcot
            self.liberarbotones()

            return (vector)

    def bloquearbotones(self):
        self.AGREGARMANUAL.setEnabled(False)
        self.BUSCARMANUAL.setEnabled(False)
        self.MECANICO.setEnabled(False)
        self.ELECTRICO.setEnabled(False)
        self.SENSORES.setEnabled(False)
        self.CONTROL.setEnabled(False)
        self.ESPECIALES.setEnabled(False)
        self.GUARDARYENVIAR.setEnabled(False)
        return

    def liberarbotones(self):
        self.AGREGARMANUAL.setEnabled(True)
        self.BUSCARMANUAL.setEnabled(True)
        self.MECANICO.setEnabled(True)
        self.ELECTRICO.setEnabled(True)
        self.SENSORES.setEnabled(True)
        self.CONTROL.setEnabled(True)
        self.ESPECIALES.setEnabled(True)
        self.GUARDARYENVIAR.setEnabled(True)
        return

    def borrartextedit(self):
        self.NUMTIENDA.setText("")
        self.TITULOCOTIZACION.setText("")

        return ()

    def AGREGARITEMS_1(self):
        script = "AGREGARITEMS_1.py"
        subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        # print("form 2 abierto")
        return ()

def consultar(determinante):
    try:
        sqliteConnection = sqlite3.connect(DBinfotiendas)
        cursor = sqliteConnection.cursor()
        SELECT = """SELECT * from Tiendas where tienda = ?  """
        cursor.execute(SELECT, (determinante,))
        record = cursor.fetchone()
        # print("tomando consulta")
        cursor.close
    except sqlite3.Error as error:
        print("Error, ALV -----> ", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            # print("Cerrando conexión")
    return (record)

def error(mensaje):
    msg = QMessageBox()
    msg.setWindowTitle("ERROR")
    msg.setIcon(QMessageBox.Information)
    msg.setText(mensaje)
    x = msg.exec_()
    return ()

def gestor():
        script = "GESTORCOTIZACIONES_1_1.py"
        # os.system(script)
        subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        sys.exit()
        #return ()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_COT = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_cotizador()
    ui.setupUi(MainWindow_COT)
    ui.bloquearbotones()
    MainWindow_COT.show()
    ui.borrartodo()
    ui.borrartextedit()
    sys.exit(app.exec_())

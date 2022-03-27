from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
from pathlib import Path
from datetime import date, datetime
import subprocess
import dateutil.parser as dp
import logging
import sqlite3
import json
import time
import sys
import os
import os.path
import shutil
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
# Enable logging
#basedatos='DBgestor.db'
basedatos='administrativo.db'
#Globales#
pagina=int(0)
vectorglobal=[]
pdf_CP=[]
pdf_factura=[]
pdf_jarboss=[]
pdf_servicio=[]
vectorcambios=[0,0,0,0,0,0,0,0,0,0,0]
notas=""
#
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(774, 591)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setGeometry(QtCore.QRect(650, 541, 111, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pedido = QtWidgets.QLabel(Dialog)
        self.pedido.setGeometry(QtCore.QRect(110, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pedido.setFont(font)
        self.pedido.setObjectName("pedido")
        self.prefijo = QtWidgets.QLabel(Dialog)
        self.prefijo.setGeometry(QtCore.QRect(320, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.prefijo.setFont(font)
        self.prefijo.setObjectName("prefijo")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(370, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.determinante = QtWidgets.QLabel(Dialog)
        self.determinante.setGeometry(QtCore.QRect(440, 10, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.determinante.setFont(font)
        self.determinante.setObjectName("determinante")
        self.cotizacion = QtWidgets.QLabel(Dialog)
        self.cotizacion.setGeometry(QtCore.QRect(110, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.cotizacion.setFont(font)
        self.cotizacion.setObjectName("cotizacion")
        self.titulo = QtWidgets.QLabel(Dialog)
        self.titulo.setGeometry(QtCore.QRect(330, 50, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.cotizacionCB = QtWidgets.QComboBox(Dialog)
        self.cotizacionCB.setGeometry(QtCore.QRect(100, 140, 141, 22))
        self.cotizacionCB.setObjectName("cotizacionCB")
        self.boton_modificarcotizacion = QtWidgets.QPushButton(Dialog)
        self.boton_modificarcotizacion.setGeometry(QtCore.QRect(10, 130, 75, 41))
        self.boton_modificarcotizacion.setObjectName("boton_modificarcotizacion")
        self.label_titulomodificado = QtWidgets.QLabel(Dialog)
        self.label_titulomodificado.setGeometry(QtCore.QRect(320, 130, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_titulomodificado.setFont(font)
        self.label_titulomodificado.setObjectName("label_titulomodificado")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(250, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(510, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tipoCB = QtWidgets.QComboBox(Dialog)
        self.tipoCB.setGeometry(QtCore.QRect(560, 20, 81, 22))
        self.tipoCB.setObjectName("tipoCB")
        self.tipoCB.addItem("")
        self.tipoCB.addItem("")
        self.tipoCB.addItem("")
        self.boton_modificartipo = QtWidgets.QPushButton(Dialog)
        self.boton_modificartipo.setGeometry(QtCore.QRect(660, 10, 75, 41))
        self.boton_modificartipo.setObjectName("boton_modificartipo")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(0, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(0, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(310, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(0, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.iniciopedido = QtWidgets.QLabel(Dialog)
        self.iniciopedido.setGeometry(QtCore.QRect(130, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.iniciopedido.setFont(font)
        self.iniciopedido.setObjectName("iniciopedido")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(250, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.inicioembarque = QtWidgets.QLabel(Dialog)
        self.inicioembarque.setGeometry(QtCore.QRect(410, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.inicioembarque.setFont(font)
        self.inicioembarque.setObjectName("inicioembarque")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(520, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.finembarque = QtWidgets.QLabel(Dialog)
        self.finembarque.setGeometry(QtCore.QRect(650, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.finembarque.setFont(font)
        self.finembarque.setObjectName("finembarque")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 110, 771, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.estatusCB = QtWidgets.QComboBox(Dialog)
        self.estatusCB.setGeometry(QtCore.QRect(150, 190, 141, 22))
        self.estatusCB.setObjectName("estatusCB")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.boton_modificarestatus = QtWidgets.QPushButton(Dialog)
        self.boton_modificarestatus.setGeometry(QtCore.QRect(70, 190, 75, 21))
        self.boton_modificarestatus.setObjectName("boton_modificarestatus")
        self.boton_modificarfactura = QtWidgets.QPushButton(Dialog)
        self.boton_modificarfactura.setGeometry(QtCore.QRect(70, 230, 75, 21))
        self.boton_modificarfactura.setObjectName("boton_modificarfactura")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 230, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(310, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.boton_modificarCP = QtWidgets.QPushButton(Dialog)
        self.boton_modificarCP.setGeometry(QtCore.QRect(420, 190, 75, 21))
        self.boton_modificarCP.setObjectName("boton_modificarCP")
        self.boton_modificarPDFfactura = QtWidgets.QPushButton(Dialog)
        self.boton_modificarPDFfactura.setGeometry(QtCore.QRect(420, 230, 75, 21))
        self.boton_modificarPDFfactura.setObjectName("boton_modificarPDFfactura")
        self.archivoCP = QtWidgets.QLabel(Dialog)
        self.archivoCP.setGeometry(QtCore.QRect(510, 190, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.archivoCP.setFont(font)
        self.archivoCP.setObjectName("archivoCP")
        self.archivofactura = QtWidgets.QLabel(Dialog)
        self.archivofactura.setGeometry(QtCore.QRect(510, 230, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.archivofactura.setFont(font)
        self.archivofactura.setObjectName("archivofactura")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(310, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.boton_modificarPDFjarboss = QtWidgets.QPushButton(Dialog)
        self.boton_modificarPDFjarboss.setGeometry(QtCore.QRect(420, 270, 75, 21))
        self.boton_modificarPDFjarboss.setObjectName("boton_modificarPDFjarboss")
        self.archivojarboss = QtWidgets.QLabel(Dialog)
        self.archivojarboss.setGeometry(QtCore.QRect(510, 270, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.archivojarboss.setFont(font)
        self.archivojarboss.setObjectName("archivojarboss")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(310, 310, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.boton_modificarPDFservicio = QtWidgets.QPushButton(Dialog)
        self.boton_modificarPDFservicio.setGeometry(QtCore.QRect(420, 320, 75, 21))
        self.boton_modificarPDFservicio.setObjectName("boton_modificarPDFservicio")
        self.archivoservicio = QtWidgets.QLabel(Dialog)
        self.archivoservicio.setGeometry(QtCore.QRect(510, 320, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.archivoservicio.setFont(font)
        self.archivoservicio.setObjectName("archivoservicio")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(180, 280, 81, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(0, 310, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(0, 260, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.fechafirmado = QtWidgets.QLabel(Dialog)
        self.fechafirmado.setGeometry(QtCore.QRect(190, 260, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.fechafirmado.setFont(font)
        self.fechafirmado.setObjectName("fechafirmado")
        self.boton_modificarfirmado = QtWidgets.QPushButton(Dialog)
        self.boton_modificarfirmado.setGeometry(QtCore.QRect(70, 270, 75, 21))
        self.boton_modificarfirmado.setObjectName("boton_modificarfirmado")
        self.boton_modificarpagado = QtWidgets.QPushButton(Dialog)
        self.boton_modificarpagado.setGeometry(QtCore.QRect(70, 320, 75, 21))
        self.boton_modificarpagado.setObjectName("boton_modificarpagado")
        self.fechapagado = QtWidgets.QLabel(Dialog)
        self.fechapagado.setGeometry(QtCore.QRect(190, 310, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.fechapagado.setFont(font)
        self.fechapagado.setObjectName("fechapagado")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(180, 330, 81, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 350, 771, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.historial = QtWidgets.QPlainTextEdit(Dialog)
        self.historial.setGeometry(QtCore.QRect(0, 390, 771, 71))
        self.historial.setPlainText("")
        self.historial.setObjectName("historial")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(250, 350, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.notas = QtWidgets.QPlainTextEdit(Dialog)
        self.notas.setGeometry(QtCore.QRect(0, 490, 771, 31))
        self.notas.setPlainText("")
        self.notas.setObjectName("notas")
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setGeometry(QtCore.QRect(300, 460, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 520, 771, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setGeometry(QtCore.QRect(0, 550, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.porcentajeavance = QtWidgets.QLabel(Dialog)
        self.porcentajeavance.setGeometry(QtCore.QRect(140, 540, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.porcentajeavance.setFont(font)
        self.porcentajeavance.setObjectName("porcentajeavance")
        self.boton_validacion = QtWidgets.QPushButton(Dialog)
        self.boton_validacion.setGeometry(QtCore.QRect(560, 540, 61, 41))
        self.boton_validacion.setObjectName("boton_validacion")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(640, 530, 3, 61))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.boton_agregararchivoextra = QtWidgets.QPushButton(Dialog)
        self.boton_agregararchivoextra.setGeometry(QtCore.QRect(380, 540, 151, 41))
        self.boton_agregararchivoextra.setObjectName("boton_agregararchivoextra")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(540, 530, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(250, 530, 3, 61))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.boton_agreagrnotas = QtWidgets.QPushButton(Dialog)
        self.boton_agreagrnotas.setGeometry(QtCore.QRect(260, 540, 101, 41))
        self.boton_agreagrnotas.setObjectName("boton_agreagrnotas")

        self.retranslateUi(Dialog)
        self.tipoCB.setCurrentIndex(2)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PEDIDO"))
        self.label_2.setText(_translate("Dialog", "Prefijo"))
        self.pedido.setText(_translate("Dialog", "0123456789"))
        self.prefijo.setText(_translate("Dialog", "123"))
        self.label_5.setText(_translate("Dialog", "COTIZACION"))
        self.label_6.setText(_translate("Dialog", "TITULO"))
        self.label_7.setText(_translate("Dialog", "TIENDA"))
        self.determinante.setText(_translate("Dialog", "12345"))
        self.cotizacion.setText(_translate("Dialog", "999-121219-CV-12345"))
        self.titulo.setText(_translate("Dialog", "TITULO DE LA COTIZACIÓN"))
        self.boton_modificarcotizacion.setText(_translate("Dialog", "Modificar\n"
"Cotizacion"))
        self.label_titulomodificado.setText(_translate("Dialog", "TITULO DE LA COTIZACIÓN"))
        self.label_12.setText(_translate("Dialog", "Titulo"))
        self.label_13.setText(_translate("Dialog", "TIPO"))
        self.tipoCB.setItemText(0, _translate("Dialog", "Correctivo"))
        self.tipoCB.setItemText(1, _translate("Dialog", "Iguala"))
        self.tipoCB.setItemText(2, _translate("Dialog", "Sin Asignar"))
        self.boton_modificartipo.setText(_translate("Dialog", "Modificar\n"
"TIPO"))
        self.label_14.setText(_translate("Dialog", "Estatus"))
        self.label_15.setText(_translate("Dialog", "Factura"))
        self.label_16.setText(_translate("Dialog", "PDF Factura"))
        self.label_17.setText(_translate("Dialog", "Inicio pedido"))
        self.iniciopedido.setText(_translate("Dialog", "12-12-2019"))
        self.label_18.setText(_translate("Dialog", "Inicio-Embarque"))
        self.inicioembarque.setText(_translate("Dialog", "12-12-2019"))
        self.label_21.setText(_translate("Dialog", "Fin-Embarque"))
        self.finembarque.setText(_translate("Dialog", "12-12-2019"))
        self.estatusCB.setItemText(0, _translate("Dialog", "No Ejecutado"))
        self.estatusCB.setItemText(1, _translate("Dialog", "Ejecutado"))
        self.estatusCB.setItemText(2, _translate("Dialog", "Ejecutado y Firmado"))
        self.estatusCB.setItemText(3, _translate("Dialog", "Proceso de Pago"))
        self.estatusCB.setItemText(4, _translate("Dialog", "Pagado"))
        self.estatusCB.setItemText(5, _translate("Dialog", "Cancelado"))
        self.boton_modificarestatus.setText(_translate("Dialog", "Modificar"))
        self.boton_modificarfactura.setText(_translate("Dialog", "Modificar"))
        self.label_23.setText(_translate("Dialog", "Comp. Pago"))
        self.boton_modificarCP.setText(_translate("Dialog", "Modificar"))
        self.boton_modificarPDFfactura.setText(_translate("Dialog", "Modificar"))
        self.archivoCP.setText(_translate("Dialog", "Nombre Archivo Compl. Pago"))
        self.archivofactura.setText(_translate("Dialog", "Nombre Archivo FACTURA"))
        self.label_26.setText(_translate("Dialog", "PDF Jarboss"))
        self.boton_modificarPDFjarboss.setText(_translate("Dialog", "Modificar"))
        self.archivojarboss.setText(_translate("Dialog", "Nombre Archivo Jarboss"))
        self.label_28.setText(_translate("Dialog", "PDF Servicio"))
        self.boton_modificarPDFservicio.setText(_translate("Dialog", "Modificar"))
        self.archivoservicio.setText(_translate("Dialog", "Nombre Archivo SERVICIO"))
        self.label_30.setText(_translate("Dialog", "Pagado"))
        self.label_31.setText(_translate("Dialog", "Firmado"))
        self.fechafirmado.setText(_translate("Dialog", "12-12-2019"))
        self.boton_modificarfirmado.setText(_translate("Dialog", "Modificar"))
        self.boton_modificarpagado.setText(_translate("Dialog", "Modificar"))
        self.fechapagado.setText(_translate("Dialog", "12-12-2019"))
        self.label_34.setText(_translate("Dialog", "Historial de cambios y comentarios"))
        self.label_35.setText(_translate("Dialog", "Agregar notas extras "))
        self.label_36.setText(_translate("Dialog", "Avance pedido->"))
        self.porcentajeavance.setText(_translate("Dialog", "100%"))
        self.boton_validacion.setText(_translate("Dialog", "Validar \n"
"Cambios"))
        self.boton_agregararchivoextra.setText(_translate("Dialog", "TODOS LOS ARCHIVOS"))
        self.boton_agreagrnotas.setText(_translate("Dialog", "AGREGAR \n"
"NOTAS"))
        self.boton_validacion.clicked.connect(self.terminar)
        self.boton_modificarcotizacion.clicked.connect(self.consultar_cotizaciones)
        self.boton_modificarCP.clicked.connect(self.ruta_CP)
        self.boton_modificarPDFfactura.clicked.connect(self.ruta_factura)
        self.boton_modificarPDFjarboss.clicked.connect(self.ruta_jarboss)
        self.boton_modificarPDFservicio.clicked.connect(self.ruta_servicio)
        self.boton_modificartipo.clicked.connect(self.modificartipo)
        self.boton_modificarestatus.clicked.connect(self.modificarestatus)
        self.boton_modificarfactura.clicked.connect(self.modifcarlineEdit)
        self.boton_modificarfirmado.clicked.connect(self.modificarfirmado)
        self.boton_modificarpagado.clicked.connect(self.modificarpagado)
        self.boton_agreagrnotas.clicked.connect(self.agregarnotas)
        self.boton_agregararchivoextra.clicked.connect(self.abrirarchivos)

    def abrirarchivos(self):
            print("pasarinfo")
            pedido=str(self.pedido.text())
            prefijo=str(self.prefijo.text())
            a=str(pedido+'-'+prefijo)
            print(a)
            item = a
            direccionBD = "items.db"
            try:
                sqliteConnection = sqlite3.connect(direccionBD)
                cursor = sqliteConnection.cursor()
                UPDATE = """Update pasar set item = ?
                            where ID = 1
                            """
                data = (item)
                cursor.execute(UPDATE, (data,))
                sqliteConnection.commit()
                print("GUARDADO")
                cursor.close
            except sqlite3.Error as error:
                print("Error, abrirarchivos -----> ", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("Cerrando conexión de Base de Datos")
                    script = "abrirarchivo.py"
                    subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT)
#                    sys.exit()

            return ()


    def tomarinfo(self):
        print("TOMANDO INFORMACIÓN")
        print("*************************")
        temporal = ""
        tempcantidad = ""
        SUBCAT = "items.db"
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT = """SELECT item, cantidad
                    from pasar
                    where ID = 1
                    """
            print("INTENTO")
            cursor.execute(SELECT)
            record = cursor.fetchone()

            temporal = record[0]
            tempcantidad = record[1]

            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                self.llenarinfopedido(str(temporal),tempcantidad)
                print("INSTANCE")

        return ()

    def obtenerruta(self):
        try:
            print("obteniendo ruta")
            ruta = QtWidgets.QFileDialog.getOpenFileName(Dialog, 'Open File', '', 'Files (*.pdf)')
            ruta2, _ = ruta
            # nombre del archivo
            nombre1 = Path(ruta2).name

            vectorarchivo = [nombre1, ruta[0]]
        except Exception as e:
            print(f'{type(e)}: {e}')
            QTimer.singleShot(3000, lambda: sys.exit(1))
            return ()
        finally:
            print("listo si se pudo")
            return (vectorarchivo)

    def terminar(self):
        revision=self.verificacion()
        if revision==0:
            return

        if revision==1:
            vacio = str(self.notas.toPlainText())
            z=globals()['vectorcambios'][10]
            if vacio == "" and z==1:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR FALTA DE INFORMCIÓN")
                msg.setIcon(QMessageBox.Information)
                msg.setText("ERROR POR FALTA INFORMACION - DEBES ESCRIBIR EN LAS NOTAS LA RAZÓN DE LOS CAMBIOS")
                x = msg.exec_()
                return ()
            print("gurdando cambios")
            self.guardarcambios()  ################################
            mensajelisto()
            script = "GESTORPEDIDOS_3.py"
            subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            sys.exit()
                #self.buttonBox.setEnabled(1)
        return ()

    def copiararchivo(self,archivoacopiar,nombrearchivo):
        numpedido = str(self.pedido.text())
        carpetainterna = str(self.pedido.text()) + '-' + str(self.prefijo.text())
        #nombrearchivoSTR=nombrearchivo
        #extension=nombrearchivoSTR.partition(".")[2]
        print(carpetainterna)
        carpeta = "DOCUMENTACION"
        b = os.getcwd()  # obtener la ruta exacta del archivo
        a = os.listdir(b +'\\'+ carpeta +'\\'+carpetainterna)  # obtener lo que hay dentro de la carpeta
        nombre = str(numpedido) + '-' +str(len(a)) + '-'+ str(nombrearchivo) # nombre del archivo #str(filename)+'.'+extension#
        rutanombre = carpeta + '\\' + str(carpetainterna) + '\\' + nombre
        shutil.copyfile(archivoacopiar, rutanombre)
        print("listo copiado el archivo")
        return(nombre)

    def guardarcambios(self):
        tiempoactual = time.mktime(time.localtime())
        tiempo = time.asctime(time.localtime(tiempoactual))  # mostrar hora con fecha
        v=globals()['vectorcambios']
        globals()['notas']=("Cambios <-->"+str(tiempo)+" <--> " )
        vacio=str(self.notas.toPlainText())
        if v[10]==1 and vacio=="":
                msg = QMessageBox()
                msg.setWindowTitle("ERROR FALTA DE INFORMCIÓN")
                msg.setIcon(QMessageBox.Information)
                msg.setText("ERROR POR FALTA INFORMACION - DEBES ESCRIBIR EN LAS NOTAS LA RAZÓN DE LOS CAMBIOS")
                x = msg.exec_()
                return()
        if v[0]==1:
            print("tipo")
            self.updatetipo()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' TIPO >>>' + str(self.tipoCB.currentText())

        if v[1]==1:
            print("cotizacion")
            self.updatecotizacion()
            cambio = globals()['notas']
            a=str(self.cotizacionCB.currentText())
            if a=="":
                return()
            else:
                globals()['notas'] = cambio + ' COTIZACION >>>' + str(self.cotizacionCB.currentText())
        if v[2]==1:
            print("estatus")
            self.updateestatus()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' ESTATUS >>>' + str(self.estatusCB.currentText())
        if v[3]==1:
            print("factura")
            self.updatefactura()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' FACTURA >>>' + str(self.lineEdit.text())
        if v[4]==1:
            print("firmado")
            a=self.updatefirmado()
            cambio = globals()['notas']
            #print(a)
            globals()['notas'] = cambio + ' FECHA FIRMADO>>>' + (a)
        if v[5]==1:
            print("pagado")
            a = self.updatepagado()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' FECHA PAGO>>>' + (a)
        if v[6]==1:
            print("CP")
            archivo=globals()['pdf_CP']
            globals()['pdf_CP'][0] = str(self.copiararchivo(archivo[1], archivo[0]))
            self.updateCP()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' Nuevo Archivo CP >>>' + str(self.archivoCP.text())

        if v[7]==1:
            print("PDFfactura")
            archivo = globals()['pdf_factura']
            globals()['pdf_factura'][0] = str(self.copiararchivo(archivo[1], archivo[0]))
            self.updatePDFfactura()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' Nuevo Archivo factura >>>' + str(self.archivofactura.text())
        if v[8]==1:
            print("Jarboss")
            archivo = globals()['pdf_jarboss']
            globals()['pdf_jarboss'][0] = str(self.copiararchivo(archivo[1], archivo[0]))
            self.updatejarboss()
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' Nuevo Archivo jarboss >>>' + str(self.archivojarboss.text())
        if v[9]==1:
            print("servicio")
            self.updateservicio()
            archivo = globals()['pdf_servicio']
            globals()['pdf_servicio'][0] = str(self.copiararchivo(archivo[1], archivo[0]))
            cambio = globals()['notas']
            globals()['notas'] = cambio + ' Nuevo Archivo jarboss >>>' + str(self.archivoservicio.text())
        if v[10] == 1:
            cambio = globals()['notas']
            historial=str(self.historial.toPlainText())
            extras = str(self.notas.toPlainText())
            sumandotexto=historial +"\n" + cambio + ' _(COMENTARIOS CAMBIOS)_ '+extras + "\n" +"***"
            self.updatenotas((sumandotexto))


        return()

    def verificacion(self):
        #4 es para pagado
        estatus=int(self.estatusCB.currentIndex())
        a=globals()['vectorglobal']

        if estatus==4:
            if a[4]==None or a[4]==1: #tipo
                if a[19] == None:  # jarboss
                    errorfaltainfo()
                    return (0)

            if a[18] == None:  #CP
                errorfaltainfo()
                return(0)
            if a[17] == None:  # factura PDF
                errorfaltainfo()
                return (0)

            if a[16] == None:  # tservicio
                errorfaltainfo()
                return (0)
            if a[12] == None:  # firmado
                errorfaltainfo()
                return (0)
            if a[13] == None:  # pagado
                errorfaltainfo()
                return (0)
            if a[9] == None:  # factura nombre
                errorfaltainfo()
                return (0)


        return(1)

    def llenarinfopedido(self,pedido,prefijo):
        vector = consultarinfo(pedido, int(prefijo))
        #vector = consultarinfo(pedido, prefijo)
        globals()['vectorglobal']=vector
        self.pedido.setText(str(vector[3]))
        self.prefijo.setText(str(vector[20]))
        self.determinante.setText(str(vector[5]))
        self.cotizacion.setText(str(vector[1]))
        self.titulo.setText(str(vector[2]))
        self.tipoCB.setCurrentIndex(int(vector[4]))#
        self.iniciopedido.setText(str(convertirFECHA(int(vector[6]))))
        self.inicioembarque.setText(str(convertirFECHA(int(vector[7]))))
        self.finembarque.setText(str(convertirFECHA(int(vector[8]))))
        self.archivoCP.setText(str(vector[18]))#
        self.archivofactura.setText(str(vector[17]))#
        self.archivojarboss.setText(str(vector[19]))#
        self.archivoservicio.setText(str(vector[16]))#
        self.estatusCB.setCurrentIndex((int(vector[10])))
        self.fechafirmado.setText(str(verificarfirmadoypagado((vector[12]))))#
        self.fechapagado.setText(str(verificarfirmadoypagado((vector[13]))))#
        self.lineEdit.setText(str(vector[9]))#
        self.historial.setPlainText(str(vector[11]))
        self.bloquear()
        iguala=int(self.tipoCB.currentIndex())
        if iguala==1:
            self.boton_modificarPDFjarboss.setEnabled(1)
        else:
            self.boton_modificarPDFjarboss.setEnabled(0)

        self.avance()

        return ()

    def convertirfecha(self):
        day = self.dateEdit.dateTime().toString("dd")
        month = self.dateEdit.dateTime().toString("MM")
        year = self.dateEdit.dateTime().toString("yyyy")
        s = '-'
        vectordate = year + s + month + s + day
        conversion = fechaatimestmp(vectordate) + 86400
        return (conversion)

    def convertirfecha2(self):
        day = self.dateEdit_2.dateTime().toString("dd")
        month = self.dateEdit_2.dateTime().toString("MM")
        year = self.dateEdit_2.dateTime().toString("yyyy")
        s = '-'
        vectordate = year + s + month + s + day
        conversion = fechaatimestmp(vectordate) + 86400
        return (conversion)

    def modificartipo(self):
        self.tipoCB.setEnabled(1)
        globals()['vectorcambios'][0] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def consultar_cotizaciones(self):
        print("FILTRANDO")
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            # print("Successfully Connected to SQLite")
            SELECT = """SELECT 
                    numcotizacion

                    FROM
                    cotizaciones

                    WHERE
                    estatus = 0


                    """
            cursor.execute(SELECT)
            record = cursor.fetchall()
            for row in record:
                self.cotizacionCB.addItem(row[0])
            print(record)
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                self.cotizacionCB.setEnabled(1)
                globals()['vectorcambios'][1] = 1
                globals()['vectorcambios'][10] = 1
                self.notas.setEnabled(1)
                # print("Cerrando conexión de Base de Datos")

        return ()
    def modificarestatus(self):
        self.estatusCB.setEnabled(1)
        globals()['vectorcambios'][2] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def modifcarlineEdit(self):
        self.lineEdit.setEnabled(1)
        globals()['vectorcambios'][3] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def modificarfirmado(self):
        self.dateEdit.setEnabled(1)
        globals()['vectorcambios'][4] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def modificarpagado(self):
        self.dateEdit_2.setEnabled(1)
        globals()['vectorcambios'][5] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def ruta_CP(self):
        globals()["pdf_CP"] = self.obtenerruta()
        self.archivoCP.setText(str(globals()["pdf_CP"][0]))
        globals()['vectorcambios'][6] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def ruta_factura(self):
        globals()["pdf_factura"] = self.obtenerruta()
        self.archivofactura.setText(str(globals()["pdf_factura"][0]))
        globals()['vectorcambios'][7] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def ruta_jarboss(self):
        globals()["pdf_jarboss"] = self.obtenerruta()
        self.archivojarboss.setText(str(globals()["pdf_jarboss"][0]))
        globals()['vectorcambios'][8] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def ruta_servicio(self):
        globals()["pdf_servicio"] = self.obtenerruta()
        self.archivoservicio.setText(str(globals()["pdf_servicio"][0]))
        globals()['vectorcambios'][9] = 1
        globals()['vectorcambios'][10] = 1
        self.notas.setEnabled(1)
        return ()
    def agregarnotas(self):
        self.notas.setEnabled(1)
        globals()['vectorcambios'][10] = 1
        return ()

    def bloquear(self):
        self.tipoCB.setEnabled(0)
        self.cotizacionCB.setEnabled(0)
        self.estatusCB.setEnabled(0)
        self.lineEdit.setEnabled(0)
        self.dateEdit.setEnabled(0)
        self.dateEdit_2.setEnabled(0)
        self.historial.setReadOnly(1)
        self.notas.setEnabled(0)
        #self.boton_agregararchivoextra.setEnabled((0))

        return ()

    def updatetipo(self):
        a = str(self.tipoCB.currentIndex())
        b = str(self.pedido.text())
        c = str(self.prefijo.text())  # función de agregar historial y el texto

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                        set 
                        tipo=?

                        where 
                        numpedido = ?
                        AND
                        prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("Cerrando conexión de Base de Datos")
        return ()
    def updatecotizacion(self):
        a = str(self.cotizacionCB.currentText())
        b = str(self.pedido.text())
        c = str(self.prefijo.text())  # función de agregar historial y el texto

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                        set 
                        numcotizacion=?

                        where 
                        numpedido = ?
                        AND
                        prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                self.updatecotizacion_DB()
        return ()
    def updatecotizacion_DB(self):
        a = str(self.cotizacionCB.currentText())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("actualizacion en cotizaciones STATUS =1")
            update = """Update cotizaciones 
                        set 
                        estatus=1

                        where 
                        numcotizacion = ? """

            data = (a)
            cursor.execute(update, (data,))
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                self.updatecotizacion_DB2()
                print("Cerrando conexión de Base de Datos")
        return ()
    def updatecotizacion_DB2(self):
        a = str(self.cotizacion.text())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("actualizacion en cotizaciones STATUS =1")
            update = """Update cotizaciones 
                           set 
                           estatus=0

                           where 
                           numcotizacion = ? """

            data = (a)
            cursor.execute(update, (data,))
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("Cerrando conexión de Base de Datos")
        return ()
    def updateestatus(self):
        a = str(self.estatusCB.currentIndex())
        b = str(self.pedido.text())
        c = str(self.prefijo.text())  # función de agregar historial y el texto

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                               set 
                               estatus=?

                               where 
                               numpedido = ?
                               AND
                               prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("estatus", a)

        return
    def updatefactura(self):
        a = str(self.lineEdit.text())
        b = str(self.pedido.text())
        c = str(self.prefijo.text())  # función de agregar historial y el texto

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                               set 
                               numfactura=?

                               where 
                               numpedido = ?
                               AND
                               prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()

        return
    def updatefirmado(self):
        a = str(self.convertirfecha())
        b = str(self.pedido.text())
        c = str(self.prefijo.text())  # función de agregar historial y el texto
        tiempo = time.asctime(time.localtime(int(a)))
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                  set 
                                  timestampfirmado=?

                                  where 
                                  numpedido = ?
                                  AND
                                  prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                  # mostrar hora con fecha
                return(tiempo)
        return
    def updatepagado(self):
        a = str(self.convertirfecha2())
        b = str(self.pedido.text())
        c = str(self.prefijo.text())  # función de agregar historial y el texto

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                  set 
                                  timestamppagado=?

                                  where 
                                  numpedido = ?
                                  AND
                                  prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                tiempo = time.asctime(time.localtime(int(a)))  # mostrar hora con fecha
                return (tiempo)
        return
    def updateCP(self):

        a = str(globals()['pdf_CP'][0])
        b = str(self.pedido.text())
        c = str(self.prefijo.text())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                  set 
                                  archivoCP=?

                                  where 
                                  numpedido = ?
                                  AND
                                  prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
        return
    def updatePDFfactura(self):

        a = str(globals()['pdf_factura'][0])
        b = str(self.pedido.text())
        c = str(self.prefijo.text())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                  set 
                                  archivofactura=?

                                  where 
                                  numpedido = ?
                                  AND
                                  prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
        return
    def updatejarboss(self):

        a = str(globals()['pdf_jarboss'][0])
        b = str(self.pedido.text())
        c = str(self.prefijo.text())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                     set 
                                     archivojarboss=?

                                     where 
                                     numpedido = ?
                                     AND
                                     prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
        return
    def updateservicio(self):

        a = str(globals()['pdf_servicio'][0])
        b = str(self.pedido.text())
        c = str(self.prefijo.text())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                     set 
                                     archivoservicio=?

                                     where 
                                     numpedido = ?
                                     AND
                                     prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
        return
    def updatenotas(self,notas):

        a = notas
        b = str(self.pedido.text())
        c = str(self.prefijo.text())

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            update = """Update pedidos 
                                     set 
                                     comentarios=?

                                     where 
                                     numpedido = ?
                                     AND
                                     prefijo= ?"""
            data = (a, b, c)
            cursor.execute(update, data)
            sqliteConnection.commit()
            print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
            cursor.close

        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
        return

    def avance(self):
            #4 es para pagado
            estatus=int(self.estatusCB.currentIndex())
            a=globals()['vectorglobal']

            tipo=int(self.tipoCB.currentIndex())
            if tipo==1:
                self.actualizartextoavance(a,8)
            else:
                self.actualizartextoavance(a,7)
            return()

    def actualizartextoavance(self,vector,cant):
        completo=cant
        cantidad=cant
        estatus = int(self.estatusCB.currentIndex())
        a=vector
        if estatus == 4:
            print("pagado")
        else:
            cantidad = cantidad - 1

        if a[4] == None or a[4] == 1:  # tipo
            if a[19] == None:  # jarboss
                cantidad = cantidad - 1

        if a[18] == None:  # CP
            cantidad = cantidad - 1

        if a[17] == None:  # factura PDF
            cantidad = cantidad - 1

        if a[16] == None:  # tservicio
            cantidad = cantidad - 1

        if a[12] == None:  # firmado
            cantidad = cantidad - 1

        if a[13] == None:  # pagado
            cantidad = cantidad - 1

        if a[9] == None:  # factura nombre
            cantidad = cantidad - 1

        print("COMPLETO-> ",completo)
        print("CANTIDAD -> ", cantidad)
        total=((cantidad / completo) * 100)
        porcentaje = str(round(total,2))
        avancetexto = porcentaje + "%"
        self.porcentajeavance.setText(avancetexto)
        return()


def consultarinfo(pedido, prefijo):
    print("++++++++BUSCANDO++++++++")
    buscar = [pedido, prefijo]
    try:
        sqliteConnection = sqlite3.connect(basedatos)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        SELECT = """SELECT * from pedidos  where numpedido = ? AND prefijo = ?  """
        cursor.execute(SELECT, (buscar))
        record = cursor.fetchone()
        # record = cursor.fetchall()
        # print(record)

        print("Record Updated successfully")
        cursor.close

    except sqlite3.Error as error:
        print("Error, ALV -----> ", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Cerrando conexión de Base de Datos")
    return (record)

def verificarfirmadoypagado(valor):
    if valor == 0 or valor == None:
        return ("Sin Asignar")
    else:
        return (convertirFECHA(valor))

    return ()

def convertirFECHA(tiempo):
    fecha = time.strftime("%D ", time.localtime(int(tiempo)))
    return (fecha)

def fechaatimestmp(fecha):
    # formato de concatenacion para fecha a Timestamp
    vectortime = fecha + "T00:00:00.000Z"
    utc_dt = datetime.strptime(vectortime, '%Y-%m-%dT%H:%M:%S.%fZ')
    # Convert UTC datetime to seconds since the Epoch
    conversion = int((utc_dt - datetime(1970, 1, 1)).total_seconds())
    return (conversion)


def errorfaltainfo():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR FALTA DE INFORMCIÓN")
    msg.setIcon(QMessageBox.Information)
    msg.setText("ERROR POR FALTA INFORMACION - Hace falta documentos y/o actualizar información para concretar el pedido como *PAGADO*")
    x = msg.exec_()
    return()
def mensajelisto():
    msg = QMessageBox()
    msg.setWindowTitle("LISTO")
    msg.setIcon(QMessageBox.Information)
    msg.setText("CAMBIOS GUARDADOS EXITOSAMENTE.")
    x = msg.exec_()
    return()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.tomarinfo()
    sys.exit(app.exec_())


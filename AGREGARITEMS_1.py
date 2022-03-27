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


categoria=""
vectorsubcat=[]
nuevonumero=""
comando=""

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 509)
        Dialog.setMinimumSize(QtCore.QSize(610, 487))
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.dialogButtonBox.setEnabled(False)
        self.dialogButtonBox.setGeometry(QtCore.QRect(410, 460, 161, 41))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.CATEGORIA = QtWidgets.QComboBox(Dialog)
        self.CATEGORIA.setGeometry(QtCore.QRect(120, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.CATEGORIA.setFont(font)
        self.CATEGORIA.setObjectName("CATEGORIA")
        self.CATEGORIA.addItem("")
        self.CATEGORIA.addItem("")
        self.CATEGORIA.addItem("")
        self.CATEGORIA.addItem("")
        self.CATEGORIA.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 90, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 51, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(200, 290, 81, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 81, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(370, 100, 20, 431))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.NOTAS = QtWidgets.QPlainTextEdit(Dialog)
        self.NOTAS.setGeometry(QtCore.QRect(10, 410, 361, 91))
        self.NOTAS.setReadOnly(False)
        self.NOTAS.setPlainText("")
        self.NOTAS.setObjectName("NOTAS")
        self.imagen = QtWidgets.QLabel(Dialog)
        self.imagen.setGeometry(QtCore.QRect(390, 110, 211, 181))
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/Sample Pictures/Jellyfish.jpg"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(420, 430, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(380, 330, 241, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ITEM = QtWidgets.QLabel(Dialog)
        self.ITEM.setGeometry(QtCore.QRect(90, 106, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.ITEM.setFont(font)
        self.ITEM.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM.setObjectName("ITEM")
        self.ID = QtWidgets.QLabel(Dialog)
        self.ID.setGeometry(QtCore.QRect(90, 130, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID.setFont(font)
        self.ID.setAlignment(QtCore.Qt.AlignCenter)
        self.ID.setObjectName("ID")
        self.DESCRIPCION = QtWidgets.QLineEdit(Dialog)
        self.DESCRIPCION.setGeometry(QtCore.QRect(100, 160, 261, 20))
        self.DESCRIPCION.setObjectName("DESCRIPCION")
        self.MARCA = QtWidgets.QLineEdit(Dialog)
        self.MARCA.setGeometry(QtCore.QRect(100, 190, 261, 20))
        self.MARCA.setObjectName("MARCA")
        self.COSTO = QtWidgets.QLineEdit(Dialog)
        self.COSTO.setGeometry(QtCore.QRect(100, 280, 71, 20))
        self.COSTO.setText("")
        self.COSTO.setAlignment(QtCore.Qt.AlignCenter)
        self.COSTO.setObjectName("COSTO")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(30, 350, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.PRECIOCLIENTE = QtWidgets.QLineEdit(Dialog)
        self.PRECIOCLIENTE.setGeometry(QtCore.QRect(160, 350, 111, 20))
        self.PRECIOCLIENTE.setObjectName("PRECIOCLIENTE")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(0, 310, 91, 16))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.TEDIAS = QtWidgets.QLineEdit(Dialog)
        self.TEDIAS.setGeometry(QtCore.QRect(100, 310, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TEDIAS.setFont(font)
        self.TEDIAS.setAlignment(QtCore.Qt.AlignCenter)
        self.TEDIAS.setObjectName("TEDIAS")
        self.SUBCAT = QtWidgets.QComboBox(Dialog)
        self.SUBCAT.setGeometry(QtCore.QRect(420, 60, 181, 31))
        self.SUBCAT.setObjectName("SUBCAT")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 40, 611, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.ITEM_2 = QtWidgets.QLabel(Dialog)
        self.ITEM_2.setGeometry(QtCore.QRect(80, 10, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.ITEM_2.setFont(font)
        self.ITEM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ITEM_2.setObjectName("ITEM_2")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 330, 381, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(10, 250, 81, 16))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.PROVEEDOR = QtWidgets.QLineEdit(Dialog)
        self.PROVEEDOR.setGeometry(QtCore.QRect(100, 250, 261, 20))
        self.PROVEEDOR.setObjectName("PROVEEDOR")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 300, 171, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(60, 380, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.PlainText)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.MEDIDA = QtWidgets.QComboBox(Dialog)
        self.MEDIDA.setGeometry(QtCore.QRect(290, 290, 71, 21))
        self.MEDIDA.setObjectName("MEDIDA")
        self.MEDIDA.addItem("")
        self.MEDIDA.addItem("")
        self.MEDIDA.addItem("")
        self.MEDIDA.addItem("")
        self.MEDIDA.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 47, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("src/additem.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(560, 0, 47, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("src/additem.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.MODELO = QtWidgets.QLineEdit(Dialog)
        self.MODELO.setGeometry(QtCore.QRect(100, 220, 261, 20))
        self.MODELO.setObjectName("MODELO")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 360, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(380, 410, 241, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.retranslateUi(Dialog)
        self.dialogButtonBox.accepted.connect(Dialog.accept)
        self.dialogButtonBox.accepted.connect(self.AGREGARITEMS_guardarinfo)
        self.dialogButtonBox.rejected.connect(Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.CATEGORIA, self.SUBCAT)
        Dialog.setTabOrder(self.SUBCAT, self.DESCRIPCION)
        Dialog.setTabOrder(self.DESCRIPCION, self.MARCA)
        Dialog.setTabOrder(self.MARCA, self.MODELO)
        Dialog.setTabOrder(self.MODELO, self.PROVEEDOR)
        Dialog.setTabOrder(self.PROVEEDOR, self.COSTO)
        Dialog.setTabOrder(self.COSTO, self.TEDIAS)
        Dialog.setTabOrder(self.TEDIAS, self.MEDIDA)
        Dialog.setTabOrder(self.MEDIDA, self.PRECIOCLIENTE)
        Dialog.setTabOrder(self.PRECIOCLIENTE, self.NOTAS)
        Dialog.setTabOrder(self.NOTAS, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CATEGORIA  --->"))
        self.CATEGORIA.setItemText(0, _translate("Dialog", "MECANICO"))
        self.CATEGORIA.setItemText(1, _translate("Dialog", "ELECTRICO"))
        self.CATEGORIA.setItemText(2, _translate("Dialog", "SENSORES"))
        self.CATEGORIA.setItemText(3, _translate("Dialog", "CONTROL"))
        self.CATEGORIA.setItemText(4, _translate("Dialog", "ESPECIALES"))
        self.label_3.setText(_translate("Dialog", "SUBCategoría ->"))
        self.label_5.setText(_translate("Dialog", "ITEM"))
        self.label_6.setText(_translate("Dialog", "ID FIDGET"))
        self.label_7.setText(_translate("Dialog", "DESCRIPCION"))
        self.label_8.setText(_translate("Dialog", "MARCA"))
        self.label_9.setText(_translate("Dialog", "UNIDAD MEDIDA"))
        self.label_10.setText(_translate("Dialog", "COSTO"))
        self.label_13.setText(_translate("Dialog", "GUARDAR PRODUCTO"))
        self.ITEM.setText(_translate("Dialog", "ITEM SELECCIONADO"))
        self.ID.setText(_translate("Dialog", "ID FIDGET"))
        self.label_14.setText(_translate("Dialog", "PRECIO CLIENTE"))
        self.label_15.setText(_translate("Dialog", "TE (dias hábiles)"))
        self.TEDIAS.setText(_translate("Dialog", "3"))
        self.ITEM_2.setText(_translate("Dialog", "AGREGAR PRODUCTO A BASE DE DATOS"))
        self.label_16.setText(_translate("Dialog", "PROVEEDOR"))
        self.pushButton.setText(_translate("Dialog", "Agregar Imagen"))
        self.label_17.setText(_translate("Dialog", "NOTAS EXTRAS SOBRE EL PRODUCTO"))
        self.MEDIDA.setItemText(0, _translate("Dialog", "Pieza"))
        self.MEDIDA.setItemText(1, _translate("Dialog", "Metro"))
        self.MEDIDA.setItemText(2, _translate("Dialog", "Servicio"))
        self.MEDIDA.setItemText(3, _translate("Dialog", "Kilo"))
        self.MEDIDA.setItemText(4, _translate("Dialog", "Litro"))
        self.MEDIDA.setItemText(5, _translate("Dialog", "Lote"))
        self.label_12.setText(_translate("Dialog", "MODELO"))
        self.pushButton_2.setText(_translate("Dialog", "VERIFICAR INFORMACION"))

        self.pushButton_2.clicked.connect(self.verificacion)
        self.CATEGORIA.currentTextChanged.connect(self.escogercategoria)
        # self.SUBCAT.currentTextChanged.connect(self.posicionCB_subcat)

    def escogercategoria(self):
        CAT = self.CATEGORIA.currentText()

        if CAT == "MECANICO":
            print("mecanico")
            seleccionarBD = """SELECT seq from sqlite_sequence where name ='mecanico' """
            lastrow = self.secuencia(seleccionarBD)
            print(lastrow)
            numerogenerado = "GME" + str(int(lastrow) + 1)
            globals()["nuevonumero"] = numerogenerado
            self.ID.setText(numerogenerado)
            subcat = "A"
            self.AGREGARITEMS_llenarCB_SUBCAT(subcat)
            COMANDOGUARDAR="""INSERT INTO 'mecanico' ('numfid', 'subcat','marca','modelo','medida', 'subtotal',
             'te', 'costo', 'proveedor','comentarios','descripcion')
                            VALUES (?,?,?,?,?,?,?,?,?,?,?);"""
            globals()["comando"]=COMANDOGUARDAR
            #vectorguardado = [numfid, subcat, marca, modelo, medida, preciocliente, tedias, costo, proveedor, comentarios, descripcion]
            return ()

        if CAT == "ELECTRICO":
            print("electrico")
            seleccionarBD = """SELECT seq from sqlite_sequence where name ='electrico' """
            lastrow = self.secuencia(seleccionarBD)
            numerogenerado = "GEL" + str(int(lastrow) + 1)
            globals()["nuevonumero"] = numerogenerado
            self.ID.setText(numerogenerado)
            subcat = "B"
            self.AGREGARITEMS_llenarCB_SUBCAT(subcat)
            COMANDOGUARDAR = """INSERT INTO 'electrico' ('numfid', 'subcat','marca','modelo','medida', 'subtotal',
                         'te', 'costo', 'proveedor','comentarios','descripcion')
                                        VALUES (?,?,?,?,?,?,?,?,?,?,?);"""
            globals()["comando"] = COMANDOGUARDAR
            return ()
        if CAT == "SENSORES":
            print("sensores")
            seleccionarBD = """SELECT seq from sqlite_sequence where name ='sensores' """
            lastrow = self.secuencia(seleccionarBD)
            numerogenerado = "GSE" + str(int(lastrow) + 1)
            globals()["nuevonumero"] = numerogenerado
            self.ID.setText(numerogenerado)
            subcat = "C"
            self.AGREGARITEMS_llenarCB_SUBCAT(subcat)
            COMANDOGUARDAR = """INSERT INTO 'sensores' ('numfid', 'subcat','marca','modelo','medida', 'subtotal',
                         'te', 'costo', 'proveedor','comentarios','descripcion')
                                        VALUES (?,?,?,?,?,?,?,?,?,?,?);"""
            globals()["comando"] = COMANDOGUARDAR
            return ()
        if CAT == "CONTROL":
            print("control")
            seleccionarBD = """SELECT seq from sqlite_sequence where name ='control' """
            lastrow = self.secuencia(seleccionarBD)
            numerogenerado = "GCO" + str(int(lastrow) + 1)
            globals()["nuevonumero"] = numerogenerado
            self.ID.setText(numerogenerado)
            subcat = "D"
            self.AGREGARITEMS_llenarCB_SUBCAT(subcat)
            COMANDOGUARDAR = """INSERT INTO 'control' ('numfid', 'subcat','marca','modelo','medida', 'subtotal',
                         'te', 'costo', 'proveedor','comentarios','descripcion')
                                        VALUES (?,?,?,?,?,?,?,?,?,?,?);"""
            globals()["comando"] = COMANDOGUARDAR
            return ()
        if CAT == "ESPECIALES":
            print("especiales")
            seleccionarBD = """SELECT seq from sqlite_sequence where name ='especiales' """
            lastrow = self.secuencia(seleccionarBD)
            numerogenerado = "GES" + str(int(lastrow) + 1)
            globals()["nuevonumero"] = numerogenerado
            self.ID.setText(numerogenerado)
            subcat = "E"
            self.AGREGARITEMS_llenarCB_SUBCAT(subcat)
            COMANDOGUARDAR = """INSERT INTO 'especiales' ('numfid', 'subcat','marca','modelo','medida', 'subtotal',
                            'te', 'costo', 'proveedor','comentarios','descripcion')
                            VALUES (?,?,?,?,?,?,?,?,?,?,?);"""
            globals()["comando"] = COMANDOGUARDAR
            return ()
        print("AGREGAR UNA FUNCION DE GUARDADO")
        return ()

    def posicionCB_subcat(self):
        idsubcat = self.SUBCAT.currentText()
        if idsubcat == "":
            print("no hay nada más")
            return ()
        a = self.filtrarsubcat(idsubcat)
        return (a)

    def filtrarsubcat(self, filtro):
        print("def filtraritems")
        basedatos = "items.db"
        subcategoria = filtro
        if subcategoria == 0:
            print("NO HAY QUE BUSCAR")
            return ()

        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            SELECT = """SELECT ID from subcategorias where subcat = ? """
            cursor.execute(SELECT, (subcategoria,))
            record = cursor.fetchone()
            # print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                # print("Cerrando conexión de Base de Datos")
        return (record)

    def AGREGARITEMS_llenarCB_SUBCAT(self, indice):
        print("llenarCB_SUBCAT")
        SUBCAT = "items.db"
        self.SUBCAT.clear()
        # vectorsubcat = globals()["vectorsubcategoria"]
        subcategoria = indice
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()

            SELECT = """SELECT subcat from subcategorias
                        where clase = ?
                        """
            cursor.execute(SELECT, subcategoria)

            record = cursor.fetchall()
            for row in record:
                a = str(row[0])
                self.SUBCAT.addItem(a)
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

    def secuencia(self, SEL):
        print("iniciando lastrow ITEMS")
        basedatos = "items.db"
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            SELECT = SEL  # """SELECT seq from sqlite_sequence where name ='AM' ""
            cursor.execute(SELECT)
            record = cursor.fetchone()
            registros = record[0]

            cursor.close
            print("ultimo registro ITEMS", registros)
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                return (registros)

    def AGREGARITEMS_guardarinfo(self):
        CAT = self.CATEGORIA.currentText()
        globals()["categoria"] = CAT
        numfid = self.ID.text()
        subcat = self.posicionCB_subcat()[0]
        marca = self.MARCA.text()
        modelo = self.MODELO.text()
        medida = self.MEDIDA.currentText()
        preciocliente = self.PRECIOCLIENTE.text()
        tedias = self.TEDIAS.text()
        costo = self.COSTO.text()
        proveedor = self.PROVEEDOR.text()
        comentarios = self.NOTAS.toPlainText()
        descripcion = self.DESCRIPCION.text()
        comando=globals()["comando"]
#        vectorguardado = [numfid, subcat, marca, modelo, medida, preciocliente, tedias, costo, proveedor, comentarios,descripcion]
        basedatos = "items.db"
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("ingresando base datos para guardar comando")
            sqlite_insert_with_param = comando

            vectorguardado = [numfid, subcat, marca, modelo, medida, preciocliente, tedias, costo, proveedor, comentarios,descripcion]

            cursor.execute(sqlite_insert_with_param, vectorguardado)
            sqliteConnection.commit()
            print("vector guardado")

            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                #self.pasarinfo()
                print("cerrando base de datos pertinente")
        return ()

    def verificacion(self):
        try:
            costo = float(self.COSTO.text())
            preciofinal = float(self.PRECIOCLIENTE.text())
            tiempoentrega = int(self.TEDIAS.text())
        except:
            errornumeros()
            return ()
        descripcion = self.DESCRIPCION.text()
        marca = self.MARCA.text()
        proveedor = self.PROVEEDOR.text()
        comentarios = self.NOTAS.toPlainText()
        print("condicionales")
        if descripcion == "":
            errorfaltainformacion()
            return ()
        if marca == "":
            errorfaltainformacion()
            return ()
        if proveedor == "":
            errorfaltainformacion()
            return ()
        if comentarios == "":
            errorfaltainformacion()
            return ()
        if costo >= preciofinal:
            errorpreciofinal()
            return ()
        if tiempoentrega == "":
            errorfaltainformacion()
            return ()
        LISTO()
        self.dialogButtonBox.setEnabled(True)

        return ()

    def inicio(self):
        self.escogercategoria()
        return ()

def errornumeros():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE FORMATO")
    msg.setIcon(QMessageBox.Information)
    msg.setText(
        "Sólo se permiten números en CANTIDAD,  TIEMPO ENTREGA Y PRECIO DEL CLIENTE, favor de volver a verificar.")
    x = msg.exec_()
    return ()

def errorfaltainformacion():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE POR FALTA INFORMACION")
    msg.setIcon(QMessageBox.Information)
    msg.setText("Hace falta información, favor de revisar y corregir")
    x = msg.exec_()
    return ()

def errorpreciofinal():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE POR FALTA INFORMACION")
    msg.setIcon(QMessageBox.Information)
    msg.setText("El costo NO debe ser MENOR o IGUAL al PRECIO FINAL DEL CLIENTE")
    x = msg.exec_()
    return ()

def LISTO():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("VALIDACIÓN CORRECTA, PUEDES PROCEDER A AGREGARLO AL COTIZADOR.")
    x = msg.exec_()
    return ()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.inicio()
    Dialog.show()
    sys.exit(app.exec_())


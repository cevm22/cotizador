# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\FEXMOVA\proyectos PYTHON\gestionsoriana\AM.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


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

class Ui_Dialog_AM(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 449)
        Dialog.setMinimumSize(QtCore.QSize(390, 449))
        Dialog.setMaximumSize(QtCore.QSize(390, 449))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 410, 161, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 190, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.DESCRIPCION = QtWidgets.QLineEdit(Dialog)
        self.DESCRIPCION.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.DESCRIPCION.setObjectName("DESCRIPCION")
        self.MARCA = QtWidgets.QLineEdit(Dialog)
        self.MARCA.setGeometry(QtCore.QRect(120, 110, 261, 20))
        self.MARCA.setObjectName("MARCA")
        self.COSTO = QtWidgets.QLineEdit(Dialog)
        self.COSTO.setGeometry(QtCore.QRect(300, 180, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.COSTO.setFont(font)
        self.COSTO.setText("")
        self.COSTO.setAlignment(QtCore.Qt.AlignCenter)
        self.COSTO.setObjectName("COSTO")
        self.CANTIDAD = QtWidgets.QLineEdit(Dialog)
        self.CANTIDAD.setGeometry(QtCore.QRect(120, 260, 61, 20))
        self.CANTIDAD.setObjectName("CANTIDAD")
        self.CBmedida = QtWidgets.QComboBox(Dialog)
        self.CBmedida.setGeometry(QtCore.QRect(120, 170, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CBmedida.setFont(font)
        self.CBmedida.setObjectName("CBmedida")
        self.CBmedida.addItem("")
        self.CBmedida.addItem("")
        self.CBmedida.addItem("")
        self.CBmedida.addItem("")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 30, 401, 21))
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.PROVEEDOR = QtWidgets.QLineEdit(Dialog)
        self.PROVEEDOR.setGeometry(QtCore.QRect(120, 140, 261, 20))
        self.PROVEEDOR.setObjectName("PROVEEDOR")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.IDGENERADO = QtWidgets.QLabel(Dialog)
        self.IDGENERADO.setGeometry(QtCore.QRect(130, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.IDGENERADO.setFont(font)
        self.IDGENERADO.setObjectName("IDGENERADO")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 230, 401, 21))
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(200, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(0, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.CBte = QtWidgets.QComboBox(Dialog)
        self.CBte.setGeometry(QtCore.QRect(160, 200, 91, 31))
        self.CBte.setObjectName("CBte")
        self.CBte.addItem("")
        self.CBte.addItem("")
        self.TE = QtWidgets.QLineEdit(Dialog)
        self.TE.setGeometry(QtCore.QRect(120, 200, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TE.setFont(font)
        self.TE.setAlignment(QtCore.Qt.AlignCenter)
        self.TE.setObjectName("TE")
        self.PRECIOFINAL = QtWidgets.QLineEdit(Dialog)
        self.PRECIOFINAL.setGeometry(QtCore.QRect(300, 250, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PRECIOFINAL.setFont(font)
        self.PRECIOFINAL.setText("")
        self.PRECIOFINAL.setAlignment(QtCore.Qt.AlignCenter)
        self.PRECIOFINAL.setObjectName("PRECIOFINAL")
        self.COMENTARIOS = QtWidgets.QPlainTextEdit(Dialog)
        self.COMENTARIOS.setGeometry(QtCore.QRect(10, 330, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.COMENTARIOS.setFont(font)
        self.COMENTARIOS.setPlainText("")
        self.COMENTARIOS.setObjectName("COMENTARIOS")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 300, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 290, 401, 21))
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 420, 161, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.DESCRIPCION, self.MARCA)
        Dialog.setTabOrder(self.MARCA, self.PROVEEDOR)
        Dialog.setTabOrder(self.PROVEEDOR, self.CBmedida)
        Dialog.setTabOrder(self.CBmedida, self.TE)
        Dialog.setTabOrder(self.TE, self.CBte)
        Dialog.setTabOrder(self.CBte, self.COSTO)
        Dialog.setTabOrder(self.COSTO, self.CANTIDAD)
        Dialog.setTabOrder(self.CANTIDAD, self.PRECIOFINAL)
        Dialog.setTabOrder(self.PRECIOFINAL, self.COMENTARIOS)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Agregar Manual"))
        self.label.setText(_translate("Dialog", "Agregar Item Manual"))
        self.label_2.setText(_translate("Dialog", "ID Generado"))
        self.label_3.setText(_translate("Dialog", "Descripcion"))
        self.label_4.setText(_translate("Dialog", "Marca"))
        self.label_5.setText(_translate("Dialog", "Unidad Medida"))
        self.label_6.setText(_translate("Dialog", "Costo"))
        self.label_7.setText(_translate("Dialog", "Cantidad"))
        self.CBmedida.setItemText(0, _translate("Dialog", "PIEZA"))
        self.CBmedida.setItemText(1, _translate("Dialog", "LOTE"))
        self.CBmedida.setItemText(2, _translate("Dialog", "LITRO"))
        self.CBmedida.setItemText(3, _translate("Dialog", "KG"))
        self.label_8.setText(_translate("Dialog", "Proveedor"))
        self.IDGENERADO.setText(_translate("Dialog", "GENERADO AUTOMATICO"))
        self.label_10.setText(_translate("Dialog", "Precio Cliente"))
        self.label_11.setText(_translate("Dialog", "Tiempo Entrega"))
        self.CBte.setItemText(0, _translate("Dialog", "DÍAS"))
        self.CBte.setItemText(1, _translate("Dialog", "SEMANAS"))
        self.TE.setText(_translate("Dialog", "3"))
        self.label_12.setText(_translate("Dialog", "COMENTARIOS ADICIONALES"))
        self.pushButton.setText(_translate("Dialog", "VERIFICAR INFORMACION"))
        self.pushButton.clicked.connect(self.verificacion)

    def guardarITEMmanual(self,numcot):
        fecha=int(time.mktime(time.localtime()))
        idgenerado=self.IDGENERADO.text()
        descripcion=self.DESCRIPCION.text()
        marca=self.MARCA.text()
        proveedor=self.PROVEEDOR.text()
        medida = self.CBmedida.currentText()
        te = self.TE.text()
        TEdimension= self.CBte.currentText()
        costo=self.COSTO.text()
        cant=self.CANTIDAD.text()
        preciocliente=self.PRECIOFINAL.text()
        comentarios=str(self.COMENTARIOS.toPlainText())
        cotizacion=numcot#"1-101119-123"# aquí se debe ingresar la variable del #cotizacion
        basedatos = "items.db"
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            print("ingresando base datos AM")
            sqlite_insert_with_param = """INSERT INTO 'AM'
                              ('fecha', 'numfid','descripcion','marca',
                              'proveedor', 'medida', 'TE', 'TEdimension',
                              'costo','cantidad','subtotal','comentarios',
                              'cotizacion') 
                              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"""

            vector = [fecha,idgenerado,descripcion,marca,proveedor,medida,te,
                      TEdimension,costo,cant,preciocliente,comentarios, cotizacion]

            cursor.execute(sqlite_insert_with_param, vector)
            sqliteConnection.commit()
            print("vector guardado")

            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                self.pasarinfo()
                print("cerrando conexión de la base datos AM")

        return()

    def pasarinfo(self):
        print("pasarinfo")
        item=str(self.IDGENERADO.text())
        cantidad=str(self.CANTIDAD.text())
        basedatos="AM"
        direccionBD="items.db"
        try:
            sqliteConnection=sqlite3.connect(direccionBD)
            cursor = sqliteConnection.cursor()
            UPDATE="""Update pasar set item = ?, cantidad=?, DB=?
                    where ID = 1
                    """
            data=(item,cantidad,basedatos)
            cursor.execute(UPDATE,(data))
            sqliteConnection.commit()
            print("GUARDADO")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                print("Cerrando conexión de Base de Datos")
        return()

    def GENERARID(self):
        sec=int(self.secuencia())
        generado=('AM'+str(sec+1))
        self.IDGENERADO.setText(generado)
        return()

    def secuencia(self):
        print("iniciando lastrow ITEMS")
        basedatos = "items.db"
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()
            SELECT = """SELECT seq from sqlite_sequence
                       where name ='AM'
                       """
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

    def verificacion(self):
        try:
            costo = float(self.COSTO.text())
            preciofinal = float(self.PRECIOFINAL.text())
            cantidad = int(self.CANTIDAD.text())
            tiempoentrega = int(self.TE.text())
        except:
            errornumeros()
            return ()
        descripcion=self.DESCRIPCION.text()
        marca = self.MARCA.text()
        proveedor = self.PROVEEDOR.text()
        comentarios = self.COMENTARIOS.toPlainText()
        print("condicionales")
        if descripcion=="":
            errorfaltainformacion()
            return()
        if marca=="":
            errorfaltainformacion()
            return()
        if proveedor=="":
            errorfaltainformacion()
            return()
        if comentarios=="":
            errorfaltainformacion()
            return()
        if costo >= preciofinal:
            errorpreciofinal()
            return()
        if cantidad =="":
            errorfaltainformacion()
            return()
        if tiempoentrega =="":
            errorfaltainformacion()
            return()
        LISTO()
        self.buttonBox.setEnabled(True)

        return()

def LISTO():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("VALIDACIÓN CORRECTA, PUEDES PROCEDER A AGREGARLO AL COTIZADOR.")
    x = msg.exec_()
    return ()

def errornumeros():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE FORMATO")
    msg.setIcon(QMessageBox.Information)
    msg.setText("Sólo se permiten números en CANTIDAD, COSTO, TIEMPO ENTREGA Y PRECIO DEL CLIENTE, favor de volver a verificar.")
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_AM()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())

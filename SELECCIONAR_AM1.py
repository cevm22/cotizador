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

vectorITEMSCB=[]
class Ui_Dialog_SELCCIONARMANUAL(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 449)
        Dialog.setMinimumSize(QtCore.QSize(390, 449))
        Dialog.setMaximumSize(QtCore.QSize(390, 449))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 410, 161, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 0, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(240, 230, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 280, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 401, 21))
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 401, 21))
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(180, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(0, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.CANTIDAD = QtWidgets.QLineEdit(Dialog)
        self.CANTIDAD.setGeometry(QtCore.QRect(120, 280, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CANTIDAD.setFont(font)
        self.CANTIDAD.setAlignment(QtCore.Qt.AlignCenter)
        self.CANTIDAD.setObjectName("CANTIDAD")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 310, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 300, 401, 21))
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ID = QtWidgets.QLabel(Dialog)
        self.ID.setGeometry(QtCore.QRect(110, 80, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ID.setFont(font)
        self.ID.setObjectName("ID")
        self.DESCRIPCION = QtWidgets.QLabel(Dialog)
        self.DESCRIPCION.setGeometry(QtCore.QRect(110, 110, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DESCRIPCION.setFont(font)
        self.DESCRIPCION.setObjectName("DESCRIPCION")
        self.MARCA = QtWidgets.QLabel(Dialog)
        self.MARCA.setGeometry(QtCore.QRect(110, 140, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MARCA.setFont(font)
        self.MARCA.setObjectName("MARCA")
        self.PROVEEDOR = QtWidgets.QLabel(Dialog)
        self.PROVEEDOR.setGeometry(QtCore.QRect(110, 170, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PROVEEDOR.setFont(font)
        self.PROVEEDOR.setObjectName("PROVEEDOR")
        self.MEDIDA = QtWidgets.QLabel(Dialog)
        self.MEDIDA.setGeometry(QtCore.QRect(110, 200, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MEDIDA.setFont(font)
        self.MEDIDA.setObjectName("MEDIDA")
        self.TE = QtWidgets.QLabel(Dialog)
        self.TE.setGeometry(QtCore.QRect(110, 230, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TE.setFont(font)
        self.TE.setObjectName("TE")
        self.COSTO = QtWidgets.QLabel(Dialog)
        self.COSTO.setGeometry(QtCore.QRect(300, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.COSTO.setFont(font)
        self.COSTO.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.COSTO.setObjectName("COSTO")
        self.PRECIOCLIENTE = QtWidgets.QLabel(Dialog)
        self.PRECIOCLIENTE.setGeometry(QtCore.QRect(290, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PRECIOCLIENTE.setFont(font)
        self.PRECIOCLIENTE.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PRECIOCLIENTE.setObjectName("PRECIOCLIENTE")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 340, 371, 71))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.SELECCIONAR_pasarinfo)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Seleccionar producto AGREGADO MANUAL"))
        self.label.setText(_translate("Dialog", "Seleccionar Item Manual (AM)"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_3.setText(_translate("Dialog", "Descripcion"))
        self.label_4.setText(_translate("Dialog", "Marca"))
        self.label_5.setText(_translate("Dialog", "Unidad Medida"))
        self.label_6.setText(_translate("Dialog", "Costo"))
        self.label_7.setText(_translate("Dialog", "Cantidad"))
        self.label_8.setText(_translate("Dialog", "Proveedor"))
        self.label_10.setText(_translate("Dialog", "Precio Cliente"))
        self.label_11.setText(_translate("Dialog", "Tiempo Entrega"))
        self.CANTIDAD.setText(_translate("Dialog", "3"))
        self.label_12.setText(_translate("Dialog", "COMENTARIOS ADICIONALES"))
        self.ID.setText(_translate("Dialog", "aqui va el ID del producto"))
        self.DESCRIPCION.setText(_translate("Dialog", "aqui va la descripcion desglosada  del producto"))
        self.MARCA.setText(_translate("Dialog", "aqui va la marca "))
        self.PROVEEDOR.setText(_translate("Dialog", "aqui va el proveedor que distribuye el item"))
        self.MEDIDA.setText(_translate("Dialog", "unidadde medida"))
        self.TE.setText(_translate("Dialog", "aqui va el ID del producto"))
        self.COSTO.setText(_translate("Dialog", "Costo"))
        self.PRECIOCLIENTE.setText(_translate("Dialog", "Costo"))

        self.comboBox.currentTextChanged.connect(self.SELECCIONAR_seleccionaritem)

    def SELECCIONAR_pasarinfo(self):
        print("pasarinfo")
        item=str(self.ID.text())
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

    def SELECCIONAR_mostrar_ITEMS(self,filtro):
        print("def SELECCIONAR_mostrar_ITEMS")
        SUBCAT="items.db"
        TEdim=""
        TEnum=""
        vectorITEMSCB = globals()["vectorITEMSCB"]
        vector=vectorITEMSCB[filtro]
        if vectorITEMSCB==[]:
            print("VECTOR VACÍO EN DEF mostrar_ITEMS ")
            return()
        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT="""SELECT numfid, descripcion, marca, medida, subtotal, comentarios, costo, proveedor, TE,
                        TEdimension 
                        from AM 
                        where numfid = ?"""

            cursor.execute(SELECT,(vector,))
            record=cursor.fetchall()
            for row in record:
                self.ID.setText(str(row[0])) #OK
                self.DESCRIPCION.setText(str(row[1])) #OK
                self.MARCA.setText(str(row[2]))#OK
                self.MEDIDA.setText(str(row[3]))#OK
                self.PRECIOCLIENTE.setText(str(row[4]))#OK
                self.plainTextEdit.clear()#OK
                self.plainTextEdit.insertPlainText(str(row[5]))#OK
                self.COSTO.setText(str(row[6]))  # OK
                self.PROVEEDOR.setText(str(row[7]))  # OK
                TEnum=str(row[8])
                TEdim=str(row[9])
                self.TE.setText(TEnum+'-'+TEdim)
            #print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                #print("Cerrando conexión de Base de Datos")
        return()

    def SELECCIONAR_seleccionaritem(self):
        posicion=self.comboBox.currentIndex()
        vectorITEMSCB=globals()["vectorITEMSCB"]
        #print(vectorITEMSCB)
        print(posicion)
        if posicion==-1:
            print("negativo")
            #print(vector)
            return()
        if vectorITEMSCB == [] :
                print("vector vacío")
                return()
        else:
                print("POSICION DEL COMBO BOX")
                self.SELECCIONAR_mostrar_ITEMS(posicion)
        return()

    def SELECCIONAR_pasarinfo(self):
        print("pasarinfo")
        item=str(self.ID.text())
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

    def SELECCIONAR_llenarCB_SUBCAT(self):
        print("SELECCIONAR_llenarCB_SUBCAT")
        a=""
        b=""
        SUBCAT = "items.db"
        globals()['vectorITEMSCB']=[]
        vectorITEMSCB=globals()['vectorITEMSCB']
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()

            SELECT = """SELECT numfid, descripcion from AM """
            cursor.execute(SELECT)
            record = cursor.fetchall()
            for row in record:
                a = str(row[0]) #numero FID interno
                b = str(row[1])  # numero descripcion
                self.comboBox.addItem(a+'<->'+b)
                vectorITEMSCB.append(a)

                # print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                globals()['vectorITEMSCB']=vectorITEMSCB
                self.SELECCIONAR_seleccionaritem()
                # print("Cerrando conexión de Base de Datos")
        return ()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_SELCCIONARMANUAL()
    ui.setupUi(Dialog)
    #ui.SELECCIONAR_llenarCB_SUBCAT()
    Dialog.show()
    sys.exit(app.exec_())

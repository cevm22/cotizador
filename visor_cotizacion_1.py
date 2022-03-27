from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from datetime import date, datetime
import logging
import sqlite3
import json
import os
import subprocess
import time


actualizacion_ON=0
cambios=0
motivo=0

class Ui_Dialog_visor_cotizador(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(678, 404)
        Dialog.setMinimumSize(QtCore.QSize(678, 404))
        Dialog.setMaximumSize(QtCore.QSize(678, 404))
        Dialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setGeometry(QtCore.QRect(240, 370, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.fecha = QtWidgets.QLabel(Dialog)
        self.fecha.setGeometry(QtCore.QRect(330, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fecha.setFont(font)
        self.fecha.setObjectName("fecha")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(130, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pedido = QtWidgets.QLabel(Dialog)
        self.pedido.setGeometry(QtCore.QRect(180, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pedido.setFont(font)
        self.pedido.setObjectName("pedido")
        self.estatusCB = QtWidgets.QComboBox(Dialog)
        self.estatusCB.setEnabled(False)
        self.estatusCB.setGeometry(QtCore.QRect(550, 80, 111, 22))
        self.estatusCB.setEditable(False)
        self.estatusCB.setObjectName("estatusCB")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.estatusCB.addItem("")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(160, 10, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.numcot = QtWidgets.QLabel(Dialog)
        self.numcot.setGeometry(QtCore.QRect(100, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.numcot.setFont(font)
        self.numcot.setObjectName("numcot")
        self.motivoCB = QtWidgets.QComboBox(Dialog)
        self.motivoCB.setEnabled(False)
        self.motivoCB.setGeometry(QtCore.QRect(550, 110, 111, 22))
        self.motivoCB.setObjectName("motivoCB")
        self.motivoCB.addItem("")
        self.motivoCB.addItem("")
        self.motivoCB.addItem("")
        self.motivoCB.addItem("")
        self.motivoCB.addItem("")
        self.motivoCB.addItem("")
        self.motivoCB.addItem("")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 30, 691, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(480, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.titulo = QtWidgets.QLabel(Dialog)
        self.titulo.setGeometry(QtCore.QRect(60, 120, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 260, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tienda = QtWidgets.QLabel(Dialog)
        self.tienda.setGeometry(QtCore.QRect(70, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tienda.setFont(font)
        self.tienda.setObjectName("tienda")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(280, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(480, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 691, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(480, 50, 181, 23))
        self.pushButton.setObjectName("pushButton")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(423, 40, 20, 111))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.historialcomentarios = QtWidgets.QPlainTextEdit(Dialog)
        self.historialcomentarios.setGeometry(QtCore.QRect(10, 180, 651, 81))
        self.historialcomentarios.setObjectName("historialcomentarios")
        self.agregarcomentarios = QtWidgets.QPlainTextEdit(Dialog)
        self.agregarcomentarios.setGeometry(QtCore.QRect(10, 290, 651, 71))
        self.agregarcomentarios.setObjectName("agregarcomentarios")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.comentario)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.fecha.setText(_translate("Dialog", "15-12-2019"))
        self.label_7.setText(_translate("Dialog", "Pedido"))
        self.label_4.setText(_translate("Dialog", "Titulo"))
        self.pedido.setText(_translate("Dialog", "1234567890"))
        self.estatusCB.setItemText(0, _translate("Dialog", "Enviada"))
        self.estatusCB.setItemText(1, _translate("Dialog", "Pedido"))
        self.estatusCB.setItemText(2, _translate("Dialog", "Cancelada"))
        self.label_12.setText(_translate("Dialog", "VISOR DE COTIZACIÓN DETALLADA"))
        self.label_3.setText(_translate("Dialog", "Tienda"))
        self.numcot.setText(_translate("Dialog", "999-SOR-151219-CV-12345"))
        self.motivoCB.setItemText(0, _translate("Dialog", "N/A"))
        self.motivoCB.setItemText(1, _translate("Dialog", "Precio Alto"))
        self.motivoCB.setItemText(2, _translate("Dialog", "Retraso COT"))
        self.motivoCB.setItemText(3, _translate("Dialog", "Prov IGUALA"))
        self.motivoCB.setItemText(4, _translate("Dialog", "No incluir INST"))
        self.motivoCB.setItemText(5, _translate("Dialog", "Tiempo Entrega"))
        self.motivoCB.setItemText(6, _translate("Dialog", "OTROS"))
        self.label_11.setText(_translate("Dialog", "Motivo"))
        self.titulo.setText(_translate("Dialog", "Aquí va el título de la cotización que se colocó cuando se envió"))
        self.label_2.setText(_translate("Dialog", "Historial de Comentarios "))
        self.label_5.setText(_translate("Dialog", "Cotizacion"))
        self.label.setText(_translate("Dialog", "Agregar comentarios extras"))
        self.tienda.setText(_translate("Dialog", "999"))
        self.label_8.setText(_translate("Dialog", "Fecha"))
        self.label_6.setText(_translate("Dialog", "Estatus"))
        self.pushButton.setText(_translate("Dialog", "ACTUALIZAR ESTATUS"))
        self.pushButton_2.setText(_translate("Dialog", "Revisar Cambios"))


        #falta DESBLOQUEAR BOTONES Y HCER LA INTEGRACION EN EL GESTOR DE COTIZACIONES
        self.pushButton.clicked.connect(self.variablesvalidacion)
        self.pushButton_2.clicked.connect(self.revisarinformacion)
        self.estatusCB.currentTextChanged.connect(self.revisarCB)


    def visor_cotizacion(self,cot):
        #cot = "12-15122019-CV-1"
        a = seleccionar(cot)
        self.historialcomentarios.setReadOnly(True)

        # print(a)
        self.mostrarinformacion(a)
        return ()

    def comentario(self):
        historial=self.historialcomentarios.toPlainText()
        comentarioextra=self.agregarcomentarios.toPlainText()
        tiempoactual = time.mktime(time.localtime())
        tiempoSTR = (str(int(tiempoactual)))
        comentariofinal= historial + "\n" + convertirFECHA(tiempoSTR) + "-->" +comentarioextra
        CB1=self.estatusCB.currentIndex()
        CB2=self.motivoCB.currentIndex()
        numcot=self.numcot.text()
        vector=[comentariofinal,CB1,CB2,numcot]
        updateinfo(vector)

        #función para actualizar datos
        return


    def revisarinformacion(self):
        variableglobal=globals()["actualizacion_ON"]
        variableCBstatus=self.estatusCB.currentIndex()
        change = globals()["cambios"]
        #PRIMERA VALIDACION
        if variableglobal==0:
            print("no hubo cambios, activando botones para salir")
            texto3 = self.agregarcomentarios.toPlainText()
            if texto3!="":
                print("se agregaron comentarios, pero no hubo cambios en estatus")
                ingresotexto()
                self.buttonBox.setEnabled(True)
                self.pushButton.setEnabled(False)
                self.agregarcomentarios.setReadOnly(True)
                return()
            else:
                validacionMSG()
                self.buttonBox.setEnabled(True)
                self.pushButton.setEnabled(True)
                self.agregarcomentarios.setReadOnly(True)

            return()
        if variableglobal==1 and variableCBstatus==0:
            texto=self.agregarcomentarios.toPlainText()

            if texto=="":
                #funcion para HABILITAR BOTONES "OK/CANCEL"
                print("NO HAY COMENTARIOS POR AGREGAR-habilitando botones")
                self.buttonBox.setEnabled(True)
                validacionMSG()
                if change!=variableCBstatus:
                    POPUPCAMBIOS()
                    return()
                return()
            else:
                #activar función para actualizar los comentarios extras que se hayan agragado
                print("guardando comentarios extras")
                self.buttonBox.setEnabled(True)
                self.pushButton.setEnabled(False)
                self.estatusCB.setEnabled(False)
                self.agregarcomentarios.setReadOnly(True)
                ingresotexto()
                #self.comentario()
                return ()

        else:
            print("hubo cambios")
            #POPUPCAMBIOS()
            #self.comentario()
            texto1=self.agregarcomentarios.toPlainText()
            if texto1 == "":
                POPUPCAMBIOS()

                return ()
            else:
                ingresotextoycambios()
                motivo=self.motivoCB.currentIndex()
                estatus=self.estatusCB.currentIndex()
                if motivo ==0 and estatus==2:
                    mensajemotivoNA()
                    return()
                else:
                    print("habilitando botones, todo correcto")
                    self.buttonBox.setEnabled(True)
                    self.pushButton.setEnabled(False)
                    self.estatusCB.setEnabled(False)
                    self.motivoCB.setEnabled(False)
                    self.agregarcomentarios.setReadOnly(True)
                    #self.comentario()
                return()

            return()

        return ()

    def variablesvalidacion(self):
        self.estatusCB.setEnabled(1)
        globals()["actualizacion_ON"] = 1
        self.revisarCB()
        return()

    def revisarCB(self):
        a=self.estatusCB.currentIndex()
        b=globals()["actualizacion_ON"]
        c=globals()["motivo"]
        if a==2 and b==1:
            print("cotizacion cancelada")
            self.motivoCB.setEnabled(1)
            self.motivoCB.setCurrentIndex(int(c))
        else:
            self.motivoCB.setEnabled(0)
            self.motivoCB.setCurrentIndex(0)

        return()

    def mostrarinformacion(self, vector):
        numcot=(vector[0])
        self.numcot.setText(str(vector[0]))
        fecha = convertirFECHA(str(vector[1]))
        self.fecha.setText(str(fecha))
        self.tienda.setText(str(vector[2]))
        self.titulo.setText(str(vector[3]))
        # self.COMENTARIOS.toPlainText() #aqui tomas el valor
        # self.plainTextEdit.insertPlainText(str(row[5]))# aquí llenas de texto
        self.historialcomentarios.insertPlainText(str(vector[6]))
        indice=int(vector[4])
        globals()["cambios"]=indice
        print(indice)
        self.estatusCB.setCurrentIndex(indice)
        if indice==1:
            print("entrando al indice 1")
            self.pedido.setText(str(buscarpedido(numcot)))

        indice2=int(vector[5])
        globals()["motivo"] = indice2
        self.motivoCB.setCurrentIndex(indice2)
        self.motivoCB.setEnabled(0)
        #print(vector)
        return ()


def seleccionar(numerocotizacion):
    print("Seleccionando cotizacion")
    basedatos = "administrativo.db"
    record = []
    try:
        sqliteConnection = sqlite3.connect(basedatos)
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        SELECT = """
                SELECT 
                numcotizacion, timestampcreacion, numtienda,
                titulocotizacion,  estatus, motivo, comentarios

                FROM
                cotizaciones

                WHERE
                numcotizacion = ?
                """
        cursor.execute(SELECT, (numerocotizacion,))
        record = cursor.fetchall()
        cursor.close

    except sqlite3.Error as error:
        print("Error, ALV -----> ", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Cerrando conexión de Base de Datos")
            #print(record)
    return (record[0])

def buscarpedido(numcot):
    basedatos="administrativo.db"
    try:
        sqliteConnection = sqlite3.connect(basedatos)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        SELECT = """SELECT numpedido 
                    FROM
                    pedidos                    
                    where 
                    numcotizacion = ?  """
        data = (str(numcot))
        cursor.execute(SELECT, (data,))
        record = cursor.fetchone()
        sqliteConnection.commit()
        print("<<<<<<<<<<<<<<Record Updated successfully>>>>>>>>>>>")
        cursor.close

    except sqlite3.Error as error:
        print("Error, ALV -----> ", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Cerrando conexión de Base de Datos")

            if record==None:
                return("SIN REGISTRO")
            else:
                return(record[0])
    return()


def updateinfo(vector):
    basedatos="administrativo.db"
    comentario=vector[0]
    estatus=vector[1]
    motivo=vector[2]
    numcot=vector[3]
    try:
        sqliteConnection = sqlite3.connect(basedatos)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        update = """Update cotizaciones 
                    set 
                    comentarios = ?,
                    estatus = ?,
                    motivo = ?
                    where 
                    numcotizacion = ?  """
        data = (comentario,estatus,motivo,numcot)
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

def convertirFECHA(tiempo):
    fecha = time.strftime("%D ", time.localtime(int(tiempo)))
    return (fecha)

def POPUPCAMBIOS():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("SE DETECTÓ QUE HUBO CAMBIOS, FAVOR DE AGREGAR INFORMACIÓN EN LA SECCIÓN DE LOS COMENTARIOS.")
    x = msg.exec_()
    return ()
def validacionMSG():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("NO SE DETECTARON CAMBIOS EN EL REGISTRO.")
    x = msg.exec_()
    return ()
def ingresotexto():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("Se detectó texto en Agregar comentarios. Favor de proceder a guardar presionando el botón")
    x = msg.exec_()
    return()
def ingresotextoycambios():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("Se detectaron cambios y texto en Agregar comentarios. "
                "Favor de proceder a guardar presionando el botón"
                " OK")
    x = msg.exec_()
    return()
def mensajemotivoNA():
    msg = QMessageBox()
    msg.setWindowTitle("VALIDACIÓN CORRECTA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("El estatus de cotización indica 'CANCELADO'. Favor de escoger otro motivo de cancelación distinto a N/A ")
    x = msg.exec_()
    return()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_visor_cotizador()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



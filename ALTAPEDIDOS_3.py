########### TODO ################
# TODO- Hacer otro  módulo para modificar los pedidos y agregar los documentos faltantes
########### TODO ################
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
PDF=""
XLSX=""
nombrePDF=""
nombreXLSX=""
nuevoPDF=""
nuevoXLSX=""
titulocotizacion=[]
class Ui_MainWindow_ALTA(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 316)
        MainWindow.setMinimumSize(QtCore.QSize(412, 316))
        MainWindow.setMaximumSize(QtCore.QSize(412, 316))
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
        self.label_4.setGeometry(QtCore.QRect(20, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 101, 21))
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
        self.line.setGeometry(QtCore.QRect(120, 60, 20, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 81, 20))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 120, 81, 22))
        self.dateEdit.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(140, 150, 81, 22))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_3.setGeometry(QtCore.QRect(140, 180, 81, 22))
        self.dateEdit_3.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(140, 210, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 210, 221, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 270, 221, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 81, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(12)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 75, 71))
        self.pushButton.setObjectName("pushButton")
        self.cotizacionesCB = QtWidgets.QComboBox(self.centralwidget)
        self.cotizacionesCB.setGeometry(QtCore.QRect(140, 240, 251, 22))
        self.cotizacionesCB.setObjectName("cotizacionesCB")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "Ruta del archivo en PDF"))
        self.label_10.setText(_translate("MainWindow", "TITULO DE COTIZACION SELECCIONADO"))
        self.pushButton.setText(_translate("MainWindow", "Guardar Alta"))
        self.label_11.setText(_translate("MainWindow", "Titulo"))
# botones de pruebas
        self.pushButton.clicked.connect(self.guardar)
        self.toolButton.clicked.connect(self.rutaPDF)
        self.cotizacionesCB.currentTextChanged.connect(self.labelcotizacion)

    # botones de pruebas

    def prueba(self):
        gestorpedidos()
        return ()

    def guardar(self):

        try:
            tienda = int(self.lineEdit.text())
            pedido = int(self.lineEdit_2.text())
        except:
            errornumeros()
            return ()
        fechapedido = self.convertirfecha() #AGREGAR 86400 seg para desfase
        iniciopedido = self.fechainicioembarque() #AGREGAR 86400 seg para desfase
        finpedido = self.fechafinembarque() #AGREGAR 86400 seg para desfase
        rutaXLSX = (globals()['XLSX'])  # se intercambio XLSX por PDF
        rutaPDF = (globals()['PDF'])  # se intercambio PDF  por XLSX
        seleccionCB=str(self.cotizacionesCB.currentText())
        rutanombrePDF = (globals()['nombrePDF'])[:-5]
        prefijo=self.pedidorepetido(pedido)
        numcotizacion=str(self.cotizacionesCB.currentText())
        titulo=str(self.label_10.text())

        if seleccionCB=="":
            errorfaltainformacion()
            return()
        if rutaPDF == "":
            errorfaltainformacion()
            return ()
        if fechapedido <= 1559347200:
            errorfechamenor()
            return ()
        if iniciopedido <= 1559347200:
            errorfechamenor()
            return ()
        if finpedido <= 1559347200:
            errorfechamenor()
            return ()
        if iniciopedido == finpedido or iniciopedido >= finpedido or fechapedido >= finpedido or fechapedido > iniciopedido:
            errorfechapedido()
            return ()

        # archivoconvertidoPDF=convertirAdatobinario(rutaPDF)
        # PDF=(archivoconvertidoPDF)
        # docs=int(20)
        # estatusID=int(1)
        # estatus="NO EJECUTADO"

        # vectorinfo=[tienda,pedido,fechapedido,iniciopedido,finpedido,rutanombreXLSX,PDF,docs,estatusID,estatus]
        # guardararchivos(vectorinfo)

        # GUARDADO()
        # gestorpedidos()
        # sys.exit()
        # print(rutaPDF)
        # self.creardirectorio(pedido)
        # self.copiararchivo(rutaPDF,pedido)

        validaciondirectorio=self.confirmardirectorio(pedido)
        validacionXSLX=self.confirmacionexistencia()
        prefijo=self.pedidorepetido(pedido)

        if prefijo==0:
            if validaciondirectorio==False:
                if validacionXSLX==False:
                    #print("no existe cotización en carpeta COTIZACIONES. Favor de hacerla primero.")
                    errrornocotizacion()
                else:
                    pedido2 = str(pedido) + '-' + str(prefijo)
                    #crear directorio
                    self.creardirectorio(pedido2)
                    #proceder a guardar los archivos dentro del directorio
                    self.copiararchivoPDF(rutaPDF,pedido2)
                    self.copiararchivoXLSX(seleccionCB,pedido2)
                    #proceder a guardar los registros en base de datos
                    print("carpeta creada, y archivos copiadas con nombres cambiados")
            else:
                pedido2 = str(pedido) + '-' + str(prefijo)
                self.copiararchivoPDF(rutaPDF, pedido2)
                self.copiararchivoXLSX(seleccionCB, pedido2)
        else:
            print("entrando para crear otro pedido parecido")
            # crear directorio
            pedido2=str(pedido)+'-'+str(prefijo)
            print(pedido2)
            self.creardirectorio(pedido2)
            # proceder a guardar los archivos dentro del directorio
            self.copiararchivoPDF(rutaPDF, pedido2)
            self.copiararchivoXLSX(seleccionCB, pedido2)

        archivopedido=globals()["nuevoPDF"]
        archivocotizacion=globals()["nuevoXSLX"]

        vectorinfo = [tienda, pedido, fechapedido, iniciopedido, finpedido,numcotizacion, titulo, 0, archivocotizacion, archivopedido,prefijo,2] #aagrega tipo
        print(vectorinfo)
        print("guardararchivos")
        guardararchivos(vectorinfo)  # vector
        print("GUARDADO")
        GUARDADO()
        print("gestorpedidos")
        gestorpedidos()
        print("updatecotizacion")
        updatecotizacion(numcotizacion)
        print("SALIR ")
        sys.exit()
        return ()

    def pedidorepetido(self,data):
        basedatos="administrativo.db"
        #data=1
        vector=[]
        try:
            sqliteConnection = sqlite3.connect(basedatos)
            cursor = sqliteConnection.cursor()

            SELECT = """SELECT numcotizacion
                    from pedidos
                    where numpedido=?                    
                     """
            cursor.execute(SELECT,(data,))
            record = cursor.fetchall()


            for row in record:
                vector.append(row[0])

            print(vector)
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()

                #print(len(vector))
                return(len(vector))
                # print("Cerrando conexión de Base de Datos")
        return()

    def LLENARCB(self):
        print("LLENANDO COMBO BOX DE COTIZACIONES")
        SUBCAT = "administrativo.db"
        globals()['titulocotizacion']=[]
        titulocotizacion=[]
        try:
            sqliteConnection = sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()

            SELECT = """SELECT numcotizacion, titulocotizacion
                    from cotizaciones
                    where estatus=0
                     """
            cursor.execute(SELECT)
            record = cursor.fetchall()
            for row in record:
                populateCB=row[0]
                self.cotizacionesCB.addItem(populateCB)
                titulocotizacion.append(row[1])
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                globals()['titulocotizacion'] = titulocotizacion
                self.labelcotizacion()
                return()
                # print("Cerrando conexión de Base de Datos")

        return ()

    def labelcotizacion(self):
        titulo=globals()['titulocotizacion']
        pos=int(self.cotizacionesCB.currentIndex())
        if titulo==[]:
            self.label_10.setText("NO HAY COTIZACIONES")
        else:
            self.label_10.setText(str(titulo[pos]))
        return()

    def confirmacionexistencia(self):
        archivo=str(self.cotizacionesCB.currentText())
        rutascript = os.getcwd()
        armar = rutascript + '\COTIZACIONES' + ('\\') + archivo+ ".xlsx"
        validacion=os.path.isfile(armar)
        return (validacion)

    def copiararchivoPDF(self, archivoacopiar, numpedido):
        carpeta = "DOCUMENTACION"
        # \DOCUMENTACION\123456789\123456789-PEDIDO
        nombre = str(numpedido) + '-' + "PEDIDO" + ".pdf"
        globals()["nuevoPDF"]=nombre
        rutanombre = carpeta + '\\' + str(numpedido) + '\\' + nombre
        shutil.copyfile(archivoacopiar, rutanombre)
        return ()

    def copiararchivoXLSX(self, archivoacopiar, numpedido):
        carpeta = "DOCUMENTACION"
        # \COTIZACIONES\1-25122019-CV-9.XLSX
        nombre = str(numpedido) + '-' + "COTIZACION" + ".xlsx"
        globals()["nuevoXSLX"]=nombre
        rutanombre = carpeta + '\\' + str(numpedido) + '\\' + nombre
        rutacotizacion="COTIZACIONES"+'\\'+archivoacopiar+".xlsx"
        shutil.copyfile(rutacotizacion, rutanombre)
        return ()

    def confirmardirectorio(self,numpedido):
        direccion = "\DOCUMENTACION" + '\\' + str(numpedido)
        rutascript = os.getcwd()
        armar=rutascript + direccion
        validacion = os.path.isfile(armar)
        return(validacion)

    def creardirectorio(self, numpedido):
        direccion = "DOCUMENTACION" + '\\' + str(numpedido)
        os.mkdir(direccion)
        # print("DIRECCION-->",direccion)
        return ()

    def rutaPDF(self):
        rutapdf = self.obtenerrutaPDF()
        globals()['PDF'] = rutapdf
        self.label_9.setText(rutapdf)
        return ()

    def rutaXLSX(self):
        rutaxlsx = self.obtenerrutaXLSX()
        globals()['XLSX'] = rutaxlsx
        self.label_10.setText(rutaxlsx)
        return ()

    # obtener ruta del archivo
    def obtenerrutaPDF(self):
        ruta = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File', '', 'Files (*.pdf)')
        ruta2, _ = ruta
        # nombre del archivo
        nombre1 = Path(ruta2).name
        nombreXLSX = ""
        globals()['nombrePDF'] = nombre1
        print(nombre1)
        return (ruta[0])

    def obtenerrutaXLSX(self):
        ruta = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File', '', 'Files (*.xlsx)')
        ruta2, _ = ruta
        # nombre del archivo
        nombre1 = Path(ruta2).name
        globals()['nombreXLSX'] = nombre1
        return (ruta[0])

    def validacionnumeros(self, a):

        try:
            b = int(a)
            return (b)
        except:
            errornumeros()
            return ()

    def convertirfecha(self):
        day = self.dateEdit.dateTime().toString("dd")
        month = self.dateEdit.dateTime().toString("MM")
        year = self.dateEdit.dateTime().toString("yyyy")
        s = '-'
        vectordate = year + s + month + s + day
        conversion = fechaatimestmp(vectordate)
        return (conversion)

    def fechainicioembarque(self):
        day = self.dateEdit_2.dateTime().toString("dd")
        month = self.dateEdit_2.dateTime().toString("MM")
        year = self.dateEdit_2.dateTime().toString("yyyy")
        s = '-'
        vectordate = year + s + month + s + day
        conversion = fechaatimestmp(vectordate)
        return (conversion)

    def fechafinembarque(self):
        day = self.dateEdit_3.dateTime().toString("dd")
        month = self.dateEdit_3.dateTime().toString("MM")
        year = self.dateEdit_3.dateTime().toString("yyyy")
        s = '-'
        vectordate = year + s + month + s + day
        conversion = fechaatimestmp(vectordate)
        return (conversion)

def fechaatimestmp(fecha):
    # formato de concatenacion para fecha a Timestamp
    vectortime = fecha + "T00:00:00.000Z"
    utc_dt = datetime.strptime(vectortime, '%Y-%m-%dT%H:%M:%S.%fZ')
    # Convert UTC datetime to seconds since the Epoch
    conversion = int((utc_dt - datetime(1970, 1, 1)).total_seconds())
    return (conversion)

def errornumeros():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE FORMATO")
    msg.setIcon(QMessageBox.Information)
    msg.setText("Sólo se permiten números en PEDIDO y TIENDA")
    x = msg.exec_()
    return ()
def errorfaltainformacion():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE POR FALTA INFORMACION")
    msg.setIcon(QMessageBox.Information)
    msg.setText("Hace falta información, favor de revisar y corregir")
    x = msg.exec_()
    return ()
def errorfechamenor():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE FECHA")
    msg.setIcon(QMessageBox.Information)
    msg.setText("NO PUEDES ELEGIR UNA FECHA MENOR DE JULIO DEL 2019, FAVOR DE CORREGIR")
    x = msg.exec_()
    return ()
def errorfechapedido():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE FECHAS DE EMBARQUE")
    msg.setIcon(QMessageBox.Information)
    msg.setText(
        "LA FECHA INICIO DE EMBARQUE NO DEBE SER MAYOR O IGUAL QUE LA FECHA DE FIN DE EMBARQUE O FECHA PEDIDO SEA MENOR QUE LAS FECHAS DE EMBARQUES")
    x = msg.exec_()
    return ()
def errrornocotizacion():
    msg = QMessageBox()
    msg.setWindowTitle("ERROR DE FECHAS DE EMBARQUE")
    msg.setIcon(QMessageBox.Information)
    msg.setText(
        "NO existe cotización. Favor de hacerla primero.")
    x = msg.exec_()
    return ()

def GUARDADO():
    msg = QMessageBox()
    msg.setWindowTitle("INFORMACION GUARDADA")
    msg.setIcon(QMessageBox.Information)
    msg.setText(
        "INFORMACIÓN GUARDADA CORRECTAMENTE")
    x = msg.exec_()
    return ()

def convertirAdatobinario(filename):
    # convert files to binary format
    with open(filename, 'rb') as file:
        blobdata = file.read()
    return (blobdata)

def updatecotizacion(data):
    basedatos="administrativo.db"
    try:
        sqliteConnection=sqlite3.connect(basedatos)
        cursor=sqliteConnection.cursor()
        update="""UPDATE cotizaciones
                set
                estatus=1
                where
                numcotizacion=?"""

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
def guardararchivos(vector):
    try:
        sqliteConnection = sqlite3.connect(basedatos)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        vector_query = """ INSERT INTO 'pedidos'
         ('numtienda','numpedido','timestamppedido','timestampIembarque','timestampFembarque',
         'numcotizacion', 'titulocotizacion','estatus','archivocotizacion','archivopedido','prefijo','tipo')
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"""

        # guardar en base de datos
        cursor.execute(vector_query, vector)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")
    return ()

def gestorpedidos():
    script = "GESTORPEDIDOS_3.py"
    subprocess.Popen([sys.executable, script], stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    print("moviendo")
    return ()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_ALTA()
    ui.setupUi(MainWindow)
    ui.LLENARCB()
    MainWindow.show()
    sys.exit(app.exec_())


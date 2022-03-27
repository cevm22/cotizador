from PyQt5 import QtCore, QtGui, QtWidgets
import logging
import sqlite3
import sys
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
#++++++++++++++++++#
#variables globales#
#++++++++++++++++++#
vectorsubcategoria=[]
subvector=[]
posvector=[]
tipo=""
m=""
buscar=""
buscar_items_subc=""
buscar_filtraritems=""
letraSUBCAT=""
consultar_items=""
#++++++++++++++++++#
#variables globales#
#++++++++++++++++++#
class Ui_Dialog(object):
    def __init__(self, m):        
        globals()["m"]=m        

    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(615, 360)
        Dialog.setMinimumSize(QtCore.QSize(615, 360))
        Dialog.setMaximumSize(QtCore.QSize(615, 360))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 310, 161, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.SUBCATEGORIA = QtWidgets.QLabel(Dialog)
        self.SUBCATEGORIA.setGeometry(QtCore.QRect(500, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SUBCATEGORIA.setFont(font)
        self.SUBCATEGORIA.setTextFormat(QtCore.Qt.PlainText)
        self.SUBCATEGORIA.setAlignment(QtCore.Qt.AlignCenter)
        self.SUBCATEGORIA.setObjectName("SUBCATEGORIA")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 40, 431, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_1 = QtWidgets.QComboBox(Dialog)
        self.comboBox_1.setGeometry(QtCore.QRect(180, 0, 161, 31))
        self.comboBox_1.setObjectName("comboBox_1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 47, 31))
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
        self.label_6.setGeometry(QtCore.QRect(30, 110, 51, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(0, 170, 81, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(0, 190, 81, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(370, 70, 20, 321))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.CANTIDAD = QtWidgets.QLineEdit(Dialog)
        self.CANTIDAD.setGeometry(QtCore.QRect(190, 210, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CANTIDAD.setFont(font)
        self.CANTIDAD.setObjectName("CANTIDAD")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 250, 361, 91))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(460, 260, 71, 20))
        self.label_12.setObjectName("label_12")
        self.imagen = QtWidgets.QLabel(Dialog)
        self.imagen.setGeometry(QtCore.QRect(400, 80, 201, 181))
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/Sample Pictures/Jellyfish.jpg"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(420, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(380, 280, 241, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ITEM = QtWidgets.QLabel(Dialog)
        self.ITEM.setGeometry(QtCore.QRect(90, 76, 261, 20))
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
        self.ID.setGeometry(QtCore.QRect(90, 110, 261, 16))
        self.ID.setAlignment(QtCore.Qt.AlignCenter)
        self.ID.setObjectName("ID")
        self.DESCRIPCION = QtWidgets.QLabel(Dialog)
        self.DESCRIPCION.setGeometry(QtCore.QRect(90, 130, 261, 16))
        self.DESCRIPCION.setAlignment(QtCore.Qt.AlignCenter)
        self.DESCRIPCION.setObjectName("DESCRIPCION")
        self.MARCA = QtWidgets.QLabel(Dialog)
        self.MARCA.setGeometry(QtCore.QRect(90, 150, 261, 16))
        self.MARCA.setAlignment(QtCore.Qt.AlignCenter)
        self.MARCA.setObjectName("MARCA")
        self.UNMED = QtWidgets.QLabel(Dialog)
        self.UNMED.setGeometry(QtCore.QRect(90, 170, 261, 16))
        self.UNMED.setAlignment(QtCore.Qt.AlignCenter)
        self.UNMED.setObjectName("UNMED")
        self.PRECIO = QtWidgets.QLabel(Dialog)
        self.PRECIO.setGeometry(QtCore.QRect(90, 190, 261, 16))
        self.PRECIO.setAlignment(QtCore.Qt.AlignCenter)
        self.PRECIO.setObjectName("PRECIO")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        ##############################################
        self.buttonBox.accepted.connect(self.pasarinfo)
        ##############################################
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Agregar Productos"))
        self.label.setText(_translate("Dialog", "CATEGORIA  --->"))
        self.SUBCATEGORIA.setText(_translate("Dialog", "MECANICO"))
        self.label_3.setText(_translate("Dialog", "SUBCategoría ->"))
        self.label_4.setText(_translate("Dialog", "SELECCIONAR PRODUCTO ->"))
        self.label_5.setText(_translate("Dialog", "ITEM"))
        self.label_6.setText(_translate("Dialog", "ID FIDGET"))
        self.label_7.setText(_translate("Dialog", "DESCRIPCION"))
        self.label_8.setText(_translate("Dialog", "MARCA"))
        self.label_9.setText(_translate("Dialog", "UNIDAD MEDIDA"))
        self.label_10.setText(_translate("Dialog", "PRECIO"))
        self.label_11.setText(_translate("Dialog", "CANTIDAD"))
        self.CANTIDAD.setText(_translate("Dialog", "1"))
        self.label_12.setText(_translate("Dialog", "Imagen DEMO"))
        self.label_13.setText(_translate("Dialog", "AGREGAR ITEM"))
        self.ITEM.setText(_translate("Dialog", "ITEM SELECCIONADO"))
        self.ID.setText(_translate("Dialog", "ID FIDGET"))
        self.DESCRIPCION.setText(_translate("Dialog", "DESCRIPCION"))
        self.MARCA.setText(_translate("Dialog", "MARCA"))
        self.UNMED.setText(_translate("Dialog", "UNIDAD DE MEDIDA"))
        self.PRECIO.setText(_translate("Dialog", "PRECIO"))
########funciones#########
        #self.BOTONPRUEBAS.clicked.connect(self.pasarinfo)
        self.comboBox_1.currentTextChanged.connect(self.seleccionarsubc)
        self.comboBox_2.currentTextChanged.connect(self.seleccionaritem)

    def pasarinfo(self):
        print("pasarinfo")
        item=str(self.ID.text())
        cantidad=str(self.CANTIDAD.text())
        basedatos = str(self.SUBCATEGORIA.text())
        SUBCAT="items.db"
        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
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
        
    def seleccionar(self,m):
        print("seleccionar")
        print(m)
        self.SUBCATEGORIA.setText(m)
        return()

    def inicio(self):
        subcategoria=self.SUBCATEGORIA.text()
        if subcategoria== "MECANICO":
            buscar = ("""SELECT numfid, descripcion, marca, medida, subtotal, comentarios from mecanico where numfid = ? """)
            buscar_items_subc = """SELECT numfid, descripcion from mecanico where subcat = ?"""
            buscar_filtraritems = """SELECT numfid, marca, modelo from mecanico where subcat = ? """
            consultar_items="""SELECT numfid, marca, modelo from mecanico where subcat = ? """
            globals()['consultar_items'] = consultar_items
            subcat = "A"
            globals()['letraSUBCAT'] = subcat
            globals()['buscar']=buscar
            globals()['buscar_items_subc'] = buscar_items_subc
            globals()['buscar_filtraritems']=buscar_filtraritems
            self.llenarCB_SUBCAT("A")
            return()
        if subcategoria== "ELECTRICO":
            buscar = (
                """SELECT numfid, descripcion, marca, medida, subtotal, comentarios from electrico where numfid = ? """)
            buscar_items_subc = ("""SELECT numfid, descripcion from electrico where subcat = ?""")
            buscar_filtraritems = ("""SELECT numfid, marca, modelo from electrico where subcat = ? """)
            consultar_items = ("""SELECT numfid, marca, modelo from electrico where subcat = ? """)
            globals()['consultar_items'] = consultar_items
            subcat = "B"
            globals()['letraSUBCAT'] = subcat
            globals()['buscar'] = buscar
            globals()['buscar_items_subc'] = buscar_items_subc
            globals()['buscar_filtraritems']=buscar_filtraritems
            print(buscar)
            self.llenarCB_SUBCAT("B")
            return()
        if subcategoria== "SENSORES":
            buscar = (
                """SELECT numfid, descripcion, marca, medida, subtotal, comentarios from sensores where numfid = ? """)
            buscar_items_subc = ("""SELECT numfid, descripcion from sensores where subcat = ?""")
            buscar_filtraritems = ("""SELECT numfid, marca, modelo from sensores where subcat = ? """)
            consultar_items = ("""SELECT numfid, marca, modelo from sensores where subcat = ? """)
            globals()['consultar_items'] = consultar_items
            subcat = "C"
            globals()['letraSUBCAT'] = subcat
            globals()['buscar'] = buscar
            globals()['buscar_items_subc'] = buscar_items_subc
            globals()['buscar_filtraritems'] = buscar_filtraritems
            self.llenarCB_SUBCAT("C")
            return()
        if subcategoria== "CONTROL":
            buscar = (
                """SELECT numfid, descripcion, marca, medida, subtotal, comentarios from control where numfid = ? """)
            buscar_items_subc = ("""SELECT numfid, descripcion from control where subcat = ?""")
            buscar_filtraritems = ("""SELECT numfid, marca, modelo from control where subcat = ? """)
            consultar_items = ("""SELECT numfid, marca, modelo from control where subcat = ? """)
            globals()['consultar_items'] = consultar_items
            subcat = "D"
            globals()['letraSUBCAT'] = subcat
            globals()['buscar'] = buscar
            globals()['buscar_items_subc'] = buscar_items_subc
            globals()['buscar_filtraritems'] = buscar_filtraritems
            self.llenarCB_SUBCAT("D")
            return()
        if subcategoria== "ESPECIALES":
            buscar = (
                """SELECT numfid, descripcion, marca, medida, subtotal, comentarios from especiales where numfid = ? """)
            buscar_items_subc = ("""SELECT numfid, descripcion from especiales where subcat = ?""")
            buscar_filtraritems = ("""SELECT numfid, marca, modelo from especiales where subcat = ? """)
            consultar_items = ("""SELECT numfid, marca, modelo from especiales where subcat = ? """)
            globals()['consultar_items'] = consultar_items
            subcat = "E"
            globals()['letraSUBCAT'] = subcat
            globals()['buscar'] = buscar
            globals()['buscar_items_subc'] = buscar_items_subc
            globals()['buscar_filtraritems'] = buscar_filtraritems
            self.llenarCB_SUBCAT("E")
            return()
        return()
    
    def seleccionaritem(self):
        b=self.comboBox_2.currentIndex()
        vector=globals()["posvector"]
        if b==-1:
            print("negativo")
            #print(vector)
            return()
        if vector == [] :
                print("vector vacío")
                return()
        else:
                self.mostrar_ITEMS(b)
        return()
    
    def seleccionarsubc(self):
        print("def seleccionarsubc")
        CBindex1=self.comboBox_1.currentText()                
        if CBindex1==0:
            print("index CERO")
            return()
        else:
            c=self.filtraritems(CBindex1)            
        if c == 0:
            return()
        else:
            self.comboBox_2.clear()
            globals()["posvector"]=[]
            vector=globals()["posvector"]
            self.filtrar_ITEMS_subc(c[0])
            CBindex2=self.comboBox_2.currentIndex()
            self.mostrar_ITEMS(CBindex2)
                 
            
    def mostrar_ITEMS(self,filtro):
        print("def mostrar_ITEMS")
        SUBCAT="items.db"
        vector=globals()["posvector"]
        buscar=globals()['buscar']
        if vector==[]:
            print("VECTOR VACÍO EN DEF mostrar_ITEMS ")
            return()
        subcategoria=vector[filtro]
        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT=buscar#"""SELECT numfid, descripcion, marca, medida, subtotal, comentarios from mecanico where numfid = ?"""

            cursor.execute(SELECT,(subcategoria,))            
            record=cursor.fetchall()
            for row in record:
                self.ID.setText(str(row[0]))
                self.DESCRIPCION.setText(str(row[1]))
                self.MARCA.setText(str(row[2]))
                self.UNMED.setText(str(row[3]))
                self.PRECIO.setText(str(row[4]))
                self.plainTextEdit.clear()
                self.plainTextEdit.insertPlainText(str(row[5]))
            #print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                #print("Cerrando conexión de Base de Datos")
        return()    
     
    
    def filtrar_ITEMS_subc(self,filtro):
        print("def filtrar_ITEMS_subc")
        SUBCAT="items.db"
        subcategoria=filtro
        vector=globals()["posvector"]###################
        buscar_items_subc = globals()['buscar_items_subc']
        print(buscar_items_subc)
        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT=buscar_items_subc#"""SELECT numfid, descripcion from mecanico where subcat = ? """
            cursor.execute(SELECT,(subcategoria,))            
            record=cursor.fetchall()
            for row in record:
                print(row)
                escoger= row[0]+"<->"+row[1]
                a=str(escoger)
                self.comboBox_2.addItem(a)
                vector.append(row[0])
            #print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                globals()["posvector"]=vector
                #print("Cerrando conexión de Base de Datos")
        return()
    
    def filtraritems(self,filtro):
        print("def filtraritems")
        SUBCAT="items.db"
        subcategoria=filtro
        print(filtro)

        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()            
            SELECT="""SELECT ID from subcategorias where subcat = ? """
            cursor.execute(SELECT,(subcategoria,))            
            record=cursor.fetchone()            
            #print("Got INFO successfully")            
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                #print("Cerrando conexión de Base de Datos")
        return(record)
    
    
    def consultar_ITEMS(self):
        print("def consultar_ITEMS")
        SUBCAT="items.db"
        subcategoria=globals()['letraSUBCAT']#"A"
        consultar_items=globals()['consultar_items']
        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            SELECT=consultar_items#"""SELECT numfid, marca, modelo from mecanico where subcat = ? """
            cursor.execute(SELECT,(subcategoria,))            
            record=cursor.fetchall()
            for row in record:                
                a=str(row)
                self.comboBox_2.addItem(a)                           
            #print("Got INFO successfully")            
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                #print("Cerrando conexión de Base de Datos")
        return(record)


    def llenarCB_SUBCAT(self,indice):
        print("llenarCB_SUBCAT")
        SUBCAT="items.db"
        vectorsubcat=globals()["vectorsubcategoria"]
        subcategoria=indice
        try:
            sqliteConnection=sqlite3.connect(SUBCAT)
            cursor = sqliteConnection.cursor()
            
            SELECT="""SELECT subcat from subcategorias
                    where clase = ?
                    """
            cursor.execute(SELECT,subcategoria)
            
            record=cursor.fetchall()
            for row in record:                
                a=str(row[0])
                self.comboBox_1.addItem(a)
                vectorsubcat.append(a)                
            #print("Got INFO successfully")
            cursor.close
        except sqlite3.Error as error:
            print("Error, ALV -----> ", error)
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                #print("Cerrando conexión de Base de Datos")
        return()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

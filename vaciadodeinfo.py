import openpyxl
import os
from openpyxl.drawing.image import Image
import excel2img

link =os.path.dirname(os.path.abspath(__file__))
def llenarformato(vectorencabezado):
    print("TOMANDO VARIABLES")
    #########################################################
    ######### VARIABLES GLOBALES PARA FUNCION ###############
    #########################################################
    anio = vectorencabezado[0][0]#LISTO
    mes = vectorencabezado[0][1]#LISTO
    dia = vectorencabezado[0][2]#LISTO
    numcotizacion = vectorencabezado[1]
    numtienda = vectorencabezado[2]#LISTO
    infotienda = vectorencabezado[3]#LISTO
    direccion = infotienda[0]+'-'+infotienda[1]+'-'+infotienda[2]#LISTO
    TE = vectorencabezado[4]#LISTO
    notas = vectorencabezado[5]#LISTO
    garantias = vectorencabezado[6]#LISTO
    quiencotiza = vectorencabezado[7] #IMPROVISADO
    titulo = vectorencabezado[8]#LISTO
    lista = vectorencabezado[9]  #IMPROVISADO
    ncelda = vectorencabezado[10]#LISTO
    
    #########################################################
    print("TOMANDO EXCEL")
    os.chdir(link)
    archivo=openpyxl.load_workbook(link + '/template.xlsx') #obtener ruta archivo con nombre del archivo
    caratula=archivo.get_sheet_by_name('PARTE 1 CARATULA')
    desglose1=archivo.get_sheet_by_name('PARTE 2 DESGLOSE')
    desglose2=archivo.get_sheet_by_name('PARTE 3 DESGLOSE')
    #########################################
    #ENCABEZADO
    #########################################
    print("COLOCANDO ENCABEZADOS")
    caratula['H8'].value= dia  #DIA
    caratula['I8'].value= mes  #MES
    caratula['J8'].value= anio #AÑO
    caratula['I13'].value= numcotizacion  #"699-SOR-19620-C-XXX"# NUMERO DE COTIZACIÓN
    caratula['C16'].value= numtienda #"699"# NUMERO DE TIENDA
    caratula['D16'].value= direccion #"SALIDA ZACATECAS POR COSTCO"# TIEMPO ENTREGA
    caratula['I16'].value= TE #"1 SEMANA"# TIEMPO ENTREGA
    #########################################
    #ENCABEZADO
    #########################################
    #########################################
    #PIE DE CARATULA
    #########################################
    print("COLOCANDO PIE DE PAGINA")
    caratula['B54'].value = notas # NOTAS O COMENTARIOS
    caratula['E64'].value = garantias#"HEHEHE NO HAY GARANTÍA HEHEHE"#CONDICIONES DE GARANTÍA
    caratula['D72'].value = quiencotiza[0] #"Cristian" #QUIEN REALIZA COTIZACIÓN
    caratula['E72'].value = quiencotiza[1] #"1234567890" #TELEFONO DE QUIEN REALIZA COTIZACION
    caratula['G72'].value = quiencotiza[2] #"CORREO.FIDGET@GMAIL.COM" #CORREO QUIEN COTIZA
    #########################################
    #PIE DE CARATULA
    #########################################

    # ***************************************************************************************************
    #########################################
    # CUERPO DE COTIZACIÓN
    #########################################
    # TITULO ES RESERVADO PARA LA PRIMERA PARTIDA
    print("ARMANDO COTIZACION")
    caratula['C20'].value = "S/C"  # NUMERO INTERNO SORIANA
    caratula['D20'].value = titulo # NUMERO INTERNO SORIANA
    # LLENAR PARTIDAS DEL 2 AL 30
    x=int(len(ncelda))
    for i in range(x):
        caratula[ncelda[i][0]].value =  lista[i][0]   # NUMERO INTERNO SORIANA
        caratula[ncelda[i][1]].value =  lista[i][1]   # "PLC DELTA DE 8IN / 4 OUT"  # DESCRIPCION
        caratula[ncelda[i][2]].value =  lista[i][2]   # MARCA
        caratula[ncelda[i][3]].value =  lista[i][3]   # MODELO/CLAVE
        caratula[ncelda[i][4]].value =  lista[i][4]   # CANTIDAD
        caratula[ncelda[i][5]].value =  lista[i][5]   # UNIDAD DE MEDIDA
        caratula[ncelda[i][6]].value =  lista[i][6]   # PRECIO UNITARIO
    #########################################
    # CUERPO DE COTIZACIÓN
    #########################################
    # ***************************************************************************************************
    #########################################
    # insertar el logo de Fidget
    #########################################
    print("INGREANDO IMAGEN")
    img = Image(link + '/LogoFIDGETreducido.png')
    img2 = Image(link + '/LogoFIDGETreducido.png')
    img3 = Image(link + '/LogoFIDGETreducido.png')
    caratula.add_image(img, 'C2')
    desglose1.add_image(img2, 'C2')
    desglose2.add_image(img3, 'C2')
    #########################################
    # insertar el logo de Fidget
    #########################################
    print("TOMANDO LINKS PARA GUARDAD")
    pathtosavexml = (link +'/COTIZACIONES/' + numcotizacion + '.xlsx')
    pathtosaveimage=(link +'/COTIZACIONES/')
    print("GUARDANDO ARCHIVO")
    archivo.save(pathtosavexml)  # GUARDAR ARCHIVO
    excel2img.export_img(pathtosavexml, (pathtosaveimage + numcotizacion +".png"), "PARTE 1 CARATULA", None)  # GENERAR imagen de la cotizacion
    print("**********************************ready alv")
    #exit()
    return

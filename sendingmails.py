
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def enviarmail(vectordestinatarios,asunto,cuerpotexto,numcotizacion):
        print("INCIANDO*script para mandar correos")

        email_user='Bot_email@email.com'
        pass_user='PASSWORD'
        destinatarios=vectordestinatarios
        asunto='Cotización FIDGET:' + asunto #'Cotización FIDGET: suministro refacciones'
        #REDACTANDO CORREO

        textoredactado=cuerpotexto
        #"""
        #Esto es un correo de prueba desde python.!

        #Aquí se da un salto de línea y tiene acentos
        #"""

        firma="""
_____________________
_____________________
FAVOR DE NO RESPONDER A ESTA DIRECCIÓN DE CORREO, ESTE ES ADMINISTRADO POR UN ROBOT PARA EL ENVÍO DE COTIZACIONES GENERADOS POR PARTE DEL EQUIPO DE GRUPO FIDGET SA DE CV.
SÍ LLEGÓ ESTE CORREO POR ERROR, FAVOR DE REPORTAR A LA COMPAÑÍA Y/O HACER CASO OMISO A ÉSTE.
¡GRACIAS!
        
ATTE: ASISTENTE ELECTRÓNICO DE GRUPO FIDGET SA DE CV.
"""
        #concatenando el cuerpo del correo
        cuerpocorreo=textoredactado + firma

        #construir encabezado del correo
        msg=MIMEMultipart()
        msg["From"]=email_user
        msg["To"]=",".join(destinatarios)#destinatarios
        msg["Subject"]=asunto
        msg.attach(MIMEText(cuerpocorreo,'plain'))

        #agregando el archivo en XLSX
        rutanombrearchivo='COTIZACIONES/'+ numcotizacion + '.xlsx'#+ '123-15122019-CV-2'+'.xlsx'
        nombre1=numcotizacion + '.xlsx'#'123-15122019-CV-2'+'.xlsx'
        attachment=open(rutanombrearchivo,'rb')
        part=MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+nombre1)
        msg.attach(part)

        #agregando el archivo en PNG
        #numcotizacion
        rutanombrearchivo2='COTIZACIONES/'+ numcotizacion + '.png' #'123-15122019-CV-2'+'.png'
        nombre2=numcotizacion + '.png'#'123-15122019-CV-2'+'.png'
        attachment2=open(rutanombrearchivo2,'rb')
        part2=MIMEBase('application','octet-stream')
        part2.set_payload((attachment2).read())
        encoders.encode_base64(part2)
        part2.add_header('Content-Disposition',"attachment; filename= "+nombre2)
        msg.attach(part2)

        # se pasa todo a texto para enviarlo por correo
        text=msg.as_string()

        #parametros de inicio de servidor seguro
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        #loogeandose en correo
        server.login(email_user,pass_user)
        #comando para enviar correo
        server.sendmail(email_user,destinatarios,text)
        #cerrar servidor
        server.quit()
        print("listo y enviado EXITO ALV!!!")
        return()

#print("pruebas de funcion para enviar correo")




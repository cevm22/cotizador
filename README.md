# cotizador

Este proyecto fue diseñado internamente para la asistencia de creación, envío y seguimiento de cotizaciones para un cliente en específico, debido a que este cliente presentaba el 80% de las cotizaciones y de tiempo enfocado para su atención.

Lo cual mediante una interfaz hecha con PYQT5 se conecta a una base de datos local con SQL-lite y permite generar cotizaciones con un template estandar por parte del cliente en .xls y es procesada por medio de sus servidores, lo convierte en PNG y PDF para que el usuario pueda verlo de una manera rápida (ya que no todos los usuarios contaban con la paquetería Office), después esta cotización es enviada automaticamente por medio de la API de Gmail dirigida al usuario final, con copia a la administracion y supervisores, finalmente se agregaba una tarea en ASANA por medio de su API tageando a los responsables para poder dar seguimiento.

Al mismo tiempo, este proyecto apoyaba en el seguimiento de documentación para la solicitud de pago por parte del cliente, en donde permitia generar una carpeta por Orden de Compra realizada y almacenaba los documentos necesarios (con un sistema de comentarios para notas adicionales) para posteriormente entregarlos como evidencia al cliente y dar por finalizada la Orden de compra.

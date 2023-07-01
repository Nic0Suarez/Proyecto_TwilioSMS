# Proyecto_TwilioSMS
Proyecto de Consulta de Clima y Notificaciones Programadas
Este proyecto consiste en consultar la información climática de una ubicación utilizando una API de clima y enviar mensajes informativos sobre el clima a través de Twilio. Además, se utiliza Ubuntu y se establece una conexión con EC2 para enviar notificaciones programadas.

Funcionalidades
Consulta de Clima: El proyecto utiliza una API de clima para obtener información actualizada sobre las condiciones climáticas de una ubicación específica. La información incluye datos como temperatura, humedad, velocidad del viento, entre otros.

Envío de Mensajes de Clima: Utilizando Twilio, el proyecto envía mensajes de texto o notificaciones informando sobre el clima de la ubicación consultada. Estos mensajes pueden ser programados para enviarse en momentos específicos o enviarse inmediatamente después de la consulta.

Notificaciones Programadas en EC2: Mediante el uso de Ubuntu y la conexión con EC2 (Amazon Elastic Compute Cloud), el proyecto permite programar notificaciones de clima para ser enviadas en momentos específicos. Esto proporciona la capacidad de recibir actualizaciones regulares sobre el clima en un horario predefinido.

Tecnologías Utilizadas
API de Clima: Se utiliza una API de clima para obtener los datos climáticos de la ubicación deseada. Esto implica hacer solicitudes HTTP a la API, procesar la respuesta y extraer la información relevante.

Twilio: La integración con Twilio permite enviar mensajes de texto o notificaciones a través de SMS o aplicaciones de mensajería. Esto se utiliza para enviar información sobre el clima obtenida desde la API a través de mensajes.

Ubuntu y EC2: Se utiliza Ubuntu como sistema operativo y se establece una conexión con EC2, que es un servicio de Amazon Web Services (AWS), para programar y enviar notificaciones de clima en momentos específicos.

Instrucciones de Configuración y Uso
Clona el repositorio a tu máquina local.
Configura las credenciales de acceso a la API de clima y Twilio en el archivo de configuración correspondiente.
Configura la conexión con EC2 en Ubuntu, estableciendo las credenciales y la programación de notificaciones deseadas.
Ejecuta el proyecto y realiza consultas de clima utilizando comandos específicos.
Recibe mensajes o notificaciones con información actualizada sobre el clima utilizando Twilio.
Programa notificaciones de clima en EC2 para recibir actualizaciones regulares según lo configurado.

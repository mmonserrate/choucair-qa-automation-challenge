# choucair-qa-automation-challenge

Tecnologías implementadas:
 ◦ Python v3.9.6
 ◦ pip v21.1.3
 ◦ Behave v1.2.6
 ◦ selenium v4.23.1
 
 Instalacion
 Descargar e instalar el interprete de python desde el siguiente link:
  https://www.python.org/downloads/
  Seguir las instrucciones de intalación - version probada en desarrollo: 3.9.6

Instalar el manejador de paquetes PIP siguiendo el tutorial de instalación desde:

https://pip.pypa.io/en/stable/installation/

Corriendo las pruebas localmente
Clonar el proyecto desde gitlab (Requiere tener git instalado - https://git-scm.com/downloads)
  git clone https://github.com/mmonserrate/choucair-qa-automation-challenge.git

Ir al directorio de fuentes del proyecto
  cd choucair-qa-automation-challenge/src

Moverse al branch master
  git checkout master

Instalar behave
pip install behave

Instalar selenium
pip install selenium

Instalar las bibliotecas de Python requeridas por el proyecto
pip download -r requirements.txt

Para correr las pruebas se debe ejecutar el siguiente comando:
  $ python test_choucair_challenge.py --browser [chrome|firefox|safari] --feature  [Login|RegistrarCandidato|Todos]

Donde browser es nombre del browser donde se desea correr la prueba y feature es el nombre del feature. Los valores posibles son:
* browser
  ◦ chrome
  ◦ firefox
  ◦ safari (Disponible sólo para MacOS)

* feature
  ◦ Login -> Login de Usuario
  ◦ Registrar Candidato -> Registro  de nuevo candidato
  ◦ All -> Se ejecutan las pruebas de ambos features

* Examples:
  $ python test_choucair_challenge.py --browser chrome --feature SignUp
  $ python test_choucair_challenge.py --browser firefox --feature All

Features y casos considerados en estas pruebas
1. Login de Usuario:
◦ El usuario debe poder loguearse con el nombre de usuario y la contraseña registrados
◦ El formulario no debe ser enviado hasta que todos los campos obligatorios estén correctos
◦ Al ingresar a la plataforma, debe mostrarse la pagina principal de OrangeHRM con las opciones del menú disponibles para el usuario

Registro de Usuario:
◦ El formulario debe permitir registrar un candidato con los sigueintes datos: Primer Nombre, Segundo Nombre y Apellido, Vacante, Correo electrónico, Número de contacto, Currículum Vitae, Palabras clave, Fecha de la solicitud, Comentarios - Notas y clic en la casilla de verificación.
◦ El formulario debe peprmitir hacer cambio de estado hasta completar a Hired
◦ El formulario debe permitir actualizar el estado a: Application Initiated y seleccionar el candidato
◦ El formulario debe permitir actualizar el estado a: Shortlisted y programar entrevista
◦ El formulario debe permitir actualizar el estado a: Interview Scheduled
◦ El formulario debe permitir actualizar el estado a: Interview Passed 
◦ El formulario debe permitir actualizar el estado a: Job Offered
◦ El formulario debe permitir actualizar el estado a: Status: Hired
◦ El formulario no debe ser enviado hasta que todos los campos obligatorios estén completos
◦ El formulario debe mostrar mensajes si alguno de los campos presenta error
◦ El formulario debe mostrar menajes al completar una acción satisfactoria

Historia de Uusairo:
Se incluye archivo .pdf con dos historias de usuarios asociadas a las pruebas automatizadas

Casos de prueba
Se incluyen los siguientes archivos como parte de la ejecución de las pruebas funcionales y automatizadas:

Autor:
mmonserrate

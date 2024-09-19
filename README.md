# choucair-qa-automation-challenge

Tecnologías implementadas:
Python v3.9.6
pip v21.1.3
Behave v1.2.6
selenium v4.23.1
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
browser
chrome
firefox
safari (Disponible sólo para MacOS)

feature
Login -> Login de Usuario
Registrar Candidato -> Registro  de nuevo candidato
All -> Se ejecutan las pruebas de ambos features

Examples:
  $ python test_choucair_challenge.py --browser chrome --feature SignUp
  $ python test_choucair_challenge.py --browser firefox --feature All

Features y casos considerados en estas pruebas
Registro de Usuario:
El formulario debe permitir registrar un usuario con nombre, email y una contraseña.
El campo de nombre debe contener mínimo 2 palabras (primer nombre y apellido).
El email debe cumplir con el estándar de una dirección de correo electrónico y ser único en la base de datos.
La contraseña debe tener al menos 8 caracteres, incluyendo una mayúscula, una minúscula, un número y un carácter especial.
El formulario no debe ser enviado hasta que todos los campos obligatorios estén completos.
La contraseña debe ser ingresada dos veces y el sistema debe informar al usuario si ambas coinciden.

Login de Usuario:
El usuario debe poder loguearse con el email y la contraseña registrados.
El formulario de login no debe ser enviado hasta que todos los campos estén diligenciados.
Al ingresar a la plataforma, debe mostrarse el nombre del usuario.
La plataforma debe permitir al usuario cerrar la sesión.

Historia de Uusairo:
Se incluye archivo .pdf con dos historias de usuarios asociadas a las pruebas automatizadas

Casos de prueba
Se incluyen los siguientes archivos como parte de la ejecución de las pruebas funcionales y automatizadas:

Autor: mmonserrate


# Choucair: Prueba técnica para QA Automation Engineer

Este Challenge es parte del proceso de selección para QA Automation Engineer en Choucair

## Tecnologías implementadas:
* Python v3.9.6
* pip v21.1.3
* Behave v1.2.6
* selenium v4.23.1



## Instalacion

Descargar e instalar el interprete de python desde el siguiente link:

```bash
  https://www.python.org/downloads/
  Seguir las instrucciones de intalación - version probada en desarrollo: 3.9.6
```

Instalar el manejador de paquetes PIP siguiendo el tutorial de instalación desde:

```bash
https://pip.pypa.io/en/stable/installation/
```



## Corriendo las pruebas localmente

Clonar el proyecto desde gitlab utilizando cualquier consola de comandos (Requiere tener git instalado - https://git-scm.com/downloads)

```bash
  git clone https://github.com/mmonserrate/choucair-qa-automation-challenge.git
```

Ir al directorio de fuentes del proyecto 

```bash
  cd choucair-qa-automation-challenge/src
```
Moverse al branch main

```bash
  git checkout main
```

Instalar las bibliotecas y dependencias de Python requeridas por el proyecto

```bash
pip download -r requirements.txt
```

Para correr las pruebas se debe ejecutar el siguiente comando:
```bash
  $ python test_choucair_challenge.py --browser [chrome|firefox|safari] --feature  [Login|RegistrarCandidato|Todos]
```
Donde browser es nombre del browser donde se desea correr la prueba y feature es el nombre del feature objeto de la prueba. Los valores posibles son:
* browser
  - chrome
  - firefox
  - safari (Disponible sólo para MacOS)
* feature
  - Login -> Ingreso de Usuario al sistema
  - RegistrarCandidato -> Registrar candidato en la plataforma
  - Todos -> Se ejecutan las pruebas de ambos features

**Ejemplos:**

```bash
  $ python test_choucair_challenge.py --browser chrome --feature RegistrarCandidato
```
```bash
  $ python test_choucair_challenge.py --browser firefox --feature Todos
```

## Features y casos considerados en estas pruebas 
1. **Login de Usuario:**
    - El usuario debe poder loguearse con el nombre de usuario y la contraseña registrados
    - El formulario no debe ser enviado hasta que todos los campos obligatorios estén correctos
    - Al ingresar a la plataforma, debe mostrarse la pagina principal de OrangeHRM con las opciones del menú disponibles para el usuario
2. **Registrar candidato:**
    - El formulario debe permitir registrar un candidato con los sigueintes datos: 
      - Primer Nombre, Segundo Nombre y Apellido 
      - Vacante 
      - Correo electrónico 
      - Número de contacto 
      - Currículum Vitae 
      - Palabras clave 
      - Fecha de la solicitud
      - Comentarios
      - Notas
   - Luego de ingresar todos los datos se debe activar la casilla de verificacíon para el consentimiento y tratamiento de datos.
   - Hacer clic en guardar para almacenar los datos del candidato.
   - Actualizar estado "Shortlisted" haciendo click en el botón "Shortlist"
   - En el siguiente formulario "Shortlist Candidate", agregar una nota.
   - Click en guardar
   - En la pantalla "Application Stage" hacer click en el botón "Schedule Interview"
   - Registrar los datos requeridos en el formulario "Schedule Interview"
   - Clic en guardar
   - Nuevamente en la pantalla "Application Stage" hacer click en el botón "Mark Interview Passed"
   - En el siguiente formulario "Mark Interview Passed", agregar una nota.
   - Clic en guardar
   - Una vez mas en la pantalla "Application Stage" hacer click en el botón "Offer Job"
   - En el siguiente formulario "Offer Job", agregar una nota.
   - Clic en guardar
   - Por ultimo en la pantalla "Application Stage" hacer click en el botón "Hire"
   - En el siguiente formulario "Hire Candidate", agregar una nota.
   - Clic en guardar
   - El status final de la aplicación debe ser "Status: Hired"

## Historias de Usuario
Se incluye un archivo .pdf con las siguientes historias de usuarios asociadas a las pruebas automatizadas
* Inicio de sesión
* Contratación de nuevo empleado

## Autor

- [@mmonserrate](https://www.github.com/mmonserrate)
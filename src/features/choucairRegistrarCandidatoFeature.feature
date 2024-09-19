# Creado por Maria Monserrate. Fecha: 18/09/2024
Feature: Inicio de sesión de usuario registrado previamente
  Este feature es parte del challenge tecnico como parte del proceso de seleccion de Choucair
  Background:
    Given Browser seleccionado
    Then Abrir la pagina principal de OrangeHRM en el browser seleccionado

  Scenario: Registrar nuevo candidato
    When Ingresar "Admin" en el campo "Username" en Login
    And Ingresar "admin123" en el campo "Password"
    Then Click en el boton "Login"
    Then El usuario Hace clic en la opción "Reclutamiento"
    Then Hacer clic en la opcion Add
    Then Ingresar el primer nombre: Manuel
    And Ingresar el segundo nombre: Carlos
    And ingresar apellido: Lino
    And Seleccionar una vacante: Payroll Administrator
    And Ingresar correo electrónico: luis.lopez@example.com
    And Ingresar número de contacto: 3054789762
    And Adjuntar hoja de vida del candidato
    And Agregar palabras claves: Lider, Calidad, OrangeHRM, Selenium
    And Agregar observación: Candidato con experiencia en pruebas manuales y automatizadas
    And Hacer clic en la casilla de verificación de consentimiento de data
    Then Hacer clic en el boton 'guardar'
    Then Hacer clic en el boton listacorta
    And Agregar comentario acerca del candidato: Posee buen perfil
    Then Hacer clic en el botón 'guardar' para continuar
    Then Hacer clic en el boton 'programar entrevista'
    Then Agregar un titulo para a entrevista: Entrevista a candidato 1 con el cliente
    And Agregar el nombre del entrevistador: Amelia  Brown
    And Agregar fecha de la entrevista: 2024-09-24
    And Agregar hora de la entrevista: 09:00 AM
    And Agregar notas para la entrevista: Candidato con buen perfil
    Then Hacer clic en el boton 'guardar' y continuar con el proceso
    Then Hacer clic en el botón: 'Marcar entrevista aprobada'
    Then Agregar notas de la entrevista realizada: Candidato aprobado para el cargo seleccionado
    And Hacer clic en el boton 'guardar' y avanzar en el proceso
    Then Hacer clic en el botón 'oferta de trabajo'
    Then Agregar notas acerca de la oferta de trabajo: Candidato aprobado
    And Hacer clic en el boton 'guardar' para continuar con el proceso
    Then Hacer clic en el boton 'contratar'
    Then Agregar notas finales del candidato a contratar: Candidato con mucha experiencia
    And Hacer clic en el boton 'guardar' para finalizar con el proceso
    Then Validar que el estado final del candidato sea: Status: Hired
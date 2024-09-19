# Created by Maria Monserrate at 18/09/2024
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
    Then Hacer clic en el boton guardar
    Then Hacer clic en el boton listacorta
    And Agregar comentario acerca del candidato: Posee buen perfil
    Then Hacer clic en el botón 'guardar'
    Then Hacer clic en el boton 'programar entrevista'
    Then Agregar un titulo para a entrevista: Entrevista a candidato 1 con el cliente
    And Seleccionar el nombre del entrevistador: Amelia  Brown
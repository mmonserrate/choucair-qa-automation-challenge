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
    Then Ingresar el primer nombre: Luis
    And Ingresar el segundo nombre: Carlos
    And ingresar apellido: Lino
    And Seleccionar una vacante: Senior QA Lead
    And Ingresar correo electrónico: luis.lopez@example.com
    And Ingresar número de contacto: 3054789772
#    And Adjuntar hoja de vida: 'https://drive.google.com/file/d/1pzopm-uJJrH-fOxys6w--CSz6R3IJWf8/view?usp=drive_link'
#    And Agregar palabras claves: Lider, Calidad, OrangeHRM
#    And Agregar observación: Candidato disponible
#    And Hacer clic en la casilla de verificación de consentimiento de data.
#

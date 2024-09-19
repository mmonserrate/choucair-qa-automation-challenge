# Creado por Maria Monserrate. Fecha: 18/09/2024
Feature: Inicio de sesión de usuario registrado previamente
  Este feature es parte del challenge tecnico como parte del proceso de seleccion de Choucair
  Background:
    Given Browser seleccionado
    Then Abrir la pagina principal de OrangeHRM en el browser seleccionado

  Scenario: Login de usuario - Login de usuario con datos validos
    When Ingresar "Admin" en el campo "Username" en Login
    And Ingresar "admin123" en el campo "Password"
    Then Click en el boton "Login"
    Then Validar que ingrese a la pagina principal "OrangeHRM" en la url "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

  Scenario: Login de usuario - Login de usuario con datos invalidos
    When Ingresar "Admins" en el campo "Username" en Login
    And Ingresar "Ladmin1234" en el campo "Password"
    Then Click en el boton "Login"
    Then Validar mensaje mostrado al usuario: Invalid credentials

# Created by Maria Monserrate at 18/09/2024
Feature: Inicio de sesión de usuario registrado previamernte
  Este feature es parte del challenge tecnico como parte del proceso de seleccion de Choucair
  Background:
    Given Browser seleccionado
    Then Abrir la pagina principal de OrangeHRM  en el browser seleccionado

  Scenario: Login de usuario - Login de usuario con datos validos
    When Ingresar "Admin" en el campo "Username" en Login
    And Ingresar "admin123" en el campo "Password"
    Then Click en el boton "Login"
    Then Redirigir a la pagina / Dashboard "OrangeHRM" en la url "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/indexl"

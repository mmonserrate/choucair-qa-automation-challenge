# Creado por Maria Monserrate. Fecha: 18/09/2024
import time

import driver
import self
from behave import *
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@given("Browser seleccionado")
def test_define_browser_driver(context):
    if context.config.userdata.get('browser') == "chrome":
        context.options = webdriver.ChromeOptions()
        # Agregar esta opcion a chromeoptions para evitar problemas de certificados
        context.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # Agregar esta opcion para evitar problemas al abrir/cerrar pestanas o ventanas
        context.options.add_argument("--disable-blink-features=AutomationControlled")
        context.driver = webdriver.Chrome(options=context.options)
        context.driver.maximize_window()

    elif context.config.userdata.get('browser') == "firefox":
        context.options = webdriver.FirefoxOptions()
        # Agregar esta opcion para evitar problemas al abrir/cerrar pestanas o ventanas
        context.options.add_argument("--disable-blink-features=AutomationControlled")
        context.driver = webdriver.Firefox(options=context.options)

    elif context.config.userdata.get('browser') == "safari":
        context.options = webdriver.SafariOptions()
        # Agregar esta opcion para evitar problemas al abrir/cerrar pestanas o ventanas
        context.options.add_argument("--disable-blink-features=AutomationControlled")
        context.options = webdriver.Safari(options=context.options)


@then("Abrir la pagina principal de OrangeHRM en el browser seleccionado")
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    # Se agrega una espera activa para dar oportunidad al browser de cargar la pagina completamente, incluyendo xpaths
    context.driver.implicitly_wait(30)
    time.sleep(5)

@when('Ingresar "{user}" en el campo "Username" en Login')
def step_impl(context, user):
    ((context.driver.find_element(By.NAME, "username"))
     .send_keys(user))
    time.sleep(3)


@step('Ingresar "{user_password}" en el campo "Password"')
def step_impl(context, user_password):
    ((context.driver.find_element(By.NAME, "password"))
     .send_keys(user_password))
    time.sleep(2)


@then('Click en el boton "Login"')
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
     .click())
    time.sleep(4)


@then('Validar que ingrese a la pagina principal "OrangeHRM" en la url "{url_orange}"')
def step_impl(context, url_orange):
    time.sleep(2)
    get_url = context.driver.current_url
    if get_url == url_orange:
        assert True
    else:
        assert False


@then('Validar mensaje mostrado al usuario "{error_login}"')
def step_impl(context):
    (context.driver.find_element(
        By.CLASS_NAME, "oxd-alert-content oxd-alert-content--error")
     .click())
    time.sleep(10)

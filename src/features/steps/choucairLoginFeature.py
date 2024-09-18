# Created by Maria Monserrate at 18/09/2024
import time
from behave import *
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By


@when('Ingresar "{user}" en el campo "Username" en Login')
def step_impl(context, user):
    (context.driver.find_element(By.NAME, 'username'))
    time.sleep(2)


@step('Ingresar "{user_password}" en el campo "Password"')
def step_impl(context, user_password):
    (context.driver.find_element(By.NAME, 'password'))
    time.sleep(2)


@then('Click en el boton "Login"')
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
     .click())
    time.sleep(2)


@then('Redirigir a la pagina principal de "OrangeHRM"{welcome_url}"')
def step_impl(context, welcome_url):
    time.sleep(2)
    get_url = context.driver.current_url
    if get_url == welcome_url:
        assert True
    else:
        assert False


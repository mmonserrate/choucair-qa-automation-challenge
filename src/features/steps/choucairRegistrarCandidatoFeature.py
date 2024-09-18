# Creado por Maria Monserrate. Fecha: 18/09/2024
import time
import driver
import self
from behave import *
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@then('El usuario Hace clic en la opción "Reclutamiento"')
def step_impl(context):
    (context.driver.find_element(
        By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a")
     .click())
    time.sleep(3)

@then("Hacer clic en la opcion Add")
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    .click())
    time.sleep(4)

@then("Ingresar el primer nombre: {primer_nombre}")
def step_impl(context, primer_nombre):
    ((context.driver.find_element(By.NAME, "firstName"))
     .send_keys(primer_nombre))
    time.sleep(2)


@step("Ingresar el segundo nombre: {segundo_nombre}")
def step_impl(context, segundo_nombre):
    ((context.driver.find_element(By.NAME, "middleName"))
     .send_keys(segundo_nombre))
    time.sleep(2)


@step("ingresar apellido: {apellido}")
def step_impl(context, apellido):
    ((context.driver.find_element(By.NAME, "lastName"))
     .send_keys(apellido))
    time.sleep(2)


@step("Seleccionar una vacante: {vacante}")
def step_impl(context, vacante):
    ((context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div"))
     .send_keys(vacante))
    time.sleep(2)
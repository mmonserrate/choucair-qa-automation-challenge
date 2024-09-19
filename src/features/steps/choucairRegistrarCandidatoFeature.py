# Creado por Maria Monserrate. Fecha: 18/09/2024
import os
import time
import driver
import self
from behave import *
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('El usuario Hace clic en la opción "Reclutamiento"')
def step_impl(context):
    (context.driver.find_element(
        By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a")
     .click())
    time.sleep(1)

@then("Hacer clic en la opcion Add")
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    .click())
    time.sleep(1)

@then("Ingresar el primer nombre: {primer_nombre}")
def step_impl(context, primer_nombre):
    ((context.driver.find_element(By.NAME, "firstName"))
     .send_keys(primer_nombre))
    time.sleep(1)


@step("Ingresar el segundo nombre: {segundo_nombre}")
def step_impl(context, segundo_nombre):
    ((context.driver.find_element(By.NAME, "middleName"))
     .send_keys(segundo_nombre))
    time.sleep(1)


@step("ingresar apellido: {apellido}")
def step_impl(context, apellido):
    ((context.driver.find_element(By.NAME, "lastName"))
     .send_keys(apellido))
    time.sleep(1)


@step("Seleccionar una vacante: {vacante}")
def step_impl(context, vacante):
    WebDriverWait(context.driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
            "div[class='oxd-select-text oxd-select-text--active']"))).click()

    WebDriverWait(context.driver, 3).until(
        EC.element_to_be_clickable((By.XPATH,
            "//div[@role='listbox']//div[@role='option']//span[contains(text(),'" + vacante + "')]"))).click()
    time.sleep(2)


@step("Ingresar correo electrónico: {email}")
def step_impl(context, email):
    (context.driver.find_element(
        By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
     .send_keys(email))
    time.sleep(1)


@step("Ingresar número de contacto: {contacto}")
def step_impl(context, contacto):
    (context.driver.find_element(
        By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input')
     .send_keys(contacto))
    time.sleep(1)


# @step("Adjuntar hoja de vida: 'https://drive.google.com/file/d/1pzopm-uJJrH-fOxys6w--CSz6R3IJWf8/view?usp=drive_link'")
# def step_impl(context):
# #    upload_element = context.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div/div[2]/div/div[1]')
# # Wait for the page to load
#     WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div/div[2]/div/div[1]')))
#
#     # Create a hidden file input element using JavaScript
#     context.driver.execute_script("""
#             var input = document.createElement('input');
#             input.type = 'file';
#             input.style.display = 'none';
#             document.body.appendChild(input);
#         """)
#
#     # Prepare the file path
#     file_path = os.path.abspath('C:\\proyectos\\choucair-qa-automatization-challenge\\src\\requirements.txt')
#
#     # Use JavaScript to set the file input's value and trigger change
#     context.driver.execute_script("arguments[0].value = arguments[1];",
#                           context.driver.find_element(By.CSS_SELECTOR, "input[type='file']"), file_path)
#
#     # Trigger change event
#     context.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));",
#                           context.driver.find_element(By.CSS_SELECTOR, "input[type='file']"))
#
#     # Add any additional steps here, like clicking a submit button if necessary
#
#     # Wait to see the result (you may need to adjust this)
#     time.sleep(5)
#
#     # context.driver.find_element(
#     #     By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div/div[2]/div/div[1]').click()
#     # time.sleep(5)
@step("Agregar palabras claves: {palabras_claves}")
def step_impl(context, palabras_claves):
    (context.driver.find_element(
        By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[1]/div/div[2]/input')
     .send_keys(palabras_claves))
    time.sleep(1)


@step("Agregar observación: {nota}")
def step_impl(context, nota):
    (context.driver.find_element(
        By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea')
     .send_keys(nota))
    time.sleep(1)


@step("Hacer clic en la casilla de verificación de consentimiento de data")
def step_impl(context):
    (context.driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/div/div/div/div[2]/div/label/span')
    .click())
    time.sleep(2)


@then("Hacer clic en el boton guardar")
def step_impl(context):
    (context.driver.find_element(
    By. XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]')
    .click())
    time.sleep(5)
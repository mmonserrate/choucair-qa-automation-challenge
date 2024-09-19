# Creado por Maria Monserrate. Fecha: 18/09/2024
import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
import os


@then('El usuario Hace clic en la opción "Reclutamiento"')
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a")
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
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
     .send_keys(email))
    time.sleep(1)


@step("Ingresar número de contacto: {contacto}")
def step_impl(context, contacto):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input')
     .send_keys(contacto))
    time.sleep(1)


@step("Adjuntar hoja de vida del candidato")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div['
                                                                                      '2]/div[2]/div/div/form/div['
                                                                                      '4]/div/div/div/div/div['
                                                                                      '2]/div/div[1]'))).click()
    time.sleep(1)
    current_working_directory = os.getcwd()
    keyboard = Controller()
    keyboard.type(current_working_directory + "\\documento-prueba.pdf")
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)


@step("Agregar palabras claves: {palabras_claves}")
def step_impl(context, palabras_claves):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[1]/div/div[2]/input')
     .send_keys(palabras_claves))
    time.sleep(1)


@step("Agregar observación: {nota}")
def step_impl(context, nota):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea')
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
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]')
     .click())
    time.sleep(1)


@then("Hacer clic en el boton listacorta")
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]')
     .click())
    time.sleep(4)


@step("Agregar comentario acerca del candidato: {comentario}")
def step_impl(context, comentario):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea')
     .send_keys(comentario))
    time.sleep(1)


@then("Hacer clic en el botón 'guardar'")
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')
     .click())
    time.sleep(2)


@then("Hacer clic en el boton 'programar entrevista'")
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]')
     .click())
    time.sleep(2)


@then("Agregar un titulo para a entrevista: {tiulo_entrevita}")
def step_impl(context, tiulo_entrevita):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
     .send_keys(tiulo_entrevita))
    time.sleep(1)


@step("Agregar el nombre del entrevistador: {entrevistador}")
def step_impl(context, entrevistador):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input')
     .send_keys(entrevistador))
    time.sleep(1)
    WebDriverWait(context.driver, 3).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@role='listbox']//div[@role='option']//span[contains(text(),'" + entrevistador + "')]"))).click()
    time.sleep(1)


@step("Agregar fecha de la entrevista: {fecha_entrevista}")
def step_impl(context, fecha_entrevista):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/div/div/input')
     .send_keys(fecha_entrevista))
    time.sleep(1)


@step("Agregar hora de la entrevista: {hora_entrevista}")
def step_impl(context, hora_entrevista):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/input')
     .send_keys(hora_entrevista))
    time.sleep(1)


@step("Agregar notas para la entrevista: {notas_entrevista}")
def step_impl(context, notas_entrevista):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/textarea')
     .send_keys(notas_entrevista))
    time.sleep(1)


@then("Hacer click and el boton 'guardar'")
def step_impl(context):
    (context.driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/textarea').click())
    time.sleep(1)

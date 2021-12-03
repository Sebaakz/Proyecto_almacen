from behave import *
from math import isclose
from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
chromedriver_autoinstaller.install()

@given('inicio sesion en el sistema como {usuario} con la contraseña {contraseña}')
def step_imp1(context, usuario, contraseña):
    context.driver = webdriver.Chrome()
    context.driver.get('http://127.0.0.1:8000/login/?next=/cliente')
    time.sleep(1)
    context.driver.find_element_by_name("campo_username").send_keys(usuario)
    context.driver.find_element_by_name("Campo_password").send_keys(contraseña)
    context.driver.find_element_by_id("login_btn").send_keys(Keys.ENTER)
    context.driver.find_element_by_id("btn-crear-cliente").send_keys(Keys.ENTER)
@when ('mi cliente no esta registrado en el sistema, ingreso su rut {rut_cliente}')
def step_imp2(context, rut_cliente):
    context.driver.find_element_by_name("rut_cliente").send_keys(rut_cliente)
@when ('su nombre es {nombre} {apellido}')
def step_imp2(context, nombre, apellido):
    context.driver.find_element_by_name("nombre").send_keys(nombre)
    context.driver.find_element_by_name("apellido").send_keys(apellido)
@when ('su direccion es {Direccion}')
def step_imp3(context, Direccion):
    context.driver.find_element_by_name("direccion").send_keys(Direccion)
@when ('su telefono es {telefono}')
def step_imp4(context, telefono):
    context.driver.find_element_by_name("telefono").send_keys(telefono)
@when ('su correo electronico es {correo}')
def step_imp5(context, correo):
    context.driver.find_element_by_name("correo").send_keys(correo)
@Then ('confirmo el registro del cliente con rut {rut_cliente}')
def step_imp6(context, rut_cliente):
    time.sleep(1)
    context.driver.find_element_by_id("boton-registro").send_keys(Keys.ENTER)
    context.driver.get('http://127.0.0.1:8000/cliente')
    resultado = context.driver.find_element_by_id(rut_cliente).text
    resultado_esperado = float(rut_cliente)
    resultado_obtenido = float(resultado)
    assert isclose(resultado_esperado, resultado_obtenido)
@then('cierro sesion')
def  step_imp7(context):
    time.sleep(1)
    context.driver.find_element_by_id("btn_logout").send_keys(Keys.ENTER)
@Given ('inicio sesion como {usuario} con la contraseña {contraseña}')
def step_login1(context,usuario,contraseña):
    time.sleep(1)
    context.driver = webdriver.Chrome()
    context.driver.get('http://127.0.0.1:8000/login')
    context.driver.find_element_by_name("campo_username").send_keys(usuario)
    context.driver.find_element_by_name("Campo_password").send_keys(contraseña)
    time.sleep(1)
@When ('presiono iniciar sesion')
def step_login2(context):
    context.driver.find_element_by_id("login_btn").send_keys(Keys.ENTER)
    time.sleep(1)
@Then ('el sistema me indica que mi usuario o contraseña es incorrecto')
def step_loginError(context):
    resultado = context.driver.find_element_by_id("error_message").text
    assert resultado ==str("Usuario o password incorrecto");
@Then ('ingreso al sistema como {usuario}')
def step_loginIngreso(context, usuario):
    nombre_usuario = usuario
    resultado = context.driver.find_element_by_id("user_name").text
    resultado_esperado =nombre_usuario
    time.sleep(1)
    assert resultado == resultado_esperado

Feature: Ingresar al sistema

    inicio sesion en el sistema
Scenario: error inicio de sesion

Given inicio sesion como pepe con la contraseña 1234 
When presiono iniciar sesion
Then el sistema me indica que mi usuario o contraseña es incorrecto

Scenario: error inicio de sesion sin el usuario
Given inicio sesion como   con la contraseña 1234 
When presiono iniciar sesion
Then el sistema me indica que mi usuario o contraseña es incorrecto

Scenario: iniciar correctamente

Given inicio sesion como admin con la contraseña avaras08 
When presiono iniciar sesion
Then ingreso al sistema como admin
Feature: gestión de cliente

    gestión de los clientes, crearlos, editarlos y eliminarlos

Scenario: registro común de cliente

Given inicio sesion en el sistema como admin con la contraseña avaras08
When mi cliente no esta registrado en el sistema, ingreso su rut 206477725
And su nombre es Roberto barria
And su direccion es calle del candil 2937
And su telefono es 933149567
And su correo electronico es usuario@gmail.com
Then confirmo el registro del cliente con rut 206477725
And cierro sesion

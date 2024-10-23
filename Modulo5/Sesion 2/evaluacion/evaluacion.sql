--Una empresa dedicada a la venta de automóviles ofrece distintos modelos. Producto de ello, se necesita almacenar la patente, marca, modelo, color y el precio de venta de cada uno. Y para sus clientes, el nombre, correo electrónico, dirección, RUT y celular. Los clientes pueden ser dados de alta o baja. Y también se requiere registrar las ventas de un cliente, y llevar una historia de las mantenciones realizadas, para poder avisarle de forma anticipada las que se realizan cada número de Kms o cada mes, dependiendo del vehículo. 
 
-Tabla empresa
PK rut
nombre
direccion
telefono
correo
web

-Tabla cliente
PK rut
nombre
correo
direccion
telefono
alta

-Tabla tipo_vehiculo
PK id_tipo_vehiculo
nombre

-Tabla mantencion
PK id_mantencion
fecha
trabajos_realizados

-Tabla Venta
PK folio
fecha
monto

-Tabla vehiculo
PK id_tipo_vehiculo
patente
marca
modelo
color
precio
frecuencia_mantencion

-Tabla marca
PK id_marca
nombre

create table empresa(
	rut varchar primary key,
	nombre varchar,
 	direccion varchar,
 	telefono varchar,
 	correo varchar,
 	web varchar
)

create table cliente(
 	rut varchar primary key,
 	nombre char,
 	correo varchar,
 	direccion varchar,
 	telefono varchar,
 	alta varchar
)

create table tipo_vehiculo(
	id_tipo_vehiculo varchar primary key,
	nombre varchar
)

create table mantencion(
	id_mantencion varchar primary key,
	fecha varchar,
 	trabajos_realizados varchar
)

create table Venta(
	folio varchar primary key,
 	fecha varchar,
	monto varchar
)

create table vehiculo(
 	id_tipo_vehiculo varchar primary key,
 	patente varchar,
 	marca varchar,
 	modelo varchar,
 	color char,
 	precio varchar,
 	frecuencia_mantencion varchar
)

create table marca(
 	id_marca varchar primary key,
 	nombre varchar
)
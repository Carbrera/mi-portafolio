--1) Crea una base de datos llamada empresa.

CREATE DATABASE empresa;

USE empresa;

--2) Dentro de la base de datos empresa, crea una tabla llamada departamentos con las siguientes columnas:
 --• id (entero, clave primaria)
 --• nombre (cadena de caracteres, hasta 100 caracteres) 
 --• ubicacion (cadena de caracteres, hasta 100 caracteres)

CREATE TABLE departamentos(
    id int PRIMARY KEY,
    nombre varchar(100),
    ubicacion varchar(100)
);

--3) Crea una tabla llamada empleados con las siguientes columnas:
 --• id (entero, clave primaria) 
 --• nombre (cadena de caracteres, hasta 100 caracteres) 
 --• puesto (cadena de caracteres, hasta 100 caracteres) 
 --• salario (decimal, hasta 10 dígitos enteros y 2 decimales) 
 --• fecha_contratacion (fecha) 
 --• departamento_id (entero, clave foránea que referencia departamentos.id)

CREATE TABLE empleados(
    id int PRIMARY KEY,
    nombre varchar(100),
    puesto varchar(100),
    salario decimal(12,2),
    fecha_contratacion date,
    departamento_id int, 
    CONSTRAINT FK_id_departamento FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

--4) Modifica la tabla empleados para agregar una nueva columna llamada email que almacenará direcciones de correo electrónico (cadena de caracteres, hasta 100 caracteres).

ALTER TABLE empleados ADD email varchar(100);

--5) Cambia el nombre de la tabla empleados a trabajadores.

ALTER TABLE empleados RENAME TO trabajadores; 

--6) Elimina la tabla departamentos.

DROP TABLE trabajadores;
DROP TABLE departamentos;
--Tomando en cuenta los conocimientos adquiridos, observa el siguiente Modelo Relacional, y genera el script SQL para implementarlo.

--Tabla empresa
CREATE TABLE empresa(
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Correo VARCHAR(80),
    Web VARCHAR(50)
);

--Tabla cliente
CREATE TABLE cliente(
    rut VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(80),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Alta CHAR
);

--Tabla tipo_vehiculo
CREATE TABLE tipo_vehiculo(
    id_tipo_vehiculo SERIAL PRIMARY KEY,
    Nombre VARCHAR(120)
);

--Tabla marca
CREATE TABLE marca(
    id_marca SERIAL PRIMARY KEY,
    Nombre VARCHAR(120)
);

--Tabla vehiculo
CREATE TABLE vehiculo(
    id_vehiculo SERIAL PRIMARY KEY,
    Patente VARCHAR(10),
    Marca VARCHAR(20),
    Modelo VARCHAR(20),
    Color VARCHAR(15),
    Precio INT,
    Frecuencia_mantencion INT,
    Id_marca INT, CONSTRAINT FK_vehiculo_id_marca FOREIGN KEY (id_marca) REFERENCES marca(id_marca),
    Id_tipo_vehiculo INT, CONSTRAINT FK_vehiculo_id_tipo_vehiculo FOREIGN KEY (id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo)
);

--Tabla venta
CREATE TABLE venta(
    Folio SERIAL PRIMARY KEY,
    Fecha DATE,
    Monto INT,
    id_vehiculo INT,
    rut_cliente VARCHAR(10),
	CONSTRAINT FK_venta_id_vehiculo FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id_vehiculo),
	CONSTRAINT FK_venta_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES cliente(rut)
);

--Tabla mantencion
CREATE TABLE mantencion(
    Id_mantencion SERIAL PRIMARY KEY,
    Fecha DATE,
    Trabajos_realizados VARCHAR(1000),
    Venta_folio INT, CONSTRAINT FK_mantencion_folio FOREIGN KEY (Venta_folio) REFERENCES venta(Folio)
);
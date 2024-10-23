--Considerando los conocimientos adquiridos, deberás aplicar 1FN, 2FN y 3FN a la tabla.

Primera Forma Normal (1FN):Cada columna debe contener un solo valor y no debe haber duplicación de datos.

Tabla Ordenes
idOrden
fecha

Tabla Clientes
IdCliente
nombre_cliente
ciudad

Tabla Articulos
codigo
nombre_articulo
cantidad
precio

Segunda Forma Normal (2FN):Debe cumplir con la 1FN y cada columna no clave(ni pk, ni fk) debe depender completamente de la clave primaria.

Tabla Ordenes
PK idOrden
fecha

Tabla Clientes
PK IdCliente
nombre_cliente
ciudad

Tabla Articulos
PK codigo
nombre_articulo
cantidad
precio


Tercera Forma Normal (3FN):Debe cumplir con la 2FN y no debe haber dependencias transitivas.

Tabla Ordenes
PK idOrden
fecha
FK IdCliente

Tabla Clientes
PK IdCliente
nombre_cliente
ciudad

Tabla Articulos
PK codigo
nombre_articulo
precio

Tabla DetalleOrdenes
PK idDetalleOrden
cantidad
FK idOrden
FK codigoArticulo

-- Desnormalización, sobrecarga de atributos en una tabla
Tabla Ordenes
idOrden
fecha
cantidad
codigo
IdCliente
FK IdCliente
FK codigo

Tabla Clientes
PK IdCliente
nombre_cliente
ciudad

Tabla Articulos
PK codigo
nombre_articulo
precio

--Crear tablas

CREATE TABLE clientes(
    cliente_id SERIAL PRIMARY KEY, 
    nombre_cliente VARCHAR(100),
    ciudad VARCHAR(50)
);

CREATE TABLE articulos(
    codigo VARCHAR(10) PRIMARY KEY,
    nombre_articulo VARCHAR(100),
    precio DECIMAL(10,2)
);

CREATE TABLE ordenes(
    orden_id INT,
    fecha DATE,
    cantidad INT,
    codigo_articulo VARCHAR(10),
    cliente_id INT,
    FOREIGN KEY (codigo_articulo) REFERENCES articulos(codigo),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

INSERT INTO clientes(nombre_cliente, ciudad) VALUES 
('Martin',  'Santiago'),
('Herman', 'Valparaíso'),
('Pedro', 'Concepción');

INSERT INTO articulos(codigo, nombre_articulo, precio) VALUES
('3786', 'Red', 35.00),
('4011', 'Raqueta', 65.00),
('9132', 'Paq-3', 4.75),
('5794', 'Paq-6', 5.00),
('3141', 'Funda', 10.00);

INSERT INTO ordenes(orden_id, fecha, cantidad, codigo_articulo, cliente_id) VALUES
('2301', '2020-02-23', 3, '3786', 1),
('2301', '2020-02-23', 3, '4011', 1),
('2301', '2020-02-23', 3, '9132', 1),
('2302', '2020-02-25', 4, '5794', 2),
('2303', '2020-02-27', 2, '4011', 3),
('2303', '2020-02-27', 2, '3141', 3);
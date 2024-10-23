--Empresa
CREATE TABLE empresa(
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Direccion VARCHAR(120),
    Telefono VARCHAR(15),
    Correo VARCHAR(80),
    Web VARCHAR(50)
);

--Cliente
CREATE TABLE cliente(
    RUT VARCHAR(10) PRIMARY KEY,
    Nombre VARCHAR(120),
    Correo VARCHAR(80),
    Direccion VARCHAR(120),
    Celular VARCHAR(15)
);

--Herramienta
CREATE TABLE herramienta(
    IDHerramienta INT PRIMARY KEY,
    Nombre VARCHAR(120),
    PrecioDia INT
);

--Arriendo
CREATE TABLE arriendo(
    Folio INT PRIMARY KEY,
    Fecha DATE,
    Dias INT,
    ValorDia INT,
    Garantia VARCHAR(30),
    IDHerramienta INT,
    RUTCliente VARCHAR(10),
    CONSTRAINT FK_arriendo_id_herramienta FOREIGN KEY (IDHerramienta) REFERENCES herramienta(IDHerramienta),
    CONSTRAINT FK_arriendo_rut_cliente FOREIGN KEY (RUTCliente) REFERENCES cliente(RUT)
);
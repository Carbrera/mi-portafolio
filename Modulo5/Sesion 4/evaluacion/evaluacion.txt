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

-- Herramienta
CREATE TABLE herramienta(    
    IDHerramienta INT PRIMARY KEY,    
    Nombre VARCHAR(120),    
    PrecioDia INT
);
    
-- Arriendo
CREATE TABLE arriendo(    
    Folio INT PRIMARY KEY,    
    Fecha DATE,    
    Dias INT,    
    ValorDia INT,    
    Garantia VARCHAR(30),    
    Herramienta_IDHerramienta INT,    
    Cliente_RUT VARCHAR(10)
);

ALTER TABLE arriendo ADD CONSTRAINT FK_arriendo_id_herramienta FOREIGN KEY (Herramienta_IDHerramienta) REFERENCES herramienta(IDHerramienta);
ALTER TABLE arriendo ADD CONSTRAINT FK_arriendo_rut_cliente FOREIGN KEY (Cliente_RUT) REFERENCES cliente(RUT);

-- 1.- Inserte los datos de una empresa
INSERT into empresa VALUES('12345678-9','Herrentamientas','0123 Avenida Real',1234567890,'datosarriendo@herrentamientas.cl','herrentamientas.cl');

-- 2.- Inserte 5 herramientas
INSERT into herramienta VALUES(1,'Taladro Electrico',10000),(2,'Sierra Electrica',20000),(3,'Pistola de Clavos',30000),(4,'Lijadora',40000),(5,'Serrucho Electrico',50000);

-- 3.- Inserte 3 clientes                
INSERT into cliente VALUES('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);

-- 4. Elimina el ultimo cliente
DELETE FROM cliente WHERE RUT = '44444444-4';

-- 5. Elimina la primera herramienta
DELETE FROM herramienta WHERE IDHerramienta = 1;

-- 6.- Inserte 2 arriendos para cada cliente
INSERT into arriendo (Folio, Fecha, Dias, ValorDia, Garantia, Herramienta_IDHerramienta, Cliente_RUT) VALUES(1,'12/11/22',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),(2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),(3,'12/11/22',1,40000,'Eficacia en 1 dia',4,'33333333-3'),(4,'12/11/22',3,40000,'Eficacia en solo 3 dias',4,'33333333-3');

-- 7. Modifique el correo del primer cliente
UPDATE cliente SET Correo = 'jperez@mail.com' WHERE RUT = '22222222-2';

-- 8. Liste todas las herramientas
SELECT * FROM herramienta;

-- 9. Liste todos los arriendos del cliente '33333333-3'
SELECT * FROM arriendo WHERE Cliente_RUT = '33333333-3';

-- 10. Liste los clientes cuyo nombre contenga la letra 'a'
SELECT * FROM cliente WHERE Nombre LIKE '%a%';SELECT * FROM cliente WHERE UPPER(Nombre) LIKE '%A%';SELECT * FROM cliente WHERE LOWER(Nombre) LIKE '%a%';

-- 11. Obtenga el nombre de la segunda herramienta insertada. 
SELECT Nombre FROM herramienta WHERE IDHerramienta = 2;

-- 12. Modifique los primeros 2 arriendos insertados con fecha 15/01/2020.
UPDATE arriendo SET Fecha = '15/01/2020' WHERE Folio IN (1, 2);

-- 13. Liste Folio, Fecha y ValorDia de los arriendos de enero del 2020. 
SELECT Folio, Fecha, ValorDia
FROM arriendo
WHERE Fecha BETWEEN '01/01/2020' and '31/01/2020';
--3. https://www.w3schools.com/postgresql/postgresql_case.phphttps://www.postgresqltutorial.com/postgresql-tutorial/postgresql-case/SELECT rut_cliente,monto,CASE  WHEN monto BETWEEN 0 AND 1000000 THEN 'Standar'  WHEN monto BETWEEN 1000001 AND 3000000 THEN 'Gold'  WHEN monto = 3000001 THEN 'Premium'    WHEN monto > 3000001 THEN 'Premium'  ELSE 'No califica'END AS Clasificacion  FROM venta;


SELECT v.*, m.nombre FROM venta as v
JOIN vehiculo as veh
ON veh.id_vehiculo = v.id_vehiculo
JOIN marca as m
ON m.id_marca = veh.id_marca
WHERE veh.id_marca =  
(SELECT veh.id_marca FROM vehiculo as veh  
JOIN venta as v  

ON veh.id_vehiculo = v.id_vehiculo  

GROUP BY veh.id_marca  

ORDER BY COUNT(*) DESC LIMIT 1)
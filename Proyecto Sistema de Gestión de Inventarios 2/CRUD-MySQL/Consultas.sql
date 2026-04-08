Insert Into usuario (usuario, contrasenia) Values ('Marcos','232006');

INSERT INTO producto (codigo, descripcion, unidad_M, presentacion, precio, estado, fecha) VALUES
('P-101', 'Taza cerámica blanca', 'Unidad', 'Caja individual', 12.50, 'Activo', '2024-10-15'),
('P-102', 'Taza viaje acero', 'Unidad', 'Caja regalo', 18.00, 'Activo', '2024-11-20'),
('P-103', 'Taza cerámica blanca', 'Unidad', 'Caja individual', 12.50, 'Agotado', '2024-12-10'),
('P-201', 'Peluche oso 30cm', 'Unidad', 'Bolsa transparente', 25.00, 'Activo', '2025-01-05'),
('P-202', 'Peluche conejo 25cm', 'Unidad', 'Caja color', 22.00, 'Activo', '2025-02-14'),
('P-203', 'Peluche oso 30cm', 'Unidad', 'Bolsa transparente', 25.00, 'Agotado', '2025-03-08'),
('P-301', 'Chocolate negro 200g', 'Caja', 'Caja regalo', 15.00, 'Activo', '2025-04-22'),
('P-302', 'Chocolate leche 150g', 'Caja', 'Caja madera', 12.00, 'Activo', '2025-05-30'),
('P-303', 'Chocolate negro 200g', 'Caja', 'Caja regalo', 15.00, 'Inactivo', '2025-06-18'),
('P-401', 'Llavero metal corazón', 'Unidad', 'Blister', 8.50, 'Activo', '2025-07-12'),
('P-402', 'Llavero acrílico foto', 'Unidad', 'Caja pequeña', 10.00, 'Activo', '2025-08-25'),
('P-403', 'Llavero metal corazón', 'Unidad', 'Blister', 8.50, 'Agotado', '2025-09-03'),
('P-501', 'Set té 6 piezas', 'Set', 'Caja regalo', 35.00, 'Activo', '2025-10-01'),
('P-502', 'Set té 12 piezas', 'Set', 'Caja lujo', 55.00, 'Activo', '2024-10-28'),
('P-503', 'Set té 6 piezas', 'Set', 'Caja regalo', 35.00, 'Inactivo', '2024-11-15');

SELECT * FROM usuario;

Select * From usuario Where usuario = '%s' and contrasenia = '%s';
SELECT * FROM usuario WHERE usuario = 'Marcos' AND contrasenia = '232006';

SELECT * FROM producto;

DELETE FROM producto WHERE codigo = 'P-201';
UPDATE producto  SET descripcion = 'Prueba', unidad_M = 'Test1', presentacion = 'Test2' , precio = 99.99, estado = 'Test3', fecha = '2025-10-24'
WHERE codigo = 'P-201';

SELECT * FROM producto WHERE codigo = '' AND fecha = '';
SELECT * FROM producto WHERE codigo = '';
SELECT * FROM producto WHERE descripcion = '';
SELECT * FROM producto WHERE fecha = '';


SET SQL_SAFE_UPDATES = 0;

TRUNCATE TABLE producto;
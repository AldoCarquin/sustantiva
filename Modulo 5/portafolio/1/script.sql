CREATE TABLE Clientes
(
	ID integer primary Key,
	Nombre varchar(20),
	Apellido varchar(20),
	Edad integer
);

INSERT INTO Clientes (ID, Nombre, Apellido, Edad)
VALUES (1, 'Nemesio', 'Ramirez', 48),
(2, 'Rigoberto', 'Perez', 52),
(3, 'Filomena', 'Muñoz', 36),
(4, 'Herminda', 'Lopez', 47);

SELECT *
FROM Clientes
WHERE Edad >45;


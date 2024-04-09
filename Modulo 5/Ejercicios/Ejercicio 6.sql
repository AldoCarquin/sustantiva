DROP TABLE IF EXISTS bandas;
CREATE TABLE bandas
(
	nombre character varying (50),
	pais character varying (50)
);

insert into bandas (nombre, pais) values ('Kraftwerk', 'Alemania');
insert into bandas (nombre, pais) values ('Los prisioneros', 'Chile');
insert into bandas (nombre, pais) values ('KMFDM', 'Alemania');
insert into bandas (nombre, pais) values ('Muse', 'UK');
insert into bandas (nombre, pais) values ('The Chemical Brothers', 'UK') ;
insert into bandas (nombre, pais) values ('TOOL', 'USA');
insert into bandas (nombre, pais) values ('The Beatles', 'UK');
insert into bandas (nombre, pais) values ('Modeselektor', 'Alemania');

DROP TABLE IF EXISTS bandas_discos;
CREATE TABLE bandas_discos
(
	nombre_disco character varying(50),
	nombre_banda character varying(50),
	anio_disco integer
);

insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Kraftwerk', 'Computer World', 1981);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Kraftwerk', 'The Man Machine', 1978);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Los prisioneros', 'La cultura de la basura', 1987);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Los prisioneros', 'Corazones', 1990);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('KMFDM', 'NIHIL', 1995);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('KMFDM', 'XTORT', 1996);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('KMFDM', 'ADIOS', 1999);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Muse', 'Showbiz', 1999);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Muse', 'Origin of symmetry', 2001);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Muse', 'Black holes and Revelations', 2006);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Chemical Brothers', 'Surrender', 1999);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Chemical Brothers', 'Born in the echoes', 2015);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Chemical Brothers', 'No Geography', 2019);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('TOOL', 'Aenima', 1996);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('TOOL', 'Lateralus', 2001);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('TOOL', 'Fear Inoculum', 2019);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Beatles', 'Rubber Soul', 1965);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Beatles', 'Revolver', 1966);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('The Beatles', 'Abbey Road', 1969);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Modeselektor', 'Hello Mom!', 2005);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Modeselektor', 'Monkeytown', 2011);
insert into bandas_discos (nombre_banda, nombre_disco, anio_disco) values ('Modeselektor', 'Who Else', 2019); 

SELECT *
FROM bandas;

SELECT *
FROM bandas_discos;

--1.- Discos de Bandas NO Alemanas Publicados desde el 2000 en adelante
SELECT bd.nombre_banda, bd.nombre_disco, bd.anio_disco
FROM bandas_discos bd
INNER JOIN bandas b ON bd.nombre_banda = b.nombre
WHERE b.pais != 'Alemania' AND bd.anio_disco >= 2000;

--2.- Listar el disco más reciente de las bandas inglesas que terminan en 's':
SELECT nombre_banda, nombre_disco, anio_disco
FROM bandas_discos
WHERE nombre_banda IN(
	SELECT nombre
	FROM bandas
	WHERE pais = 'UK' AND nombre LIKE '%s'
)
ORDER BY anio_disco desc
LIMIT 1;

--3.- Listar todas las bandas alemanas con al menos una letra 'k' en su nombre que tenga discos publicados en 1999 o superior:
SELECT b.nombre, bd.nombre_disco, bd.anio_disco
FROM bandas b
INNER JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
WHERE b.pais ='Alemania' AND b.nombre LIKE '%k%' and bd.anio_disco >=1999 
	OR b.nombre LIKE 'k%' and bd.anio_disco >=1999 
	OR b.nombre LIKE '%k' and bd.anio_disco >=1999;

--4.- Listar todas las bandas y el número de discos registrados:
SELECT b.nombre, COUNT(bd.nombre_disco) as numero_disco
FROM bandas b
LEFT JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
GROUP BY b.nombre;

--5.- Mostrar todos los años en que todas las bandas sacaron un disco. Ordene la lista por año:
SELECT DISTINCT bd.anio_disco, bd.nombre_banda
FROM bandas_discos bd
ORDER BY bd.anio_disco, bd.nombre_banda;

--6.- Listar todas las bandas que tienen un disco con nombre empezando en 'a'. Listar el nombre de la banda y del disco:
SELECT bd.nombre_banda, bd.nombre_disco
FROM bandas_discos bd
WHERE bd.nombre_disco LIKE 'A%'
GROUP BY bd.nombre_banda, bd.nombre_disco;

--7.- Listar todas las bandas que tengan discos con más de una palabra. Listar el nombre de la banda y el disco:
SELECT bd.nombre_banda, bd.nombre_disco
FROM bandas_discos bd
WHERE bd.nombre_disco LIKE '% %';

--8.- Listar todas las bandas que tengan discos con más de una palabra. Listar el nombre de la banda y la cantidad de discos:
SELECT b.nombre, COUNT(bd.nombre_disco) AS cantidad_discos
FROM bandas b
INNER JOIN bandas_discos bd ON b.nombre = bd.nombre_banda
WHERE bd.nombre_disco LIKE '% %'
GROUP BY b.nombre;
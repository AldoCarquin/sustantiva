-- Tabla Libro
CREATE TABLE Libro (
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(255),
    -- Otros atributos del libro
);

-- Tabla Autor
CREATE TABLE Autor (
    id_autor INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    -- Otros atributos del autor
);

-- Tabla Ejemplar
CREATE TABLE Ejemplar (
    id_ejemplar INT PRIMARY KEY,
    id_libro INT,
    estado VARCHAR(50),
    -- Otros atributos del ejemplar
    FOREIGN KEY (id_libro) REFERENCES Libro(id_libro)
);

-- Tabla Prestamo
CREATE TABLE Prestamo (
    id_prestamo INT PRIMARY KEY,
    id_ejemplar INT,
    fecha_ini DATE,
    fecha_fin DATE,
    -- Otros atributos del préstamo
    FOREIGN KEY (id_ejemplar) REFERENCES Ejemplar(id_ejemplar)
);

-- Tabla Libro_Autor (para la relación muchos a muchos entre Libro y Autor)
CREATE TABLE Libro_Autor (
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES Libro(id_libro),
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
);

-- Datos de ejemplo para la tabla Libro
INSERT INTO Libro (id_libro, titulo) VALUES
(1, 'Libro 1'),
(2, 'Libro 2'),
(3, 'Libro 3');

-- Datos de ejemplo para la tabla Autor
INSERT INTO Autor (id_autor, nombre, apellido) VALUES
(1, 'Autor 1', 'Apellido 1'),
(2, 'Autor 2', 'Apellido 2'),
(3, 'Autor 3', 'Apellido 3');

-- Datos de ejemplo para la tabla Ejemplar
INSERT INTO Ejemplar (id_ejemplar, id_libro, estado) VALUES
(1, 1, 'Disponible'),
(2, 1, 'Prestado'),
(3, 2, 'Disponible'),
(4, 3, 'Prestado');

-- Datos de ejemplo para la tabla Prestamo
INSERT INTO Prestamo (id_prestamo, id_ejemplar, fecha_ini, fecha_fin) VALUES
(1, 2, '2024-03-15', '2024-04-15'),
(2, 4, '2024-03-10', '2024-04-10');

-- Datos de ejemplo para la tabla Libro_Autor
INSERT INTO Libro_Autor (id_libro, id_autor) VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 3);

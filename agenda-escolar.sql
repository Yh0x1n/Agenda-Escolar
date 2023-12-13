DROP DATABASE IF EXISTS agenda_escolar;
CREATE DATABASE agenda_escolar;

USE agenda_escolar;

CREATE TABLE Materias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    profesor VARCHAR(100),
    aula VARCHAR(50)
);

CREATE TABLE Tareas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_entrega DATE,
    completada BOOLEAN,
    materia_id INT,
    FOREIGN KEY (materia_id) REFERENCES Materias(id)
);

CREATE TABLE Horarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    hora TIME,
    materia_id INT,
    FOREIGN KEY (materia_id) REFERENCES Materias(id)
);

--Inserciones de prueba

INSERT INTO Materias (nombre, profesor, aula) VALUES ('Matemáticas', 'Profesor A', 'Aula 101');
INSERT INTO Materias (nombre, profesor, aula) VALUES ('Ciencias', 'Profesora B', 'Aula 201');

INSERT INTO Tareas (nombre, descripcion, fecha_entrega, completada, materia_id) VALUES ('Tarea de álgebra', 'Resolver ejercicios del capítulo 5', '2023-12-14', 0, 1);
INSERT INTO Tareas (nombre, descripcion, fecha_entrega, completada, materia_id) VALUES ('Informe de biología', 'Investigación sobre ecosistemas locales', '2023-12-16', 0, 2);

INSERT INTO Horarios (dia_semana, hora, materia_id) VALUES ('Lunes', '08:00:00', 1);
INSERT INTO Horarios (dia_semana, hora, materia_id) VALUES ('Miércoles', '10:00:00', 2);

#MÓDULO PARA REALIZAR PRUEBAS A LA BASE DE DATOS
import mariadb, sys


try:
    conn = mariadb.connect(
        user = 'root',
        password = 'root',
        host = 'localhost',
        port = 3306,
        database = 'agenda_escolar'
    )

    cur = conn.cursor()
    
    cur.execute('drop database if exists agenda_escolar;')
    cur.execute('create database agenda_escolar;')
    cur.execute('use agenda_escolar;')

    print('[!] Connected to database!')

except mariadb.Error as e:
    print(f'[!] Error connecting to database!:\n{e}')
    sys.exit(1)

#Crear tabla
try:
    cur.execute('DROP TABLE IF EXISTS Materias;')
    cur.execute(
                'CREATE TABLE Materias ('
                'id INT PRIMARY KEY AUTO_INCREMENT,'
                'nombre VARCHAR(100) NOT NULL,'
                'profesor VARCHAR(100),'
                'aula VARCHAR(50)'
                ');'
    )
    
    cur.execute('DROP TABLE IF EXISTS Tareas;')
    cur.execute(
                'CREATE TABLE Tareas ('
                'id INT PRIMARY KEY AUTO_INCREMENT,'
                'nombre VARCHAR(100) NOT NULL,'
                'descripcion TEXT NULL,'
                'fecha_entrega DATE NULL,'
                'completada BOOLEAN,'
                'materia_id INT NOT NULL,'
                'FOREIGN KEY (materia_id) REFERENCES Materias(id)'
                ');'
    )

    cur.execute('DROP TABLE IF EXISTS Horarios;')
    cur.execute(
                'CREATE TABLE Horarios ('
                'id INT PRIMARY KEY AUTO_INCREMENT,'
                'dia_semana ENUM("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"),'
                'hora TIME,'
                'materia_id INT,'
                'FOREIGN KEY (materia_id) REFERENCES Materias(id)'
                ');'
    )

    cur.execute(
        'INSERT INTO Materias(nombre, profesor, aula) values'
        "('Auditoría de Sistemas', 'Yocceline Rosillo', 'B2'),"
        "('Defensa Integral VIII', 'Rubén Toyo', 'B2'),"
        "('Higiene y Seguridad Industrial', 'Robert González', 'C2'),"
        "('Marco Legal para el Ejercicio de la Ingeniería', 'Johanna Castillo', 'B2'),"
        "('Teoría de Decisiones', 'Adelina Medina', 'B2'),"
        "('Teleprocesos', 'Argenis Chirino', 'B2, C2'),"
        "('Tradición Cultura y Folclor Local', 'José Gómez', 'Biblioteca');"
    )

except mariadb.Error as e:
    print(e)
    sys.exit(1)
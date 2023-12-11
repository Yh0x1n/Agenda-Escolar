#Database for the Agenda

import mariadb
import sys
import os
'''from main import tasks'''
os.system('sudo su')
os.system('Yh0x4l1n1*')
def DB_conn():
    try:
        conn = mariadb.connect(
            user = 'root',
            password = 'root',
            port = 3306,
            database = 'Agenda'
        )
        cur = conn.cursor()
        cur.execute('USE Agenda')
        print('[!] Connected to database!')

    except mariadb.Error as e:
        print(f'[!] Error connecting to database!:\n{e}')
        sys.exit(1)

    #TO-DO: Crear las sentencias SQL y funciones correspondientes a cada campo de la agenda
    
    #Crear tabla
    try:
        cur.execute('DROP TABLE IF EXISTS MATERIAS;')
        cur.execute(
                    'CREATE TABLE Materias ('
                    'id INT PRIMARY KEY AUTO_INCREMENT,'
                    'nombre VARCHAR(100) NOT NULL,'
                    'profesor VARCHAR(100),'
                    'aula VARCHAR(50)'
                    ');'
        )
        
        cur.execute(
                'CREATE TABLE Tareas ('
                'id INT PRIMARY KEY AUTO_INCREMENT,'
                'nombre VARCHAR(100) NOT NULL,'
                'descripcion TEXT,'
                'fecha_entrega DATE,'
                'completada BOOLEAN,'
                'materia_id INT,'
                'FOREIGN KEY (materia_id) REFERENCES Materias(id)'
                ');'
        )

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
            "('Defensa Integral VIII', 'Rubén Toyo', B2),"
            "('Higiene y Seguridad Industrial', 'Robert González', 'B2')"
        )

    except mariadb.Error as e:
        print(e)
#Database for the Agenda

import mariadb
import sys
'''from main import tasks'''

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
        cur.execute('CREATE TABLE MATERIAS('
                    'ID INT NOT NULL AUTO_INCREMENT,'
                    'NOMBRE VARCHAR(100) NOT NULL,'
                    'MATERIA VARCHAR(100) NOT NULL,'
                    'PRIMARY KEY (ID));'
        )
    except mariadb.Error as e:
        print(e)

DB_conn()
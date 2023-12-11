#Agenda Escolar
#Authors: Yhoxin Rossell, Guillermo López and Jesús Campos

'''
IMPORTACIONES
'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as FileDialog
from tkcalendar import *
import mariadb
import sys

route = ''

'''
Base de datos
'''

try:
    conn = mariadb.connect(
        user = 'root',
        password = 'root',
        host = 'localhost',
        port = 3306,
        database = 'agenda_escolar'
    )
    cur = conn.cursor()
    print('[!] Connected to database!')
    cur.execute('drop database if exists agenda_escolar;')
    cur.execute('create database agenda_escolar;')
    cur.execute('use agenda_escolar;')

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
        "('Higiene y Seguridad Industrial', 'Robert González', 'B2');"
    )

except mariadb.Error as e:
    print(e)

##############################################################################################################

'''
Ventana de gestión de tareas
'''



def tasks():
    def guardar():
        try: 
            nombre = nombre_tarea.get()
            materia = materia_entry.get()
            description_text = descripcion.get(1.0, "end-1c") 
            fecha_entrega = cal.get_date()

            # Ejecuta la sentencia SQL para insertar los datos en la tabla "tareas"
            cur.execute("INSERT INTO Tareas (nombre, descripcion, fecha_entrega, materia_id) VALUES (?, ?, ?, ?)",
                        (nombre, description_text, fecha_entrega, materia))
            
            conn.commit()  # Realiza el commit para confirmar la inserción
            print("[!] Data saved successfully")
            Tasks_window.destroy()  # Cierra la ventana después de guardar los datos
            actualizar_listbox()
        
        except mariadb.Error as e:
            print(e)
    

    Tasks_window = Tk()
    Tasks_window.geometry("600x400")
    Tasks_window.title("Agregar Tarea")

    Label(Tasks_window, text='Nombre de la tarea:').pack()
    nombre_tarea = Entry(Tasks_window)
    nombre_tarea.pack()

    Label(Tasks_window, text='Materia:').pack()
    opciones = []
    materia_entry = ttk.Combobox(Tasks_window, values = opciones)
    materia_entry.pack()

    Label(Tasks_window, text='Descripción:').pack()
    descripcion = Text(Tasks_window, height = 1, width=40)
    descripcion.pack()

    Label(Tasks_window, text='Fecha de entrega:').pack()
    cal = Calendar(Tasks_window, selectmode='day', year=2023, month=11, day=16)
    cal.pack()

    # Botón para guardar los datos
    btn_guardar = Button(Tasks_window, text='Guardar', command=guardar)
    btn_guardar.pack()

def eliminar():
    selecc = main_list.curselection()
    tarea_id = main_list.get(selecc[0])[0]
    if selecc:
        main_list.delete(selecc)
        cur.execute(f'delete from Tareas where id = {tarea_id}')
        conn.commit()
    print(tarea_id)

        
#Salir del programa
def exit():
    exit = messagebox.askyesno("Exit", "Exit program?")
    
    if exit: 
        root.quit()

##################################################################################################################################

'''
Bloque principal; menú y botones
'''
root = Tk()  
root.geometry("600x400")
root.title("AGENDA ESCOLAR")
label = Label(root, text = "¡BIENVENIDO A TU AGENDA ESCOLAR!\n"
              "Echa un vistazo a tus tareas  pendientes.")
label.place(x = 175, y = 30)

main_list = Listbox(root, height = 10, width = 60)
main_list.place(x = 50, y = 75)

def actualizar_listbox():
    # Realizar la consulta para obtener las tareas
    query = 'SELECT t.id, t.nombre AS tarea, m.nombre AS materia, t.fecha_entrega FROM Tareas t LEFT JOIN Materias m ON t.materia_id = m.id;'
    cur.execute(query)
    result = cur.fetchall()

    main_list.delete(0, END)

    for tarea in result:
        main_list.insert(END, f'{tarea}')
    
#Botones
btn1 = Button(root, text = "Exit", fg = "black", bg = "white", command = exit, borderwidth = 3, relief = 'solid')
btn1.place(x = 400, y = 300, width = 100, height = 50)

btn2 = Button(root, text = "Añadir tareas", fg = "white", bg = "purple", command = tasks, borderwidth = 3, relief = 'solid')
btn2.place(x = 100, y = 300, width = 100, height = 50)

btn3 = Button(root, text = "Eliminar", fg = 'white', bg = 'red', command = eliminar, borderwidth = 3, relief = "solid")
btn3.place(x = 250, y = 300, width = 100, height = 50)

btn4 = Button(root, text = 'Actualizar', borderwidth = 3, relief = 'solid', command = actualizar_listbox)
btn4.pack(side = LEFT, anchor = 'sw')
def keypress_handler(e):
    #Si se presiona la tecla ESC, se llama a esta función (No sé por qué no funciona :c)
    if e.keycode == 27:
        exit()

root.bind('<KeyPress>', keypress_handler)

root.mainloop()
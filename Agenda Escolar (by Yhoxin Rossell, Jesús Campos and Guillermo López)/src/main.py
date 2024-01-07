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
from datetime import *
import mariadb
import sys

route = ''

'''
Base de datos
'''

try:
    conn = mariadb.connect(
        user = 'root',
        host = 'localhost',
        port = 3306,
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

##############################################################################################################

'''
Funciones y ventana de gestión de tareas
'''

#Función que crea la ventana de agregar tarea
def v_tareas():

    #Mensaje de éxito en caso de que se guarden los datos correctamente
    def aviso():
        a = messagebox.showinfo('Información', 'Datos guardados correctamente')
        if a:
            Tasks_window.destroy()

    #Función que se llama cuando se presiona el botón de guardar tarea
    def guardar_tarea():
        try: 
            nombre = nombre_tarea.get()
            materia = materia_entry.get()
            id_materia = next(key for key, value in opciones.items() if value == materia)
            description_text = descripcion.get(1.0, "end-1c") 
            fecha_entrega = cal.get_date()

            # Ejecuta la sentencia SQL para insertar los datos en la tabla "Tareas"
            cur.execute("INSERT INTO Tareas (nombre, descripcion, fecha_entrega, materia_id) VALUES (?, ?, ?, ?)",
                        (nombre, description_text, fecha_entrega, id_materia))
            conn.commit()

            print("[!] Data saved successfully")
            aviso()
            actualizar_listbox()
        
        except mariadb.Error as e:
            print(e)

    #Creación de la ventana
    Tasks_window = Tk()
    Tasks_window.geometry("600x400")
    Tasks_window.title("Agregar Tarea")

    #Entrada para el nombre de la tarea
    Label(Tasks_window, text = 'Nombre de la tarea:').pack()
    nombre_tarea = Entry(Tasks_window)
    nombre_tarea.pack()

    #Entrada para las materias
    Label(Tasks_window, text = 'Materia:').pack()
    query = 'select id, nombre from Materias;'
    cur.execute(query)
    result = cur.fetchall()
    opciones = {materia[0] : materia[1] for materia in result}
    materia_entry = ttk.Combobox(Tasks_window, values = list(opciones.values()))
    materia_entry.pack()

    #Entrada para añadir una descripción a la tarea
    Label(Tasks_window, text = 'Descripción:').pack()
    descripcion = Text(Tasks_window, height = 1, width = 40)
    descripcion.pack()

    #Calendario para establecer la fecha de entrega
    Label(Tasks_window, text = 'Fecha de entrega:').pack()
    cal = Calendar(Tasks_window, selectmode = 'day', day = 12, month = 12, year = 2023)
    cal.pack()

    #Botón para guardar los datos
    Button(Tasks_window, text = 'Guardar', command = guardar_tarea, borderwidth = 3, relief = 'solid').pack()

#Función para agregar una materia
def v_materias():

    #Mensaje de éxito en caso de que se guarden los datos correctamente
    def aviso():
        a = messagebox.showinfo('Información', 'Datos guardados correctamente')
        if a:
            Materias_window.destroy()

    def agregar_materia():
        try:
            nombre = nombre_materia.get()
            profesor = nombre_profesor.get()
            aula = nombre_aula.get()

            cur.execute('insert into Materias(nombre, profesor, aula) values (?,?,?)',
                        (nombre, profesor, aula))
            
            aviso()
            print("[!] Data saved successfully")
        
        except mariadb.Error as e:
            print(e)
    
    Materias_window = Tk()
    Materias_window.geometry("300x200")
    Materias_window.title("Agregar Materia")
    
    #Entrada para el nombre de la materia
    Label(Materias_window, text = 'Nombre de la materia:').pack()
    nombre_materia = Entry(Materias_window)
    nombre_materia.pack()

    #Entrada para el nombre del profesor que da la materia
    Label(Materias_window, text = 'Nombre del profesor:').pack()
    nombre_profesor = Entry(Materias_window)
    nombre_profesor.pack()

    #Entrada para el aula donde se da la materia
    Label(Materias_window, text = 'Aula: ').pack()
    nombre_aula = Entry(Materias_window)
    nombre_aula.pack()

    #Botón para guardar los cambios
    Button(Materias_window, text = 'Guardar', borderwidth = 3, relief = 'solid', command = agregar_materia).pack()

#Función para actualizar la listbox
def actualizar_listbox():
    #Realizar la consulta para obtener las tareas
    query = 'SELECT t.id, t.nombre AS tarea, m.nombre AS materia, t.fecha_entrega FROM Tareas t LEFT JOIN Materias m ON t.materia_id = m.id;'
    cur.execute(query)
    result = cur.fetchall()

    main_list.delete(0, END)

    for tarea in result:
        id_tarea = tarea[0]
        nombre_tarea = tarea[1]
        nombre_materia = tarea[2]
        fecha_entrega = tarea[3]

        formato = f'{id_tarea} - {nombre_tarea} - {nombre_materia} - Fecha: {fecha_entrega}'
        main_list.insert(END, formato)

#Función para eliminar una tarea
def eliminar_tarea():
    selecc = main_list.curselection()
    tarea_id = main_list.get(selecc[0])[0]
    if selecc:
        main_list.delete(selecc)
        cur.execute(f'delete from Tareas where id = {tarea_id}')
        conn.commit()
    print(f'[!] Task {tarea_id} eliminated successfully')
        
#Salir del programa
def exit():
    exit = messagebox.askyesno("Salir", "¿Salir del programa?")
    
    if exit: 
        root.quit()

##################################################################################################################################

'''
Bloque principal; listbox, menú y botones
'''

root = Tk()  
root.geometry("600x400")
root.title("AGENDA ESCOLAR")
label = Label(root, text = "¡BIENVENIDO A TU AGENDA ESCOLAR!\n"
              "Echa un vistazo a tus tareas  pendientes.")
label.place(x = 175, y = 30)

#Ventana emergente que muestra los detalles de una tarea agregada
def detalles(event):
    
    #Se cierra la ventana emergente al presionar el botón "Atrás"
    def salir_detalles():
        det.destroy()

    det = Toplevel()
    det.title('Detalles')

    index = main_list.curselection()[0]
    id_tarea = main_list.get(index) #.split('-')[0].strip()
    cur.execute('select t.nombre, m.nombre, m.profesor, m.aula, t.descripcion, t.fecha_entrega from Tareas t join Materias m on t.materia_id = m.id where t.id = %s;', (id_tarea,))
    result = cur.fetchone()

    Label(det, text = f'{result[0]}').pack()
    Label(det, text = f'Materia: {result[1]}').pack()
    Label(det, text = f'Profesor: {result[2]}').pack()
    Label(det, text = f'Aula: {result[3]}').pack()
    Label(det, text = f'Descripción: {result[4]}').pack()
    Label(det, text = f'Fecha tope: {result[5]}').pack()
    Button(det, text = 'Atrás', borderwidth = 3, relief = 'solid', command = salir_detalles).pack()

main_list = Listbox(root, height = 10, width = 60)
main_list.place(x = 50, y = 75)
main_list.bind('<<ListboxSelect>>', detalles)

#Botones
btn1 = Button(root, text = "Salir", fg = "black", bg = "white", command = exit, borderwidth = 3, relief = 'solid')
btn1.place(x = 400, y = 300, width = 100, height = 50)

btn2 = Button(root, text = "Añadir tareas", fg = "white", bg = "purple", command = v_tareas, borderwidth = 3, relief = 'solid')
btn2.place(x = 100, y = 300, width = 100)

btn3 = Button(root, text = "Eliminar", fg = 'white', bg = 'red', command = eliminar_tarea, borderwidth = 3, relief = "solid")
btn3.place(x = 250, y = 300, width = 100, height = 50)

btn4 = Button(root, text = 'Actualizar', borderwidth = 3, relief = 'solid', command = actualizar_listbox)
btn4.pack(side = 'right', anchor = 'sw')

btn5 = Button(root, text = 'Añadir materias', fg = 'white', bg = 'purple', borderwidth = 3, relief = 'solid', command = v_materias)
btn5.place(x = 82, y = 335)

#Si se presiona la tecla ESC, se llama a esta función
def keypress_handler(e):
    if e.keysym == 'Escape':
        exit()

root.bind('<KeyPress>', keypress_handler)

root.mainloop()
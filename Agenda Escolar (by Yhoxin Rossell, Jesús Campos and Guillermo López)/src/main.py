#Agenda Escolar
#Authors: Yhoxin Rossell, Guillermo López and Jesús

'''
IMPORTACIONES
'''
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as FileDialog
from tkcalendar import *
import core

route = ''


'''
Ventana de gestión de tareas
'''
def tasks():
    Tasks_window = Tk()
    Tasks_window.geometry("800x600")
    Tasks_window.title("TAREAS")

    '''def selection():
        var.get()'''

    #Valores necesarios para la lista de materias a elegir
    var = IntVar()
    valueMaterias = StringVar(Tasks_window)
    valueMaterias.set('Elige una materia')
    listMaterias = ['Auditoría de Sistemas', 'Defensa Integral VIII', 'Higiene y Seguridad Industrial', 'Marco Legal para el Ejercicio de la Ingeniería',
                    'Sistemas Avazados de Bases de Datos', 'Teoría de Decisiones', 'Teleprocesos', 'Tradición, Cultura y Folclor Local']
    
    #Botones de elección única para determinar si la tarea es un examen, un trabajo o una exposición
    radio1 = Radiobutton(Tasks_window, text = 'Trabajo', variable = var, value = 1).place(x = 100, y = 40)
    radio2 = Radiobutton(Tasks_window, text = 'Examen', variable = var, value = 2).place(x = 200, y = 40)
    radio3 = Radiobutton(Tasks_window, text = 'Exposición', variable = var, value = 3).place(x = 300, y = 40)

    #Labels para identificar cada campo
    Label(Tasks_window, text = 'Nombre:', font = ('Noto Sans', 12)).place(x = 100, y = 100)
    Label(Tasks_window, text = 'Materia:', font = ('Noto Sans', 12)).place(x = 100, y = 150)
    Label(Tasks_window, text = 'Añade una descripción', font = ('Noto Sans', 12)).place(x = 100, y = 225)
    Label(Tasks_window, text = 'Fecha', font = ('Noto Sans', 12)).place(x = 525, y = 225)

    #Botones para guardar y salir
    '''TO-DO: Añadir comandos para los botones'''
    Button(Tasks_window, text = 'Guardar')
    Button(Tasks_window, text = 'Salir')

    nombre_tarea = Text(Tasks_window, width = 35, height = 0, font = ('Noto Sans', 12))
    nombre_tarea.place(x = 200, y = 100)
    materias = OptionMenu(Tasks_window, valueMaterias, *listMaterias).place(x = 175, y = 150)
    descripcion = Text(Tasks_window, font = ('Noto Sans', 12),
                       width = 45, height = 5)
    descripcion.place(x = 100, y = 250)

    #Calendario para elegir la fecha de la tarea
    cal = Calendar(Tasks_window, selectmode = 'day', year = 2023, month = 11, day = 16)
    cal.place(x = 525, y = 250)

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
label.place(x = 175, y = 50)

#Botones
btn1 = Button(root, text = "Exit", fg = "black", bg = "white", command = exit, borderwidth = 3, relief = 'solid')
btn1.place(x = 400, y = 300, width = 100, height = 50)

btn2 = Button(root, text = "Añadir tareas", fg = "white", bg = "purple", command = tasks, borderwidth = 3, relief = 'solid')
btn2.place(x = 100, y = 300, width = 100, height = 50)

def keypress_handler(e):
    #Si se presiona la tecla ESC, se llama a esta función (No sé por qué no funciona :c)
    if e.keycode == 27:
        exit()

root.bind('<KeyPress>', keypress_handler)

root.mainloop()
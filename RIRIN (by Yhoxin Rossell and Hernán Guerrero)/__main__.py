#RIRIN
#By Yhoxin Rossell and Hernán Guerrero, 2022.

from tkinter import *
from tkinter import messagebox
import random
from tkinter import filedialog as FileDialog
from io import open

route = ''
#Nota del creador
def note():
    Note_window = Tk()
    Note_window.geometry("500x125")
    Note_window.title ("Creator note")
    label2 = Label(Note_window, text = "This is a simple program, exclusively created for people that are getting through a hard time.\nWe hope you can use this program everytime you don't feel okay.\nWe will always be there for you. <3 \n-Y & H")
    label2.pack()

#Función para mostrar frases motivacionales
def motivation():
    phrases = ["Keep it up! You're almost there!",
    "You are great, you are beautiful,\nyou are everything that's fine.",
    "Love yourself.",
    "You're an angel.",
    "You make everyone blind\nbecause you're shining bright.",
    "We dream with the day you'll be turning\ninto a succesful person.",
    "Look at the sky before you go to sleep...\nYou see? We're under the same sky as you,\neven though the time is different.",
    "You're never alone.",
    "My shoulder is yours if you need to cry.\nJust let it out. It's okay.~",
    "Be yourself, speak yourself",
    "If you can imagine it, you can make it true.\nThe only limit is your mind.",
    "Don't let anyone make you believe\nthat you can't do something."]
    Motiv_window = Tk()
    Motiv_window.geometry("300x150")
    Motiv_window.title ("Motivation for you")
    label2 = Label(Motiv_window, text = random.choice(phrases))
    label2.pack()   


def diary():
    Diary_window = Tk()
    Diary_window.geometry("800x600")
    Diary_window.title("My Diary")
    
    def nuevo():
        global route
        message.set("Nuevo file")
        route = ""
        Diary_text.delete(1.0, "end")
        Diary_window.title("Mi editor")

    def abrir():
        global route
        message.set("Open file")
        route = FileDialog.askopenfilename(
            initialdir = '.', 
            filetypes = (("Text files", "*.txt"),),
            title = "Open text file")

        if route != "":
            file = open(route, 'r')
            contenido = file.read()
            Diary_text.delete(1.0,'end')
            Diary_text.insert('insert', contenido)
            file.close()
            Diary_window.title(route + " - My Diary")

    def guardar():
        message.set("Save file")
        if route != "":
            contenido = Diary_text.get(1.0, 'end-1c')
            file = open(route, 'w+')
            file.write(contenido)
            file.close()
            message.set("File succesfully saved")
        else:
            guardar_como()

    def guardar_como():
        global route
        message.set("Save file as...")

        file = FileDialog.asksaveasfile(title = "Save file", 
            mode = "w", defaultextension = ".txt")

        if file is not None:
            route = file.name
            contenido = Diary_text.get(1.0, 'end-1c')
            file = open(route, 'w+')
            file.write(contenido)
            file.close()
            message.set("File succesfully saved")
        else:
            message.set("Operation cancelled")
            route = ""

    menubar = Menu(Diary_window)
    Diary_window.config(menu = menubar)

    filemenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "File", menu = filemenu)
    filemenu.add_command(label = "New", command = nuevo)
    filemenu.add_command(label = "Open", command = abrir)
    filemenu.add_command(label = "Save", command = guardar)
    filemenu.add_command(label = "Save File As...", command = guardar_como)
    filemenu.add_command(label = "Close")
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = Diary_window.quit)

    editmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "Edit", menu = editmenu)
    editmenu.add_command(label = "Cut") #Comandos aún no configurados
    editmenu.add_command(label = "Copy")
    editmenu.add_command(label = "Paste")

    helpmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    helpmenu.add_command(label = "About...")

    # Caja de texto central
    Diary_text = Text(Diary_window)
    Diary_text.pack(fill = 'both', expand = 1)
    Diary_text.config(padx = 6, pady = 4, bd = 0, font = ("Consolas", 12))

    # Monitor inferior (Esto no se muestra al pie de la ventana, no sé por qué :/)
    message = StringVar()
    message.set("Tell us how you feel ^^")
    monitor = Label(Diary_window, textvar = message, justify = 'left')
    monitor.pack(side = "left")

#Salir del programa
def exit():
    choice = messagebox.askyesno("Exit", "Exit program?")
    if choice == True:
        root.quit() 

#Bloque principal; menú y botones
root = Tk()  
root.geometry("600x400")
root.title("RIRIN: An app for motivation")
label = Label(root, text = "WELCOME!!!\nWe hope you feel good today~")
label.place(x = 200, y = 50, width = 200, height = 50)

#Botones del menú
btn = Button(root, text = "Read creator note", fg = "black", bg = "white", command = note)
btn.place(x = 100, y = 300, width = 100, height = 50)

btn2 = Button(root, text = "Show motivation~", fg = "white", bg = "blue", command = motivation)
btn2.place(x = 100, y = 150, width = 100, height = 50)

btn3 = Button(root, text = "Exit", fg = "black", bg = "white", command = exit)
btn3.place(x = 400, y = 300, width = 100, height = 50)

btn4 = Button(root, text = "Diary", fg = "white", bg = "purple", command = diary)
btn4.place(x = 400, y = 150, width = 100, height = 50)

root.mainloop()
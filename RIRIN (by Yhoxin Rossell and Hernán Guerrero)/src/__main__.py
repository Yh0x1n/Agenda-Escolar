#RIRIN
#By Yhoxin Rossell and Hernán Guerrero, 2022.
#Contributor: Douglas Socorro -> github: Douglas571

from threading import Thread
import queue
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as FileDialog
import core

route = ''

# A communication channel between 
# main thread and subthreads
EVENT_Q = queue.Queue()

#Nota del creador
def note():
    Note_window = Tk()
    Note_window.geometry("500x125")
    Note_window.title ("Creator note")
    label2 = Label(Note_window, text = "This is a simple program, exclusively created for people that are getting through a hard time.\nWe hope you can use this program everytime you don't feel okay.\nWe will always be there for you. <3 \n-Y & H")
    label2.pack()

def random_quote():
    """ This function create a new windows 
    with a random quote.
    """
    win = Tk()
    win.geometry("300x250")
    win.title ("Motivation for you")
    text = Label(win, text = 'searching...', wraplength = 300)
    text.pack()

    # A function to be executed 
    # concurrently in another thread.
    def search_quote():
        msg = core.get_random_quote()

        def update():
            text['text'] = msg

        EVENT_Q.put(lambda: update())
    
        btn = Button(win, text = "Search again", command = note)
        btn.pack(side = 'left', width = 100, height = 50)

        btn2 = Button(win, text = "Read quote offline", command = motivation)
        btn2.pack(side = 'right', width = 100, height = 50)
    # pass the above function to
    # be excecuted concurrently
    Thread(target = search_quote).start()

def quotes_table():
    """Create a new window for manage saved quotes"""
    win = Tk()
    win.geometry("400x300")
    win.title ("Quotes")
    win.grid()
    # win.columnconfigure(0, weight=1)
    # win.columnconfigure(1, weight=1)
    # win.rowconfigure(0, weight=1)
    # win.rowconfigure(1, weight=1)

    author_lb = Label(win, text = 'Author')
    author_etr = ttk.Entry(win, width = 30)
    
    # year_lb = Label(win, text='Year')

    content_lb = Label(win, text = 'Quote')
    content_txt = Text(win, height = 3, width = 22)

    def new_quote(etr):
        quote = etr.get()
        print(quote)

    btn = ttk.Button(win, text = 'New', command = lambda: new_quote(content_txt))
    author_lb.grid(column = 0, row = 0)
    author_etr.grid(column = 1, row = 0, columnspan = 2)

    content_lb.grid(column = 0, row = 1)
    content_txt.grid(column = 1, row = 1, rowspan = 2, columnspan = 2)

    btn.grid(column=2, row=3, padx=10, pady=10)

#Función para mostrar frases motivacionales
def motivation():
    msg = core.get_motivation_phrase()

    Motiv_window = Tk()
    Motiv_window.geometry("300x150")
    Motiv_window.title ("Motivation for you")
    label2 = Label(Motiv_window, text = msg)
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
    
     # Opciones del menú de Editar   
    def close_diary():
        choice = messagebox.askyesnocancel("Exit, Exit diary?\nIf you haven't saved your file, you might lose your progress.")
        if choice == True:
            guardar()
            Diary_window.quit()
        elif choice == False:
            Diary_window.quit()         
            
    def copiar():
        Diary_text.event_generate('<<Copy>>')
    
    def cortar():
        Diary_text.event_generate('<<Cut>>')
    
    def pegar():
        Diary_text.event_generate('<<Paste>>')
    
    def deshacer():
        Diary_text.event_generate('<<Undo>>')

    def rehacer():
        Diary_text.event_generate('<<Redo>>')
    ##############################

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
    filemenu.add_command(label = "Exit", command = close_diary)

    editmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = "Edit", menu = editmenu)
    editmenu.add_command(label = "Cut    Ctrl + X", command = cortar)
    editmenu.add_command(label = "Copy   Ctrl + C", command = copiar)
    editmenu.add_command(label = "Paste  Ctrl + V", command = pegar)
    editmenu.add_command(label = "Undo   Ctrl + Z", command = deshacer)
    editmenu.add_command(label = "Redo   Ctrl + Y", command = rehacer)

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
    exit = messagebox.askyesno("Exit", "Exit program?")
    
    if exit: 
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

# Use ttk for a more modern style
btn5 = ttk.Button(root, text='Random Quote', command=random_quote)
btn5.place(x = 250, y = 150, width = 100, height = 50)

btn6 = ttk.Button(root, text='Quotes', command=quotes_table)
btn6.place(x=100, y=225, width=100, height=50)

def keypress_handler(e):
    # Is press ESC key, call exit funciton.
    if e.keycode == 27:
        exit()

root.bind('<KeyPress>', keypress_handler)

UPDATE_RATE = 100
def update():
    # Review the communication channel 
    # and execute the functions into it.
    while not EVENT_Q.empty():
        f = EVENT_Q.get()
        f()    

    root.after(UPDATE_RATE, update)

root.after(UPDATE_RATE, update)
root.mainloop()
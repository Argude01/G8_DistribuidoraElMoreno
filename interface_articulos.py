from tkinter import *
from tkinter import ttk

window=Tk()
frame_app = Frame(window, width=900, height=580, bg="red3")
frame_app.pack()



def wakeup():
    window.destroy()

frame_titulo = Frame(frame_app, width= 900, height= 80, bg= "cornflower blue")
frame_titulo.place(x=0, y=0)

frame_answers = Frame(frame_app, width=700, height=500, bg="red3")
frame_answers.place(x=100, y=81)

frame_btn = Frame(frame_app, width=100, height=90, bg="red3")
frame_btn.place(x=800, y=480)

label_titulo = Label(frame_titulo, 
              text="ARTICULOS (EN DESARROLLO) ",
              font=("Century Gothic", "30", "bold"),
              bg="cornflower blue",
              fg="firebrick3")
label_titulo.place(x=10, y=10)

label_answer1 = Label(frame_answers, 
              text="Nombre del destinatario ",
              font=("Century Gothic", "14", "bold"),
              bg="red3",
              fg="white")
label_answer1.place(x=10, y=15)

entry_answer1 = Entry(frame_answers, width=80, 
             font=("Century Gothic", "15"))
entry_answer1.place(x=10, y=50)

label_answer2 = Label(frame_answers, 
              text="Nombre del proveedor ",
              font=("Century Gothic", "14", "bold"),
              bg="red3",
              fg="white")
label_answer2.place(x=10, y=115)

entry_answer2 = Entry(frame_answers, width=80, 
             font=("Century Gothic", "15"))
entry_answer2.place(x=10, y=150)

label_answer3 = Label(frame_answers, 
              text="Ubicación de la sucursal ",
              font=("Century Gothic", "14", "bold"),
              bg="red3",
              fg="white")
label_answer3.place(x=10, y=215)

entry_answer1 = Entry(frame_answers, width=80, 
             font=("Century Gothic", "15"))
entry_answer1.place(x=10, y=250)

label_answer4 = Label(frame_answers, 
              text="Nombre del Articulo ",
              font=("Century Gothic", "14", "bold"),
              bg="red3",
              fg="white")
label_answer4.place(x=10, y=315)

entry_answer4 = Entry(frame_answers, width=80, 
             font=("Century Gothic", "15"))
entry_answer4.place(x=10, y=350)

button_save = Button(frame_titulo, text="VOLVER A INICIO", 
                        font=("Century Gothic", "14", "bold"),
                        width=18,
                        height=2,
                        bg=("CadetBlue1"),
                        fg=("gray12"),
                        border=1,
                        command=wakeup)
button_save.place(x=610, y=10)


button_save = Button(frame_btn, text="ENVIAR", 
                        font=("Century Gothic", "12", "bold"),
                        width=8,
                        height=2,
                        bg=("CadetBlue1"),
                        fg=("gray12"),
                        border=1,
                        command="")
button_save.place(x=0, y=10)


window.mainloop()
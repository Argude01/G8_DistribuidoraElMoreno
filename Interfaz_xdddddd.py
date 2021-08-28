from tkinter import *
from tkinter import messagebox

window=Tk()
frame_app = Frame(window, width=900, height=580, bg="firebrick3")
frame_app.pack()




def Lol():
    rss=entry_answer1.get()
    rss2=entry_answer2.get()

    if rss == "Holaxd":
        
        if rss2 == "Jotron123":
            window.destroy()
            import welcome_interface
            
        else:messagebox.showerror(message="Contraseña o usuario incorrecto, intente de nuevo", title="DATOS INCORRECTOS")
            
    else:
        messagebox.showerror(message="Contraseña o usuario incorrecto, intente de nuevo", title="DATOS INCORRECTOS")

def cerrar():
    window.destroy()

frame_titulo = Frame(frame_app, width= 700, height= 80, bg= "azure3")
frame_titulo.place(x=100, y=0)

frame_answers = Frame(frame_app, width=700, height=300, bg="DodgerBlue3")
frame_answers.place(x=100, y=80)

frame_btn = Frame(frame_app, width=900, height=250, bg="firebrick3")
frame_btn.place(x=0, y=480)


label_titulo = Label(frame_titulo, 
              text="     DISTRIBUIDORA EL MORENO",
              font=("Century Gothic", "33", "bold"),
              bg="azure3",
              fg="grey23")
label_titulo.place(x=0, y=10)

label_titulo2 = Label(frame_answers, 
              text="Ingrese su usuario y contraseña",
              font=("Century Gothic", "25", "bold"),
              bg="DodgerBlue3",
              fg="azure3")
label_titulo2.place(x=100, y=25)

label_answer1 = Label(frame_answers, 
              text="USUARIO",
              font=("Century Gothic", "14", "bold"),
              bg="DodgerBlue3",
              fg="white")
label_answer1.place(x=310, y=115)

entry_answer1 = Entry(frame_answers, width=25, 
             font=("Century Gothic", "15"))
entry_answer1.place(x=215, y=150)

label_answer2 = Label(frame_answers, 
              text="CONTRASEÑA",
              font=("Century Gothic", "14", "bold"),
              bg="DodgerBlue3",
              fg="white")
label_answer2.place(x=285, y=215)

entry_answer2 = Entry(frame_answers, width=25, 
             font=("Century Gothic", "15"))
entry_answer2.place(x=215, y=250)

button_save = Button(frame_btn, text="SALIR", 
                        font=("Century Gothic", "20", "bold"),
                        width=16,
                       
                        bg=("azure3"),
                        fg=("gray12"),
                        border=1,
                        command=cerrar)
button_save.place(x=320, y=10)


button_save = Button(frame_app, text="INGRESAR", 
                        font=("Century Gothic", "20", "bold"),
                        width=12,
                        
                        bg=("azure3"),
                        fg=("gray12"),
                        border=1,
                        command= Lol)
button_save.place(x=355, y=390)


window.mainloop()
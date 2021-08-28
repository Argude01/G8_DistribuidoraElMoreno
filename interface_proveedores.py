from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import G8_datbase






def show_users():
    fila = 0 
    print(fila)
    print('data resultado: ' + str(G8_datbase.data))
    for user in G8_datbase.data:
        registro = user
        print ('variable registro: ' + str(registro))
        
        print(str(fila) + ' - ' + str(user))
        fila = fila + 1 


def GUARDAR():

    empresa = entry_answer1.get()
    nombre = entry_answer2.get()
    apellido = entry_answer3.get()
    id_pais = entry_answer4.get()
    
  
   
    lol_db = G8_datbase.MyDatabase()
    lol_db.insert_db2( empresa, nombre, apellido, id_pais)
    lol_db.read_db1()
    show_users()

def donda():
    messagebox.showinfo(message="Esta función no está disponible por ahora;(", title="Función en desarrollo")
    
def iluvtameimpala():
    window.destroy()
   

    

window=Tk()
frame_app = Frame(window, width=900, height=580, bg="firebrick3")
frame_app.pack()

frame_titulo = Frame(frame_app, width=900, height=85, bg="RoyalBlue3")
frame_titulo.place(x=0, y=0)

frame_contenido = Frame(frame_app, width=900, height=330, bg="firebrick3")
frame_contenido.place(x=0, y=86)

frame_botones = Frame (frame_app, width=900, height=157,bg="firebrick3")
frame_botones.place(x=0, y=417)

label_titulo = Label(frame_titulo,
              text="PROVEEDORES",
              font=("Century Gothic", "33", "bold"),
              bg="RoyalBlue3",
              fg="firebrick3")
label_titulo.place(x=10, y=10)


label_answer1 = Label(frame_contenido,
              text="NOMBRE",
              font=("Century Gothic", "17", "bold"),
              bg="firebrick3",
              fg="black")
label_answer1.place(x=30, y=30)

entry_answer1 = Entry(frame_contenido, width=20, 
             font=("Century Gothic", "12"))
entry_answer1.place(x=200, y=30)

label_answer2 = Label(frame_contenido,
              text="EMPRESA",
              font=("Century Gothic", "17", "bold"),
              bg="firebrick3",
              fg="black")
label_answer2.place(x=430, y=30)

entry_answer2 = Entry(frame_contenido, width=20, 
             font=("Century Gothic", "12"))
entry_answer2.place(x=603, y=30)

label_answer3 = Label(frame_contenido,
              text="APELLIDO",
              font=("Century Gothic", "17", "bold"),
              bg="firebrick3",
              fg="black")
label_answer3.place(x=30, y=200)

entry_answer3 = Entry(frame_contenido, width=20, 
             font=("Century Gothic", "12"))
entry_answer3.place(x=200, y=200)

label_answer4 = Label(frame_contenido,
              text="PAIS",
              font=("Century Gothic", "17", "bold"),
              
              bg="firebrick3",
              fg="black")
label_answer4.place(x=430, y=150)

label_answer4 = Label(frame_contenido,
              text="ID del país",
              font=("Century Gothic", "17", "bold"),
              
              bg="firebrick3",
              fg="black")
label_answer4.place(x=600, y=150)


combo= Combobox(frame_contenido, 
                values=[
                    "1.México",
                    "2.Alemania",
                    "3.Honduras",
                    "4.Estados Unidos",
                    "5.Colombia",
                    "6.China",
                    "7.Japón",
                    "8.Brasil",
                    "9.Argentina",
                    "10.Canadá",
                    "11.España",
                    "12.Rusia",
                    "13.Venezuela",
                    "14.Taiwán",
                    "15.Uruguay",
                    "16.Albania",
                    "17.Reino Unido",
                    "18.Perú",	
                    "19.Portugal",
                    "20.Islandia",
                ])
combo.place(x=430, y=200)



entry_answer4 = Entry(frame_contenido, width=20, 
             font=("Century Gothic", "12"))
entry_answer4.place(x=603, y=200)


button_save = Button(frame_botones, text="GUARDAR", 
                        font=("Century Gothic", "14", "bold"),
                        width=15,
                        height=2,
                        bg=("CadetBlue1"),
                        fg=("NavajoWhite4"),
                        border=1,
                        command=GUARDAR)
button_save.place(x=110, y=10)

button_save = Button(frame_botones, text="ELIMINAR", 
                        font=("Century Gothic", "14", "bold"),
                        width=15,
                        height=2,
                        bg=("CadetBlue1"),
                        fg=("NavajoWhite4"),
                        border=1,
                        command=donda)
button_save.place(x=350, y=10)

button_save = Button(frame_botones, text="REGRESAR", 
                        font=("Century Gothic", "14", "bold"),
                        width=15,
                        height=2,
                        bg=("CadetBlue1"),
                        fg=("NavajoWhite4"),
                        border=1,
                        command=iluvtameimpala)
button_save.place(x=600, y=10)

window.mainloop()
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
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

def SAVE():

    nombre_sucursal = entry_cont1.get()
    id_pais = entry_cont2.get()
    id_estado = entry_cont3.get()
    ubicacion = entry_cont4.get()
    nombre_gerente = entry_cont5.get()
    telelfono = entry_cont6.get()
    
    

    lol_db = G8_datbase.MyDatabase()
    lol_db.insert_db( nombre_sucursal, id_pais, id_estado, ubicacion, nombre_gerente, telelfono)
    lol_db.read_db1()
    show_users()

    messagebox.showinfo(message="Su registro fue exitoso;))",title="REGISTRO EXITOSO")


def lolmoment():
    window.destroy()
    
    
    


window=Tk()
frame_app = Frame(window, width=900, height=580, bg="orangered3")
frame_app.pack()

frame_titulo = Frame(frame_app, width=900, height=80, bg="orangered4")
frame_titulo.place(x= 0, y=0)

frame_cont = Frame(frame_app, width=700, height=380, bg="orangered3")
frame_cont.place(x=90, y=81)

frame_btn = Frame(frame_app, width=900, height=100, bg="orangered3")
frame_btn.place(x=0, y=470)


combo= Combobox(frame_cont, 
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
combo.place(x=5, y=80)


combo= Combobox(frame_cont, 
                values=[
                    "1.CDM",
                    "2.Nuevo León",
                    "3.Chiapas",
                    "4.Bavaria",
                    "5.Berlín",
                    "6.Hamburgo",
                    "7.Francisco Morazán",
                    "8.Valle",
                    "9.Cortés",
                    "10.Texas",
                    "11.Nueva York",
                    "12.Maryland",
                    "13.Pekín",
                    "14.Jilín",
                    "15.Tokyo",
                    "16.Osaka",
                    "17.Río de Janeiro",
                    "18.Moto Grosso",	
                    "19.Sao Paulo"
                    "20.Buenos Aires",
                ])
combo.place(x=5, y=150)

label_titulo = Label (frame_titulo,
              text="ARTICULOS ",
              font=("Century Gothic", "33", "bold"),
              bg="orangered4",
              fg="burlywood2")
label_titulo.place(x=10, y=10)


label_cont = Label (frame_cont,
              text="SUCURSAL ",
              font=("Century Gothic", "14", "bold"),
              bg="orangered3",
              fg="salmon2")
label_cont.place(x=5, y=10)

entry_cont1 = Entry(frame_cont, width=45, 
             font=("Century Gothic", "15"))
entry_cont1.place(x=175, y=10)


label_cont = Label (frame_cont,
              text="PAÍS (1-20)",
              font=("Century Gothic", "14", "bold"),
              bg="orangered3",
              fg="salmon2")
label_cont.place(x=5, y=45)

entry_cont2 = Entry(frame_cont, width=45, 
             font=("Century Gothic", "15"))
entry_cont2.place(x=175, y=45)

label_cont = Label (frame_cont,
              text="CIUDAD/ESTADO ",
              font=("Century Gothic", "14", "bold"),
              bg="orangered3",
              fg="salmon2")
label_cont.place(x=5, y=115)

entry_cont3 = Entry(frame_cont, width=45, 
             font=("Century Gothic", "15"))
entry_cont3.place(x=175, y=115)


label_cont = Label (frame_cont,
              text="DIRECCIÓN ",
              font=("Century Gothic", "14", "bold"),
              bg="orangered3",
              fg="salmon2")
label_cont.place(x=5, y=185)

entry_cont4 = Entry(frame_cont, width=45, 
             font=("Century Gothic", "15"))
entry_cont4.place(x=175, y=185)

label_cont = Label (frame_cont,
              text="GERENTE ",
              font=("Century Gothic", "14", "bold"),
              bg="orangered3",
              fg="salmon2")
label_cont.place(x=5, y=255)


entry_cont5 = Entry(frame_cont, width=45, 
             font=("Century Gothic", "15"))
entry_cont5.place(x=175, y=255)

label_cont = Label (frame_cont,
              text="TELEFONO ",
              font=("Century Gothic", "14", "bold"),
              bg="orangered3",
              fg="salmon2")
label_cont.place(x=5, y=325)

entry_cont6 = Entry(frame_cont, width=45,
             font=("Century Gothic", "15"))
entry_cont6.place(x=175, y=325)


button_save = Button(frame_btn, text="SALIR", 
                        font=("Century Gothic", "14", "bold"),
                        width=16,
                        height=2,
                        bg=("burlywood2"),
                        fg=("black"),
                        border=1,
                        command=lolmoment)
button_save.place(x=180, y=10)



button_save = Button(frame_btn, text="AGREGAR", 
                        font=("Century Gothic", "14", "bold"),
                        width=16,
                        height=2,
                        bg=("burlywood2"),
                        fg=("black"),
                        border=1,
                        command=SAVE)
button_save.place(x=480, y=10)


window.mainloop()
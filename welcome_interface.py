from tkinter import *
from tkinter import messagebox


window=Tk()
frame_app = Frame(window, width=900, height=580, bg="brown3")
frame_app.pack()



def pnten():
    
    import interface_articulos1
       

def abrir2():
    
    import interface_proveedores
   
def abrir3():
    
    import inerface_sucursale
    
    
    

def abrir4():
    messagebox.showerror(message="Esta pantalla presenta errores y funciones no acabadas, regrese a la pantalla de inicio.",title="PANTALLA EN DESARROLLO")
    import interface_articulos
    

def cerrar():
    window.destroy()



frame_welcome = Frame(frame_app, width=860, height=90, bg="cadetblue2")
frame_welcome.place(x=20, y =20)

frame_botones = Frame(frame_app, width=860, height=430, bg="cadetblue2")
frame_botones.place(x=20, y =140)

label_tituloxd = Label(frame_welcome,
              text="BIENVENIDOS :D",
              font=("Century Gothic", "36", "bold"),
              bg="brown3",
              fg="black")
label_tituloxd.place(x=220, y=15)


label_tituloxd = Label(frame_botones,
              text="    ELIJA UNA OPCIÓN",
              font=("Century Gothic", "20", "bold"),
              bg="cadetblue2",
              fg="black")
label_tituloxd.place(x=240, y=15)



button_save = Button(frame_botones, text="HACER ENVIOS", 
                        font=("Century Gothic", "20", "bold"),
                        width=16,
                        height=2,
                        bg=("brown3"),
                        fg=("black"),
                        border=1,
                        command=pnten)
button_save.place(x=80, y=90)


button_save = Button(frame_botones, text="PROVEEDORES", 
                        font=("Century Gothic", "20", "bold"),
                        width=16,
                        height=2,
                        bg=("brown3"),
                        fg=("black"),
                        border=1,
                        command=abrir2)
button_save.place(x=500, y=90)


button_save = Button(frame_botones, text="SUCURSALES", 
                        font=("Century Gothic", "20", "bold"),
                        width=16,
                        height=2,
                        bg=("brown3"),
                        fg=("black"),
                        border=1,
                        command=abrir3)
button_save.place(x=80, y=220)


button_save = Button(frame_botones, text="ARTICULOS", 
                        font=("Century Gothic", "20", "bold"),
                        width=16,
                        height=2,
                        bg=("brown3"),
                        fg=("black"),
                        border=1,
                        command=abrir4)
button_save.place(x=500, y=220)

button_save = Button(frame_botones, text="SALIR", 
                        font=("Century Gothic", "20", "bold"),
                        width=16,
                        height=2,
                        bg=("brown3"),
                        fg=("black"),
                        border=1,
                        command=cerrar)
button_save.place(x=280, y=330)

window.mainloop()
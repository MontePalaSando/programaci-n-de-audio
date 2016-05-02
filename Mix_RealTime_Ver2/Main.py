#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
from  ArchivoOpen import Abrir1
from  ArchivoOpen import Abrir2
from  ArchivoOpen import Abrir3
from  ArchivoOpen import Abrir4
from  ArchivoOpen import reproduce1
from  ArchivoOpen import reproduce2
from  ArchivoOpen import reproduce3
from  ArchivoOpen import reproduce4
from ArchivoOpen import reproduce


def main():

    # Creacion de la ventana

    ventana = Tk()

    ventana.title("Ventana Principal")
    ventana.config(bg = "black")

    d = BooleanVar(ventana)
    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    global arreglo1

    arreglo1 = []


    # Uso de frames para organizar la ventana.
    frame1 = Frame(ventana,bg = "black")
    frame1.pack(side=TOP)
    frame2 = Frame(ventana,bg = "black")
    frame2.pack(side=TOP)
    frame3 = Frame(ventana,bg = "black")
    frame3.pack(side=TOP)
    frame4 = Frame(ventana,bg = "black")
    frame4.pack(side=TOP)
    frame5 = Frame(ventana,bg = "black")
    frame5.pack(side=TOP)

    def AbrirArchivo1():
        d.set(True)
        Abrir1()
        mensaje1.pack(side=LEFT)
        ReproButton1.pack(side=LEFT)


    def AbrirArchivo2():
        d.set(True)
        Abrir2()
        mensaje2.pack(side=LEFT)
        ReproButton2.pack(side=LEFT)

    def AbrirArchivo3():
        d.set(True)
        Abrir3()
        mensaje3.pack(side=LEFT)
        ReproButton3.pack(side=LEFT)

    def AbrirArchivo4():
        d.set(True)
        Abrir4()
        mensaje4.pack(side=LEFT)
        ReproButton4.pack(side=LEFT)

    def Reproducir1():
        d.set(True)
        reproduce1()

    def Reproducir2():
        d.set(True)
        reproduce2()

    def Reproducir3():
        d.set(True)
        reproduce3()

    def Reproducir4():
        d.set(True)
        reproduce4()

    def ReproducirMain():
        d.set(True)
        reproduce()



    # Creacion de botones.

    Titulo = Label(frame1, fg='red', padx=15, pady=10, text='Mixer Reproductor',bg = "black")
    Titulo.pack(side=TOP)
    Titulo1 = Label(frame1, fg='red', padx=15, pady=10, text='Luis Sandoval, Andres Palacio, Libardo Montealegre',bg = "black")
    Titulo1.pack(side=TOP)


    OpenButton1 = Button(frame1, padx=30, pady=2, text="Abrir Archivo 1", command=AbrirArchivo1,bg = "blue",fg="white")
    OpenButton1.pack(side=TOP)
    OpenButton2 = Button(frame2, padx=30, pady=2, text="Abrir Archivo 2", command=AbrirArchivo2,bg = "blue",fg="white")
    OpenButton2.pack(side=LEFT)
    OpenButton3 = Button(frame3, padx=30, pady=2, text="Abrir Archivo 3", command=AbrirArchivo3,bg = "blue",fg="white")
    OpenButton3.pack(side=LEFT)
    OpenButton4 = Button(frame4, padx=30, pady=2, text="Abrir Archivo 4", command=AbrirArchivo4,bg = "blue",fg="white")
    OpenButton4.pack(side=LEFT)

    # Mensajes de de  archivos  cargados.
    mensaje1 = Label(frame1, fg='green', padx=15, pady=10, text='Archivo 1 Cargado',bg = "black")
    mensaje2 = Label(frame2, fg='green', padx=15, pady=10, text='Archivo 2 Cargado',bg = "black")
    mensaje3 = Label(frame3, fg='green', padx=15, pady=10, text='Archivo 3 Cargado',bg = "black")
    mensaje4 = Label(frame4, fg='green', padx=15, pady=10, text='Archivo 4 Cargado',bg = "black")

    ReproButton1 = Button(frame1, padx=30, pady=2, text="Reproducir Archivo 1", command=Reproducir1,bg = "green",fg="black")
    ReproButton2 = Button(frame2, padx=30, pady=2, text="Reproducir Archivo 2", command=Reproducir2,bg = "green",fg="black")
    ReproButton3 = Button(frame3, padx=30, pady=2, text="Reproducir Archivo 3", command=Reproducir3,bg = "green",fg="black")
    ReproButton4 = Button(frame4, padx=30, pady=2, text="Reproducir Archivo 3", command=Reproducir4,bg = "green",fg="black")


     # Boton de reproduccion
    ReproMainButton1 = Button(frame5, padx=30, pady=2, text="Reproducir Mezcla",bg = "green",fg="black", command=ReproducirMain)
    ReproMainButton1.pack(side=TOP)

    ventana.mainloop()

if __name__ == "__main__":
    main()

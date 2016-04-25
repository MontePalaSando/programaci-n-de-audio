#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
from  ArchivoOpen import reproduce1
from  ArchivoOpen import Abrir1
from ArchivoOpen import Audio1
import tkMessageBox
from Delay_Audio import GenerarDelay
from Reproduccion import reproduce


def Main3():

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
    frame6 = Frame(ventana,bg = "black")
    frame6.pack(side=TOP)
    frame7 = Frame(ventana,bg = "black")
    frame7.pack(side=TOP)

    def AbrirArchivo1():
        d.set(True)
        Abrir1()
        mensaje1.pack(side=LEFT)
        ReproButton1.pack(side=LEFT)

    def Reproducir1():
        d.set(True)
        reproduce1()



    def Delay3():

        if e2.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso la cantidad de repeticiones.')

        if e6.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso los milisegundos.')

        if e4.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:
            d.set(True)
            Repe= int( e2.get())
            Time= float(e6.get())
            Niveles = float(Nivel.get())
            Nombre = e4.get()
            DelayA=GenerarDelay(Time,Repe)
            DelayA.DelayOn()
            DelayA.NivelModificado(Niveles)
            DelayA.GenerarAudio1(Nombre)


    def ReproducirMain():
        nombre = e4.get()
        reproduce(nombre)



    cuadro= Label(frame1, padx=15, pady=1, text="DELAY 3 ",fg = "red",bg = "black")
    cuadro.pack(side=TOP)
    cuadro1= Label(frame1, padx=15, pady=1, text="Luis Sandoval , Andres Palacio, Libardo Montealegre",fg = "red",bg = "black")
    cuadro1.pack(side=TOP)

    OpenButton1 = Button(frame2, padx=30, pady=2, text="Abrir Archivo 1",command= AbrirArchivo1 ,bg = "blue",fg="white")
    OpenButton1.pack(side=LEFT)

    mensaje1 = Label(frame2, fg='green',bg = "black", padx=15, pady=10, text='Archivo 1 Cargado')

    ReproButton1 = Button(frame2, padx=30, pady=2, text="Reproducir Archivo 1", command=Reproducir1,bg = "green",fg="black")

    cuadro3= Label(frame3, padx=15, pady=10, text="Digite la cantidad de repeticiones:",fg = "white",bg = "black")
    cuadro3.pack(side=LEFT)
    e2 = Entry(frame3, bd=5, insertwidth=1)
    e2.pack(side=LEFT, padx=15, pady=10)

    cuadro4= Label(frame4, padx=15, pady=10, text="Cantidad de milisegundos",fg = "white",bg = "black")
    cuadro4.pack(side=LEFT)
    e6 = Entry(frame4, bd=5, insertwidth=1)
    e6.pack(side=LEFT, padx=15, pady=10)

    cuadro5= Label(frame5, padx=15, pady=10, text="Nombre del Archivo a generar",fg = "white",bg = "black")
    cuadro5.pack(side=LEFT)
    e4 = Entry(frame5, bd=5, insertwidth=1)
    e4.pack(side=LEFT, padx=15, pady=10)

    cuadro2= Label(frame6, padx=15, pady=10, text="VOLUMEN",fg = "blue",bg = "black")
    cuadro2.pack(side=TOP)

    Nivel = Scale(frame6, from_= -20.0, to=0.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "black", fg="white")
    Nivel.pack(side=TOP, padx=1, pady=1)

    cuadro6= Label(frame6, padx=15, pady=2, text="",fg = "white",bg = "black")
    cuadro6.pack(side=TOP)


    GenerarButton1 = Button(frame7, padx=30, pady=2, text="Generar Archivo",bg = "red",fg="white",command= Delay3)
    GenerarButton1.pack(side=LEFT)

    ReproducirButton1 = Button(frame7, padx=30, pady=2, text="Reproducir",bg = "green",fg="black",command=ReproducirMain )
    ReproducirButton1.pack(side=LEFT)


    ventana.mainloop()

if __name__ == "__main__":
    Main3()
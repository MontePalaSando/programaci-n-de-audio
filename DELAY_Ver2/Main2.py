#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
from Main3 import Main3
import tkMessageBox
from Delay_Frames import GenerarRetraso
from Reproduccion import reproduce


def Main2():

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

# se obtienen los valores para el archivo de audio y se grafica segun un retraso de la senal en pi
    def Delay():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso frecuencia a generar.')

        if e2.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso duracion del audio.')

        if e4.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:
            d.set(True)
            Frecuencia = int( e1.get())
            Time = int( e2.get())
            Frames = int(44100*(1/float(e1.get())/2.0))
            Nombre = e4.get()
            Niveles = Nivel.get()

            Delay1 = GenerarRetraso(Time,Frecuencia,Frames)
            Delay1.generar()
            Delay1.NivelModificado(Niveles)
            Delay1.GenerarAudio1(Nombre)
            Delay1.graficar()


# se obtienen los valores para el archivo de audio y se grafica segun un retraso de la senal en pi medios
    def Delay2():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso frecuencia a generar.')

        if e2.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso duracion del audio.')

        if e4.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:
            d.set(True)
            Frecuencia = int( e1.get())
            Time = int( e2.get())
            Frames = int(44100*(1/float(e1.get())/4.0))
            Nombre = e4.get()
            Niveles = Nivel.get()

            Delay1 = GenerarRetraso(Time,Frecuencia,Frames)
            Delay1.generar()
            Delay1.NivelModificado(Niveles)
            Delay1.GenerarAudio1(Nombre)
            Delay1.graficar()


# se obtienen los valores para el archivo de audio y se grafica segun un retraso de la senal en pi cuartos
    def Delay3():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso frecuencia a generar.')

        if e2.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso duracion del audio.')

        if e4.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:
            d.set(True)
            Frecuencia = int( e1.get())
            Time = int( e2.get())
            Frames = int(44100*(1/float(e1.get())/8.0))
            Nombre = e4.get()
            Niveles = Nivel.get()

            Delay1 = GenerarRetraso(Time,Frecuencia,Frames)
            Delay1.generar()
            Delay1.NivelModificado(Niveles)
            Delay1.GenerarAudio1(Nombre)
            Delay1.graficar()


# se obtienen los valores para el archivo de audio y se grafica segun un retraso de la senal en pi octavos
    def Delay4():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso frecuencia a generar.')

        if e2.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso duracion del audio.')

        if e4.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:
            d.set(True)
            Frecuencia = int( e1.get())
            Time = int( e2.get())
            Frames = int(44100*(1/float(e1.get())/16.0))
            Nombre = e4.get()
            Niveles = Nivel.get()

            Delay1 = GenerarRetraso(Time,Frecuencia,Frames)
            Delay1.generar()
            Delay1.NivelModificado(Niveles)
            Delay1.GenerarAudio1(Nombre)
            Delay1.graficar()

# funcion para cerrar la ventana actual y abrir el main
    def Ventana3():
        ventana.destroy()
        Main3()

# funcion que reproduce el audio final
    def ReproducirMain():
        nombre = e4.get()
        reproduce(nombre)

# Label para la interfraz grafica - definicion de los botones
    cuadro= Label(frame1, padx=15, pady=1, text="DELAY 2 ",fg = "red",bg = "black")
    cuadro.pack(side=TOP)
    cuadro1= Label(frame1, padx=15, pady=1, text="Luis Sandoval , Andres Palacio, Libardo Montealegre",fg = "red",bg = "black")
    cuadro1.pack(side=TOP)

    cuadro2= Label(frame2, padx=15, pady=10, text="Digite la frecuencia a generar:",fg = "white",bg = "black")
    cuadro2.pack(side=LEFT)
    e1 = Entry(frame2, bd=5, insertwidth=1)
    e1.pack(side=LEFT, padx=15, pady=10)

    cuadro3= Label(frame3, padx=15, pady=10, text="Digite la duracion del Audio:",fg = "white",bg = "black")
    cuadro3.pack(side=LEFT)
    e2 = Entry(frame3, bd=5, insertwidth=1)
    e2.pack(side=LEFT, padx=15, pady=10)


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

    GenerarButton1 = Button(frame7, padx=30, pady=2, text="Generar pi",bg = "red",fg="white",command=Delay)
    GenerarButton1.pack(side=LEFT)

    GenerarButton2 = Button(frame7, padx=30, pady=2, text="Generar pi/2",bg = "red",fg="white",command=Delay2)
    GenerarButton2.pack(side=LEFT)

    GenerarButton3 = Button(frame7, padx=30, pady=2, text="Generar pi/4",bg = "red",fg="white",command=Delay3)
    GenerarButton3.pack(side=LEFT)

    GenerarButton4 = Button(frame7, padx=30, pady=2, text="Generar pi/8",bg = "red",fg="white",command=Delay4)
    GenerarButton4.pack(side=LEFT)

    ReproducirButton1 = Button(frame7, padx=30, pady=2, text="Reproducir",bg = "green",fg="black",command=ReproducirMain )
    ReproducirButton1.pack(side=LEFT)

    NextButton1 = Button(frame7, padx=30, pady=2, text=" Delay 3",bg = "blue",fg="white",command= Ventana3)
    NextButton1.pack(side=LEFT)


    ventana.mainloop()

if __name__ == "__main__":
    Main2()
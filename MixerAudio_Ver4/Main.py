#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from  ArchivoOpen import Abrir1
from  ArchivoOpen import Abrir2
from  ArchivoOpen import Abrir3
from  AudioMono2 import  GenerarMix2
from  AudioMono2 import  GenerarAudio2
from AudioMono2 import NivelModificado2
from  AudioMono1 import GenerarMix1
from  AudioMono1 import  GenerarAudio1
from AudioMono1 import  NivelModificado
from  AudioStereo3 import GenerarMix3
from  AudioStereo3 import  GenerarAudio3
from AudioStereo3 import NivelModificado3
from AudioStereo3 import NivelModificado4
from  ArchivoOpen import reproduce1
from  ArchivoOpen import reproduce2
from  ArchivoOpen import reproduce3
from Reproduccion import reproduce


def main():
    Frecuenciadesampleo = 44100
    MaxBits = 16

    # Creacion de la ventana

    ventana = Tk()

    ventana.title("Ventana Principal")

    d = BooleanVar(ventana)
    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    global arreglo1

    arreglo1 = []


    # Uso de frames para organizar la ventana.
    frame1 = Frame(ventana)
    frame1.pack(side=TOP)
    frame2 = Frame(ventana)
    frame2.pack(side=TOP)
    frame3 = Frame(ventana)
    frame3.pack(side=TOP)
    frame4 = Frame(ventana)
    frame4.pack(side=TOP)
    frame5 = Frame(ventana)
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

    def Reproducir1():
        d.set(True)
        reproduce1()

    def Reproducir2():
        d.set(True)
        reproduce2()

    def Reproducir3():
        d.set(True)
        reproduce3()


    def Mezclar1():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')
        else:
            d.set(True)
            Niveles = Nivel.get()
            e1.configure(state='disabled')
            GenerarMix1()
            NivelModificado(Niveles)
            nombre= e1.get()
            GenerarAudio1(nombre)
            ReproMainButton1.pack(side=LEFT)

    def Mezclar2():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')
        else:
            d.set(True)
            Niveles = Nivel.get()
            e1.configure(state='disabled')
            GenerarMix2()
            NivelModificado2(Niveles)
            nombre= e1.get()
            GenerarAudio2(nombre)
            ReproMainButton1.pack(side=LEFT)

    def Mezclar3():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')
        else:
            d.set(True)
            Niveles = Nivel.get()
            e1.configure(state='disabled')
            GenerarMix3()
            NivelModificado3(Niveles)
            NivelModificado4(Niveles)
            nombre= e1.get()
            GenerarAudio3(nombre)
            ReproMainButton1.pack(side=LEFT)

    def ReproducirMain():
        nombre = e1.get()
        reproduce(nombre)

    # Creacion de botones.

    OpenButton1 = Button(frame1, padx=30, pady=2, text="Abrir Archivo 1", command=AbrirArchivo1,bg = "blue",fg="white")
    OpenButton1.pack(side=LEFT)

    OpenButton2 = Button(frame2, padx=30, pady=2, text="Abrir Archivo 2", command=AbrirArchivo2,bg = "blue",fg="white")
    OpenButton2.pack(side=LEFT)

    OpenButton3 = Button(frame3, padx=30, pady=2, text="Abrir Archivo 3", command=AbrirArchivo3,bg = "blue",fg="white")
    OpenButton3.pack(side=LEFT)

    # Mensajes de grabacion activada.
    mensaje1 = Label(frame1, fg='green', padx=15, pady=10, text='Archivo 1 Cargado')
    mensaje2 = Label(frame2, fg='green', padx=15, pady=10, text='Archivo 2 Cargado')
    mensaje3 = Label(frame3, fg='green', padx=15, pady=10, text='Archivo 3 Cargado')

    ReproButton1 = Button(frame1, padx=30, pady=2, text="Reproducir Archivo 1", command=Reproducir1,bg = "green",fg="black")
    ReproButton2 = Button(frame2, padx=30, pady=2, text="Reproducir Archivo 2", command=Reproducir2,bg = "green",fg="black")
    ReproButton3 = Button(frame3, padx=30, pady=2, text="Reproducir Archivo 3", command=Reproducir3,bg = "green",fg="black")

    # Creacion e insercion del cuadro de texto 1.
    cuadro= Label(frame4, padx=15, pady=10, text="Digite el nombre del archivo:")
    cuadro.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 1.
    e1 = Entry(frame4, bd=5, insertwidth=1)
    e1.pack(side=LEFT, padx=15, pady=10)

     # Creacion e insercion del cuadro de texto 1.
    cuadro2= Label(frame5, padx=15, pady=10, text="VOLUMEN")
    cuadro2.pack(side=TOP)
    Nivel = Scale(frame5, from_= -20.0, to=0.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "black", fg="white")
    Nivel.pack(side=TOP, padx=1, pady=1)
    GenerarButton1 = Button(frame5, padx=30, pady=2, text="Generar Mezcla 1", command= Mezclar1,bg = "white",fg="black")
    GenerarButton1.pack(side=LEFT)
    GenerarButton2 = Button(frame5, padx=30, pady=2, text="Generar Mezcla 2", command= Mezclar2,bg = "black",fg="white")
    GenerarButton2.pack(side=LEFT)
    GenerarButton3 = Button(frame5, padx=30, pady=2, text="Generar Mezcla 3(Stereo)", command= Mezclar3,bg = "red",fg="black")
    GenerarButton3.pack(side=LEFT)
    ReproMainButton1 = Button(frame5, padx=30, pady=2, text="Reproducir Mezcla", command= ReproducirMain,bg = "green",fg="black")


    ventana.mainloop()

if __name__ == "__main__":
    main()

from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from grabar import Grabar
import pyaudio
from Metronomo import Metro

def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # Creacion de la ventana

    ventana = Tk()

    ventana.title("Ventana Principal")
    audio1 = Grabar(CHUNK, FORMAT, CHANNELS, RATE)

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


    # Creacion e insercion del cuadro de texto 1.
    cuadro= Label(frame1, fg="black", padx=15, pady=1, text="Digite el nombre del archivo 1:")
    cuadro.pack(side=TOP)

    # Creacion e insercion de cuadro de entrada 1.
    e1 = Entry(frame1, bd=5, insertwidth=1)
    e1.pack(side=TOP, padx=15, pady=1)

    cuadro= Label(frame1, fg="black", padx=15, pady=1, text="Digite la nota del metronomo:")
    cuadro.pack(side=TOP)

    Nota = Scale(frame1, from_=1, to=12,length = 200, orient= HORIZONTAL )
    Nota.pack(side=TOP, padx=1, pady=1)

    cuadro= Label(frame1, fg="black", padx=15, pady=1, text="Digite el BPM del metronomo:")
    cuadro.pack(side=TOP)

    Tempo = Scale(frame1, from_=40, to=240,length = 200, orient= HORIZONTAL )
    Tempo.pack(side=TOP, padx=1, pady=1)

    cuadro= Label(frame1, fg="black", padx=15, pady=1, text="Digite el volumne del metronomo :")
    cuadro.pack(side=TOP)

    Nivel = Scale(frame1, from_= -20.0, to=0.0,length = 200, orient= HORIZONTAL, resolution=0.1 )
    Nivel.pack(side=TOP, padx=1, pady=1)

    # Mensajes de grabacion activada.
    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Grabando...')

    # Funcion activa mensaje y grabar

    def activasms1():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:

            Notas = Nota.get()
            Niveles = Nivel.get()
            BPM = Tempo.get()
            onda = Metro(CHUNK, FORMAT, CHANNELS, RATE,Notas,Niveles,BPM)
            onda.metrono()
            d.set(True)
            e1.configure(state='disabled')
            audio1.inicio()
            mensaje1.pack(side=LEFT)
            while d.get():
                audio1.grabacion()
                ventana.update()
                if d.get() is False:
                    break



    # Funcion desactiva mensaje y para de grabar.
    def desactivasms1():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        global  arreglo1
        arreglo1 = audio1.parar()

        audio1.creaAudio(e1.get())
        grabarButton1.pack_forget()
        pararButton1.pack_forget()





    def reproduccion1():
        audio1.reproduce(e1.get())



    # Creacion de botones.
    grabarButton1 = Button(frame2, padx=30, pady=5, text="Grabar", command=activasms1)
    grabarButton1.pack(side=LEFT)

    pararButton1 = Button(frame2, padx=30, pady=5, text="Parar", command=desactivasms1)
    pararButton1.pack(side=LEFT)

    reproducirButton1 = Button(frame2, padx=20,pady=5, text="Reproducir", command=reproduccion1)
    reproducirButton1.pack(side=RIGHT)



    ventana.mainloop()

if __name__ == "__main__":
    main()
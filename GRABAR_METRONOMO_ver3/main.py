#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from grabar import Grabar
import pyaudio
from Metronomo4Cuartos import Metro44
from Metronomo2Cuartos import Metro24
from Metronomo3Cuartos import Metro34
from Metronomo5Cuartos import Metro54

def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # Creacion de la ventana

    ventana = Tk()

    ventana.title("Ventana Principal")
    ventana.config(bg = "black")
    audio1 = Grabar(CHUNK, FORMAT, CHANNELS, RATE)

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

    mensaje3 = Label(frame1, fg='red', padx=15, pady=10, text='GRABADOR-METRONOMO',bg = "black" )
    mensaje3.pack(side=TOP)

    # Creacion e insercion del cuadro de texto 1.
    cuadro= Label(frame1, padx=15, pady=1, text="Digite el nombre del archivo 1:",bg = "black", fg="white")
    cuadro.pack(side=TOP)

    # Creacion e insercion de cuadro de entrada 1.
    e1 = Entry(frame1, bd=5, insertwidth=1)
    e1.pack(side=TOP, padx=15, pady=1)

    cuadro= Label(frame1, padx=15, pady=1, text="Digite la nota del metronomo:",bg = "black", fg="white")
    cuadro.pack(side=TOP)

    Nota = Scale(frame1, from_=1, to=12,length = 200, orient= HORIZONTAL,bg = "red", fg="white" )
    Nota.pack(side=TOP, padx=1, pady=1)

    cuadro= Label(frame1, padx=15, pady=1, text="Digite el BPM del metronomo:",bg = "black", fg="white")
    cuadro.pack(side=TOP)

    Tempo = Scale(frame1, from_=40, to=240,length = 200, orient= HORIZONTAL,bg = "white", fg="black" )
    Tempo.pack(side=TOP, padx=1, pady=1)

    cuadro= Label(frame1, padx=15, pady=1, text="Digite el volumne del metronomo :",bg = "black", fg="white")
    cuadro.pack(side=TOP)

    Nivel = Scale(frame1, from_= -20.0, to=0.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "black", fg="white")
    Nivel.pack(side=TOP, padx=1, pady=1)

    # Mensajes de grabacion activada.
    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Grabando...',bg = "black" )

    # Funcion activa mensaje y grabar

    def activasms1():

        if e1.get() == '':
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')

        else:
            d.set(True)
            e1.configure(state='disabled')
            audio1.inicio()
            mensaje1.pack(side=LEFT)
            while d.get():
                audio1.grabacion()
                ventana.update()
                if d.get() is False:
                    break

    def Metro():

        opcion = var.get()
        if opcion == 1:
            d.set(True)
            e1.configure(state='disabled')
            while d.get():
                Notas = Nota.get()
                Niveles = Nivel.get()
                BPM = Tempo.get()
                onda = Metro24(CHUNK, FORMAT, CHANNELS, RATE,Notas,Niveles,BPM)
                onda.metrono1()
                ventana.update()
                if d.get() is False:
                    break

        if opcion == 2:
            d.set(True)
            e1.configure(state='disabled')
            while d.get():
                Notas = Nota.get()
                Niveles = Nivel.get()
                BPM = Tempo.get()
                onda = Metro34(CHUNK, FORMAT, CHANNELS, RATE,Notas,Niveles,BPM)
                onda.metrono2()
                ventana.update()
                if d.get() is False:
                    break

        if opcion == 3:
            d.set(True)
            e1.configure(state='disabled')
            while d.get():
                Notas = Nota.get()
                Niveles = Nivel.get()
                BPM = Tempo.get()
                onda = Metro44(CHUNK, FORMAT, CHANNELS, RATE,Notas,Niveles,BPM)
                onda.metrono44()
                ventana.update()
                if d.get() is False:
                    break

        if opcion == 4:
            d.set(True)
            e1.configure(state='disabled')
            while d.get():
                Notas = Nota.get()
                Niveles = Nivel.get()
                BPM = Tempo.get()
                onda = Metro54(CHUNK, FORMAT, CHANNELS, RATE,Notas,Niveles,BPM)
                onda.metrono3()
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
        MetroButton1.pack_forget()
        InsButton1.pack_forget()

    def Instruc():
        tkMessageBox._show('Instrucciones de Uso', '1. Ingresar nombre del archivo \n'+ '2. Ingresar parametros del Metronomo \n'+ '3. Oprimir "Grabar" \n'+ '4. Oprimir "Metronomo"  \n'+ '5. Al terminar de grabar oprima "Parar" \n'+ '5. Oprima "Reproducir" para escuchar \n' )

    def reproduccion1():
        audio1.reproduce(e1.get())

    # Creacion de botones.

    cuadro6= Label(frame2,padx=20,pady=5, text=" ",bg = "black", fg="white")
    cuadro6.pack(side=TOP)

    grabarButton1 = Button(frame2, padx=30, pady=5, text="Grabar",command= activasms1,bg = "red" )
    grabarButton1.pack(side=LEFT)

    pararButton1 = Button(frame2, padx=30, pady=5, text="Parar", command=desactivasms1,bg = "black",  fg="white")
    pararButton1.pack(side=LEFT)

    reproducirButton1 = Button(frame2, padx=20,pady=5, text="Reproducir", command=reproduccion1,bg = "green")
    reproducirButton1.pack(side=LEFT)

    MetroButton1 = Button(frame2, padx=20,pady=5, text="Metronomo", command=Metro,bg = "blue",fg="white")
    MetroButton1.pack(side=LEFT)

    InsButton1 = Button(frame2, padx=20,pady=5, text="Instrucciones de uso", command=Instruc,bg = "orange" )
    InsButton1.pack(side=LEFT)

    var = IntVar()

    cuadro6= Label(frame1, padx=15, pady=1, text="Metrica del metronomo:",bg = "black", fg="white")
    cuadro6.pack(side=TOP)

    R1 = Radiobutton(frame1, padx=20,pady=5, text="2/4", variable=var, value=1,bg = "black", fg="red")
    R1.pack( side=LEFT )

    R2 = Radiobutton(frame1, padx=20,pady=5,  text="3/4", variable=var, value=2,bg = "black", fg="red")
    R2.pack( side=LEFT )

    R3 = Radiobutton(frame1, padx=20,pady=5,  text="4/4", variable=var, value=3,bg = "black", fg="red")
    R3.pack( side=LEFT )

    R4 = Radiobutton(frame1,padx=20,pady=5,  text="5/4", variable=var, value=4,bg = "black", fg="red")
    R4.pack( side=LEFT )

    ventana.mainloop()

if __name__ == "__main__":
    main()
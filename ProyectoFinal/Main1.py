#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
import numpy as np
import wave
import struct
from EQ1 import EQ1
from EQ2 import EQ2
from EQ3 import EQ3
from EQ4 import EQ4
from Grabar import Grabador1
from Grabar2 import Grabador2
from Grabar3 import Grabador3
from Grabar4 import Grabador4
from Niveles import NivelModificado1
from Niveles import NivelModificado2
from Niveles import NivelModificado3
from Niveles import NivelModificado4
from Niveles import NivelModificadoMix
from Archivar import file
from itertools import izip_longest
from MixRealTime import RealTimePLay1
import pygame.mixer
from Reproduccion import reproduce

import  pyaudio

def Main1():
    global reproducir
    reproducir=0
    # Creacion de la ventana

    ventana = Tk()
    ventana.title("Proyecto Final")
    ventana.config(bg = "black")

    d = BooleanVar(ventana)
    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio1 = Grabador1(CHUNK, FORMAT, CHANNELS, RATE)
    audio2 = Grabador2(CHUNK, FORMAT, CHANNELS, RATE)
    audio3 = Grabador3(CHUNK, FORMAT, CHANNELS, RATE)
    audio4 = Grabador4(CHUNK, FORMAT, CHANNELS, RATE)

    global Array1,Array2,Array3,Array4
    global Rec1,Rec2,Rec3,Rec4
    global ArrayFinal1,ArrayFinal2,ArrayFinal3,ArrayFinal4
    global ArrayComprimido1, ArrayComprimido2, ArrayComprimido3, ArrayComprimido4
    global FinalArray1,FinalArray2,FinalArray3,FinalArray4
    global MezclaFinalFinal,MezclaMixFinal
    global FinalArrayAux1,FinalArrayAux2,FinalArrayAux3,FinalArrayAux4
    global MezclaAUXFINAL, MezclaMixAux

    # Arreglos globales
    Array1 = []
    Array2 = []
    Array3 = []
    Array4 = []

    #Los de la grabacion
    Rec1 = []
    Rec2 = []
    Rec3 = []
    Rec4 = []

    #Arreglos comprimidos del Audio
    ArrayComprimido1= []
    ArrayComprimido2= []
    ArrayComprimido3= []
    ArrayComprimido4= []


     # Arreglos finales antes del fader
    ArrayFinal1 = []
    ArrayFinal2 = []
    ArrayFinal3 = []
    ArrayFinal4 = []

    # Arreglos finales antes del fader

    FinalArray1= []
    FinalArray2= []
    FinalArray3= []
    FinalArray4= []


    MezclaFinalFinal= []
    MezclaMixFinal = []

    #Arreglos de envio de AUX
    FinalArrayAux1 = []
    FinalArrayAux2 = []
    FinalArrayAux3 = []
    FinalArrayAux4 = []
    MezclaAUXFINAL = []
    MezclaMixAux = []


    audiocom1=BooleanVar(ventana)
    audiocom1.set(False)


    # Uso de frames para organizar la ventana.

    frame1 = Frame(ventana,bg = "black")
    frame1.pack(side=TOP)
    frame2 = Frame(ventana,bg = "black")
    frame2.pack(side=LEFT)
    frame3 = Frame(ventana,bg = "black")
    frame3.pack(side=LEFT)
    frame4 = Frame(ventana,bg = "black")
    frame4.pack(side=LEFT)
    frame5 = Frame(ventana,bg = "black")
    frame5.pack(side=LEFT)
    frame6 = Frame(ventana,bg = "black")
    frame6.pack(side=LEFT)
    frame7 = Frame(ventana,bg = "black")
    frame7.pack(side=LEFT)

    #PARTE FUNCIONES DE GRABACION POR CANAL !!!--------------------------------------------------------------------------

#Chanel 1 -----------------------------------------------------------

    def Grabar1():
        d.set(True)
        audio1.inicio()
        mensaje1.pack(side=TOP)
        while d.get():
                audio1.grabacion()
                ventana.update()
                if d.get() is False:
                    break
    def Stop1():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        Nombre ='AudioUno'
        global Array1, Rec1
        Rec1 = audio1.parar()
        audio1.creaAudio(Nombre)
        RecordButton1.configure(state='disabled')
        StopButton1.configure(state='disabled')
        file = wave.open(Nombre+'.wav','rb')
        tamano = int(file.getnframes())
        for i in range (0,tamano):
            dato=file.readframes(1)
            packed_value = struct.unpack('<h', dato)
            Array1.append(packed_value)

#Chanel 2 -----------------------------------------------------------
    def Grabar2():
        d.set(True)
        audio2.inicio()
        mensaje1.pack(side=TOP)
        while d.get():
                audio2.grabacion()
                ventana.update()
                if d.get() is False:
                    break
    def Stop2():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        Nombre ='AudioDos'
        global Array2, Rec2
        Rec2 = audio2.parar()
        audio2.creaAudio(Nombre)
        RecordButton2.configure(state='disabled')
        StopButton2.configure(state='disabled')
        file = wave.open(Nombre+'.wav','rb')
        tamano = int(file.getnframes())
        for i in range (0,tamano):
            dato=file.readframes(1)
            packed_value = struct.unpack('<h', dato)
            Array2.append(packed_value)
#Chanel 3------------------------------------------------------------
    def Grabar3():
        d.set(True)
        audio3.inicio()
        mensaje1.pack(side=TOP)
        while d.get():
                audio3.grabacion()
                ventana.update()
                if d.get() is False:
                    break
    def Stop3():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        Nombre ='AudioTres'
        global Array3, Rec3
        Rec3 = audio3.parar()
        audio3.creaAudio(Nombre)
        RecordButton3.configure(state='disabled')
        StopButton3.configure(state='disabled')
        file = wave.open(Nombre+'.wav','rb')
        tamano = int(file.getnframes())
        for i in range (0,tamano):
            dato=file.readframes(1)
            packed_value = struct.unpack('<h', dato)
            Array3.append(packed_value)

# Chanel 4---------------------------------------------
    def Grabar4():
        d.set(True)
        audio4.inicio()
        mensaje1.pack(side=TOP)
        while d.get():
                audio4.grabacion()
                ventana.update()
                if d.get() is False:
                    break
    def Stop4():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        Nombre ='AudioCuatro'
        global Array4, Rec4
        Rec4 = audio4.parar()
        audio4.creaAudio(Nombre)
        RecordButton4.configure(state='disabled')
        StopButton4.configure(state='disabled')
        file = wave.open(Nombre+'.wav','rb')
        tamano = int(file.getnframes())
        for i in range (0,tamano):
            dato=file.readframes(1)
            packed_value = struct.unpack('<h', dato)
            Array4.append(packed_value)

# PARTE FUNCION DE COMPRESORES ------------------------------------------------------------------------------------------------------------------------

    def Equal1():
        if Eq1.get()==1:

            EQ1()
    def Equal2():
        if Eq2.get()==1:
            EQ2()
    def Equal3():
        if Eq3.get()==1:
            EQ3()
    def Equal4():
        if Eq4.get()==1:
            EQ4()


# PARTE REPRODUCIR


    def Compresor1():

        compresor=Tk()

        compresor.title("Compresor 1 ")
        compresor.config(bg = "black")

        # Uso de frames para organizar la ventana.
        frame1 = Frame(compresor,bg = "black")
        frame1.pack(side=TOP)

        global Array1, ArrayComprimido1

        def compresoraudio1():

            NivelThresh=Threshold.get()
            Thresh1 = (10**float(NivelThresh/20))*((2**16)/2.0)
            Attack1=float(Attack.get()/1000.0)
            CuadrosAttack=int(Attack1*44100)
            ratio=Ratio.get()
            Knee=float((ratio-1)/CuadrosAttack)

            ArregloAttack=[]

            for j in range(1, CuadrosAttack):
                Dato1=1+float(Knee*j)
                ArregloAttack.append(Dato1)


            for i in range(0, len(Array1)):

                if Array1[i][0]>Thresh1:
                    if i<CuadrosAttack:
                        c=Array1[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array1[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                if Array1[i][0]<(Thresh1*(-1)):
                    if i<CuadrosAttack:
                        c=Array1[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array1[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                else:
                    Amp=Array1[i][0]

                ArrayComprimido1.append(Amp)

        Label1= Label(frame1, padx=15, pady=1, text="Compresor 1",fg = "white",bg = "black")
        Label1.pack(side=TOP)

        espacio2= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio2.pack(side=TOP)

        #threshold
        Label2= Label(frame1, padx=15, pady=1, text="Threshold",fg = "white",bg = "black")
        Label2.pack(side=TOP)
        Threshold= Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=-60,to=0,bg = "yellow", fg="black")
        Threshold.pack(side=TOP)

        #ratio
        Label3= Label(frame1, padx=15, pady=1, text="Ratio",fg = "white",bg = "black")
        Label3.pack(side=TOP)
        Ratio=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=9,to=0,bg = "blue", fg="white")
        Ratio.pack(side=TOP)

        #attack
        Label4= Label(frame1, padx=15, pady=1, text="Attack",fg = "white",bg = "black")
        Label4.pack(side=TOP)
        Attack=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=50,to=500,bg = "red", fg="white")
        Attack.pack(side=TOP)

        #realease
        Label5= Label(frame1, padx=15, pady=1, text="Release",fg = "white",bg = "black")
        Label5.pack(side=TOP)
        Release=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=4000,to=5,fg = "white",bg = "black")
        Release.pack(side=TOP)

        #gain
        Label6= Label(frame1, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
        Label6.pack(side=TOP)
        Gain=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=40,to=0,bg = "white", fg="black")
        Gain.pack(side=TOP)

        espacio1= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio1.pack(side=TOP)

        # Comprimir
        ComprimirButton1 = Button(frame1, padx=30, pady=2, text="Comprimir",bg = "red",fg="white",command= compresoraudio1)
        ComprimirButton1.pack(side=TOP)

        compresor.mainloop()
    def Compresor2():

        compresor=Tk()

        compresor.title("Compresor 2 ")
        compresor.config(bg = "black")

        # Uso de frames para organizar la ventana.
        frame1 = Frame(compresor,bg = "black")
        frame1.pack(side=TOP)

        global Array2, ArrayComprimido2

        def compresoraudio2():

            NivelThresh=Threshold.get()
            Thresh1 = (10**float(NivelThresh/20))*((2**16)/2.0)
            Attack1=float(Attack.get()/1000.0)
            CuadrosAttack=int(Attack1*44100)
            ratio=Ratio.get()
            Knee=float((ratio-1)/CuadrosAttack)

            ArregloAttack=[]

            for j in range(1, CuadrosAttack):
                Dato1=1+float(Knee*j)
                ArregloAttack.append(Dato1)


            for i in range(0, len(Array2)):

                if Array2[i][0]>Thresh1:
                    if i<CuadrosAttack:
                        c=Array2[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array2[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                if Array2[i][0]<(Thresh1*(-1)):
                    if i<CuadrosAttack:
                        c=Array2[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array2[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                else:
                    Amp=Array2[i][0]

                ArrayComprimido2.append(Amp)

        Label1= Label(frame1, padx=15, pady=1, text="Compresor 2",fg = "white",bg = "black")
        Label1.pack(side=TOP)

        espacio2= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio2.pack(side=TOP)

        #threshold
        Label2= Label(frame1, padx=15, pady=1, text="Threshold",fg = "white",bg = "black")
        Label2.pack(side=TOP)
        Threshold= Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=-60,to=0,bg = "yellow", fg="black")
        Threshold.pack(side=TOP)

        #ratio
        Label3= Label(frame1, padx=15, pady=1, text="Ratio",fg = "white",bg = "black")
        Label3.pack(side=TOP)
        Ratio=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=9,to=0,bg = "blue", fg="white")
        Ratio.pack(side=TOP)

        #attack
        Label4= Label(frame1, padx=15, pady=1, text="Attack",fg = "white",bg = "black")
        Label4.pack(side=TOP)
        Attack=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=50,to=500,bg = "red", fg="white")
        Attack.pack(side=TOP)

        #realease
        Label5= Label(frame1, padx=15, pady=1, text="Release",fg = "white",bg = "black")
        Label5.pack(side=TOP)
        Release=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=4000,to=5,fg = "white",bg = "black")
        Release.pack(side=TOP)

        #gain
        Label6= Label(frame1, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
        Label6.pack(side=TOP)
        Gain=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=40,to=0,bg = "white", fg="black")
        Gain.pack(side=TOP)

        espacio1= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio1.pack(side=TOP)

        # Comprimir
        ComprimirButton1 = Button(frame1, padx=30, pady=2, text="Comprimir",bg = "red",fg="white",command= compresoraudio2)
        ComprimirButton1.pack(side=TOP)

        compresor.mainloop()
    def Compresor3():

        compresor=Tk()

        compresor.title("Compresor 3 ")
        compresor.config(bg = "black")

        # Uso de frames para organizar la ventana.
        frame1 = Frame(compresor,bg = "black")
        frame1.pack(side=TOP)

        global Array3, ArrayComprimido3

        def compresoraudio3():

            NivelThresh=Threshold.get()
            Thresh1 = (10**float(NivelThresh/20))*((2**16)/2.0)
            Attack1=float(Attack.get()/1000.0)
            CuadrosAttack=int(Attack1*44100)
            ratio=Ratio.get()
            Knee=float((ratio-1)/CuadrosAttack)

            ArregloAttack=[]

            for j in range(1, CuadrosAttack):
                Dato1=1+float(Knee*j)
                ArregloAttack.append(Dato1)


            for i in range(0, len(Array3)):

                if Array3[i][0]>Thresh1:
                    if i<CuadrosAttack:
                        c=Array3[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array3[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                if Array3[i][0]<(Thresh1*(-1)):
                    if i<CuadrosAttack:
                        c=Array3[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array3[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                else:
                    Amp=Array3[i][0]

                ArrayComprimido3.append(Amp)

        Label1= Label(frame1, padx=15, pady=1, text="Compresor 3",fg = "white",bg = "black")
        Label1.pack(side=TOP)

        espacio2= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio2.pack(side=TOP)

        #threshold
        Label2= Label(frame1, padx=15, pady=1, text="Threshold",fg = "white",bg = "black")
        Label2.pack(side=TOP)
        Threshold= Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=-60,to=0,bg = "yellow", fg="black")
        Threshold.pack(side=TOP)

        #ratio
        Label3= Label(frame1, padx=15, pady=1, text="Ratio",fg = "white",bg = "black")
        Label3.pack(side=TOP)
        Ratio=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=9,to=0,bg = "blue", fg="white")
        Ratio.pack(side=TOP)

        #attack
        Label4= Label(frame1, padx=15, pady=1, text="Attack",fg = "white",bg = "black")
        Label4.pack(side=TOP)
        Attack=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=50,to=500,bg = "red", fg="white")
        Attack.pack(side=TOP)

        #realease
        Label5= Label(frame1, padx=15, pady=1, text="Release",fg = "white",bg = "black")
        Label5.pack(side=TOP)
        Release=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=4000,to=5,fg = "white",bg = "black")
        Release.pack(side=TOP)

        #gain
        Label6= Label(frame1, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
        Label6.pack(side=TOP)
        Gain=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=40,to=0,bg = "white", fg="black")
        Gain.pack(side=TOP)

        espacio1= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio1.pack(side=TOP)

        # Comprimir
        ComprimirButton1 = Button(frame1, padx=30, pady=2, text="Comprimir",bg = "red",fg="white",command= compresoraudio3)
        ComprimirButton1.pack(side=TOP)

        compresor.mainloop()
    def Compresor4():

        compresor=Tk()

        compresor.title("Compresor 4 ")
        compresor.config(bg = "black")

        # Uso de frames para organizar la ventana.
        frame1 = Frame(compresor,bg = "black")
        frame1.pack(side=TOP)

        global Array4, ArrayComprimido4

        def compresoraudio4():

            NivelThresh=Threshold.get()
            Thresh1 = (10**float(NivelThresh/20))*((2**16)/2.0)
            Attack1=float(Attack.get()/1000.0)
            CuadrosAttack=int(Attack1*44100)
            ratio=Ratio.get()
            Knee=float((ratio-1)/CuadrosAttack)

            ArregloAttack=[]

            for j in range(1, CuadrosAttack):
                Dato1=1+float(Knee*j)
                ArregloAttack.append(Dato1)


            for i in range(0, len(Array4)):

                if Array4[i][0]>Thresh1:
                    if i<CuadrosAttack:
                        c=Array4[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array4[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                if Array4[i][0]<(Thresh1*(-1)):
                    if i<CuadrosAttack:
                        c=Array4[i][0]-Thresh1
                        k=float(c/ArregloAttack[i])
                        Amp=k+Thresh1
                    if i >CuadrosAttack:
                        c=Array4[i][0]-Thresh1
                        k=float(c/ratio)
                        Amp=k+Thresh1
                else:
                    Amp=Array4[i][0]

                ArrayComprimido4.append(Amp)

        Label1= Label(frame1, padx=15, pady=1, text="Compresor 1",fg = "white",bg = "black")
        Label1.pack(side=TOP)

        espacio2= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio2.pack(side=TOP)

        #threshold
        Label2= Label(frame1, padx=15, pady=1, text="Threshold",fg = "white",bg = "black")
        Label2.pack(side=TOP)
        Threshold= Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=-60,to=0,bg = "yellow", fg="black")
        Threshold.pack(side=TOP)

        #ratio
        Label3= Label(frame1, padx=15, pady=1, text="Ratio",fg = "white",bg = "black")
        Label3.pack(side=TOP)
        Ratio=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=9,to=0,bg = "blue", fg="white")
        Ratio.pack(side=TOP)

        #attack
        Label4= Label(frame1, padx=15, pady=1, text="Attack",fg = "white",bg = "black")
        Label4.pack(side=TOP)
        Attack=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=50,to=500,bg = "red", fg="white")
        Attack.pack(side=TOP)

        #realease
        Label5= Label(frame1, padx=15, pady=1, text="Release",fg = "white",bg = "black")
        Label5.pack(side=TOP)
        Release=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=4000,to=5,fg = "white",bg = "black")
        Release.pack(side=TOP)

        #gain
        Label6= Label(frame1, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
        Label6.pack(side=TOP)
        Gain=Scale(frame1, orient=HORIZONTAL,width=10, length=250,from_=40,to=0,bg = "white", fg="black")
        Gain.pack(side=TOP)

        espacio1= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
        espacio1.pack(side=TOP)

        # Comprimir
        ComprimirButton1 = Button(frame1, padx=30, pady=2, text="Comprimir",bg = "red",fg="white",command= compresoraudio4)
        ComprimirButton1.pack(side=TOP)

        compresor.mainloop()

    def PLAY():

        global Array1,Array2,Array3,Array4
        global Rec1,Rec2,Rec3,Rec4
        global ArrayFinal1,ArrayFinal2,ArrayFinal3,ArrayFinal4
        global ArrayComprimido1, ArrayComprimido2, ArrayComprimido3, ArrayComprimido4
        global FinalArray1,FinalArray2,FinalArray3,FinalArray4
        global MezclaFinalFinal,MezclaMixFinal

        ArrayFinal1 = np.asarray(Array1)
        ArrayFinal2 = np.asarray(Array2)
        ArrayFinal3 = np.asarray(Array3)
        ArrayFinal4 = np.asarray(Array4)

        ArregloCom1=np.asanyarray(ArrayComprimido1)
        ArregloCom2=np.asanyarray(ArrayComprimido2)
        ArregloCom3=np.asanyarray(ArrayComprimido3)
        ArregloCom4=np.asanyarray(ArrayComprimido4)

        #COMPRESOR 1
        if Compre1.get()==0:
            FinalArray1= NivelModificado1(ArrayFinal1,Nivel.get())
            if mute1.get()==1:#MUTE ON
                FinalArray1= (FinalArray1*0)
            if mute1.get()==0:#MUTE OFF
                FinalArray1= (FinalArray1*1)

        if Compre1.get()==1:
            FinalArray1=NivelModificado1(ArregloCom1,Nivel.get())
            if mute1.get()==1:#MUTE ON
                FinalArray1= (FinalArray1*0)
            if mute1.get()==0:#MUTE OFF
                FinalArray1= (FinalArray1*1)

        #COMPRESOR 2
        if Compre2.get()==0:
            FinalArray2= NivelModificado2(ArrayFinal2,Nivel2.get())
            if mute2.get()==1:#MUTE ON
                FinalArray2= (FinalArray2*0)
            if mute2.get()==0:#MUTE OFF
                FinalArray2= (FinalArray2*1)

        if Compre2.get()==1:
            FinalArray2=NivelModificado2(ArregloCom2,Nivel2.get())
            if mute2.get()==1:#MUTE ON
                FinalArray2= (FinalArray2*0)
            if mute2.get()==0:#MUTE OFF
                FinalArray2= (FinalArray2*1)

        #COMPRESOR 3
        if Compre3.get()==0:
            FinalArray3= NivelModificado3(ArrayFinal3,Nivel3.get())
            if mute3.get()==1:#MUTE ON
                FinalArray3= (FinalArray3*0)
            if mute3.get()==0:#MUTE OFF
                FinalArray3= (FinalArray3*1)

        if Compre3.get()==1:
            FinalArray3=NivelModificado3(ArregloCom3,Nivel3.get())
            if mute3.get()==1:#MUTE ON
                FinalArray3= (FinalArray2*0)
            if mute3.get()==0:#MUTE OFF
                FinalArray3= (FinalArray2*1)

        #COMPRESOR 4
        if Compre4.get()==0:
            FinalArray4= NivelModificado4(ArrayFinal4,Nivel4.get())
            if mute4.get()==1:#MUTE ON
                FinalArray4= (FinalArray4*0)
            if mute4.get()==0:#MUTE OFF
                FinalArray4= (FinalArray4*1)

        if Compre4.get()==1:
            FinalArray4=NivelModificado4(ArregloCom4,Nivel4.get())
            if mute4.get()==1:#MUTE ON
                FinalArray4= (FinalArray4*0)
            if mute4.get()==0:#MUTE OFF
                FinalArray4= (FinalArray4*1)

        # MEZCLA !!

        MezclaFinalFinal= [w+x+y+z for w,x,y,z in izip_longest(FinalArray1,FinalArray2,FinalArray3,FinalArray4,fillvalue=0)]
        MixFinalFinal= np.asarray(MezclaFinalFinal)
        NivelFaderMix= Nivel6.get()
        MezclaMixFinal= NivelModificadoMix(MixFinalFinal,NivelFaderMix)

        #REPRODUCCION EN TIEMPO REAL

        PlayRealTime=[]

        p=pyaudio.PyAudio()
        stream=p.open(format=2,channels=1,rate=44100,output=True)

        for k in range(0, len(MezclaMixFinal)):
            packed_value = struct.pack('<h', MezclaMixFinal[k])
            PlayRealTime.append(packed_value)



        value_str=''.join(PlayRealTime)
        stream.write(value_str)
        stream.close()

    def Aux():
        #ENVIO DE AUXILIAR

        global FinalArrayAux1,FinalArrayAux2,FinalArrayAux3,FinalArrayAux4
        global MezclaAUXFINAL, MezclaMixAux

        FinalArrayAux1= NivelModificado1(ArrayFinal4,ReverbNivel1.get())
        FinalArrayAux2= NivelModificado1(ArrayFinal4,ReverbNivel2.get())
        FinalArrayAux3= NivelModificado1(ArrayFinal4,ReverbNivel3.get())
        FinalArrayAux4= NivelModificado1(ArrayFinal4,ReverbNivel4.get())



        MezclaAUXFINAL= [w+x+y+z for w,x,y,z in izip_longest(FinalArrayAux1,FinalArrayAux2,FinalArrayAux3,FinalArrayAux4,fillvalue=0)]
        MixFinalFinalAux= np.asarray(MezclaAUXFINAL)
        NivelFaderAUX= Nivel5.get()
        MezclaMixAux= NivelModificadoMix(MixFinalFinalAux,NivelFaderAUX)

    def ExportarMix():

        global MezclaMixFinal

        doc=file(44100,16,'MEZCLA')
        doc.archive(MezclaMixFinal)

        mensaje2.pack(side=TOP)
        ReproButton1.pack(side=TOP)

    def Reproducir1():
        nombre = 'MEZCLA'
        reproduce(nombre)

    def RealPlay1():

        pygame.mixer.init(44100,-16,2,4096)
        Grabacion1 = pygame.mixer.Sound('AudioUno')
        Grabacion2 = pygame.mixer.Sound('AudioDos')
        Grabacion3 = pygame.mixer.Sound('AudioTres')
        Grabacion4 = pygame.mixer.Sound('AudioCuatro')

        RealTimePLay1(Grabacion1,Grabacion2,Grabacion3,Grabacion4,Nivel.get(),Nivel2.get(),Nivel3.get(),Nivel4.get(),Nivel6.get(),mute1.get(),mute2.get(),mute3.get(),mute4.get())

# Label para la interfraz grafica - definicion de los botones----------------------------------------------------------------------------------------

    Label1= Label(frame1, padx=15, pady=1, text="Luis Sandoval, Andres Palacio, Libardo Montealegre",fg = "white",bg = "black")
    Label1.pack(side=TOP)

    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Grabando...',bg = "black" )

    #CHANEL 1--------------------------------------------------------------------------------------------------------------

    mute1=IntVar()
    Eq1 = IntVar()
    Compre1 = IntVar()

    Label2= Label(frame2, padx=15, pady=1, text=" Canal 1",fg = "red",bg = "black")
    Label2.pack(side=TOP)

    RecordButton1 = Button(frame2, padx=30, pady=2, text="Record 1",bg = "red",fg="white", command= Grabar1 )
    RecordButton1.pack(side=TOP)

    StopButton1 = Button(frame2, padx=30, pady=2, text=" Stop ",bg = "red",fg="white", command= Stop1)
    StopButton1.pack(side=TOP)

    LabelPro1= Label(frame2, padx=15, pady=1, text="Procesos",fg = "red",bg = "black")
    LabelPro1.pack(side=TOP)

    EQButton1 =  Checkbutton(frame2, padx=30,variable= Eq1,onvalue=1,offvalue=0, pady=2, text="EQ1",bg = "red",fg="black", command= Equal1)
    EQButton1.pack(side=TOP)

    ACompresorButton1= Button(frame2, padx=30, pady=2, text="Compresor",bg = "red",fg="black",command=Compresor1)
    ACompresorButton1.pack(side=TOP)

    CompresorButton1= Checkbutton(frame2, padx=30,variable= Compre1,onvalue=1,offvalue=0, pady=2, text="ON / OFF",bg = "black",fg="red")
    CompresorButton1.pack(side=TOP)

    LabelReverb1= Label(frame2, padx=15, pady=1, text="Reverb",fg = "red",bg = "black")
    LabelReverb1.pack(side=TOP)

    ReverbNivel1 = Scale(frame2, from_= -20.0, to=0.0, orient= HORIZONTAL, resolution=0.1,bg = "red", fg="white")
    ReverbNivel1.pack(side=TOP)

    MuteButton1 = Checkbutton(frame2, padx=30,variable= mute1,onvalue=1,offvalue=0, pady=2, text="MUTE",bg = "red",fg="black")
    MuteButton1.pack(side=TOP)

    Nivel = Scale(frame2, from_= -20.0, to=0.0,length = 200, orient= VERTICAL, resolution=0.1,bg = "red", fg="white")
    Nivel.pack(side=TOP, padx=1, pady=1)

    #CHANEL 2------------------------------------------------------------------------------------------------

    mute2 = IntVar()
    Eq2 = IntVar()
    Compre2 = IntVar()

    Label3= Label(frame3, padx=15, pady=1, text=" Canal 2",fg = "blue",bg = "black")
    Label3.pack(side=TOP)

    RecordButton2 = Button(frame3, padx=30, pady=2, text="Record 2",bg = "blue",fg="white",command= Grabar2 )
    RecordButton2.pack(side=TOP)

    StopButton2 = Button(frame3, padx=30, pady=2, text=" Stop ",bg = "blue",fg="white",command= Stop2 )
    StopButton2.pack(side=TOP)

    LabelPro2= Label(frame3, padx=15, pady=1, text="Procesos",fg = "blue",bg = "black")
    LabelPro2.pack(side=TOP)

    EQButton2 =  Checkbutton(frame3, padx=30,variable= Eq2,onvalue=1,offvalue=0, pady=2, text="EQ2",bg = "blue",fg="black",command= Equal2)
    EQButton2.pack(side=TOP)

    ACompresorButton2= Button(frame3, padx=30, pady=2, text="Compresor",bg = "blue",fg="black",command=Compresor2)
    ACompresorButton2.pack(side=TOP)

    CompresorButton2= Checkbutton(frame3, padx=30,variable= Compre2,onvalue=1,offvalue=0, pady=2, text="ON / OFF",bg = "black",fg="blue")
    CompresorButton2.pack(side=TOP)

    LabelReverb2= Label(frame3, padx=15, pady=1, text="Reverb",fg = "blue",bg = "black")
    LabelReverb2.pack(side=TOP)

    ReverbNivel2 = Scale(frame3, from_= -20.0, to=0.0, orient= HORIZONTAL, resolution=0.1,bg = "blue", fg="white")
    ReverbNivel2.pack(side=TOP)

    MuteButton2 = Checkbutton(frame3, padx=30,variable= mute2,onvalue=1,offvalue=0, pady=2, text="MUTE",bg = "blue",fg="black")
    MuteButton2.pack(side=TOP)

    Nivel2 = Scale(frame3, from_= -20.0, to=0.0,length = 200, orient= VERTICAL, resolution=0.1,bg = "blue", fg="white")
    Nivel2.pack(side=TOP, padx=1, pady=1)

    #CHANEL 3-----------------------------------------------------------------------------
    mute3 = IntVar()
    Eq3 = IntVar()
    Compre3 = IntVar()

    Label4= Label(frame4, padx=15, pady=1, text=" Canal 3",fg = "green",bg = "black")
    Label4.pack(side=TOP)

    RecordButton3 = Button(frame4, padx=30, pady=2, text="Record 3",bg = "green",fg="white",command= Grabar3)
    RecordButton3.pack(side=TOP)

    StopButton3 = Button(frame4, padx=30, pady=2, text=" Stop ",bg = "green",fg="white",command= Stop3)
    StopButton3.pack(side=TOP)

    LabelPro3= Label(frame4, padx=15, pady=1, text="Procesos",fg = "green",bg = "black")
    LabelPro3.pack(side=TOP)

    EQButton3 =  Checkbutton(frame4, padx=30,variable= Eq3,onvalue=1,offvalue=0, pady=2, text="EQ3",bg = "green",fg="black",command= Equal3)
    EQButton3.pack(side=TOP)

    ACompresorButton3= Button(frame4, padx=30, pady=2, text="Compresor",bg = "green",fg="black",command=Compresor3)
    ACompresorButton3.pack(side=TOP)

    CompresorButton3 = Checkbutton(frame4, padx=30,variable= Compre3,onvalue=1,offvalue=0, pady=2, text="ON / OFF",bg = "black",fg="green")
    CompresorButton3.pack(side=TOP)

    LabelReverb3= Label(frame4, padx=15, pady=1, text="Reverb",fg = "green",bg = "black")
    LabelReverb3.pack(side=TOP)

    ReverbNivel3 = Scale(frame4, from_= -20.0, to=0.0, orient= HORIZONTAL, resolution=0.1,bg = "green", fg="white")
    ReverbNivel3.pack(side=TOP)

    MuteButton3 = Checkbutton(frame4, padx=30,variable= mute3,onvalue=1,offvalue=0, pady=2, text="MUTE",bg = "green",fg="black")
    MuteButton3.pack(side=TOP)

    Nivel3 = Scale(frame4, from_= -20.0, to=0.0,length = 200, orient= VERTICAL, resolution=0.1,bg = "green", fg="white")
    Nivel3.pack(side=TOP, padx=1, pady=1)

    #CHANEL 4-------------------------------------------------------------------------------------------

    mute4 = IntVar()
    Eq4 = IntVar()
    Compre4 = IntVar()


    Label5= Label(frame5, padx=15, pady=1, text=" Canal 4",fg = "purple",bg = "black")
    Label5.pack(side=TOP)

    RecordButton4 = Button(frame5, padx=30, pady=2, text="Record 4",bg = "purple",fg="white", command= Grabar4)
    RecordButton4.pack(side=TOP)

    StopButton4 = Button(frame5, padx=30, pady=2, text=" Stop ",bg = "purple",fg="white", command= Stop4)
    StopButton4.pack(side=TOP)

    LabelPro4= Label(frame5, padx=15, pady=1, text="Procesos",fg = "purple",bg = "black")
    LabelPro4.pack(side=TOP)

    EQButton4 =  Checkbutton(frame5, padx=30,variable= Eq4,onvalue=1,offvalue=0, pady=2, text="EQ4",bg = "purple",fg="black",command= Equal4)
    EQButton4.pack(side=TOP)

    ACompresorButton4= Button(frame5, padx=30, pady=2, text="Compresor",bg = "purple",fg="black",command=Compresor4)
    ACompresorButton4.pack(side=TOP)

    CompresorButton4 = Checkbutton(frame5, padx=30,variable= Compre4,onvalue=1,offvalue=0, pady=2, text="ON / OFF ",bg = "black",fg="purple")
    CompresorButton4.pack(side=TOP)

    LabelReverb4= Label(frame5, padx=15, pady=1, text="Reverb",fg = "purple",bg = "black")
    LabelReverb4.pack(side=TOP)

    ReverbNivel4 = Scale(frame5, from_= -20.0, to=0.0, orient= HORIZONTAL, resolution=0.1,bg = "purple", fg="white")
    ReverbNivel4.pack(side=TOP)

    MuteButton4 = Checkbutton(frame5, padx=30,variable= mute4,onvalue=1,offvalue=0, pady=2, text="MUTE",bg = "purple",fg="black")
    MuteButton4.pack(side=TOP)

    Nivel4 = Scale(frame5, from_= -20.0, to=0.0,length = 200, orient= VERTICAL, resolution=0.1,bg = "purple", fg="white")
    Nivel4.pack(side=TOP, padx=1, pady=1)

    # AUXILIAR------------------------------------------------------------------------------------------

    Label6= Label(frame6, padx=15, pady=1, text=" Auxiliar Reverb",fg = "orange",bg = "black")
    Label6.pack(side=TOP)

    Nivel5 = Scale(frame6, from_= -20.0, to=0.0,length = 200, orient= VERTICAL, resolution=0.1,bg = "orange", fg="white")
    Nivel5.pack(side=TOP, padx=1, pady=1)

    AUXButton = Button(frame6, padx=10, pady=2, text="AUX MIX",bg = "orange",fg="black",command= Aux)
    AUXButton.pack(side=TOP)

    # MAIN MIX ------------------------------------------------------------------------------------------

    Label7= Label(frame7, padx=15, pady=1, text=" Main MIX",fg = "turquoise",bg = "black")
    Label7.pack(side=TOP)

    Nivel6 = Scale(frame7, from_= -20.0, to=0.0,length = 200, orient= VERTICAL, resolution=0.1,bg = "turquoise", fg="black")
    Nivel6.pack(side=TOP, padx=1, pady=1)

    PlayButton = Button(frame7, padx=30, pady=2, text="PLAY",bg = "turquoise",fg="black",command= PLAY)
    PlayButton.pack(side=TOP)

    StopButton = Button(frame7, padx=30, pady=2, text="STOP",bg = "turquoise",fg="black")
    StopButton.pack(side=TOP)

    ExportButton = Button(frame7, padx=30, pady=2, text="Exportar",bg = "turquoise",fg="black",command= ExportarMix)
    ExportButton.pack(side=TOP)

    mensaje2 = Label(frame7, fg='green', padx=15, pady=10, text='Archivo Exportado',bg = "black")

    ReproButton1 = Button(frame7, padx=30, pady=2, text="Reproducir Archivo Exportado",command=Reproducir1 ,bg = "turquoise",fg="black")

    ventana.mainloop()

if __name__ == "__main__":
    Main1()
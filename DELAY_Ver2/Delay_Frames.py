#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE
import pyaudio
import struct
import wave
import numpy as np
import math
import matplotlib.pylab as plt

global lol, datosModifi

#funcion para el programa en general que calcula el corrimiento de la senal segun el numero de cuadros

class GenerarRetraso:

    def __init__(self, Time, Frecuencia, Frames):
            self.Frecuencia = Frecuencia
            self.Time = Time
            self.Frames = Frames

    def generar(self):

        global lol

    #Arreglo de datos
        ArregloTono=[]
        ArregloFrames=[]
        ArregloDelay=[]

#genera la onda seno
        for i in range(0,(44100*self.Time)):
            valores=math.sin((2*math.pi*self.Frecuencia*i)/44100.0)
            ArregloTono.append(valores)
#se define el largo de cuadros

        for i in range (0,self.Frames):
            ArregloFrames.append(0)

 #segun el valor de cuadros se obtiene el largo del arreglo con retraso
        for i in range(0,(len(ArregloTono)-self.Frames)):
            ArregloFrames.append(ArregloTono[i])


#se genera el arreglo final que contiene la senal retrasada
        for i in range(0,len(ArregloTono)):
            a=ArregloTono[i]+ArregloFrames[i]
            ArregloDelay.append(a)

        lol=np.asanyarray(ArregloDelay)

        return lol


# obtiene el nivel pico por fader y modifica el max value del arreglo

    def NivelModificado(self,Nuevolevel):

            global lol , datosModifi

            Nivelpico = max(abs(lol))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi = lol * NivelNew
            return datosModifi

# genera el archivo wav de arreglo fina

    def GenerarAudio1(self,nombre):

        global datosModifi
        audio = pyaudio.PyAudio()
        wf = wave.open(nombre+'.wav', 'wb')
        wf.setnchannels(1)
        wf.setframerate(44100)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        packed_value = ""
        for i in range(0, len(datosModifi)):
            packed_value += struct.pack('h',datosModifi[i])
        wf.writeframes(packed_value)
        wf.close()

# Genera la grafica

    def graficar(self):

                global datosModifi
                plt.plot(datosModifi, color="red", linewidth=1.0, linestyle="-")
                plt.show()




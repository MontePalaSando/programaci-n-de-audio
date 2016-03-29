import pyaudio
import math
import matplotlib.pylab as plt
import numpy as np
from Seno import Seno
from ReproAudio import Audio
from Guardar import Archivo

class Metro:

     def __init__(self, BUFFER, FORMAT, CHANNELS, RATE,Notas,Niveles,BPM):
        self.BUFFER = BUFFER
        self.FORMAT = FORMAT
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.NOTA = Notas
        self.NIVEL = Niveles
        self.BPM = BPM
        self.audio = pyaudio.PyAudio()

     def metrono(self):

            print
            Bl= 60.0/self.BPM #Negra
            Frecuenciadesampleo = float(Bl)*44100
            MaxBits = 16
            Buffer = self.BUFFER
            Nombre = "Metronomo.wav"
            NivelPi= self.NIVEL

            print self.BPM
            print Bl

            Do= 261.63
            Doso=277.18
            Re= 293.66
            Reso=311.13
            Mi= 329.63
            Fa= 349.23
            Faso= 369.99
            Sol=392
            Solso=415.30
            La=440
            Laso=466.16
            Si=493.88

            Notas = [Do,Doso,Re,Reso,Mi,Fa,Faso,Sol,Solso,La,Laso,Si]

            opcion2 = self.NOTA

            if opcion2 == 1: # DO
                Tono = [Do,Do,Do,Do]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 2: # DO SOSTENIDO
                Tono = [Doso,Doso,Doso,Doso]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 3: # RE
                Tono = [Re,Re,Re,Re]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 4: # RE SOSTENIDO
                Tono = [Reso,Reso,Reso,Reso]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 5: # MI
                Tono = [Mi,Mi,Mi,Mi]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 6: # FA
                Tono = [Fa,Fa,Fa,Fa]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 7: # FA SOSTENIDO
                Tono = [Faso,Faso,Faso,Faso]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 8: # SOL
                Tono = [Sol,Sol,Sol,Sol]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 9: # SOL SOSTENIDO
                Tono = [Solso,Solso,Solso,Solso]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 10: # LA
                Tono = [La,La,La,La]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 11: # LA SOSTENIDO
                Tono = [Laso,Laso,Laso,Laso]
                Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 12: # SI
                Tono = [Si,Si,Si,Si]
                Tiempo =[Bl,Bl,Bl,Bl]

            #Crear la instancia de la clase audio para generar los datos
            onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
            #Generar el arreglo
            datos = onda.generar()
            datosAjustados = onda.NivelModificado(datos, NivelPi)
            archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
            archivo.archivar(datosAjustados)
            audio = Audio(Buffer)
            Datos = audio.abrir(Nombre)
            audio.inicio(Datos[0],Datos[1],Datos[2])
            audio.reproducir(Datos[3])
            audio.cerrar()




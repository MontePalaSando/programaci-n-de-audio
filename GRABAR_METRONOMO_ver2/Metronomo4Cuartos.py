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

            Bl= 60.0/self.BPM #Negra
            Cor= Bl /2.0
            Frecuenciadesampleo = float(Bl)*44100
            MaxBits = 16
            Buffer = self.BUFFER
            Nombre = "Metronomo.wav"
            NivelPi= self.NIVEL
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

            Silencio= 0

            Do2= 523.25
            Doso2=554.37
            Re2= 587.33
            Reso2=622.25
            Mi2= 659.26
            Fa2= 698.46
            Faso2=739.99
            Sol2=783.99
            Solso2=830.61
            La2=880.0
            Laso2=932.33
            Si2=987.77

            Notas = [Do,Doso,Re,Reso,Mi,Fa,Faso,Sol,Solso,La,Laso,Si]

            opcion2 = self.NOTA

            if opcion2 == 1: # DO
                Tono = [Do2,Silencio,Do,Silencio,Do,Silencio,Do,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 2: # DO SOSTENIDO
                Tono = [Doso2,Silencio,Doso,Silencio,Doso,Silencio,Doso,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 3: # RE
                Tono = [Re2,Silencio,Re,Silencio,Re,Silencio,Re,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 4: # RE SOSTENIDO
                Tono = [Reso2,Silencio,Reso,Silencio,Reso,Silencio,Reso,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 5: # MI
                Tono = [Mi2,Silencio,Mi,Silencio,Mi,Silencio,Mi,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 6: # FA
                Tono = [Fa2,Silencio,Fa,Silencio,Fa,Silencio,Fa,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 7: # FA SOSTENIDO
                Tono = [Faso2,Silencio,Faso,Silencio,Faso,Silencio,Faso,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 8: # SOL
                Tono = [Sol2,Silencio,Sol,Silencio,Sol,Silencio,Sol,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 9: # SOL SOSTENIDO
                Tono = [Solso2,Silencio,Solso,Silencio,Solso,Silencio,Solso,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 10: # LA
                Tono = [La2,Silencio,La,Silencio,La,Silencio,La,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 11: # LA SOSTENIDO
                Tono = [Laso2,Silencio,Laso,Silencio,Laso,Silencio,Laso,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

            if opcion2 == 12: # SI
                Tono = [Si2,Silencio,Si,Silencio,Si,Silencio,Si,Silencio]
                Tiempo =[Cor,Cor,Cor,Cor,Cor,Cor,Cor,Cor]

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




#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

import pyaudio
import struct
import wave
import numpy as np
import math
import matplotlib.pylab as plt
from ArchivoOpen import Audio1

global lol, datosModifi

class GenerarDelay:

    def __init__(self, Time, Repe):
            self.Time = Time
            self.Repe = Repe

    def DelayOn(self):
        global lol

        MixDelay=[]

        Time=self.Time/100.0
        TimeDelay=int(441000*Time)

        for j in range(0,self.Repe):
            K=TimeDelay*j
            for i in range(0,(len(Audio1)+TimeDelay)):

                if (i+K) < len(Audio1):
                    B=Audio1[i][0]+Audio1[i+K][0]
                    MixDelay.append(B)

        lol=np.asanyarray(MixDelay)
        return lol

    def NivelModificado(self,Nuevolevel):

            global lol , datosModifi

            Nivelpico = max(abs(lol))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi = lol * NivelNew
            return datosModifi

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

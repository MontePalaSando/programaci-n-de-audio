#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from  ArchivoOpen import Audio1
from  ArchivoOpen import Audio2
from  ArchivoOpen import Audio3
import numpy as np
import wave, struct
import pyaudio

global Mix2,lol2,datosModifi

Mix2 = []

def GenerarMix2():

    global Mix2,lol2

    for i in range(0,len(Audio1)):
       Mix2.append(Audio1[i])
    for i in range(0,len(Audio2)):
       Mix2.append(Audio2[i])
    for i in range(0,len(Audio3)):
       Mix2.append(Audio3[i])

    lol2 = np.asarray(Mix2)
    return lol2

def NivelModificado2( Nuevolevel):

            global lol2, datosModifi

            Nivelpico = max(abs(lol2))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi = lol2 * NivelNew
            return datosModifi



def GenerarAudio2(nombre):

    global lol2,datosModifi

    audio = pyaudio.PyAudio()
    wf = wave.open(nombre+'.wav', 'wb')
    wf.setnchannels(1)
    wf.setframerate(44100)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    packed_value = ""
    for i in range(0,len(datosModifi)):

        packed_value += struct.pack('h', datosModifi[i][0])
    wf.writeframes(packed_value)
    wf.close()



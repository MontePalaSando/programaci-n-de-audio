#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from  ArchivoOpen import Audio1
from  ArchivoOpen import Audio2
from  ArchivoOpen import Audio3
import pyaudio
import struct
import wave
import numpy as np

global Mix1 ,lol, datosModifi

Mix1=[]

def GenerarMix1():

        global Mix1,lol

        cuadros1=len(Audio1)
        cuadros2=len(Audio2)
        cuadros3=len(Audio3)


        if cuadros1 < cuadros2 and cuadros1 < cuadros3:

            for i in range(0, cuadros1):

                dato1=Audio1[i][0]+Audio2[i][0]+Audio3[i][0]
                Mix1.append(dato1)

            if cuadros2 < cuadros3:

                for i in range(cuadros1, cuadros2):
                    dato2=Audio2[i][0]+Audio3[i][0]
                    Mix1.append(dato2)

                for i in range(cuadros2, cuadros3):
                    Mix1.append(Audio3[i][0])

            if cuadros3< cuadros2:

                for i in range(cuadros1, cuadros3):
                    dato2=Audio2[i][0]+Audio3[i][0]
                    Mix1.append(dato2)

                for i in range(cuadros3, cuadros2):
                    Mix1.append(Audio2[i][0])


        if cuadros2 < cuadros3 and cuadros2 < cuadros1:

            for i in range(0, cuadros2):

                dato1=Audio1[i][0]+Audio2[i][0]+Audio3[i][0]
                Mix1.append(dato1)

            if cuadros1 < cuadros3:

                for i in range(cuadros2, cuadros1):
                    dato2=Audio2[i][0]+Audio3[i][0]
                    Mix1.append(dato2)

                for i in range(cuadros1, cuadros3):
                    Mix1.append(Audio3[i][0])

            if cuadros3 < cuadros1:

                for i in range(cuadros2, cuadros3):
                    dato2=Audio2[i][0]+Audio3[i][0]
                    Mix1.append(dato2)

                for i in range(cuadros3, cuadros1):
                    Mix1.append(Audio2[i][0])


        if cuadros3 < cuadros2 and cuadros3 < cuadros1:

            for i in range(0, cuadros3):

                dato1=Audio1[i][0]+Audio2[i][0]+Audio3[i][0]
                Mix1.append(dato1)

            if cuadros1 < cuadros2:

                for i in range(cuadros3, cuadros1):
                    dato2=Audio2[i][0]+Audio3[i][0]
                    Mix1.append(dato2)

                for i in range(cuadros1, cuadros2):
                    Mix1.append(Audio3[i][0])

            if cuadros2 < cuadros1:

                for i in range(cuadros3, cuadros2):
                    dato2=Audio2[i][0]+Audio3[i][0]
                    Mix1.append(dato2)

                for i in range(cuadros2, cuadros1):
                    Mix1.append(Audio2[i][0])

        lol = np.asarray(Mix1)
        return lol

def NivelModificado( Nuevolevel):

            global lol, datosModifi

            Nivelpico = max(abs(lol))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi = lol * NivelNew
            return datosModifi



def GenerarAudio1(nombre):

    global Mix1

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
from  ArchivoOpen import Audio1
from  ArchivoOpen import Audio2
from  ArchivoOpen import Audio3
import pyaudio
import struct
import wave

global Mix1

Mix1 = []

def GenerarMix1():

        global Mix1

        Cuadros1=len(Audio1)
        Cuadros2=len(Audio2)
        Cuadros3=len(Audio3)

        if (Cuadros1 >= Cuadros2) and (Cuadros1 > Cuadros3):

            for i in range(0, Cuadros1):
                Mix1.append(Audio1[i][0])
            for i in range(0,Cuadros2):
                Mix1[i]=Mix1[i]+Audio2[i][0]
            for i in range(0, Cuadros3):
                Mix1[i] = Mix1[i] + Audio3[i][0]

        if Cuadros2 >= Cuadros3 and Cuadros2 > Cuadros1:

                for i in range(0, Cuadros2):
                    Mix1.append(Audio2[i][0])
                for i in range(0, Cuadros1):
                    Mix1[i] = Mix1[i] + Audio1[i][0]
                for i in range(0, Cuadros3):
                    Mix1[i] = Mix1[i] + Audio3[i][0]

        if Cuadros3 >= Cuadros1 and Cuadros3 > Cuadros2:

            for i in range(0, Cuadros3):
                Mix1.append(Audio3[i][0])
            for i in range(0, Cuadros2):
                Mix1[i] = Mix1[i] + Audio2[i][0]
            for i in range(0, Cuadros1):
                Mix1[i] = Mix1[i] + Audio1[i][0]

        for i in range(0,len(Mix1)) :
            if Mix1[i]>37767:
                Mix1[i]=37767
            if Mix1[i]<-37767:
                Mix1[i]=-37767




def GenerarAudio1(nombre):
    audio = pyaudio.PyAudio()
    wf = wave.open(nombre+'.wav', 'wb')
    wf.setnchannels(1)
    wf.setframerate(44100)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    packed_value = ""
    for i in range(0, len(Mix1)):
        packed_value += struct.pack('h', Mix1[i])
    wf.writeframes(packed_value)
    wf.close()
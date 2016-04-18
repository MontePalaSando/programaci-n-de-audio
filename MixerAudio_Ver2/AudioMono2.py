from  ArchivoOpen import Audio1
from  ArchivoOpen import Audio2
from  ArchivoOpen import Audio3
from struct import pack
from math import sin, pi
import wave, struct

import pyaudio

global Mix2
Mix2 = []
def GenerarMix2():

    global Mix2
    for i in range(0,len(Audio1)):
       Mix2.append(Audio1[i])
    for i in range(0,len(Audio2)):
       Mix2.append(Audio2[i])
    for i in range(0,len(Audio3)):
       Mix2.append(Audio3[i])



def GenerarAudio2(nombre):
    audio = pyaudio.PyAudio()
    wf = wave.open(nombre+'.wav', 'wb')
    wf.setnchannels(1)
    wf.setframerate(44100)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    packed_value = ""
    for i in range(0,len(Mix2)):

        packed_value += struct.pack('h', Mix2[i][0])
        #packed_value += struct.pack('h', Mix2[i][1])
    wf.writeframes(packed_value)
    wf.close()



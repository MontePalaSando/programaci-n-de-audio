from  ArchivoOpen import Audio1
from  ArchivoOpen import Audio2
from  ArchivoOpen import Audio3
from struct import pack
global Mix3
mixl = []
mixr=[]
import wave

def GenerarMix3():
    Cuadros1 = len(Audio1)
    Cuadros2 = len(Audio2)
    Cuadros3 = len(Audio3)

    if (Cuadros1 >= Cuadros2) and (Cuadros1 > Cuadros3):

        for i in range(0, Cuadros1):
            mixl.append(Audio1[i][0])
            mixr.append(0)
        for i in range(0, Cuadros2):
            mixl[i] = mixl[i] + Audio2[i][0]
            mixr[i] = mixr[i] + Audio2[i][0]
        for i in range(0, Cuadros3):
            mixr[i] = mixr[i] + Audio3[i][0]

    if Cuadros2 >= Cuadros3 and Cuadros2 > Cuadros1:

        for i in range(0, Cuadros2):
            mixl.append(Audio2[i][0])
            mixr.append(Audio2[i][0])
        for i in range(0, Cuadros1):
            mixl[i] = mixl[i] + Audio1[i][0]
        for i in range(0, Cuadros3):
            mixr[i] = mixr[i] + Audio3[i][0]

    if Cuadros3 >= Cuadros1 and Cuadros3 > Cuadros2:

        for i in range(0, Cuadros3):
            mixr.append(Audio3[i][0])
            mixl.append(0)
        for i in range(0, Cuadros2):
            mixl[i] = mixl[i] + Audio2[i][0]
            mixr[i] = mixr[i] + Audio2[i][0]
        for i in range(0, Cuadros1):
            mixl[i] = mixr[i] + Audio1[i][0]

    for i in range(0,len(mixr)) :
                if mixr[i]>37767:
                    mixr[i]=37767
                if mixr[i]<-37767:
                    mixr[i]=-37767
                if mixl[i] > 37767:
                    mixl[i] = 37767
                if mixl[i] < -37767:
                    mixl[i] = -37767

def GenerarAudio3(nombre):

    wv = wave.open(nombre+'.wav', 'w')
    wv.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
    wvData=""
    for i in range(0, len(mixr)):
        wvData+=pack('h',mixl[i]) #left
        wvData+=pack('h',mixr[i]) #right
    wv.writeframes(wvData)
    wv.close()
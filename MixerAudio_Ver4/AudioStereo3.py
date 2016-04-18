#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from  ArchivoOpen import Audio1
from  ArchivoOpen import Audio2
from  ArchivoOpen import Audio3
from struct import pack
import numpy as np

global Mixl, Mixr , lol3 , lol4,Mix3
Mixl = []
Mixr = []
Mix3 = []
import wave

def GenerarMix3():

    global Mixl, Mixr , lol3 , lol4, datosModifi1, datosModifi2

    Cuadros1 = len(Audio1)
    Cuadros2 = len(Audio2)
    Cuadros3 = len(Audio3)


    if Cuadros1 <Cuadros3:
            for i in range(0, Cuadros1 ):
                dato=Audio1[i][0]+Audio3[i][0]
                Mixl.append(dato)
            for i in range(Cuadros1 , Cuadros3):
                Mixl.append(Audio3[i][0])

    if Cuadros3<Cuadros1 :
            for i in range(0, Cuadros3):
                dato2=Audio1[i][0]+Audio3[i][0]
                Mixl.append(dato2)

            for  i in range(Cuadros3, Cuadros1):
                Mixl.append(Audio1[i][0])

    lol3=np.asanyarray(Mixl)

    if Cuadros2<Cuadros3:
            for i in range(0, Cuadros2):
                dato=Audio2[i][0]+Audio3[i][0]
                Mixr.append(dato)
            for i in range(Cuadros2, Cuadros3):
                Mixr.append(Audio3[i][0])

    if Cuadros3<Cuadros2:
            for  i in range(0, Cuadros3):
                dato2=Audio2[i][0]+Audio3[i][0]
                Mixr.append(dato2)

            for  i in range(Cuadros3, Cuadros2):
                Mixr.append(Audio2[i][0])
    lol4=np.asanyarray(Mixr)


def NivelModificado3( Nuevolevel):

            global lol3, datosModifi1

            Nivelpico = max(abs(lol3))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi1 = lol3 * NivelNew
            return datosModifi1

def NivelModificado4( Nuevolevel):

            global lol4, datosModifi2

            Nivelpico = max(abs(lol4))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi2 = lol4 * NivelNew
            return datosModifi2


def GenerarAudio3(nombre):

    global Mixr , Mixl, Mix3, lol3 , lol4, datosModifi1, datosModifi2

    wv = wave.open(nombre+'.wav', 'w')
    wv.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
    a=len(datosModifi1)
    b=len(datosModifi2)
    if a<b:
            for i in range(0,a):
                            l =pack('<h', datosModifi1[i])
                            r= pack('<h', datosModifi2[i])
                            Mix3.append(l)
                            Mix3.append(r)
            for i in range(a,b):
                            l =pack('<h', 0)
                            r= pack('<h', datosModifi2[i])
                            Mix3.append(l)
                            Mix3.append(r)
    if b<a:
            for i in range(0,b):
                            l =pack('<h', datosModifi1[i])
                            r= pack('<h', datosModifi2[i])
                            Mix3.append(l)
                            Mix3.append(r)
            for i in range(b,a):
                            l= pack('<h', datosModifi1[i])
                            r= pack('<h', 0)
                            Mix3.append(l)
                            Mix3.append(r)

    value_str=''.join(Mix3)
    wv.writeframes(value_str)
    wv.close()
import wave
import math
import struct

class Audio:

    def __init__(self,AudioIn):
        self.AudioIn= AudioIn

    def operar7(self):

        x= self.AudioIn
        Archivo= wave.open(x,'rb')
        y=Archivo.getnframes()
        op=1/44100


        for i in range(0,3):
            u='so'
            t= struct.unpack("<h",u)
            r= 1
            r=r+int(t[0])**2;

        p = math.sqrt(r/y)
        t = struct.unpack("<h",u)


        op= 1 /44100

        for i in range(0,y):
            u='st'
            t=struct.unpack("<h",u)
            r2=1
            r2=r2+((float(p)**2)*op)
        leq  = 20*math.log10((1/1)*(r2)/(6.02*16))



        print ("El Nivel pico maximo del audio es: ")
        print (y)

        print ("El Valor RMS del audio es: ")
        print (p)

        print ("El Leq del audio es: ")
        print (leq)











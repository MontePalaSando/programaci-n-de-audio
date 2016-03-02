import wave
import math
import struct

class Nivelpico:

    def __init__(self,AudioIn):
        self.AudioIn= AudioIn

    def operar7(self):

        x= self.AudioIn
        Archivo= wave.open(x,"rb")
        tamano=Archivo.getnframes()

        for i in range(0,tamano):
            DatosArray = Archivo.readframes(1)
            Datos = struct.unpack("<h",DatosArray)

        Valopico = max(Datos)
        Valopico2 = abs(Valopico)
        ValodB = 20*math.log10(float(Valopico2)/2**16)

        print ("El Nivel pico maximo del audio es: ")
        print (ValodB)

class NivelRMS:

    def __init__(self,AudioIn):
        self.AudioIn= AudioIn

    def operar8(self):

        x= self.AudioIn
        Archivo= wave.open(x,"rb")
        tamano=Archivo.getnframes()

        for i in range(0,tamano):
            DatosArray2 = Archivo.readframes(1)
            Datos = struct.unpack("<h",DatosArray2)
            sumatoria = 0
            sumatoria = sumatoria + int(Datos[0])**2

        RMS = float(math.sqrt(float(sumatoria)/float(tamano)))

        ValorRMS= 20.0*math.log10(float(RMS)/2**16.0)

        print ("El Valor RMS del audio es: ")
        print (ValorRMS)

class NivelLeq:

    def __init__(self,AudioIn):
        self.AudioIn= AudioIn

    def operar9(self):

        x= self.AudioIn
        Archivo= wave.open(x,"rb")
        tamano=Archivo.getnframes()
        T1 = 1.0 / 44100

        for i in range(0,tamano):
            DatosArray3 = Archivo.readframes(1)
            Datos = struct.unpack("<h", DatosArray3)
            sumatoria = 0
            sumatoria = sumatoria + ((int(Datos[0])**2)*T1)

        leq  = 10*math.log10((1.0/1.0)*(sumatoria)/(2**16))

        print ("El Leq del audio es: ")
        print (leq)











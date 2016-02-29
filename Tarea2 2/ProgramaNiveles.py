import wave
import math
import struct

class Audio:


    def __init__(self,AudioIn):
        self.AudioIn= AudioIn

    def operar7(self):
# se procede a abrir el archivo de audio y el tamano del arreglo
        x= self.AudioIn
        Archivo= wave.open(x,'rb')
# valor pico de la senal_valor maximo del arreglo que contiene el archivo de audio definido como tamano
        tamano=Archivo.getnframes()
        T1= 1 / 44100

# se procede a hacer la sumatoria de los cuadrados por medio de una iteracion
        for i in range(0,3):

            DatosArray = Archivo.readframes(1)
            DatosArray1 = 'so'
            Datos = struct.unpack("<h",DatosArray1)

            sumatoria = 1
            sumatoria = sumatoria + int(Datos[0])**2;

        #valor RMS del archivo de audio
        RMS = math.sqrt(sumatoria/tamano)

#sumatoria de los cuadrados
        for i in range(0,tamano):
            DatosArray = Archivo.readframes(1)
            DatosArray1 = 'so'
            Datos = struct.unpack("<h",DatosArray1)

            sumatoria = sumatoria + ((int(Datos[0])**2)*T1)
#valor leq del archivo de audio
        leq  = 20*math.log10((1/1)*(sumatoria)/(6.02*16))



        print ("El Nivel pico maximo del audio es: ")
        print (tamano)

        print ("El Valor RMS del audio es: ")
        print (RMS)

        print ("El Leq del audio es: ")
        print (leq)











import math
import matplotlib.pylab as plt
# Importar Librerias
#Codigo de la clase para generar la senal sinusoidal

class Seno:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Andres Palacio
        def __init__(self, frecuencia, sampling, bits, time,NivelPi):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time
            self.Max = int((2**bits)*(10**(float(NivelPi)/20)))

        def generar(self):

            for i in range(0,self.tamano):

                    datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
                    Seno.wavearray.append(datos)

            return Seno.wavearray

        def graficar(self,array):
                plt.plot(Seno.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()

class cuadro:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Andres Palacio
        def __init__(self, frecuencia, sampling, bits, time,NivelPi):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time
            self.Max = int((2**bits)*(10**(float(NivelPi)/20)))


        def generar(self):


            for i in range(0, self.tamano):

                A = (float(4/math.pi)*(2**self.NumeroBit)/100)
                datos = 0

                for j in range(0,100):
                    par = j %2

                    if par:
                        value =math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                        datos = datos + value
                frame = datos * A
                cuadro.wavearray.append(frame)

            return cuadro.wavearray

        def graficar(self,array):
                plt.plot(cuadro.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()

class triangulo:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time,NivelPi):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time
            self.Max = int((2**bits)*(10**(float(NivelPi)/20)))


        def generar(self):


            for i in range(0, self.tamano):

                A = (8/float(math.pi**2))*(2**self.NumeroBit)/100
                datos = 0

                for j in range(0,100):
                    par = j %2

                    if par:
                        val = (-1**(float(j-1)/2))/j**2
                        value = val*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                        datos = datos + value
                frame = datos * A
                triangulo.wavearray.append(frame)

            return triangulo.wavearray

        def graficar(self,array):
                plt.plot(triangulo.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()

class sierra:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time,NivelPi):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time
            self.Max = int((2**bits)*(10**(float(NivelPi)/20)))



        def generar(self):


            for i in range(0, self.tamano):

                A = ((0.5)-1/float(math.pi))*(2**self.NumeroBit)/50
                datos = 0

                for j in range(1,100):
                    par = j %2

                    if par:
                        val = 1/float(j)
                        value = val*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                        datos = datos + value
                frame = datos * A
                sierra.wavearray.append(frame)


            return sierra.wavearray

        def graficar(self,array):
                plt.plot(sierra.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()

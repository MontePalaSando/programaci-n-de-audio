import math
import matplotlib.pylab as plt
import numpy as np
# Importar Librerias

#Codigo de la clase para generar la senal diente de  triangular

class triangulo:
    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Frecuencia = frecuencia
            self.tamano = sampling
            self.seconds = time


        def generar(self):
            wavearray = [] #Arreglo de datos que contendra los samples

            for k in range(0,len(self.seconds)):
                for i in range(0, int(self.seconds[k]*self.tamano)):
                    A = (8 / math.pi**2)*(2**self.NumeroBit)/100
                    datos = 0
                    for j in range (0, 100):
                        par = j % 2
                        if par:
                            val = (-1**((j-1)/2.0))/float(j)**2
                            value =  val * math.sin((j*math.pi*self.Frecuencia[k]*i)/44100)
                            datos = datos + value
                frame = datos * A
                wavearray.append(frame)
            data3 = np.asarray(wavearray)
            return data3

        def graficar(self,array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()

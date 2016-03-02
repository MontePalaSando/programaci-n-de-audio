import math
import matplotlib.pylab as plt
import numpy as np
# Importar Librerias

#Codigo de la clase para generar la senal diente de  triangular

class sierra:
    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time

        def generar(self):
            #Arreglo de datos que contendra los samples
            wavearray = []
            for i in range(0, self.tamano):
                A = ((0.5)-(1/float(math.pi)))*(2**self.NumeroBit)/100
                datos = 0

                for j in range(1,100):
                    val = 1/float(j)
                    value = val*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                    datos = datos + value
                frame = datos * A
                wavearray.append(frame)
            data4 = np.asarray(wavearray)
            return data4

        def graficar(self,array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()


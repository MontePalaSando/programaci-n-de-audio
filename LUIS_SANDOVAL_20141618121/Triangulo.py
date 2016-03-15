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

            #Arreglo de datos que contendra los samples
            wavearray = []
            for j in range(0,len(self.seconds)):
                for i in range(0, int(self.seconds[j]*self.tamano)):
                    A = (8 / float(math.pi**2))*((2**self.NumeroBit)/100)
                    datos = 0
                    for k in range (0, 100):
                        par = k % 2
                        if par:
                            val = (-1**((k-1)/2.0))/float(k**2)
                            datos1= val*math.sin((k*2*math.pi*self.Frecuencia[j]*i)/44100.0)
                            datos=  datos + datos1
                    frame = datos * A
                    wavearray.append(frame)
            data = np.asarray(wavearray)
            return data


        def graficar(self,array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()

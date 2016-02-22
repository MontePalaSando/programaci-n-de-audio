import math
import matplotlib.pylab as plt
# Importar Librerias
#Codigo de la clase para generar la senal sinusoidal

class Seno:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Andres Palacios
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time

        def generar(self):

            for i in range(0, self.tamano):

                    datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
                    Seno.wavearray.append(datos)

            return Seno.wavearray



        def graficar(self, array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()
import math
import matplotlib.pylab as plt
import numpy as np
# Importar Librerias
#Codigo de la clase para generar la senal sinusoidal

class Seno:
    #Arreglo de datos que contendra los samples
    #Constructor de la clase
    #Desarrollado por: Andres Palacio
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time

        def generar(self):
            wavearray = []

            for i in range(0,self.tamano):

                    datos = math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
                    wavearray.append(datos)

            data = np.asarray(wavearray)
            return data

        def NivelModificado(self, datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi = datos * NivelNew
            return datosModifi

        def graficar(self,array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()



        def graficar(self, array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()
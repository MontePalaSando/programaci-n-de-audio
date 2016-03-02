# Importar Librerias
import math
import matplotlib.pylab as plt
import numpy as np

#Codigo de la clase para generar la senal cuadrada

class cuadro:
    #Arreglo de datos que contendra los samples

    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time

        def generar(self):
            wavearray = []
            for i in range(0, self.tamano):
                    A = (4 / math.pi)
                    datos = 0
                    for j in range (0, 100):
                        par = j % 2
                        if par:
                            value = (1/float(j))*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                            datos = datos +  value
                    frame = datos * A
                    wavearray.append(frame)
            data2 = np.asarray(wavearray)
            return data2

        def NivelModificado(self, datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            datosModifi = datos * NivelNew
            return datosModifi

        def graficar(self,array):
                plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                plt.show()

# Importar Librerias
import math
import matplotlib.pylab as plt
import numpy as np

#Codigo de la clase para generar la senal cuadrada

class cuadro:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Frecuencia = frecuencia
            self.tamano = sampling
            self.seconds = time

        def generar(self):
            wavearray = []
            for i in range(0, self.seconds*self.tamano):
                    A = (4 / math.pi) *(2**self.NumeroBit)/100
                    datos = 0
                    for j in range (0, 100):
                        par = j % 2
                        if par:
                            value = (1/float(j))*math.sin((j*math.pi*self.Frecuencia*i)/44100)
                            datos = datos +  value
                    frame = datos * A
                    wavearray.append(frame)
            data2 = np.asarray(wavearray)
            return data2
import math
import matplotlib.pylab as plt
import numpy as np
# Importar Librerias
#Codigo de la clase para generar la senal sinusoidal

class Seno:
    #Constructor de la clase

        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Frecuencia = frecuencia
            self.tamano = sampling
            self.seconds = time

        def generar(self):

            #Arreglo de datos que contendra los samples
            wavearray = []
            for i in range(0, int(self.seconds*self.tamano)):
                    datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/44100)
                    wavearray.append(datos)
            data = np.asarray(wavearray)
            return data
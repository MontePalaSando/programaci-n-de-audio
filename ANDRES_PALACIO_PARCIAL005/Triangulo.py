import math
import matplotlib.pylab as plt
# Importar Librerias

#Codigo de la clase para generar la senal diente de  triangular

class triangulo:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
    #Desarrollado por: Luis Sandoval
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time


        def generar(self):


            for i in range(0, self.tamano):

                A = (8/math.pi**2)*(2**self.NumeroBit)/100
                datos = 0

                for j in range(0,100):
                    par = j %2

                    if par:
                        val = (-1**((j-1)/2))/j**2
                        value = val*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                        datos = datos + value
                frame = datos * A
                triangulo.wavearray.append(frame)

            return triangulo.wavearray

	def graficar(self,array):
                plt.plot(triangulo.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()
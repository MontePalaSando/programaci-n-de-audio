# Importar Librerias
import math
import matplotlib.pylab as plt

#Codigo de la clase para generar la senal cuadrada

class cuadro:
    #Arreglo de datos que contendra los samples
        wavearray = []
    #Constructor de la clase
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time
            self.amplitud= (2**bits)/2
            self.pi = math.pi

        def generar(self):


            for i in range(0, self.tamano):
                datos = self.amplitud*math.sin((2*self.pi*self.Frecuencia*i)/self.SamplingRate)
		if datos<0:
                      datos=(-(2**self.NumeroBit)/2)
		if datos>0:
                      datos=((2**self.NumeroBit)/2)
                cuadro.wavearray.append(datos)

	def graficar(self):
                plt.plot(cuadro.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()

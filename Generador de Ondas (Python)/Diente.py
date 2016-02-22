# Importar Librerias
import math
import matplotlib.pylab as plt
#Codigo de la clase para generar la senal sinusoidal
#Desarrollado por
class sawtooth():
        wavearray=[]
	def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time


	def generar(self):
            m=self.Frecuencia*(2**self.NumeroBit)
	    a=((2**self.NumeroBit)/2)
	    s=0
            for i in range(0, self.tamano):
                datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)

		s=s+m
                sawtooth.wavearray.append(s)
		if (datos==a):
			s=(-(2**self.NumeroBit)/2)



	def graficar(self):
		plt.plot(sawtooth.wavearray)
		plt.show()


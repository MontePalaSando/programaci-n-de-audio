import math
import matplotlib.pylab as plt

class triangle:
        wavearray=[]
	def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time


	def generar(self):
            m=2*self.Frecuencia*(2**self.NumeroBit)
	    a=((2**self.NumeroBit)/2)
	    s=0
            for i in range(0, self.tamano):
                datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)

		s=s+m
                triangle.wavearray.append(s)
		if (abs(datos)==a):
			m=-1*m


	def graficar(self):
		plt.plot(triangle.wavearray)
		plt.show()
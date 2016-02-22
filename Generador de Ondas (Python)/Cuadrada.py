import math
import matplotlib.pylab as plt


class square:
        wavearray = []

        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time

        def generar(self):


            for i in range(0, self.tamano):
                datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
		if datos<0:
                      datos=(-(2**self.NumeroBit)/2)
		if datos>0:
                      datos=((2**self.NumeroBit)/2)
                square.wavearray.append(datos)

	def graficar(self):
		plt.plot(square.wavearray)
		plt.show()

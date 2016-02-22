# Importar Librerias
import math
import matplotlib.pylab as plt
#Codigo de la clase para generar la senal diente de sierra
class sierra():
    #Arreglo de datos que contendra los samples
        wavearray=[]
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
            m=self.Frecuencia*(2**self.NumeroBit)
	    a=((2**self.NumeroBit)/2)
	    s=0
            for i in range(0, self.tamano):
                datos = self.amplitud*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)

		s=s+m
                sierra.wavearray.append(s)
		if (datos==a):
			s=(-(2**self.NumeroBit)/2)



	def graficar(self):
                plt.plot(sierra.wavearray, color="red", linewidth=1.0, linestyle="-")
                plt.show()


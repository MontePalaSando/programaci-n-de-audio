import wave
import struct
import math
import numpy as np
import matplotlib.pylab as plt
def graficar(array):
   plt.plot(array, color="red", linewidth=1.0, linestyle="-")
   plt.show()
def main():
    bpm=int(raw_input('ingrese bpm: '))
    negra=float(60.0/bpm)*44100
    print negra

    notas=[220,164.81,174.61,196,174.61,164.81,146.83,146.83,174.61,220,196,174.61,164.81,164.81,174.61,196,220,176.61,146.83,146.83,0,196,233.08,293.66,293.66,261.63,233.08,220,174.61,220,220,196,176.61,164.81,164.81,174.61,196,220,174.61,146.83,146.83,0,174.61,146.83,138.6,164.81,220,174.61,196,146.83,164.81,220]
    ritmo=[1,0.5,0.5,1,0.5,0.5,1,0.5,0.5,1,0.5,0.5,1,0.5,0.5,1,1,1,1,2,0.5,1,0.5,0.5,0.5,0.5,0.5,1.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]
    print(ritmo[1]*negra)
    print('1. seno')
    print('2. cuadrada')
    print('3. triangular')
    print('4. diente de sable')
    eleccion = raw_input('Elija: ')
    data=[]
    nombre='sine.wav'
    for i in range(0,len(ritmo)):
        for a in range(0,int(ritmo[i]*negra)):
            datos = 8000*math.sin((2*math.pi*notas[i]*a)/44100.0)
            data.append(datos)
        data1 = np.asarray(data)
    if eleccion == '2':
        nombre='square.wav'
        for i in range(0,len(data)):
            if (data[i]>0):
                data[i]=10000
            elif (data[i]<0):
                data[i]=-10000
        data1 = np.asarray(data)
        print len(data1)
    if eleccion == '3':
        nombre='triangle.wav'
        data = [] #Arreglo de datos que contendra los samples
        for i in range(0,52):

            for a in range(0,int(ritmo[i]*negra)):

                A = (8 / math.pi**2)
                datos = 0
                for j in range (0, 100):
                    par = j % 2
                    if par:
                        val = (-1**((j-1)/2.0))/float(j)**2
                        value =  val * math.sin((j*math.pi*notas[i]*a)/44100)
                        datos = datos + value
                frame = datos * A
                data.append(8000*frame)
        data1 = np.asarray(data)

    if eleccion == '4':
        nombre='sawtooth.wav'
        data = [] #Arreglo de datos que contendra los samples
        for i in range(0,52):
            for a in range(0,int(ritmo[i]*negra)):
                A = ((0.5)-(1/float(math.pi)))
                datos = 0

                for j in range(1,100):
                    val = 1/float(j)
                    value = val*math.sin((j*math.pi*notas[i]*a)/44100)
                    datos = datos + value
                frame = datos * A
                data.append(8000*frame)
        data1 = np.asarray(data)
    graficar(data1)
    output = wave.open(nombre, 'w')
    output.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))
    values = []
    for i in range(0, len(data1)):

                packed_value = struct.pack('<h', data1[i])

                values.append(packed_value)


    value_str = ''.join(values)
    output.writeframes(value_str)
    output.close()
if __name__ == '__main__':
    main()
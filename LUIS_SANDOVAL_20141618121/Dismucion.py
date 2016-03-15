import math
import matplotlib.pylab as plt

class Disminuido:

    def __init__(self, NotaFunda,Notas,position):
            self.NotaFunda= NotaFunda
            self.Notas= Notas
            self.Position= position


    def generarAcorde(self):
        opcion7ma = input("Desea el acorda con : 1. Sin 7ma  2. 7ma Mayor  3. 7ma menor  ")

        if opcion7ma == 1:
            Tono1= self.NotaFunda

            Tono2= self.Notas[self.Position+3]

            Tono3= self.Notas[self.Position+6]

            Tono4= self.Notas[24]

        if opcion7ma == 2:

            Tono1= self.NotaFunda

            Tono2= self.Notas[self.Position+3]

            Tono3= self.Notas[self.Position+6]

            Tono4= self.Notas[self.Position+11]

        if opcion7ma == 3:

            Tono1= self.NotaFunda

            Tono2= self.Notas[self.Position+3]

            Tono3= self.Notas[self.Position+6]

            Tono4= self.Notas[self.Position+10]

        Tono=[Tono1,Tono2,Tono3,Tono4]
        return Tono
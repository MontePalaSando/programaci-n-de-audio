#LUIS SANDOVAL
#LIBARDO MONTEALEGRE
#ANDRES PALACIO

from Seno import Seno
from Guardar import Archivo
from Cuadrada import square
from Triangulo import triangle
from Diente import sawtooth




def main():
        Bucle = 1
        while Bucle ==1:

            print ("Generador de Ondas\n")

            print ("Seleccione el tipo de onda que desea generar\n")



            Tono = input("Digite la frecuencia del tono a generar: ")
            Tiempo = input("Ingrese el tiempo de audio en segundos: ")
            Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
            MaxBits = input("Ingrese el numero de bits: ")
            Nombre = raw_input("Ingrese el nombre del archivo a generar: ")

            print ("1. Onda Sinusoidal")
            print ("2. Onda Cuadrada")
            print ("3. Onda Triangular")
            print ("4. Onda Sierra\n")

            opcion = input("Digite una opcion: ")

            if opcion == 1:
                    print("Senosoidal")

                    onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    datos = onda.generar()

                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)
                    onda.graficar(datos)

            if opcion == 2:
                    print("Cuadrada")

                    onda = square(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    onda.generar()
                    onda.graficar()

            if opcion == 3:
                    print("Triangular")

                    onda = triangle(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    onda.generar()
                    onda.graficar()

            if opcion == 4:
                    print("Diente Sierra")

                    onda = sawtooth(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    onda.generar()
                    onda.graficar()

            Confirmacion = int(input("Desea generar otra onda? 1.Si 2.No"))

            if Confirmacion != 1:
                Bucle=0
                print ("CHAO")





if __name__ == "__main__":
    main()
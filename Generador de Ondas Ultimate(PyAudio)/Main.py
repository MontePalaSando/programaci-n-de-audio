#LUIS SANDOVAL
#LIBARDO MONTEALEGRE
#ANDRES PALACIOS


# Importar Librerias
from Seno import Seno
from Guardar import Archivo
from Cuadrada import cuadro
from Triangulo import triangulo
from Diente import sierra
from ReproAudio import Audio

def main():
        Bucle = 1
        while Bucle ==1:

            print ("Generador de Ondas\n")

            print ("Seleccione el tipo de onda que desea generar\n")


            #Datos de entrada
            Tono = input("Digite la frecuencia del tono a generar: ")
            Tiempo = input("Ingrese el tiempo de audio en segundos: ")
            Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
            MaxBits = input("Ingrese el numero de bits: ")
            NivelPi = input("Ingrese el nivel pico deseado: ")
            Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
            Buffer = 1024

            print ("1. Onda Sinusoidal")
            print ("2. Onda Cuadrada")
            print ("3. Onda Triangular")
            print ("4. Onda Sierra\n")
            #Desarrollado por: Libardo Montealegre
            opcion = input("Digite una opcion: ")

            if opcion == 1:
                    print("Senosoidal")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Modificar nivel Pico
                    datosAjustados = onda.NivelModificado(datos, NivelPi)
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datosAjustados)
                    #Graficar
                    onda.graficar(datos[:500])

            if opcion == 2:
                    print("Cuadrada")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = cuadro(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Modificar nivel Pico
                    datosAjustados = onda.NivelModificado(datos, NivelPi)
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datosAjustados)
                    #Graficar
                    onda.graficar(datos[:500])

            if opcion == 3:
                    print("Triangular")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = triangulo(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Modificar nivel Pico
                    datosAjustados = onda.NivelModificado(datos, NivelPi)
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datosAjustados)
                    #Graficar
                    onda.graficar(datos[:500])

            if opcion == 4:
                    print("Diente Sierra")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = sierra(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Modificar nivel Pico
                    datosAjustados = onda.NivelModificado(datos, NivelPi)
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datosAjustados)
                    #Graficar
                    onda.graficar(datos[:500])

            Reproducir = int(input("Desea reproducir la onda? 1.Si 2.No  "))

            if Reproducir == 1:

                audio = Audio(Buffer)
                Datos = audio.abrir(Nombre)
                audio.inicio(Datos[0],Datos[1],Datos[2])
                audio.reproducir(Datos[3])
                audio.cerrar()


            Confirmacion = int(input("Desea generar otra onda? 1.Si 2.No  "))

            if Confirmacion != 1:
                Bucle=0
                print ("Hasta Luego")





if __name__ == "__main__":
    main()
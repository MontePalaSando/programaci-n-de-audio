#LUIS SANDOVAL
#LIBARDO MONTEALEGRE
#ANDRES PALACIOS


# Importar Librerias
from AmplitudPico import Calc1
from AmplitudPico import Calc2
from RangoDinamico import Calc3
from RangoDinamico import Calc4
from Valores import Calc5
from Valores import Calc6
from ProgramaNiveles import Nivelpico
from ProgramaNiveles import NivelRMS
from ProgramaNiveles import NivelLeq
from Guardar import Archivo
from GeneradorDeTonos import Seno
from GeneradorDeTonos import cuadro
from GeneradorDeTonos import triangulo
from GeneradorDeTonos import sierra

def main():
        Bucle = 1
        while Bucle ==1:

            print ("EJERCICIOS\n")

            print ("Seleccione el ejercicio a realizar \n")

            print ("1. Exprese los siguientes valores de amplitud pico en dBFS")
            print ("2. Obtenga rango dinamico para 2,4,6 y 12 bits")
            print ("3. Obtenga los valores de las opereciones en dBFS")
            print ("4. Programa (Niveles Pico, RMS, leq)")
            print ("5. Generador de tonos puros\n")

            opcion = input("Digite una opcion: \n")

            # PUNTO 1

            if opcion == 1:
                print ("1) Exprese los valores de amplitud pico en dBFS\n")
                print ("1. Modo ingresar valores")
                print ("2. Modo arrojar resultados")

                opcion2 = input("Seleccione un modo\n")
                if opcion2 == 1:
                    print("1. Modo ingresar valores")

                    VP= input("Digite el valor pico maximo: ")
                    Bits = input("Ingrese el numero de bits: ")

                    #Crear la instancia de la clase audio para generar los datos
                    resul1 = Calc1(VP, Bits)
                    resul1.operar()

                if opcion2 == 2:
                    print("2. Modo arrojar resultados")
                    resul2 = Calc2()
                    resul2.operar2()

            # PUNTO 2

            if opcion == 2:
                print ("2) Obtenga rango dinamico para 2,4,6 y 12 bits\n")
                print ("1. Modo ingresar valores")
                print ("2. Modo arrojar resultados")

                opcion3 = input("Seleccione un modo\n")

                if opcion3 == 1:
                    print("1. Modo ingresar valores")

                    NumBits = input("Ingrese el numero de bits: ")

                    #Crear la instancia de la clase audio para generar los datos
                    resul3 = Calc3(NumBits)
                    resul3.operar3()

                if opcion3 == 2:
                    print("2. Modo arrojar resultados")
                    resul4 = Calc4()
                    resul4.operar4()

            # PUNTO 3

            if opcion == 3:
                print ("3) Obtenga los valores de las opereciones en dBFS\n")
                print ("1. Modo ingresar valores")
                print ("2. Modo arrojar resultados")

                opcion4 = input("Seleccione un modo\n")

                if opcion4 == 1:
                    print("1. Modo ingresar valores")

                    dBFS1= input("Digite primer valor dBFS: ")
                    dBFS2 = input("Digite segundo valor dBFS: ")

                    #Crear la instancia de la clase audio para generar los datos
                    resul5 = Calc5(dBFS1, dBFS2)
                    resul5.operar5()


                if opcion4 == 2:
                    print("2. Modo arrojar resultados")
                    resul6 = Calc6()
                    resul6.operar6()

            #PUNTO 4

            if opcion == 4:
                print ("4) Programa (Niveles Pico, RMS, leq\n")

                print('Ingrese la ubicacion del archivo de audio: ')
                AudioIn= raw_input('')

                #Crear la instancia de la clase audio para generar los datos
                resul7 = Nivelpico(AudioIn)
                resul7.operar7()
                resul8 = NivelRMS(AudioIn)
                resul8.operar8()
                resul9 = NivelLeq(AudioIn)
                resul9.operar9()


            #PUNTO 5

            if opcion == 5:
                print ("5) Generador de tonos puros\n")

                print ("Seleccione el tipo de onda que desea generar\n")


                #Datos de entrada
                Tono = input("Digite la frecuencia del tono a generar: ")
                Tiempo = input("Ingrese el tiempo de audio en segundos: ")
                Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
                MaxBits = input("Ingrese el numero de bits: ")
                Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
                NivelPi = input("Ingrese el nivel pico deseado: ")

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

            Confirmacion = int(input("Desea realizar otro ejercicio? 1.Si 2.No"))

            if Confirmacion != 1:
                Bucle=0
                print ("Hasta Luego")





if __name__ == "__main__":
    main()
#LUIS SANDOVAL
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

            Do= 261.63
            Re=293.66
            Mi=324.63
            Fa=349.23
            Sol=342
            La=440
            Si=493

            Bl= 1 #Negra
            Wh = 2#Blanca
            Co= 0.5#Corchea



            #Datos de entrada
            Tono = [Re,Re,Mi,Re,Sol,Fa,Re,Re,Sol,Re,Re,Re,Si,Sol,Fa,Mi,Do,Do,Si,Sol,La,Sol,Re,Re,Sol]
            Tiempo =[Co,Co,Bl,Bl,Bl,Wh,Co,Co,Wh,Co,Co,Bl,Bl,Bl,Bl,Bl,Co,Co,Bl,Bl,Bl,Wh,Co,Co,Wh]
            Frecuenciadesampleo = 44100/120
            MaxBits = 16
            Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
            Buffer = 1024

            print ("1. Onda Sinusoidal")
            print ("2. Onda Cuadrada")
            print ("3. Onda Triangular")
            print ("4. Onda Sierra\n")

            opcion = input("Digite una opcion: ")

            if opcion == 1:
                    print("Senosoidal")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)

            if opcion == 2:
                    print("Cuadrada")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = cuadro(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)

            if opcion == 3:
                    print("Triangular")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = triangulo(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)


            if opcion == 4:
                    #Crear la instancia de la clase audio para generar los datos
                    onda = sierra(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)


            Reproducir = int(input("Desea reproducir la onda? 1.Si 2.No  "))

            if Reproducir == 1:

                audio = Audio(Buffer)
                Datos = audio.abrir(Nombre)
                audio.inicio(Datos[0],Datos[1],Datos[2])
                audio.reproducir(Datos[3])
                audio.cerrar()



            Confirmacion = int(input("Desea generar otra onda? 1.Si 2.No"))

            if Confirmacion != 1:
                Bucle=0
                print ("CHAO")





if __name__ == "__main__":
    main()
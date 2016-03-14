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

            Do= 523.25
            Re= 587.33
            Mi= 659.26
            Fa= 698.46
            Sol=392
            La=440
            Si=493.88

            #Tempo= 140 bpm
            Bl= 0.42 #Negra
            Wh = 0.85#Blanca
            Co= 0.21#Corchea
            BlPto= Bl + (Bl/2) #Negra Con Punto
            WhPto= Wh + (Wh/2) #Blanca con Punto

            # Song: Luis Silva - Venezuela

            #Datos de entrada
            Tono = [Sol,Do,Do,Re,Do,Re,Mi,Re,Do,Sol,Sol,Do,Sol,La,Do,Fa,Mi,Mi,Mi,Mi,Mi,Fa,Mi,Re,Re,Do,Si,Do,Mi,Mi,Mi,Mi,Re,La,Do,Si]
            Tiempo =[Bl,Bl,Bl,Bl,Bl,Bl,Bl,Bl,Bl,WhPto,Bl,Bl,Bl,Bl,Bl,Bl,WhPto,WhPto,Bl,BlPto,Co,Bl,Bl,Bl,Bl,Bl,Bl,WhPto,Bl,BlPto,Co,Bl,Bl,Bl,WhPto,WhPto]
            Frecuenciadesampleo = float(60.0/140)*44100
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
                    #Graficar
                    onda.graficar(datos[:500])
                    #Generar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)

            if opcion == 2:
                    print("Cuadrada")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = cuadro(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar
                    onda.graficar(datos[:500])
                    #Generar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)

            if opcion == 3:
                    print("Triangular")
                    #Crear la instancia de la clase audio para generar los datos
                    onda = triangulo(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar
                    onda.graficar(datos[:500])
                    #Generar Archivo
                    archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
                    archivo.archivar(datos)


            if opcion == 4:
                    #Crear la instancia de la clase audio para generar los datos
                    onda = sierra(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                    #Generar el arreglo
                    datos = onda.generar()
                    #Graficar
                    onda.graficar(datos[:500])
                    #Generar Archivo
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
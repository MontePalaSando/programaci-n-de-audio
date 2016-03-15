#LUIS SANDOVAL
#C.E 475112
#Codigo 20141618121
# Importar Librerias
from Seno import Seno
from Guardar import Archivo
from Cuadrada import cuadro
from Triangulo import triangulo
from Diente import sierra
from ReproAudio import Audio
from Mayor import Mayores
from Menor import Menores
from Aumento import Aumentados
from Dismucion import Disminuido
def main():
        Bucle = 1
        while Bucle ==1:

            print ("Generador de Ondas\n")
            print ("Seleccione el tipo de onda que desea generar\n")

            Do= 261.63
            Doso=277.18
            Re= 293.66
            Reso=311.13
            Mi= 329.63
            Fa= 349.23
            Faso= 369.99
            Sol=392
            Solso=415.30
            La=440
            Laso=466.16
            Si=493.88

            Silencio= 0

            Do2= 523.25
            Doso2=554.37
            Re2= 587.33
            Reso2=622.25
            Mi2= 659.26
            Fa2= 698.46
            Faso2=739.99
            Sol2=783.99
            Solso2=830.61
            La2=880.0
            Laso2=932.33
            Si2=987.77

            #Datos de entrada
            #Codigo: 20141618121
            #Ultimos digitos: 21
            #Tempo= 210 bpm
            Bl= 0.28 #Negra
            Frecuenciadesampleo = float(0.28)*44100
            MaxBits = 16
            Buffer = 1024
            Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
            print("Notas fundamentales: ")
            print ("1. DO")
            print ("2. DO#")
            print ("3. RE")
            print ("4. RE#")
            print ("5. MI")
            print ("6. FA")
            print ("7. FA#")
            print ("8. SOL")
            print ("9. SOL#")
            print ("10. LA")
            print ("11. LA#")
            print ("12. SI \n")

            Notas = [Do,Doso,Re,Reso,Mi,Fa,Faso,Sol,Solso,La,Laso,Si,Do2,Doso2,Re2,Reso2,Mi2,Fa2,Faso2,Sol2,Solso2,La2,Laso2,Si2,Silencio]


            opcion2 = input("Digite el numero de la nota que desea:")

            if opcion2 == 1: # DO
                print ("1. DO")
                posicion = 0
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 2: # DO#
                print ("2. DO#")
                posicion = 1
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 3: # RE
                print ("3. RE")
                posicion = 2
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]


            if opcion2 == 4: # RE#
                print ("4. RE#")
                posicion = 3
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 5: # MI
                print ("5. MI")
                posicion = 4
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 6: # FA
                print ("6. FA")
                posicion = 5
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 7: # FA#
                print ("7. FA#")
                posicion = 6
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 8: # SOL
                print ("8. SOL")
                posicion = 7
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]


            if opcion2 == 9: # SOL#
                print ("9. SOL#")
                posicion = 8
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 10: # LA
                print ("10. LA")
                posicion = 9
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 11: # LA#
                print ("11. LA#")
                posicion = 10
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

            if opcion2 == 12: # SI
                print ("12. SI \n")
                posicion = 11
                opcion3 = input("Digite que tipo de acorde desea?: 1. MAYORES  2. MENORES  3.Aumentados 4.Disminuidos  ")

                if opcion3 == 1:
                    print("1. MAYORES")

                    fundamental1= Notas[posicion]
                    Acorde = Mayores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 2:
                    print("2. MENORES")

                    fundamental1= Notas[posicion]
                    Acorde = Menores(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 3:
                    print("3.Aumentados")
                    fundamental1= Notas[posicion]
                    Acorde = Aumentados(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

                if opcion3 == 4:
                    print("4.Disminuidos")
                    fundamental1= Notas[posicion]
                    Acorde = Disminuido(fundamental1,Notas,posicion)
                    Tono = Acorde.generarAcorde()
                    Tiempo =[Bl,Bl,Bl,Bl]

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
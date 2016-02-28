import math

class Calc5:


            def __init__(self, dBFS1,dBFS2):
                self.dBFS1 = dBFS1*-1
                self.dBFS2 = dBFS2*-1

            def operar5(self):

                Max= ((2**16)*(10**(float(self.dBFS2)/20)))
                Max1= ((2**16)*(10**(float(self.dBFS2)/20)))
                MaxResul= Max + Max1
                resul=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul)


class Calc6:

            def operar6(self):
                print("Para 10dBFS + 12dBFS")
                Max= ((2**16)*(10**(float(-10)/20)))
                Max1= ((2**16)*(10**(float(-12)/20)))
                MaxResul= Max + Max1
                resul1=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul1)
                print ("\n")

                print("Para 20dBFS - 10dBFS")
                Max= ((2**16)*(10**(float(-20)/20)))
                Max1= ((2**16)*(10**(float(-10)/20)))
                MaxResul= Max - Max1
                resul2=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es:")
                print(resul2)
                print ("\n")

                print("Para 30d BFS + 30dBFS")
                Max= ((2**16)*(10**(float(-30)/20)))
                Max1= ((2**16)*(10**(float(-30)/20)))
                MaxResul= Max + Max1
                resul3=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es:")
                print(resul3)
                print ("\n")

                print("Para 15dBFS + 45dBFS ")
                Max= ((2**16)*(10**(float(15)/20)))
                Max1= ((2**16)*(10**(float(45)/20)))
                MaxResul= Max + Max1
                resul4=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es:")
                print(resul4)
                print ("\n")

                print("Para 25dBFS - 8dBFS")
                Max= ((2**16)*(10**(float(-25)/20)))
                Max1= ((2**16)*(10**(float(-8)/20)))
                MaxResul= Max - Max1
                resul5=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul5)
                print ("\n")

                print("Para 90dBFS - 45dBFS")
                Max= ((2**16)*(10**(float(-90)/20)))
                Max1= ((2**16)*(10**(float(-45)/20)))
                MaxResul= Max + Max1
                resul6=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul6)
                print ("\n")

                print("Para 90dBFS + 90dBFS")
                Max= ((2**16)*(10**(float(-90)/20)))
                Max1= ((2**16)*(10**(float(-90)/20)))
                MaxResul= Max + Max1
                resul7=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul7)
                print ("\n")

                print("Para 10dBFS - 90dBFS")
                Max= ((2**16)*(10**(float(-10)/20)))
                Max1= ((2**16)*(10**(float(-90)/20)))
                MaxResul= Max + Max1
                resul8=20*math.log10(float(MaxResul)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul8)
                print ("\n")
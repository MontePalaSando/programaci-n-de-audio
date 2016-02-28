import math

class Calc1:


            def __init__(self, VP, Bits):
                self.VP = VP
                self.Bits = Bits

            def operar(self):

                resul=20*math.log10(abs((float(self.VP))/(2**self.Bits)))
                print("La amplitud pico en dBFS es: ")
                print(resul)


class Calc2:

            def operar2(self):
                print("Para 2565 ")
                resul=20*math.log10(float(2565)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul)
                print ("\n")

                print("Para -7890 ")
                resul2=20*math.log10(abs((float(-7890))/(2**16)))
                print("La amplitud pico en dBFS es: ")
                print(resul2)
                print ("\n")

                print("Para 12567 ")
                resul3=20*math.log10(float(12567)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul3)
                print ("\n")

                print("Para 15679 ")
                resul4=20*math.log10(float(15679)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul4)
                print ("\n")

                print("Para 30908 ")
                resul5=20*math.log10(float(30908)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul5)
                print ("\n")

                print("Para -6890 ")
                resul6=20*math.log10(abs((float(-6890))/(2**16)))
                print("La amplitud pico en dBFS es: ")
                print(resul6)
                print ("\n")

                print("Para -12789 ")
                resul7=20*math.log10(abs((float(-12789))/(2**16)))
                print("La amplitud pico en dBFS es: ")
                print(resul7)
                print ("\n")

                print("Para 1 ")
                resul8=20*math.log10(float(1)/(2**16))
                print("La amplitud pico en dBFS es: ")
                print(resul8)
                print ("\n")


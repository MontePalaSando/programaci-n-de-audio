

def NivelModificado1(datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            NewArray1 = datos * NivelNew
            return NewArray1

def NivelModificado2(datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            NewArray2 = datos * NivelNew
            return NewArray2

def NivelModificado3(datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            NewArray3 = datos * NivelNew
            return NewArray3

def NivelModificado4(datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            NewArray4 = datos * NivelNew
            return NewArray4

def NivelModificadoMix(datos, Nuevolevel):
            Nivelpico = max(abs(datos))
            Nivelpi = (10**(Nuevolevel/20))*((2**16)/2.0)
            NivelNew = Nivelpi / float(Nivelpico)
            NewArrayMix= datos * NivelNew
            return NewArrayMix
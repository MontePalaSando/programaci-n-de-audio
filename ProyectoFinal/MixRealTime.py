
import pygame.mixer

global Audio1,Audio2,Audio3,Audio4

def RealTimePLay1(Audio1,Audio2,Audio3,Audio4,Nivel1,Nivel2,Nivel3,Nivel4,Nivel6,Mute1,Mute2,Mute3,Mute4):

    pygame.mixer.init(44100,-16,2,4096)
    Nivel1= Nivel1/(-20)
    Nivel2= Nivel2/(-20)
    Nivel3= Nivel3/(-20)
    Nivel4= Nivel4/(-20)

    Audio1.set_volume(Nivel1)
    Audio2.set_volume(Nivel2)
    Audio3.set_volume(Nivel3)
    Audio4.set_volume(Nivel4)

    Nivel6= Nivel6/(-20)

    if Nivel6== 0.0:
        Audio1.set_volume(Nivel6)
        Audio2.set_volume(Nivel6)
        Audio3.set_volume(Nivel6)
        Audio4.set_volume(Nivel6)
    else:
        if Nivel1>Nivel6:
            Audio1.set_volume(Nivel6)
        else:
            Audio1.set_volume(Nivel1)

        if Nivel2>Nivel6:
            Audio2.set_volume(Nivel6)
        else:
            Audio2.set_volume(Nivel2)

        if Nivel3>Nivel6:
            Audio3.set_volume(Nivel6)
        else:
            Audio3.set_volume(Nivel3)

        if Nivel4>Nivel6:
            Audio4.set_volume(Nivel6)
        else:
            Audio4.set_volume(Nivel4)

    Audio1.play()
    Audio2.play()
    Audio3.play()
    Audio4.play()




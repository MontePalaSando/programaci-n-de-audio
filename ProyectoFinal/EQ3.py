#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from Tkinter import *
from Tkinter import Tk
import tkMessageBox

def EQ3():

    # Creacion de la ventana

    EQ = Tk()

    EQ.title("EQ 3 ")
    EQ.config(bg = "black")

    d = BooleanVar(EQ)
    e = BooleanVar(EQ)
    e.set(False)
    f = BooleanVar(EQ)
    f.set(False)

    global arreglorcompre1

    arreglocompre1 = []

    # Uso de frames para organizar la ventana.
    frame1 = Frame(EQ,bg = "black")
    frame1.pack(side=TOP)
    frame2 = Frame(EQ,bg = "black")
    frame2.pack(side=LEFT)
    frame3 = Frame(EQ,bg = "black")
    frame3.pack(side=LEFT)
    frame4 = Frame(EQ,bg = "black")
    frame4.pack(side=LEFT)
    frame5 = Frame(EQ,bg = "black")
    frame5.pack(side=LEFT)


# Label para la interfraz grafica - definicion de los botones

    Label1= Label(frame1, padx=15, pady=1, text="EQ 3 ",fg = "white",bg = "black")
    Label1.pack(side=TOP)



    espacio2= Label(frame1, padx=15, pady=1, text=" ",fg = "white",bg = "black")
    espacio2.pack(side=TOP)


    Label2= Label(frame2, padx=15, pady=1, text="LF",fg = "white",bg = "black")
    Label2.pack(side=TOP)

    Label22= Label(frame2, padx=15, pady=1, text="Q",fg = "white",bg = "black")
    Label22.pack(side=TOP)
    Q1= Scale(frame2, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "yellow", fg="black")
    Q1.pack(side=TOP, padx=1, pady=1)

    Label223= Label(frame2, padx=15, pady=1, text="Freq",fg = "white",bg = "black")
    Label223.pack(side=TOP)

    Freq1= Scale(frame2, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "yellow", fg="black")
    Freq1.pack(side=TOP, padx=1, pady=1)

    Label224= Label(frame2, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
    Label224.pack(side=TOP)

    Gain1= Scale(frame2, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "yellow", fg="black")
    Gain1.pack(side=TOP, padx=1, pady=1)



    Label3= Label(frame3, padx=15, pady=1, text="MF",fg = "white",bg = "black")
    Label3.pack(side=TOP)

    Label33= Label(frame3, padx=15, pady=1, text="Q",fg = "white",bg = "black")
    Label33.pack(side=TOP)

    Q3= Scale(frame3, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "red", fg="black")
    Q3.pack(side=TOP, padx=1, pady=1)

    Label333= Label(frame3, padx=15, pady=1, text="Freq",fg = "white",bg = "black")
    Label333.pack(side=TOP)

    Freq3= Scale(frame3, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "red", fg="black")
    Freq3.pack(side=TOP, padx=1, pady=1)

    Label33333= Label(frame3, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
    Label33333.pack(side=TOP)

    Gain3= Scale(frame3, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "red", fg="black")
    Gain3.pack(side=TOP, padx=1, pady=1)



    Label4= Label(frame4, padx=15, pady=1, text="HF",fg = "white",bg = "black")
    Label4.pack(side=TOP)

    Label44= Label(frame4, padx=15, pady=1, text="Q",fg = "white",bg = "black")
    Label44.pack(side=TOP)

    Q4= Scale(frame4, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "blue", fg="black")
    Q4.pack(side=TOP, padx=1, pady=1)

    Label444= Label(frame4, padx=15, pady=1, text="Freq",fg = "white",bg = "black")
    Label444.pack(side=TOP)

    Freq4= Scale(frame4, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "blue", fg="black")
    Freq4.pack(side=TOP, padx=1, pady=1)

    Label44444= Label(frame4, padx=15, pady=1, text="Gain",fg = "white",bg = "black")
    Label44444.pack(side=TOP)

    Gain4= Scale(frame4, from_= 0.0, to=-60.0,length = 200, orient= HORIZONTAL, resolution=0.1,bg = "blue", fg="black")
    Gain4.pack(side=TOP, padx=1, pady=1)



    EQ.mainloop()

if __name__ == "__main__":
    EQ3()
#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

from tkFileDialog import askopenfilename
import wave
import struct
import  pyaudio

global Audio1, File1
Audio1= []


def Abrir1():

    global Audio1, File1

    File1= askopenfilename()

    WAV1=wave.open(File1, "rb")
    Array=int(WAV1.getnframes())

    for i in range(0, Array):
            datos=WAV1.readframes(1)
            packed_value = struct.unpack('<h', datos)
            Audio1.append(packed_value)


def reproduce1():
        rf = wave.open(File1, 'rb')
        prof = rf.getsampwidth()
        channels = rf.getnchannels()
        rate = rf.getframerate()
        audioN = pyaudio.PyAudio()
        streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
        datos = rf.readframes(1024)
        while datos != '':
            streamN.write(datos)
            datos = rf.readframes(1024)

        rf.close()
        streamN.stop_stream()
        streamN.close()
        audioN.terminate()







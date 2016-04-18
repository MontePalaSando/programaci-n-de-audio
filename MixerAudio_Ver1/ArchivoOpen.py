from tkFileDialog import askopenfilename
import wave
import struct
import  pyaudio

global Audio1, Audio2, Audio3, File1,File2,File3
Audio1= []
Audio2= []
Audio3= []

def Abrir1():

    global Audio1, File1

    File1= askopenfilename()

    WAV1=wave.open(File1, "rb")
    Array=int(WAV1.getnframes())

    for i in range(0, Array):
            datos=WAV1.readframes(1)
            packed_value = struct.unpack('<h', datos)
            Audio1.append(packed_value)



def Abrir2():

    global Audio2, File2

    File2= askopenfilename()

    WAV2=wave.open(File2, "rb")
    Array2=int(WAV2.getnframes())

    for i in range(0, Array2):
            datos=WAV2.readframes(1)
            packed_value = struct.unpack('<h', datos)
            Audio2.append(packed_value)


def Abrir3():

    global Audio3, File3

    File3= askopenfilename()

    WAV3=wave.open(File3, "rb")
    Array3=int(WAV3.getnframes())

    for i in range(0, Array3):
            datos=WAV3.readframes(1)
            packed_value = struct.unpack('<h', datos)
            Audio3.append(packed_value)


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

def reproduce2():
        rf = wave.open(File2, 'rb')
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


def reproduce3():
        rf = wave.open(File3, 'rb')
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






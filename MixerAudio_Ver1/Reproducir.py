import pyaudio
import wave

class Repro:

    def reproduce(nombre):
        rf = wave.open(nombre + '.wav', 'rb')
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
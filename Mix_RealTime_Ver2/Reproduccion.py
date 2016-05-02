#LUIS SANDOVAL
#ANDRES PALACIO
#LIBARDO MONTEALEGRE

import  wave
import pyaudio

class Repro:

    def __init__(self, CHUNK):
        self.CHUNK = CHUNK


    def open(self, nombre):

        self.wf = wave.open(nombre, 'rb')
        sampwidth = self.wf.getsampwidth()
        channels = self.wf.getnchannels()
        rate = self.wf.getframerate()
        return (sampwidth, channels, rate, self.wf)

# funcion para reproducir en simultaneo junto con los threads

    def start(self, sampwidth, channels, framerate):
        self.p = pyaudio.PyAudio()
        self.stream=self.p.open(format=self.p.get_format_from_width(sampwidth),
                        channels=channels,
                        rate=framerate,
                        output=True)

# reproducion a partir de la obtencion de cuadros de archivo de audio por medio de un buffer

    def play(self, archivodeaudio):
        data = archivodeaudio.readframes(self.CHUNK)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.CHUNK)

#funcion para hacer un standby para cuando los archivos terminan de reproducirce

    def closed(self):

        self.wf.close()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()




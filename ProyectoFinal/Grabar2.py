
import pyaudio
import wave

class Grabador2:

    def __init__(self, BUFFER, FORMAT, CHANNELS, RATE):
        self.BUFFER = BUFFER
        self.FORMAT = FORMAT
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.audio = pyaudio.PyAudio()

    def inicio(self):
        self.arreglo = []
        data = self.audio.get_default_host_api_info()
        print data
        self.transferencia = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.BUFFER)

    def grabacion(self):
        datos = self.transferencia.read(self.BUFFER)
        self.arreglo.append(datos)

    def parar(self):
        self.transferencia.stop_stream()
        self.transferencia.close()
        self.audio.terminate()
        return self.arreglo

    def creaAudio(self, nombre):
        wf = wave.open(nombre+'.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setframerate(self.RATE)
        wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wf.writeframes(b''.join(self.arreglo))
        wf.close()
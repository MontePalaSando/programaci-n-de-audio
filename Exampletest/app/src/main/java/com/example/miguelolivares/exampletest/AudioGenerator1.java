package com.example.miguelolivares.exampletest;

import android.os.Environment;

import java.io.IOException;
import java.io.RandomAccessFile;

/**
 * Created by miguelolivares on 2/10/16.
 */
public class AudioGenerator1 {

    // Output file path
   // private String          filePath = null;


    // File writer (only in uncompressed mode)
   private RandomAccessFile randomAccessWriter;

    // Number of channels, sample rate, sample size(size in bits), buffer size, audio source, sample size(see AudioFormat)
    private short                    nChannels = 1;
    private int                      sRate = 44100;
    private short                    mBitsPersample = 16;
    private String filePath = Environment.getExternalStorageDirectory() + "/grabacion.wav";





    public void HeaderWrite() throws IOException {
        try {
            randomAccessWriter = new RandomAccessFile(filePath, "rw");
            randomAccessWriter.setLength(0);
            randomAccessWriter.writeBytes("RIFF");
            randomAccessWriter.writeInt(0); // Final file size not known yet, write 0
            randomAccessWriter.writeBytes("WAVE");
            randomAccessWriter.writeBytes("fmt ");
            randomAccessWriter.writeInt(Integer.reverseBytes(16)); // Sub-chunk size, 16 for PCM
            randomAccessWriter.writeShort(Short.reverseBytes((short) 1)); // AudioFormat, 1 for PCM
            randomAccessWriter.writeShort(Short.reverseBytes(nChannels));// Number of channels, 1 for mono, 2 for stereo
            randomAccessWriter.writeInt(Integer.reverseBytes(sRate)); // Sample rate
            randomAccessWriter.writeInt(Integer.reverseBytes(sRate*nChannels*mBitsPersample/8)); // Byte rate, SampleRate*NumberOfChannels*mBitsPersample/8
            randomAccessWriter.writeShort(Short.reverseBytes((short)(nChannels*mBitsPersample/8))); // Block align, NumberOfChannels*mBitsPersample/8
            randomAccessWriter.writeShort(Short.reverseBytes(mBitsPersample)); // Bits per sample
            randomAccessWriter.writeBytes("data"); // Set file length to 0, to prevent unexpected behavior in case the file already existed
        } catch (IOException e) {
            e.printStackTrace();
        }



    }



    public void AudioGenerator1(int duracion, int frecuencia) throws IOException {
        int numSamples = duracion * sRate;
        try {
            randomAccessWriter.writeInt(Integer.reverseBytes(numSamples));
        } catch (IOException e) {
            e.printStackTrace();
        }
        double sample;
        Double Amplitud = Math.pow(2, mBitsPersample);

        /* Short value; */
        //ArrayList<Byte[]> Datos = new ArrayList<>();
        for (int i = 0; i < numSamples; ++i) {
            sample = Amplitud*Math.sin(2 * Math.PI * i / (sRate / frecuencia));
            short s1 = (short)sample;
            try {
                randomAccessWriter.writeShort(Short.reverseBytes(s1));
            } catch (IOException e) {
                e.printStackTrace();
            }

            //Datos.add(value);
        }

    }




}

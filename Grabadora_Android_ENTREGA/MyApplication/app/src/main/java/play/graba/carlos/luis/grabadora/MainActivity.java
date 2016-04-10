/*
programa desarrollado por
Luis Carlos Sandoval
Andres Felipe Palacio
Libardo Montealegre
 */

package play.graba.carlos.luis.grabadora;


//importar las funciones de androir para grabar y reproducir los archivos de audio
import android.app.Activity;
import android.media.MediaPlayer;
import android.media.MediaRecorder;

import android.os.Bundle;
import android.os.Environment;

import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageButton;


import android.widget.ImageView;
import android.widget.Toast;

import java.io.IOException;

//implemento de las imagenes para interfaz grafica
public class MainActivity extends Activity {
    ImageButton record, stop, play ;
    private MediaRecorder myAudioRecorder;
    private String outputFile = null;

    //se asigna las funciones para cada imageButton (grabar, parar la grabacion, reproducir)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        play = (ImageButton) findViewById(R.id.imageButton3);
        stop = (ImageButton) findViewById(R.id.imageButton2);
        record = (ImageButton) findViewById(R.id.imageButton);

        //se asigna los valores booleanos para los botones de parar y reproducir.
        stop.setEnabled(false);
        play.setEnabled(false);

        //se asigna el formato que contendra el archivo de audio
        outputFile = Environment.getExternalStorageDirectory().getAbsolutePath() + "/recording.wav";
        ;

        //mediante permisos se habilita el uso de dispositivos externos para poder grabar y reproducir
        myAudioRecorder = new MediaRecorder();
        myAudioRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        myAudioRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
        myAudioRecorder.setAudioEncoder(MediaRecorder.OutputFormat.AMR_NB);
        myAudioRecorder.setOutputFile(outputFile);

        //se asigan los valores que interactuan con el boton de grabar
        record.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    myAudioRecorder.prepare();
                    myAudioRecorder.start();
                } catch (IllegalStateException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }

                //valores booleanos para los botones de grabar y parar
                //cuando la funcion esta en proceso, el boton de grabar se desactiva y el boton stop se habilita
                record.setEnabled(false);
                stop.setEnabled(true);

                //se habilita un texto resultante del valor booleano del boton grabar que indica que la funcion esta en proceso
                Toast.makeText(getApplicationContext(), "Grabando...", Toast.LENGTH_LONG).show();
            }
        });

        // el codigo de .setonclick se utiliza para activar las diferentes funciones que cumple el boton cuando es oprimido

        //funciones que cumple el boton de parar
        stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                myAudioRecorder.stop();
                myAudioRecorder.release();
                myAudioRecorder = null;

                //se asignan los valores booleanos de los botones justamente despues de parar la grabacion
                stop.setEnabled(false);
                play.setEnabled(true);
            }
        });

        //asignacion de la funcion del boton play
        play.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) throws IllegalArgumentException, SecurityException, IllegalStateException {
                MediaPlayer m = new MediaPlayer();

                //uso de try para evluar si hay un archivo de audio para reproducir
                //en caso de no encontrar un archivo el programa continua fucionando
                try {
                    m.setDataSource(outputFile);
                } catch (IOException e) {
                    e.printStackTrace();
                }

                try {
                    m.prepare();
                } catch (IOException e) {
                    e.printStackTrace();
                }

                //texto emergente para indicar que la aplicacion esta reproduciendo un audio previamente grabado
                m.start();
                Toast.makeText(getApplicationContext(), "Reproduciendo...", Toast.LENGTH_LONG).show();

            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    //funcion que se utiliza para retornar el valor o ID del usuarion
    //se utiliza para berificar los valores que arroja las diferentes opciones disponibles en la aplicacion
    public boolean onOptionsItemSelected(MenuItem item) {

        int id = item.getItemId();

        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}

package com.example.miguelolivares.exampletest;

import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.RadioGroup;
import android.widget.RadioButton;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.common.api.GoogleApiClient;

import java.io.IOException;


public class Generar extends AppCompatActivity {

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;

    private ListView Texto;
    private Button Generar;
    private EditText time_input, tone_input;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_generar);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        final AudioGenerator AG = new AudioGenerator();

        time_input = (EditText) findViewById(R.id.time_input);
        tone_input = (EditText) findViewById(R.id.tone_input);

        Generar = (Button) findViewById(R.id.button);

        Generar.setOnClickListener(new View.OnClickListener() {


            @Override
            public void onClick(View view) {

                public void onRadioButtonClicked(View view) {
                    // Is the button now checked?
                    boolean checked = ((RadioButton) view).isChecked();

                    // Check which radio button was clicked
                    switch(view.getId()) {
                        case R.id.radioButton:
                            if (checked)
                                // Pirates are the best
                                break;
                        case R.id.radioButton2:
                            if (checked)
                                // Ninjas rule
                                break;
                        case R.id.radioButton3:
                            if (checked)
                                // Ninjas rule
                                break;
                        case R.id.radioButton4:
                            if (checked)
                                // Ninjas rule
                                break;
                    }
                }




                try {
                    Snackbar.make(view, "Generando Tono", Snackbar.LENGTH_LONG)
                            .setAction("Action", null).show();
                    AG.HeaderWrite();
                    AG.AudioGenerator(Integer.parseInt(time_input.getText().toString()), Integer.parseInt(tone_input.getText().toString()));
                } catch (IOException e) {
                    e.printStackTrace();

                }

                Snackbar.make(view, "Tono de " + tone_input.getText().toString() +"Hz y "+ time_input.getText().toString()+ " segundos generado", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });


        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
    }

    @Override
    public void onStart() {
        super.onStart();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Generar Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://com.example.miguelolivares.exampletest/http/host/path")
        );
        AppIndex.AppIndexApi.start(client, viewAction);
    }

    @Override
    public void onStop() {
        super.onStop();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Generar Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://com.example.miguelolivares.exampletest/http/host/path")
        );
        AppIndex.AppIndexApi.end(client, viewAction);
        client.disconnect();
    }
}

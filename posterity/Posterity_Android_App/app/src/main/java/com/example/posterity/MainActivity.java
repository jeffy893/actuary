package com.example.posterity;

import android.os.Bundle;


import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.SeekBar;

public class MainActivity extends AppCompatActivity {


    final EditText editText2 = findViewById(R.id.editText2);
    final EditText editText = findViewById(R.id.editText);
    final  SeekBar seekBar2 = findViewById(R.id.seekBar2);
        seekBar2.setMax(1);
    final SeekBar seekBar = findViewById(R.id.seekBar);
        seekBar.setMax(1);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                double flux_people = Double.parseDouble(editText2.getText().toString());
                double num_people = Double.parseDouble(ediText.getText().toString());

                seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
                    @Override
                    public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                        double pace = (((double)progress / 1.0) * 0.8 ) + 0.1;
                        // value now holds the decimal value between 0.0 and 10.0 of the progress
                        // Example:
                        // If the progress changed to 45, value would now hold 4.5
                    }

                    @Override
                    public void onStartTrackingTouch(SeekBar seekBar) {}
                    @Override
                    public void onStopTrackingTouch(SeekBar seekBar) {}
                });

                seekBar2.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
                    @Override
                    public void onProgressChanged(SeekBar seekBar2, int progress, boolean fromUser) {
                        double heat = ((double)progress / 1.0) * 0.125;
                        // value now holds the decimal value between 0.0 and 10.0 of the progress
                        // Example:
                        // If the progress changed to 45, value would now hold 4.5
                    }

                    @Override
                    public void onStartTrackingTouch(SeekBar seekBar2) {}
                    @Override
                    public void onStopTrackingTouch(SeekBar seekBar2) {}
                });


                calculate.battle(num_people, flux_people, pace, heat);

            }
        });
    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}

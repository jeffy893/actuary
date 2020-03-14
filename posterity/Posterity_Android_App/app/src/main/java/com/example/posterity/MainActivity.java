package com.example.posterity;

import android.graphics.Color;
import android.os.Bundle;


import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

import lecho.lib.hellocharts.model.Axis;
import lecho.lib.hellocharts.model.AxisValue;
import lecho.lib.hellocharts.model.Line;
import lecho.lib.hellocharts.model.LineChartData;
import lecho.lib.hellocharts.model.PointValue;
import lecho.lib.hellocharts.view.LineChartView;


public class MainActivity extends AppCompatActivity {


    private EditText et2, et;
    private SeekBar sb2, sb;
    private TextView tv;
    private double heat, pace, flux_people, num_people;
    LineChartView lineChartView;
    int[] axisData;
    List bAxisValues, axisValues, cAxisValues;
    Line bline, cline;
    Axis axis, byaxis, cyaxis;
    double[][] unexData, neutralData, epicData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);







        et2 = findViewById(R.id.editText2);
        et = findViewById(R.id.editText);
        sb2 = findViewById(R.id.seekBar2);
        sb = findViewById(R.id.seekBar);
        tv = findViewById(R.id.textView4);
        heat = 0.5;
        pace = 0.5;
        flux_people = 1.0;
        num_people = 1.0;


        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {



                flux_people = Double.parseDouble(et2.getText().toString());
                num_people = Double.parseDouble(et.getText().toString());

                sb.setMax(10000);
                sb2.setMax(10000);
                pace = (((double)sb2.getProgress() / 10000.0) * 0.125) + 0.02;
                heat = (((double)sb.getProgress() / 10000.0) * 0.8 ) + 0.1;

                tv.setText("Num_People=" + num_people + ", Flux_People=" + flux_people + ", Heat=" + heat + ", Pace=" + pace);


                calculate compete = new calculate();

                compete.battle(num_people, flux_people, pace, heat);
                unexData = compete.getUnexData();
                epicData = compete.getEpicData();
                neutralData = compete.getNeutralData();



                for(int i = 0; i < 100; i++){
                    axisData[i] = i + 1;
                }

                bAxisValues = new ArrayList();
                cAxisValues = new ArrayList();
                axisValues = new ArrayList();

                lineChartView = findViewById(R.id.chart);






                for(int i = 0; i < i; i++){
                    axisValues.add(i, new AxisValue(i).setLabel(String.valueOf(axisData[i])));
                }

                for (int i = 0; i < 100; i++){
                    bAxisValues.add(new PointValue(i, bison[i][1]));
                }
                for (int i = 0; i < 100; i++){
                    cAxisValues.add(new PointValue(i, bison[i][1]));
                }


                bline = new Line(bAxisValues);

                List lines = new ArrayList();
                lines.add(line);



                bline = new Line(byAxisValues).setColor(Color.parseColor("#9C27B0"));
                cline = new Line(cyAxisValues).setColor(Color.parseColor("#9C27B0"));

                axis.setTextColor(Color.parseColor("#03A9F4"));

                byAxis.setTextColor(Color.parseColor("#03A9F4"));
                cyAxis.setTextSize(16);




                LineChartData data = new LineChartData();
                data.setLines(lines);

                axis = new Axis();
                axis.setValues(axisValues);
                data.setAxisXBottom(axis);


                byAxis = new Axis();
                cyAxis = new Axis();
                data.setAxisYLeft(byAxis);
                data.setAxisYLeft(cyAxis);


                lineChartView.setLineChartData(data);




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

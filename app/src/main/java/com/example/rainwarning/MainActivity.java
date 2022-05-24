package com.example.rainwarning;

import androidx.appcompat.app.AppCompatActivity;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = (TextView)findViewById(R.id.textview);

        //this will start python
        if (!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }

        //now creating python instance
        Python py = Python.getInstance();
        //now creating python object
        PyObject pyObject = py.getModule("GetWeather"); //using python script name

        //now we can call methods from function
        PyObject obj = pyObject.callAttr("main");

        //now set returned text to textview
        textView.setText(obj.toString());
    }
}
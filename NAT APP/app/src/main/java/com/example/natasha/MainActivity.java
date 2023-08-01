package com.example.natasha;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.Manifest;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {
    String phno="";
    DatabaseReference databasereference = FirebaseDatabase.getInstance().getReferenceFromUrl("https://natasha-bd631-default-rtdb.firebaseio.com/data/");
    private static final int MY_PERMISSIONS_REQUEST_SEND_SMS = 0;
    public void sendsms(View view){
        Log.d("MyApp", "Sending SMS");
        SharedPreferences sharedPreferences = getSharedPreferences("MyPreferences", MODE_PRIVATE);
        String savedText = sharedPreferences.getString("myStringKey", "");
        phno=savedText;
        Toast.makeText(this,"the number is "+phno,Toast.LENGTH_SHORT).show();
        SmsManager smsManager = SmsManager.getDefault();
        String phoneNumber = phno ;
        String message = "This person has saved your number as the emergency contact . He is in need of help. Please contact or reach out as soon as possible."+"\n"+"- natasha VAPC-1";
        smsManager.sendTextMessage(phoneNumber, null, message, null, null);
        Toast.makeText(this,"the message is sent to the emergency contact",Toast.LENGTH_SHORT).show();
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView abc=(TextView)findViewById(R.id.textView3);
        SharedPreferences sharedPreferences = getSharedPreferences("MyPreferences", MODE_PRIVATE);
        String sa = sharedPreferences.getString("myStringKey", "");
        phno=sa;
        abc.setText(phno);
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.SEND_SMS},
                    MY_PERMISSIONS_REQUEST_SEND_SMS);
        }
        databasereference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                String dataValue = snapshot.getValue(String.class);
                if (dataValue != null && dataValue.equals("true")) {
                    sendsms(null);
                    databasereference.setValue("false"); // Change the value of "data" to false
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Handle errors here
            }
        });


    }
    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        switch (requestCode) {
            case MY_PERMISSIONS_REQUEST_SEND_SMS: {
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    // permission was granted, do your SMS sending task here
                    sendsms(null);
                } else {
                    // permission denied
                    Toast.makeText(getApplicationContext(), "SMS sending permission denied", Toast.LENGTH_LONG).show();
                }
                return;
            }
        }
    }
    public void savefun(View view){
        EditText txt = (EditText) findViewById(R.id.editTextTextPersonName);
        String number=txt.getText().toString().strip();
        SharedPreferences sharedPreferences = getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putString("myStringKey", number);
        editor.apply();
        TextView abc=(TextView)findViewById(R.id.textView3);
        abc.setText(number);
        Toast.makeText(getApplicationContext(), "The emergency number is saved as "+number, Toast.LENGTH_LONG).show();
    }


}
package io.oz.sharedprefs;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.preference.PreferenceManager;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity {
    static final String Tag = "Hello";

    ActivityResultLauncher<Intent> prefDemoStart;
    ActivityResultLauncher<Intent> qrScannStart;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        prefDemoStart = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            result -> {
                if (result.getResultCode() == AppCompatActivity.RESULT_OK) {
                    Intent data = result.getData();
                    Log.i(Tag, data.getAction());
                }
                SharedPreferences sharedPreferences =
                        PreferenceManager.getDefaultSharedPreferences(this /* Activity context */);
                String name = sharedPreferences.getString("key_gallery_name", "");
                Log.i(Tag, name);
            }
        );

        qrScannStart = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            result -> {
                if (result.getResultCode() == AppCompatActivity.RESULT_OK) {

                    SharedPreferences sharedPreferences =
                            PreferenceManager.getDefaultSharedPreferences(this /* Activity context */);
                    String name = sharedPreferences.getString("key_qr", "");
                    Log.i(Tag, name);
                }
                else
                    Log.i(Tag, "jserv-qr cancled");
            }
        );
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();

        if (id == R.id.action_settings) {
            // launch settings activity
            // startActivity(new Intent(MainActivity.this, SettingsPrefActivity.class));
//            startActivityForResult(new Intent(MainActivity.this, SettingsPrefActivity.class), 0);
            prefDemoStart.launch(new Intent(MainActivity.this, SettingsPrefActivity.class));

            return true;
        }
        else if (id == R.id.action_scan) {
            qrScannStart.launch(new Intent(MainActivity.this, QrScanActy.class));
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
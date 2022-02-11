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

    ActivityResultLauncher<Intent> startActivityForResult;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        startActivityForResult = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            result -> {
                if (result.getResultCode() == AppCompatActivity.RESULT_OK) {
                    Intent data = result.getData();
                    Log.i("jserv-root", data.getAction());
                }
                SharedPreferences sharedPreferences =
                        PreferenceManager.getDefaultSharedPreferences(this /* Activity context */);
                String name = sharedPreferences.getString("key_gallery_name", "");
                Log.i("jserv-root-name", name);
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
            startActivityForResult.launch(new Intent(MainActivity.this, SettingsPrefActivity.class));

            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
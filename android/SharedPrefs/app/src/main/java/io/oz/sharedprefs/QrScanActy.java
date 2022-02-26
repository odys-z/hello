package io.oz.sharedprefs;

import android.content.Intent;
import android.os.Bundle;
import android.preference.EditTextPreference;
import android.preference.Preference;
import android.preference.PreferenceFragment;
import android.util.Log;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

public class QrScanActy extends AppCompatActivity {
    private ScanPreferenceFragment prefragment;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        // load settings fragment
        prefragment = new ScanPreferenceFragment();
        getFragmentManager().beginTransaction().replace(android.R.id.content, prefragment).commit();
    }

    public void onScan() {
        Log.d("TAG", "...........\n.\n.\n.\n.\n.\n..");

        IntentIntegrator intentIntegrator = new IntentIntegrator(this);
        intentIntegrator.setPrompt("Scan a barcode or QR Code");
        intentIntegrator.initiateScan();
    }

    public static class ScanPreferenceFragment extends PreferenceFragment {
        private Preference mContent;
        private Preference mFormat;

        @Override
        public void onCreate(final Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            addPreferencesFromResource(R.xml.pref_scan);

            ScanPreferenceFragment ctx = this;

            // bindPreferenceSummaryToValue(findPreference(getString(R.string.key_scan_text)));
            // bindPreferenceSummaryToValue(findPreference(getString(R.string.key_scan_number)));
            mContent = findPreference(getString(R.string.key_scan_content));
            mFormat  = findPreference(getString(R.string.key_scan_format));

            // feedback preference click listener
            Preference prefScan = findPreference(getString(R.string.key_scan_format));
            prefScan.setOnPreferenceClickListener(new Preference.OnPreferenceClickListener() {
                public boolean onPreferenceClick(Preference preference) {
                    IntentIntegrator intentIntegrator = new IntentIntegrator(getActivity());
                    intentIntegrator.setPrompt("Scan a barcode or QR Code");
                    intentIntegrator.initiateScan();
                    return true;
                }
            });
        }

        public void setText(String contentext, String formatName) {
            mContent.setSummary(contentext);
            mFormat.setSummary(formatName);
        }
    }

    /**
     * Tried <a href='https://github.com/journeyapps/zxing-android-embedded#usage-with-scancontract'>
     * new way</a>, registerForActivityResult, but not working for starting activity in preference
     * fragment.
     * @param requestCode
     * @param resultCode
     * @param data
     */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        IntentResult intentResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
        // if the intentResult is null then
        // toast a message as "cancelled"
        if (intentResult != null) {
            if (intentResult.getContents() == null) {
                Toast.makeText(getBaseContext(), "Cancelled", Toast.LENGTH_SHORT).show();
            } else {
                // if the intentResult is not null we'll set
                // the content and format of scan message
                if (prefragment != null) {
                    prefragment.setText(intentResult.getContents(), intentResult.getFormatName());
                }
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }
}

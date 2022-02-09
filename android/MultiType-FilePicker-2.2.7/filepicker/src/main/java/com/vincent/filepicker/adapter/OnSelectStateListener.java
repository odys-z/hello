package com.vincent.filepicker.adapter;

import android.view.View;

/**
 * Created by Vincent Woo
 * Date: 2016/10/14
 * Time: 16:06
 */

public interface OnSelectStateListener<T> {
    void OnSelectStateChanged (int position, boolean state, T file, View animation );
    void onAudioStateChanged(boolean state,T file,View animation);
    void onFileStateChanged(boolean state,T file,View animation);
}

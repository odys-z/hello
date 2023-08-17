package com.vincent.filepicker.adapter;

import android.content.Context;
import android.graphics.drawable.AnimationDrawable;
import androidx.recyclerview.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.vincent.filepicker.R;
import com.vincent.filepicker.ToastUtil;
import com.vincent.filepicker.Util;
import com.vincent.filepicker.filter.entity.AudioFile;

import java.io.File;
import java.util.ArrayList;

/**
 * Created by Vincent Woo
 * Date: 2016/10/25
 * Time: 10:57
 */

public class AudioPickAdapter extends BaseAdapter<AudioFile, AudioPickAdapter.AudioPickViewHolder> {
    private int mMaxNumber;
    private int mCurrentNumber = 0;

    public AudioPickAdapter(Context ctx, int max) {
        this(ctx, new ArrayList<AudioFile>(), max);
    }

    public AudioPickAdapter(Context ctx, ArrayList<AudioFile> list, int max) {
        super(ctx, list);
        mMaxNumber = max;
    }

    @Override
    public AudioPickViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(mContext).inflate(R.layout.vw_layout_item_audio_pick, parent, false);
        AudioPickViewHolder holder=new AudioPickViewHolder(itemView);
        holder.setIsRecyclable ( false );
        return holder;
    }

    @Override
    public void onBindViewHolder(final AudioPickViewHolder holder, final int position) {
        final AudioFile file = mList.get(position);

        holder.mTvTitle.setText(file.getName());
        holder.mTvTitle.measure(View.MeasureSpec.UNSPECIFIED, View.MeasureSpec.UNSPECIFIED);
        if (holder.mTvTitle.getMeasuredWidth() >
                Util.getScreenWidth(mContext) - Util.dip2px(mContext, 10 + 32 + 10 + 48 + 10 * 2)) {
            holder.mTvTitle.setLines(2);
        } else {
            holder.mTvTitle.setLines(1);
        }

        holder.mTvDuration.setText(Util.getDurationString(file.getDuration()));
        if (file.isSelected()) {
            holder.mCbx.setSelected(true);
            holder.animation.setVisibility ( View.VISIBLE );
            holder.animation.setAlpha ( 1f );
            AnimationDrawable animationDrawable = (AnimationDrawable) holder.animation.getBackground ( );
            Animation a= AnimationUtils.loadAnimation ( mContext,R.anim.rotate_animation );
//                    animation.startAnimation ( animationDrawable );
            animationDrawable.start ();

        } else {
            holder.mCbx.setSelected(false);
            holder.animation.setVisibility ( View.INVISIBLE );
            holder.animation.setAlpha ( 0f );
        }
        //change itemview to mCbx
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!v.isSelected() && isUpToMax()) {
                    ToastUtil.getInstance(mContext).showToast(R.string.vw_up_to_max);
                    return;
                }

                if (v.isSelected()) {
                    holder.mCbx.setSelected(false);
                    mCurrentNumber--;
                } else {
                    holder.mCbx.setSelected(true);
                    mCurrentNumber++;
                }

                mList.get(holder.getAdapterPosition()).setSelected(holder.mCbx.isSelected());

                if (mListener != null) {
                    mListener.onAudioStateChanged (holder.mCbx.isSelected(), mList.get(holder.getAdapterPosition()),holder.animation);
                }
            }
        });

//        holder.itemView.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent intent = new Intent(Intent.ACTION_VIEW);
//                Uri uri;
//                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
//                    intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
//                    File f = new File(file.getPath());
//                    uri = FileProvider.getUriForFile(mContext, mContext.getApplicationContext().getPackageName() + ".provider", f);
//                }else{
//                    uri = Uri.parse("file://" + file.getPath());
//                }
//                intent.setDataAndType(uri, "audio/mp3");
//                if (Util.detectIntent(mContext, intent)) {
//                    mContext.startActivity(intent);
//                } else {
//                    ToastUtil.getInstance(mContext).showToast(mContext.getString(R.string.vw_no_audio_play_app));
//                }
//            }
//        });
    }

    @Override
    public int getItemCount() {
        return mList.size();
    }

    class AudioPickViewHolder extends RecyclerView.ViewHolder {
        private TextView mTvTitle;
        private TextView mTvDuration;
        private ImageView mCbx;
        private RelativeLayout animation;
        public AudioPickViewHolder(View itemView) {
            super(itemView);
            mTvTitle = (TextView) itemView.findViewById(R.id.tv_audio_title);
            mTvDuration = (TextView) itemView.findViewById(R.id.tv_duration);
            mCbx = (ImageView) itemView.findViewById(R.id.cbx);
            animation = itemView.findViewById ( R.id.animationAudio );
        }
    }

    public boolean isUpToMax() {
        return mCurrentNumber >= mMaxNumber;
    }

    public void setCurrentNumber(int number) {
        mCurrentNumber = number;
    }
}

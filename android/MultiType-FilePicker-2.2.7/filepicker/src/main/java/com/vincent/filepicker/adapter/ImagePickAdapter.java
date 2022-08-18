package com.vincent.filepicker.adapter;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.ContentValues;
import android.content.Context;
import android.content.Intent;
import android.graphics.drawable.AnimationDrawable;
import android.media.Image;
import android.net.Uri;
import android.os.Environment;
import android.provider.MediaStore;
import androidx.recyclerview.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.RelativeLayout;

import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;
import com.vincent.filepicker.Constant;
import com.vincent.filepicker.R;
import com.vincent.filepicker.ToastUtil;
import com.vincent.filepicker.Util;
import com.vincent.filepicker.activity.ImageBrowserActivity;
import com.vincent.filepicker.activity.ImagePickActivity;
import com.vincent.filepicker.filter.entity.ImageFile;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;

import static android.os.Environment.DIRECTORY_DCIM;
import static com.bumptech.glide.load.resource.drawable.DrawableTransitionOptions.withCrossFade;
import static com.vincent.filepicker.activity.ImageBrowserActivity.IMAGE_BROWSER_INIT_INDEX;
import static com.vincent.filepicker.activity.ImageBrowserActivity.IMAGE_BROWSER_SELECTED_LIST;

/**
 * Created by Vincent Woo
 * Date: 2016/10/13
 * Time: 16:07
 */

public class ImagePickAdapter extends BaseAdapter<ImageFile, ImagePickAdapter.ImagePickViewHolder> {
    private boolean isNeedImagePager;
    private boolean isNeedCamera;
    private int mMaxNumber;
    private int mCurrentNumber = 0;
    public String mImagePath;
    public Uri mImageUri;

    public ImagePickAdapter ( Context ctx , boolean needCamera , boolean isNeedImagePager , int max ) {
        this ( ctx , new ArrayList<ImageFile> ( ) , needCamera , isNeedImagePager , max );
    }

    public ImagePickAdapter ( Context ctx , ArrayList<ImageFile> list , boolean needCamera , boolean needImagePager , int max ) {
        super ( ctx , list );
        isNeedCamera = needCamera;
        mMaxNumber = max;
        isNeedImagePager = needImagePager;
    }

    @Override
    public ImagePickViewHolder onCreateViewHolder ( ViewGroup parent , int viewType ) {
        View itemView = LayoutInflater.from ( mContext ).inflate ( R.layout.vw_layout_item_image_pick , parent , false );
        ViewGroup.LayoutParams params = itemView.getLayoutParams ( );
        if ( params != null ) {
            WindowManager wm = (WindowManager) mContext.getSystemService ( Context.WINDOW_SERVICE );
            int width = wm.getDefaultDisplay ( ).getWidth ( );
            params.height = width / ImagePickActivity.COLUMN_NUMBER;
        }
        ImagePickViewHolder imagePickViewHolder = new ImagePickViewHolder ( itemView );
        imagePickViewHolder.setIsRecyclable ( false );
        return imagePickViewHolder;
    }

//    @Override
//    public long getItemId ( int position ) {
//        return position;
//    }
//
//    @Override
//    public int getItemViewType ( int position ) {
//        return position;
//    }

    @Override
    public void onBindViewHolder ( final ImagePickViewHolder holder , @SuppressLint("RecyclerView") final int position ) {
        if ( isNeedCamera==true && position == 0 ) {
            holder.mIvCamera.setVisibility ( View.VISIBLE );
            holder.mIvThumbnail.setVisibility ( View.INVISIBLE );
            holder.mCbx.setVisibility ( View.GONE );
            holder.mShadow.setVisibility ( View.INVISIBLE );
//            holder.itemView.setOnClickListener ( new View.OnClickListener ( ) {
//                @Override
//                public void onClick ( View v ) {
//                    Intent intent = new Intent ( MediaStore.ACTION_IMAGE_CAPTURE );
//                    String timeStamp = new SimpleDateFormat ( "yyyyMMdd_HHmmss" , Locale.ENGLISH ).format ( new Date ( ) );
//                    File file = new File ( Environment.getExternalStoragePublicDirectory ( DIRECTORY_DCIM ).getAbsolutePath ( )
//                            + "/IMG_" + timeStamp + ".jpg" );
//                    mImagePath = file.getAbsolutePath ( );
//
//                    ContentValues contentValues = new ContentValues ( 1 );
//                    contentValues.put ( MediaStore.Images.Media.DATA , mImagePath );
//                    mImageUri = mContext.getContentResolver ( ).insert ( MediaStore.Images.Media.EXTERNAL_CONTENT_URI , contentValues );
//
//                    intent.putExtra ( MediaStore.EXTRA_OUTPUT , mImageUri );
//                    if ( Util.detectIntent ( mContext , intent ) ) {
//                        ( (Activity) mContext ).startActivityForResult ( intent , Constant.REQUEST_CODE_TAKE_IMAGE );
//                    }
//                    else {
//                        ToastUtil.getInstance ( mContext ).showToast ( mContext.getString ( R.string.vw_no_photo_app ) );
//                    }
//                }
//            } );
        }
        else {
            holder.mIvCamera.setVisibility ( View.INVISIBLE );
            holder.mIvThumbnail.setVisibility ( View.VISIBLE );
            holder.mCbx.setVisibility ( View.GONE );

            ImageFile file;
            if ( isNeedCamera ) {
                file = mList.get ( position - 1 );
            }
            else {
                file = mList.get ( position );
            }

            RequestOptions options = new RequestOptions ( );
            Glide.with ( mContext )
                    .load ( file.getPath ( ) )
                    .apply ( options.centerCrop ( ) )
                    .transition ( withCrossFade ( ) )
//                    .transition(new DrawableTransitionOptions().crossFade(500))
                    .into ( holder.mIvThumbnail );

            if ( file.isSelected ( ) ) {
                holder.mCbx.setSelected ( true );
                holder.mShadow.setVisibility ( View.VISIBLE );
                holder.animation.setVisibility ( View.VISIBLE );
                holder.animation.setAlpha ( 1f );
                AnimationDrawable animationDrawable = (AnimationDrawable) holder.animation.getBackground ( );
                Animation a= AnimationUtils.loadAnimation ( mContext,R.anim.rotate_animation );
//                    animation.startAnimation ( animationDrawable );
                animationDrawable.start ();
            }
            else {
                holder.mCbx.setSelected ( false );
                holder.animation.setVisibility ( View.GONE );
                holder.animation.setAlpha ( 0f );
                holder.mShadow.setVisibility ( View.INVISIBLE );
            }

//            if ( isNeedImagePager ) {
//                holder.itemView.setOnClickListener ( new View.OnClickListener ( ) {
//                    @Override
//                    public void onClick ( View v ) {
//                        Intent intent = new Intent ( mContext , ImageBrowserActivity.class );
//                        intent.putExtra ( Constant.MAX_NUMBER , mMaxNumber );
//                        intent.putExtra ( IMAGE_BROWSER_INIT_INDEX ,
//                                isNeedCamera ? holder.getAdapterPosition ( ) - 1 : holder.getAdapterPosition ( ) );
//                        intent.putParcelableArrayListExtra ( IMAGE_BROWSER_SELECTED_LIST , ( (ImagePickActivity) mContext ).mSelectedList );
//                        ( (Activity) mContext ).startActivityForResult ( intent , Constant.REQUEST_CODE_BROWSER_IMAGE );
//                    }
//                } );
//            }
//            else {
                final int p = holder.getAdapterPosition ( );

                holder.mIvThumbnail.setOnClickListener ( new View.OnClickListener ( ) {
                    @Override
                    public void onClick ( View view ) {
                        if ( !holder.mCbx.isSelected ( ) && isUpToMax ( ) ) {
                            ToastUtil.getInstance ( mContext ).showToast ( R.string.vw_up_to_max );
                            return;
                        }

                        int index = isNeedCamera ? holder.getAdapterPosition ( ) - 1 : holder.getAdapterPosition ( );

                        if ( holder.mCbx.isSelected ( ) ) {
                            holder.mShadow.setVisibility ( View.GONE );
                            holder.mCbx.setSelected ( false );
                            mCurrentNumber--;
                            mList.get ( index ).setSelected ( false );

//                                holder.animation.setAlpha ( 0f );

                        }
                        else {
                            holder.mShadow.setVisibility ( View.VISIBLE );
                            holder.mCbx.setSelected ( true );
                            mCurrentNumber++;
                            mList.get ( index ).setSelected ( true );
//                                holder.animation.setAlpha ( 1f );
//                                final Animation a = AnimationUtils.loadAnimation ( mContext , R.anim.rotate_animation );
//                                holder.animation.startAnimation ( a );


                        }

                        if ( mListener != null ) {
                            mListener.OnSelectStateChanged ( index , holder.mCbx.isSelected ( ) , mList.get ( index ) , holder.animation );
                        }
                    }
                } );

//            }
        }
    }

    @Override
    public int getItemCount () {
        return isNeedCamera ? mList.size ( ) + 1 : mList.size ( );
    }

    class ImagePickViewHolder extends RecyclerView.ViewHolder {
        private ImageView mIvCamera;
        private ImageView mIvThumbnail;
        private View mShadow;
        private ImageView mCbx;
        private RelativeLayout animation;

        public ImagePickViewHolder ( View itemView ) {
            super ( itemView );
            mIvCamera = (ImageView) itemView.findViewById ( R.id.iv_camera );
            mIvThumbnail = (ImageView) itemView.findViewById ( R.id.iv_thumbnail );
            mShadow = itemView.findViewById ( R.id.shadow );
            mCbx = (ImageView) itemView.findViewById ( R.id.cbx );
            animation = itemView.findViewById ( R.id.animationSquare );
        }
    }

    public boolean isUpToMax () {
        return mCurrentNumber >= mMaxNumber;
    }

    public void setCurrentNumber ( int number ) {
        mCurrentNumber = number;
    }
}

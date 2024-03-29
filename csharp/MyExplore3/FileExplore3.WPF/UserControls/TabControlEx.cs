﻿using FileExplorer.WPF.BaseControls;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace FileExplorer.WPF.UserControls
{
    public class TabControlEx : TabControl
    {

        #region Constructors

        static TabControlEx()
        {
            DefaultStyleKeyProperty.OverrideMetadata(typeof(TabControlEx),
                new FrameworkPropertyMetadata(typeof(TabControlEx)));
        }

        #endregion

        #region Methods

        protected override DependencyObject GetContainerForItemOverride()
        {
            var newTabItem = new TabItemEx();
            return newTabItem;
            //return base.GetContainerForItemOverride();
        }

        public override void OnApplyTemplate()
        {
            base.OnApplyTemplate();
            _ancestorWindow = UITools.FindAncestor<Window>(this);
            //_titlebar = this.Template.FindName("PART_TitleBar", this) as Titlebar;
        }

        protected override void OnMouseDoubleClick(System.Windows.Input.MouseButtonEventArgs e)
        {
            var parentTabItem =
                UITools.FindAncestor<TabItem>(e.OriginalSource as System.Windows.DependencyObject, null);
            var parentButton =
                UITools.FindAncestor<Button>(e.OriginalSource as System.Windows.DependencyObject, null);

            if ((e.OriginalSource as FrameworkElement).Name ==
                "HeaderPanelScrollViewer")
                if (parentTabItem == null && parentButton == null &&
                    _ancestorWindow.WindowState == WindowState.Maximized)
                    _ancestorWindow.WindowState = WindowState.Normal;
                else
                    base.OnMouseDoubleClick(e);
        }

        #endregion

        #region Data

        private Window _ancestorWindow;

        #endregion

        #region Public Properties


        public static DependencyProperty LeftTabHeaderContentProperty = DependencyProperty.Register(
            "LeftTabHeaderContent", typeof(object), typeof(TabControlEx));

        public object LeftTabHeaderContent
        {
            get { return GetValue(LeftTabHeaderContentProperty); }
            set { SetValue(LeftTabHeaderContentProperty, value); }
        }

        public static DependencyProperty RightTabHeaderContentProperty = DependencyProperty.Register(
            "RightTabHeaderContent", typeof(object), typeof(TabControlEx));

        public object RightTabHeaderContent
        {
            get { return GetValue(RightTabHeaderContentProperty); }
            set { SetValue(RightTabHeaderContentProperty, value); }
        }

        #endregion
    }

    public class TabItemEx : TabItem
    {
        #region Constructors

        static TabItemEx()
        {
            DefaultStyleKeyProperty.OverrideMetadata(typeof(TabItemEx),
                new FrameworkPropertyMetadata(typeof(TabItemEx)));
        }

        public TabItemEx()
        {


        }


        #endregion

        #region Methods



        #endregion

        #region Data


        #endregion

        #region Public Properties

        public static DependencyProperty ShowPlaceHolderProperty = DependencyProperty.Register("ShowPlaceHolder",
            typeof(bool), typeof(TabItemEx), new PropertyMetadata(false));

        public bool ShowPlaceHolder
        {
            get { return (bool)GetValue(ShowPlaceHolderProperty); }
            set { SetValue(ShowPlaceHolderProperty, value); }
        }

        public static DependencyProperty HeaderOpacityProperty = DependencyProperty.Register("HeaderOpacity",
           typeof(float), typeof(TabItemEx), new PropertyMetadata(1.0f));

        public float HeaderOpacity
        {
            get { return (float)GetValue(HeaderOpacityProperty); }
            set { SetValue(HeaderOpacityProperty, value); }
        }

        #endregion
    }
}

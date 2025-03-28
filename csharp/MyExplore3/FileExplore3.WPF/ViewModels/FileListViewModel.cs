﻿using System;
using System.Collections.Generic;
#if WINRT
using Windows.UI.Xaml.Controls;
#else
using System.ComponentModel.Composition;
using System.Windows.Controls;
#endif
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Caliburn.Micro;
using FileExplorer.Defines;
using FileExplorer.WPF.Models;
using System.Diagnostics;
using System.Windows.Data;
using System.ComponentModel;
using System.Windows;
using System.Collections;
using FileExplorer.WPF.ViewModels.Actions;
using FileExplorer.WPF.Utils;
using System.Collections.ObjectModel;
using FileExplorer.WPF.ViewModels.Helpers;
using Cinch;
using System.Windows.Input;
using FileExplorer.Defines;
using System.Threading;
using FileExplorer.Utils;
using FileExplorer.WPF.Defines;
using FileExplorer.Models;


namespace FileExplorer.WPF.ViewModels
{
#if !WINRT
    [Export(typeof(FileListViewModel))]
#endif
    public class FileListViewModel : ViewAware, IFileListViewModel,
        IHandle<ViewChangedEvent>, IHandle<DirectoryChangedEvent>, ISupportDragHelper, ISupportDropHelper
    {

        #region FileListDrag/DropHelper
        internal class FileListDropHelper : DropHelper<IEntryModel>
        {
            public FileListDropHelper(FileListViewModel flvm)
                : base(() => flvm.CurrentDirectory.Label,
                (ems, eff) => flvm.CurrentDirectory.Profile.DragDrop().QueryDrop(ems, flvm.CurrentDirectory, eff),
                    da => flvm.CurrentDirectory.Profile.DragDrop().GetEntryModels(da),
                (ems, da, eff) => flvm.CurrentDirectory.Profile.DragDrop().OnDropCompleted(ems, da, flvm.CurrentDirectory, eff), em => EntryViewModel.FromEntryModel(em))
            { }

        }
        private class FileListDragHelper : TreeDragHelper<IEntryModel>
        {
            public FileListDragHelper(FileListViewModel flvm)
                : base(
                () => flvm.Selection.SelectedItems.ToArray(),
                ems => ems.First().Profile.DragDrop().QueryDrag(ems),
                ems => AsyncUtils.RunSync(() => ems.First().Profile.DragDrop().GetDataObject(ems)),
                (ems, da, eff) => ems.First().Profile.DragDrop().OnDragCompleted(ems, da, eff)
                , d => (d as IEntryViewModel).EntryModel)
            { }
        }
        #endregion

        #region Cosntructor

        public FileListViewModel(IEventAggregator events, ISidebarViewModel sidebar = null)
        {
            Events = events;
            var entryHelper = new EntriesHelper<IEntryViewModel>(loadEntriesTask) { ClearBeforeLoad = false };
            ProcessedEntries = new EntriesProcessor<IEntryViewModel>(entryHelper, evm => evm.EntryModel);
            Columns = new ColumnsHelper(ProcessedEntries,
                (col, direction) =>
                    new EntryViewModelComparer(
                        col.Comparer != null ? col.Comparer : CurrentDirectory.Profile.GetComparer(col),
                        direction)
            );
            Selection = new ListSelector<IEntryViewModel, IEntryModel>(entryHelper);
            DropHelper = new FileListDropHelper(this);
            DragHelper = new FileListDragHelper(this);

            Selection.SelectionChanged += (o, e) =>
            { events.PublishOnUIThread(new SelectionChangedEvent(this, Selection.SelectedItems)); };

            if (events != null)
                events.Subscribe(this);

            Sidebar = sidebar ?? new SidebarViewModel(events);
            Sidebar.PropertyChanged += (o, e) =>
                {
                    if (e.PropertyName == "IsVisible")
                        NotifyOfPropertyChange(() => ShowSidebar);
                };
            Commands = new FileListCommandManager(this, events, Selection, Sidebar.Commands);
        }

        #endregion

        #region Methods

        async Task<IEnumerable<IEntryViewModel>> loadEntriesTask(bool refresh)
        {
            if (CurrentDirectory == null)
                return new List<IEntryViewModel>();

            var subEntries = await CurrentDirectory.Profile.ListAsync(CurrentDirectory, CancellationToken.None, null, refresh);
            return subEntries.Select(s => CreateSubmodel(s));
        }

        public IEntryViewModel CreateSubmodel(IEntryModel entryModel)
        {
            return new FileListItemViewModel(entryModel, Selection);
        }


        #region Actions

        public async Task SetCurrentDirectoryAsync(IEntryModel em)
        {
            _currentDirVM = em;

            ProcessedEntries.EntriesHelper.IsLoaded = false;
            await ProcessedEntries.EntriesHelper.LoadAsync(UpdateMode.Replace, false);
            Task.Run(() =>
                Columns.CalculateColumnHeaderCount(
                    from vm in ProcessedEntries.EntriesHelper.AllNonBindable select vm.EntryModel));

            NotifyOfPropertyChange(() => CurrentDirectory);
        }

        //public IEnumerable<IResult> ToggleRename()
        //{
        //    yield return new ToggleRename(this);
        //}


        #endregion

        protected override void OnViewAttached(object view, object context)
        {
            base.OnViewAttached(view, context);
            var uiEle = view as System.Windows.UIElement;
            Commands.RegisterCommand(uiEle, ScriptBindingScope.Local);
        }

        public void SignalChangeDirectory(IEntryModel newDirectory)
        {
            Events.PublishOnUIThread(new DirectoryChangedEvent(this,
                     newDirectory, CurrentDirectory));
        }

        private void setProfiles(IProfile[] profiles)
        {
            Commands.ToolbarCommands.RootProfiles = profiles;
        }

        public void Handle(ViewChangedEvent message)
        {
            if (!(message.Sender.Equals(this)))
                Parameters.ViewMode = message.ViewMode;
        }

        public void Handle(DirectoryChangedEvent message)
        {
            if (message.NewModel != null)
                CurrentDirectory = message.NewModel;
        }


        #endregion

        #region Data

        private IEntryModel _currentDirVM = null;

        //private IToolbarViewModel _toolbar = null;
        private bool _showToolbar = true, _showGridHeader = true;
        private bool _isCheckboxVisible = false, _isContextMenuVisible = false;
        private bool _enableDrag = true, _enableDrop = true, _enableMultiSelect = true;
        private IFileListParameters _parameters = new FileListParameters();

        #endregion

        #region Public Properties
        public IProfile[] Profiles { set { setProfiles(value); } }


        public bool ShowGridHeader { get { return _showGridHeader; } set { _showGridHeader = value; NotifyOfPropertyChange(() => ShowGridHeader); } }
        public bool ShowToolbar { get { return _showToolbar; } set { _showToolbar = value; NotifyOfPropertyChange(() => ShowToolbar); } }
        public bool ShowSidebar { get { return Sidebar.IsVisible; } set { Sidebar.IsVisible = value; } }
        public bool EnableDrag { get { return _enableDrag; } set { _enableDrag = value; NotifyOfPropertyChange(() => EnableDrag); } }
        public bool EnableDrop { get { return _enableDrop; } set { _enableDrop = value; NotifyOfPropertyChange(() => EnableDrop); } }
        public bool EnableMultiSelect { get { return _enableMultiSelect; } set { _enableMultiSelect = value; NotifyOfPropertyChange(() => EnableMultiSelect); } }

        public ICommandManager Commands { get; private set; }
        public IEntriesProcessor<IEntryViewModel> ProcessedEntries { get; private set; }
        public IColumnsHelper Columns { get; private set; }
        public IEventAggregator Events { get; private set; }
        public IListSelector<IEntryViewModel, IEntryModel> Selection { get; private set; }
        public ISupportDrag DragHelper { get; private set; }
        public ISupportDrop DropHelper { get; private set; }

        public ISidebarViewModel Sidebar { get; private set; }

        //public IToolbarViewModel Toolbar { get { return _toolbar; } set { _toolbar = value; NotifyOfPropertyChange(() => Toolbar); } }

        public IEntryModel CurrentDirectory
        {
            get { return _currentDirVM; }
            set
            {
                if (!value.Equals(_currentDirVM))
                    SetCurrentDirectoryAsync(value);
            }
        }

        public bool IsCheckBoxVisible
        {
            get { return _isCheckboxVisible; }
            set { _isCheckboxVisible = value; NotifyOfPropertyChange(() => IsCheckBoxVisible); }
        }

        public bool IsContextMenuVisible
        {
            get { return _isContextMenuVisible; }
            set { _isContextMenuVisible = value; NotifyOfPropertyChange(() => IsContextMenuVisible); }
        }



        public IFileListParameters Parameters
        {
            get { return _parameters; }
            set { _parameters = value; NotifyOfPropertyChange(() => Parameters); }
        }


        #endregion


    }
}



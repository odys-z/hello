using Caliburn.Micro;
using MyExplore3.ViewModels;
using System.Windows;

namespace MyExplore3
{
    class AppBootstrapper: BootstrapperBase
    {
        // private IWindowManager winmgr;

        public AppBootstrapper()
        {
            Initialize();
        }

        //public AppBootstrapper(IEventAggregator e, IWindowManager mgr)
        //{
        //    Initialize();
        //    this.winmgr = mgr;
        //}

        protected override void OnStartup(object sender, StartupEventArgs e)
        {
            // base.OnStartup(sender, e);
            DisplayRootViewFor<ShellViewModel>();
            // winmgr.ShowWindowAsync(new ExplorerViewModel((IEventAggregator)e, winmgr, null));
        }

    }
}

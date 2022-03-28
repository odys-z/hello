using Caliburn.Micro;
using MyExplore3.ViewModels;
using System.Windows;

namespace MyExplore3
{
    class AppBootstrapper: BootstrapperBase
    {
        public AppBootstrapper()
        {
            Initialize();
        }

        protected override void OnStartup(object sender, StartupEventArgs e)
        {
            DisplayRootViewFor<ShellViewModel>();
        }

    }
}

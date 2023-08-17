using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration.Install;
using System.Linq;
using System.Threading.Tasks;

namespace Confige
{
    [RunInstaller(true)]
    public partial class Installer1 : System.Configuration.Install.Installer
    {
        public Installer1()
        {
            InitializeComponent();
        }

        public override void Commit(System.Collections.IDictionary savedState)
        {
            base.Commit(savedState);
            System.Diagnostics.Process.Start(Context.Parameters["TARGETDIR"].ToString() + "Confige.exe");
            // Very important! Removes all those nasty temp files.
            base.Dispose();
        }
    }
}

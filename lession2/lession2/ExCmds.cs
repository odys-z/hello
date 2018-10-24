using Autodesk.Revit.UI;
using System;
using System.Reflection;
using Autodesk.Revit.DB;

using System.Windows.Media.Imaging;
using lession2.UI;

namespace io.odysz.hello.revit.lession2 {
    /// <summary>
    /// This application's main class. The class must be Public.
    /// 
    /// </summary>
    public class ExCmds : IExternalApplication {
        private static string icoPath = @"F:\revit\works\git-repo\hello\lession2\lession2\res\writing32.png";

        public Result OnStartup(UIControlledApplication application) {
            // Add a new ribbon panel
            RibbonPanel ribbonPanel = application.CreateRibbonPanel("Inforise Test");

            // Create a push button to trigger a command add it to the ribbon panel.
            string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;
            PushButtonData buttonData = new PushButtonData("cmdHelloWorld",
               "Hello World", thisAssemblyPath, "io.odysz.hello.revit.lession2.HelloWorld");

            PushButton pushButton = ribbonPanel.AddItem(buttonData) as PushButton;

            // Optionally, other properties may be assigned to the button
            // a) tool-tip
            pushButton.ToolTip = "Test Connection.";

            // b) large bitmap
            Uri uriImage = new Uri(icoPath);
            BitmapImage largeImage = new BitmapImage(uriImage);
            pushButton.LargeImage = largeImage;

            return Result.Succeeded;
        }

        public Result OnShutdown(UIControlledApplication application) {
            // nothing to clean up in this simple case
            return Result.Succeeded;
        }
    }

    /// <remarks>
    /// The "HelloWorld" external command. The class must be Public.
    /// </remarks>
    [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
    public class HelloWorld : IExternalCommand {
        // The main Execute method (inherited from IExternalCommand) must be public
        public Result Execute(ExternalCommandData revit,
                ref string message, ElementSet elements) {
            // TaskDialog.Show("Revit", "Hello World");
            Document doc = revit.Application.ActiveUIDocument.Document;

            HelloForm f = new HelloForm(doc, doc.ActiveView);
            f.Show();
            return Result.Succeeded;
        }
    }

}

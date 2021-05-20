using Autodesk.Revit.UI;
using System;
using System.Reflection;
using Autodesk.Revit.DB;
using System.Windows.Media.Imaging;
using System.IO;

namespace io.odysz.hello.revit.lession6
{
    /// <summary>
    /// This application's main class. The class must be Public.
    ///
    /// </summary>
    public class ExApp : IExternalApplication {
        private static string icoPath = @"odysz.png";

        public Result OnStartup(UIControlledApplication application) {
            // Add a new ribbon panel
            RibbonPanel ribbonPanel = application.CreateRibbonPanel("Inforise Test");

            // Create a push button to trigger a command add it to the ribbon panel.
            string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;
            PushButtonData buttonData = new PushButtonData("cmdHelloWorld",
               "Hello World", thisAssemblyPath, "io.odysz.hello.revit.lession6.ExCmds");

            PushButton pushButton = ribbonPanel.AddItem(buttonData) as PushButton;

            // Optionally, other properties may be assigned to the button
            // a) tool-tip
            pushButton.ToolTip = "Test Connection.";

            // b) large bitmap
            Uri uriImage = new Uri(Path.GetDirectoryName(thisAssemblyPath) + @"\" + icoPath);

            BitmapImage largeImage = new BitmapImage(uriImage);
            pushButton.LargeImage = largeImage;

            return Result.Succeeded;
        }

        public Result OnShutdown(UIControlledApplication application) {
            // nothing to clean up in this simple case
            return Result.Succeeded;
        }
    }
}

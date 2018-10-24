using Autodesk.Revit.DB;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lession2.UI {
    public partial class HelloForm : System.Windows.Forms.Form {
        private Document document;
        private Autodesk.Revit.DB.View view;

        public HelloForm(Document document, Autodesk.Revit.DB.View uiview) {
            InitializeComponent();
            this.document = document;
            view = uiview;
        }

        private void btnExpt_Click(object sender, EventArgs e) {
            
        }

        private void exportFBX() {
            // https://forums.autodesk.com/t5/revit-api-forum/how-to-export-with-all-categories-of-3d-view-of-rvt-file-to-fbx/m-p/7112555
            UIApplication uiApp = commandData.Application;
            Document doc = uiApp.ActiveUIDocument.Document;
            
            ViewSet viewSet = new ViewSet();
            viewSet.Insert(doc.ActiveViewSet);
            doc.Export("C:/......PATH......", "nameFBXExportedFile", viewSet, new FBXExportOptions());
        }

        /// <summary>
        /// Find families
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnFind_Click(object sender, EventArgs e) {
            /*
            // sample code: https://help.autodesk.com/view/RVT/2017/ENU/?guid=GUID-85E4A43E-88B5-43C6-908C-2D138C9F611D#GUID-85E4A43E-88B5-43C6-908C-2D138C9F611D
            // Find all Wall instances in the document by using category filter
            ElementCategoryFilter filter = new ElementCategoryFilter(BuiltInCategory.OST_Walls);

            // Apply the filter to the elements in the active document
            // Use shortcut WhereElementIsNotElementType() to find wall instances only
            FilteredElementCollector collector = new FilteredElementCollector(document);
            IList<Element> walls =
            collector.WherePasses(filter).WhereElementIsNotElementType().ToElements();
            String prompt = "The walls in the current document are:\n";
            foreach (Element e in walls) {
                prompt += e.Name + "\n";
            }
            TaskDialog.Show("Revit", prompt);
            */
            getAllFamilies();

            getWall();

            getFireAlarms();
        }

        private void getFireAlarms() {
             ElementCategoryFilter filter = new ElementCategoryFilter(BuiltInCategory.OST_FireAlarmDevices);

            // Apply the filter to the elements in the active document
            // Use shortcut WhereElementIsNotElementType() to find wall instances only
            FilteredElementCollector collector = new FilteredElementCollector(document);
            IList<Element> fireAlarms =
            collector.WherePasses(filter).WhereElementIsNotElementType().ToElements();
            String prompt = String.Format("The {0} in the current document are:\n",
                                    BuiltInCategory.OST_FireAlarmDevices.GetType());
            foreach (Element e in fireAlarms) {
                //  prompt += " | " + e.Name + "\n";
                prompt += $"{e.Name}: {e.Id}, type {e.GetType()} : {e.GetTypeId()}, {e.IsHidden(view)}\n";
            }
            // TaskDialog.Show("Revit", prompt);
            txtFireAlarms.Text = prompt;
        }

        private void getWall() {
            // sample code: https://help.autodesk.com/view/RVT/2017/ENU/?guid=GUID-85E4A43E-88B5-43C6-908C-2D138C9F611D#GUID-85E4A43E-88B5-43C6-908C-2D138C9F611D
            // Find all Wall instances in the document by using category filter
            ElementCategoryFilter filter = new ElementCategoryFilter(BuiltInCategory.OST_Walls);

            // Apply the filter to the elements in the active document
            // Use shortcut WhereElementIsNotElementType() to find wall instances only
            FilteredElementCollector collector = new FilteredElementCollector(document);
            IList<Element> walls =
            collector.WherePasses(filter).WhereElementIsNotElementType().ToElements();
            String prompt = "The walls in the current document are:\n";
            foreach (Element e in walls) {
                prompt += " | " + e.Name + "\n";
            }
            // TaskDialog.Show("Revit", prompt);
            txtWall.Text = prompt;
        }

        private void getAllFamilies() {
            try {
                FilteredElementCollector collector = new FilteredElementCollector(document);
                ICollection<Element> elements = collector.OfClass(typeof(Family)).ToElements();

                StringBuilder sb = new StringBuilder();

                foreach (Element el in elements) {
                    sb.AppendLine(String.Format("{0}, id: {5}, type: {1}, typeId: {2}, levelId: {3}, category: {4}",
                        el.Name, el.GetType(), el.GetTypeId(), el.LevelId, el.Category, el.Id));
                }

                // TaskDialog.Show("reavit", sb.ToString());
                txtFamilies.Text = String.Format("BuiltInCategory.OST_Walls : {0}\n\n", BuiltInCategory.OST_Walls);
                txtFamilies.Text += sb.ToString();

            } catch (Exception ex) {
                // msg = ex.ToString();
                txtFamilies.Text = ex.ToString();
            }
        }
    }
}

using Autodesk.Revit.DB;
using Autodesk.Revit.DB.ExtensibleStorage;
using Autodesk.Revit.UI;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Text;
using System.Windows.Forms;
using TextBox = Autodesk.Revit.UI.TextBox;

namespace io.odysz.hello.revit.lession2 {
    public partial class HelloForm : System.Windows.Forms.Form {
        private Autodesk.Revit.UI.UIDocument uidoc; // = commandData.Application.ActiveUIDocument;
        private Document dbdoc;
        private Autodesk.Revit.DB.View view;

        public HelloForm(Document dbdoc, Autodesk.Revit.UI.UIDocument uidoc, Autodesk.Revit.DB.View uiview) {
            InitializeComponent();
            this.dbdoc = dbdoc;
            this.uidoc = uidoc;
            view = uiview;
        }

        private Schema deviceSchema;
        private static Guid guid = new Guid("17760704-1971-1911-1010-197101234567");

        private void btnExpt_Click(object sender, EventArgs e) {
            // exportFBX();
            // SmClient.Test(txtConn);

            // save extensibleStorage and update DB
            // extensible storage:
            // https://thebuildingcoder.typepad.com/blog/2011/04/extensible-storage.html
            // http://help.autodesk.com/view/RVT/2018/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Storing_Data_in_the_Revit_model_Extensible_Storage_html
            if (deviceSchema == null)
                deviceSchema = initSchema(dbdoc);

            // check is there alread has the entity
            //if (selectedElem != null) { }

        }

        /// <summary>
        /// Init a Revit ExtensibleStorage Schema.
        /// see https://thebuildingcoder.typepad.com/blog/2011/04/extensible-storage.html 
        /// </summary>
        /// <param name="document"></param>
        /// <returns></returns>
        private static Schema initSchema(Document document) {
            Transaction createSchemaAndStoreData = new Transaction(document, "tCreateAndStore");
            createSchemaAndStoreData.Start();
            SchemaBuilder schemaBuilder = new SchemaBuilder(guid);
            schemaBuilder.SetReadAccessLevel(AccessLevel.Public); // allow anyone to read the object
            schemaBuilder.SetWriteAccessLevel(AccessLevel.Vendor); // restrict writing to this vendor only
            schemaBuilder.SetVendorId("io.odysz"); // required because of restricted write-access
            schemaBuilder.SetSchemaName("DeviceInfo");
            // create a field to store an XYZ
            FieldBuilder fieldBuilder =
                    schemaBuilder.AddSimpleField("xyz0", typeof(XYZ));
            fieldBuilder.SetUnitType(UnitType.UT_Length);
            fieldBuilder.SetDocumentation("A stored location value representing a wiring splice in a wall.");

            Schema schema = schemaBuilder.Finish(); // register the Schema object
            return schema;
        }

        private void exportFBX() {
            /* https://forums.autodesk.com/t5/revit-api-forum/how-to-export-with-all-categories-of-3d-view-of-rvt-file-to-fbx/m-p/7112555
            UIApplication uiApp = commandData.Application;
            Document doc = uiApp.ActiveUIDocument.Document;
            
            ViewSet viewSet = new ViewSet();
            viewSet.Insert(doc.ActiveViewSet);
            doc.Export("C:/......PATH......", "nameFBXExportedFile", viewSet, new FBXExportOptions());
            */
            ViewSet viewSet = new ViewSet();
            viewSet.Insert(view);
            dbdoc.Export("f:/revit/temp", "lesson2.fbx", viewSet, new FBXExportOptions());
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
            FilteredElementCollector collector = new FilteredElementCollector(dbdoc);
            IList<Element> fireAlarms =
            collector.WherePasses(filter).WhereElementIsNotElementType().ToElements();
            String prompt = String.Format("The {0} in the current document are:\r\n - \r\n",
                                    BuiltInCategory.OST_FireAlarmDevices.GetType());
            foreach (Element e in fireAlarms) {
                //  prompt += " | " + e.Name + "\n";
                prompt += $"{e.Name} {e.ParametersMap}: {e.Id}, type {e.GetType()} : {e.GetTypeId()}, {e.IsHidden(view)}\r\n";
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
            FilteredElementCollector collector = new FilteredElementCollector(dbdoc);
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
                FilteredElementCollector collector = new FilteredElementCollector(dbdoc);
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

        private void btnConn_ClickAsync(object sender, EventArgs e) {
            string serv = "http://192.168.0.201:8080/ifire/echo.serv?t=echo&p1=x";
            postConn(serv, null);
        }

        private static string s;
        public static async void postConn(string url, TextBox txtbox) {
            using (var client = new HttpClient()) {

                try {
                    StringContent content = getPostPayload();

                    var responseTsk = await client.PostAsync(url, content);

                    var responseString = await responseTsk.Content.ReadAsStringAsync();

                    s = url + "\n" + responseString;
                    if (txtbox != null)
                        txtbox.ItemText = s;
                    else Debug.WriteLine(s);
                }catch (Exception ex) {
                    Debug.WriteLine("ERROR ERROR ERROR ERROR ERROR ");
                    Debug.WriteLine(ex.Message);
                }
            }
        }

        public static StringContent getPostPayload() {
            var values = new Dictionary<string, string> {
                    { "thing1", "hello" },
                    { "thing2", "world" } };

            // var content = new FormUrlEncodedContent(values);
            // return new StringContent(values.ToString(), Encoding.UTF8);
            return new StringContent("{}", Encoding.UTF8, "application/json");
        }

        /// <summary>
        /// Find a selected element.
        /// https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2016/ENU/Revit-API/files/GUID-C67BE1BC-50D6-403C-8458-61BEBADFC6CE-htm.html
        /// </summary>
        private void btnSelected_Click(object sender, EventArgs e) {
            ICollection<ElementId> selectedIds = uidoc.Selection.GetElementIds();
            if (0 == selectedIds.Count) {
                // If no elements selected.
                TaskDialog.Show("Revit", "You haven't selected any elements.");
            } else {
                String info = "Ids of selected elements in the document are: ";
                foreach (ElementId id in selectedIds) {
                    info += "\n\t" + id.IntegerValue;
                }

                TaskDialog.Show("Revit", info);
            }
        }
    }
}

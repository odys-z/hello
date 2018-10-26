using System;
using System.Text;
using System.Runtime.Serialization.Json;
using System.IO;
using System.Windows.Forms;
using System.Runtime.Serialization;

namespace io.odysz.hello.revit {
    public class SmClient {

        public static void Test (TextBox txtConn) {
            string json = @"{
                'Email': 'james@example.com',
                'Active': true,
                'CreatedDate': '2013-01-20T00:00:00Z'
                ";

            // 'Roles': [
            // {'User':'111','Admin':'123'}
            // ]}


            DataContractJsonSerializer js1 = new DataContractJsonSerializer(typeof(Pojo));
            MemoryStream ms1 = new MemoryStream(ASCIIEncoding.ASCII.GetBytes(json));
            Pojo pj = (Pojo)js1.ReadObject(ms1);
            txtConn.Text = pj.ToString();

            /*
            DataContractJsonSerializer js = new DataContractJsonSerializer(typeof(Pojo));
            MemoryStream ms = new MemoryStream();
            // Pojo pj = new Pojo();
            js.WriteObject(ms, pj);

            ms.Position = 0;
            StreamReader sr = new StreamReader(ms);
            string s1 = sr.ReadToEnd();
            Console.WriteLine(s1);
            sr.Close();
            ms.Close();
            txtConn.Text = s1;
            */

        }
    }

    [DataContract]
    public class Pojo {
        [DataMember]
        string Email;
        [DataMember]
        bool Active;
        [DataMember]
        DateTime CreatedDate;

        //Role[] Roles;
        public override
        string ToString() {
            return string.Format(@"
Email: {0}
Active: {1}
DateTime: {2}", Email, Active, CreatedDate);
        }
    }

    internal class Role {
        string User;
        string Admin;
    }
}

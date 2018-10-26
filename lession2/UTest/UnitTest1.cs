using System;
using System.Diagnostics;
using Microsoft.VisualStudio.TestTools.UnitTesting;

using System.Runtime.Serialization.Json;
using System.Text;
using System.IO;

using System.Runtime.Serialization;
using System.Collections.ObjectModel;


namespace io.odysz.hello.revit {
    [TestClass]
    public class UnitTest1 {
        [TestMethod]
        public void TestMethod1() {
            string json = "{" +
                "\"Email\": \"james@example.com\"," +
                "\"Active\": true," +
                "\"CreatedDate\": \"\\/Date(2013-01-20 00:00:00)\\/\"" +
            // 'Roles': [
            // {'User':'111','Admin':'123'}
            // ]}
                "";


            DataContractJsonSerializer js1 = new DataContractJsonSerializer(typeof(Pojo));
            MemoryStream ms1 = new MemoryStream(ASCIIEncoding.ASCII.GetBytes(json));
            Pojo pj = (Pojo)js1.ReadObject(ms1);
            Debug.WriteLine(pj.ToString());

        }

        [TestMethod]
        public void TestGson() {
        }
    }

    [DataContract]
    class A {
        [DataMember]
        public String s;
        [DataMember]
        public int i;
        [DataMember(Name = "b")]
        public String _b;
        public byte[] b;
        [DataMember]
        public DateTime d;
    }



}

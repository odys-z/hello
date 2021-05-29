using System;
using System.Diagnostics;
using Microsoft.VisualStudio.TestTools.UnitTesting;

using System.Runtime.Serialization.Json;
using System.Text;
using System.IO;

using System.Runtime.Serialization;
using lession2.frame.protocol;
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Threading;

namespace io.odysz.hello.revit {
    [TestClass]
    public class UnitTest1 {
        public static void Main() {
            A a = new A();
            a.b = new byte[] { 65, 66, 67, 68 };
            a.s = "xyz";
            a.i = 12345;
            a.d = DateTime.Now;
            String s = Zson.toJson(a, typeof(A));
            Console.WriteLine(s);
            A a2 = (A)Zson.fromJson(s, typeof(A));
            Console.WriteLine(a2.s + " " + a2.i + " " + a2.b[0] + " " + a2.b[1] + " " +
                                          a2.b[2] + " " + a2.b[3] + " " + a2.d);
        }



        [TestMethod]
        public void TestSerialize() {

            //string json = "{" +
            //    "\"Email\": \"james@example.com\"," +
            //    "\"Active\": true," +
            //    "\"CreatedDate\": \"2013-01-20T00:00:00Z\"," +
            //    "\"Roles\": [ {\"role\":\"111\",\"id\":\"123\"} ]}";
            string json = @"{
                ""Email"": ""james@example.com"",
                ""Active"": true,
                ""CreatedDate"": ""2013-01-20T00:00:00Z"",
                ""Roles"": [ {""role"":""111"",""id"":""123""} ]}";



            DataContractJsonSerializer js1 = new DataContractJsonSerializer(typeof(Pojo2),
                new DataContractJsonSerializerSettings {
                    DateTimeFormat = new DateTimeFormat("yyyy-MM-dd'T'HH:mm:ssZ")
                });

            MemoryStream ms1 = new MemoryStream(ASCIIEncoding.ASCII.GetBytes(json));
            Pojo2 pj = (Pojo2)js1.ReadObject(ms1);
            Debug.WriteLine(pj.ToString());

        }

        [TestMethod]
        public void TestGson() {
            SmClient.Test(null);
        }


        [TestMethod]
        public async Task testZclientAsync() {
            string serv = "http://192.168.0.201:8080/ifire/echo.serv?t=echo&p1=x";
            using (var client = new HttpClient()) {
                Debug.WriteLine(" ......................");
                Debug.WriteLine(serv);

                var values = new Dictionary<string, string> {
                    { "thing1", "hello" },
                    { "thing2", "world" } };

                var content = new FormUrlEncodedContent(values);

                var responseTsk = await client.PostAsync(serv, content);

                var responseString = await responseTsk.Content.ReadAsStringAsync();
                Debug.WriteLine(responseString);

                /*
                postConn(serv, null);
                */
            }
        }

        [TestMethod]
        public void testPostEcho() {
            string serv = "http://192.168.0.201:8080/ifire/echo.serv?t=echo&p1=x";
            postEcho2(serv);
            Thread.Sleep(3000);
        }

        public async Task postEcho2(String url) {
            // string serv = "http://192.168.0.201:8080/ifire/echo.serv?t=echo&method=postEcho2";
            using (var client = new HttpClient()) {

                try {
                    Debug.WriteLine(" ---------    ---------    ------- ");
                    // StringContent content = HelloForm.getPostPayload();
                    EchoPayload echoPay = new EchoPayload("I'm UnitTest1.");
                    StringContent content = new StringContent(echoPay.ToString(), Encoding.UTF8, "application/json");

                    /*
                    var values = new Dictionary<string, string> {
                        { "thing1", "hello" },
                        { "thing2", "world" } };

                    var content = new FormUrlEncodedContent(values);
                    */

                    var responseTsk = await client.PostAsync(url, content);

                    var responseString = await responseTsk.Content.ReadAsStringAsync();

                    Debug.WriteLine(responseString);
                } catch (HttpRequestException ex) {
                    Debug.WriteLine(" ----  ----  ----  ----  ----  ---- RRROREE ERROR ERROR ERROR ERROR ");
                    Debug.WriteLine(ex.Message);
                }
            }
        }

        public async Task postEcho(String url) {
            // string serv = "http://192.168.0.201:8080/ifire/echo.serv?t=echo&p1=x";
            using (var client = new HttpClient()) {

                try {
                    Debug.WriteLine(" ||||||||||||||||||||||||||");
                    // StringContent content = HelloForm.getPostPayload();
                    StringContent content = new StringContent("{bc: 3}", Encoding.UTF8, "application/json");

                    /*
                    var values = new Dictionary<string, string> {
                        { "thing1", "hello" },
                        { "thing2", "world" } };

                    var content = new FormUrlEncodedContent(values);
                    */

                    var responseTsk = await client.PostAsync(url, content);

                    var responseString = await responseTsk.Content.ReadAsStringAsync();

                    Debug.WriteLine(responseString);
                } catch (HttpRequestException ex) {
                    Debug.WriteLine(" ----  ----  ----  ----  ----  ---- RRROREE ERROR ERROR ERROR ERROR ");
                    Debug.WriteLine(ex.Message);
                }
            }
        }
    }

    [DataContract]
    class A : ZObj {
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


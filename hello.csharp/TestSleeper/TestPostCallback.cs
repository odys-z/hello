using Microsoft.VisualStudio.TestTools.UnitTesting;
using Sleeper;
using System;
using System.Threading;
using System.Threading.Tasks;

namespace anclient
{
    [TestClass]
    public class TestPostCallback
    {
        [TestMethod]
        public async Task TestPost()
        {
            string ret = "403";
            bool onOk = false;
            ret = await PostClient.Post(false,
                (ok) => {
                    // set success
                    ret = ok;
                    onOk = true;
                },
                (err) => {
                    // set error
                    ret = err;
                    Assert.Fail("goWrong == false");
                });
            if (ret != "400")
                Assert.Fail("Why not returned after waiting?");
            if (!onOk)
                Assert.Fail("Not succeed!");
        }

        [TestMethod]
        public void TestCommit()
        {
            string[] myPara = new string[2];

            string ret = "403";
            bool onOk = false;
            PostClient client = new();
            CancellationTokenSource waker = new();
            client.CommitAsync("Hello",
                    (p) => {
                        ret = p;
                        myPara[0] = p;
                        myPara[1] = "Hello";
                        onOk = true;
                    },
                    waker);

            // only tests need this
            try { Task.Delay(1000, waker.Token).Wait();
            } catch (AggregateException _) { }
            finally { waker.Dispose(); }


            Assert.AreEqual("400", ret, "Why not returned after waiting?");
            Assert.IsTrue(onOk, "Not succeed!");
            Assert.AreEqual("400", myPara[0]);
            Assert.AreEqual("Hello", myPara[1]);
        }
    }
}

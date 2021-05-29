using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Threading;
using System.Threading.Tasks;

namespace Sleeper
{
    [TestClass]
    public class OnWakeCallback
    {
        [TestMethod]
        public async Task Test1Async()
        {
            CancellationTokenSource waker = new CancellationTokenSource();
            int ret = int.MaxValue;
            try
            {
                ret = await Sleep200.Sleep(waker.Token,
                    (ok) => {
                        // set success
                        ret = ok;
                        waker.Cancel();
                    },
                    (err) => {
                        // set error
                        ret = err;
                        if (ret > 200)
                            Assert.Fail("Sorry Late!");
                    });
                if (ret > 200)
                    Assert.Fail("Late honey!");
            }
            catch (AggregateException ex)
            {
                // We been waked up
                Assert.IsNotNull(ex);
                Assert.AreEqual(200, ret);
            }
            finally
            {
                waker.Dispose();
            }
        }
    }
}

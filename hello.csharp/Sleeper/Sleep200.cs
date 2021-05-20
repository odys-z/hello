using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Sleeper
{
    public class Sleep200
    {
        static void Main(string[] args)
        {
        }

        public async static Task<int> Sleep(CancellationToken waker, Action<int> onBreak, Action<int> onTimeOver)
        {
            int callbackPara = 200;
            int longtime = 6000;

            Thread.Sleep(200);
            onBreak(callbackPara);

            Task.Delay(longtime, waker).Wait();
            onTimeOver(callbackPara);

            return longtime + 200;
        }
    }
}

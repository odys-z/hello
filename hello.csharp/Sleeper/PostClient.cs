using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace anclient
{
    public class PostClient
    {
        public static async Task<string> Post(bool goWrong, Action<string> onOk, Action<string> onErr)
        {
            await Task.Delay(200);
            if (goWrong) onErr("404");
            else onOk("200");
            return "400";
        }

        public PostClient CommitAsync(string para, Action<string> onOk = null, CancellationTokenSource waker = null)
        {
            Task<string> t = Task.Run(async delegate
            {
                await Task.Delay(200);
                return "400";
            });
            t.Wait();
            if (onOk != null)
                onOk(t.Result);

            if (waker != null)
                waker.Cancel();
            return this;
        }
    }
}

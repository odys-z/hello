# About

The test demo from [Pywin32](https://github.com/mhammond/pywin32/tree/main/win32/Demos/service).


- Error

Can't start service installed with win32serviceutil.ServiceFramework.svcDoRun(). 

See [pywin32 #1771](https://github.com/mhammond/pywin32/issues/1771)

```
    py pipeTestService.py install
    py pipeTestService.py start
    Starting service PyPipeTestService
    Error 1053: The service did not respond to the start or control request in a timely fashion
```
# About

Test project for starting jar as windows service, with
[Apache Common Daemon](https://commons.apache.org/proper/commons-daemon/index.html).

# Troubleshootings

- Get current path in bat

```
    %cd%
```

- Where to download procrun

At Tomcat download.

- Error 2. System Can not find file

Use absolute path for registering service.

- Jvm.dll failed.

Error Log

```
    [2022-02-28 17:04:16] [info]  [20012] Starting service...
    [2022-02-28 17:04:16] [error] [20012] Found 'C:\jdk-15.0.2\bin\server\jvm.dll' but couldn't load it.
    [2022-02-28 17:04:16] [error] [20012] %1 不是有效的 Win32 应用程序。
    [2022-02-28 17:04:16] [error] [20012] Invalid JVM DLL handle.
```

Download the x64 version procrun.exe.

# Resources

*How to create a windows service from java app* answer [1](https://stackoverflow.com/a/2518162/7362888)
and [2](https://stackoverflow.com/a/10756495/7362888)

[*Java as Windows Service with Apache Commons Daemon*](http://web.archive.org/web/20090228071059/http://blog.platinumsolutions.com/node/234)

[Windows Environment Variables](http://libertyboy.free.fr/computing/reference/envariables/index.php)

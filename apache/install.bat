echo %cd%
hellosrv.exe //IS//hellosrv --Install=%cd%\hellosrv.exe ^
--ServiceUser LocalSystem ^
--Description="Hello Service" ^
--Jvm=auto ^
--Classpath=%cd%\target\classes ^
--Startup=auto ^
--StartMode=jvm ^
--StartClass=io.oz.hello.daemon.HelloDaemon ^
--StartMethod=windowsService ^
--StartParams=start ^
--StopMode=jvm ^
--StopClass=io.oz.hello.daemon.HelloDaemon ^
--StopMethod=windowsService ^
--StopParams=stop ^
--LogPath=%cd%\logs ^
--StdOutput=auto ^
--StdError=auto

hellosrv.exe //ES//hellosrv

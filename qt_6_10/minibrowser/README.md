# About

```
    The facts in this page is verified with Qt Creator 18 and Qt 6.10.1.
```

The Minibrowser is an example from Qt Creator. The Source is a Qt subproject
of [QtWebWiew](https://doc.qt.io/qt-6.5/qtwebview-index.html). 

The [QtWebView Soucre](https://code.qt.io/cgit/qt/qtwebview.git/)
is avaliable via Qt Git Project wizard. 

# Using web view in Qt Applications

Since Qt 6.10, Qt WebView will find Qt WebEngine (Chromium) by default, and if 
failed, will try [Microsoft Edge WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH).

Cons & Pros for choosing Qt WebEngine or WebView (Google AI):

```
    Summary Table
    Feature                 Qt WebEngine	        Qt WebView
    Supports iOS/iPhone     No                      Yes
    Underlying Engine	    Chromium	            Native (WKWebView on iOS)
    Supported Platforms     Windows, Linux, macOS	iOS, Android, macOS, Windows
    App Store Friendly	    No (for iOS)	        Yes
```

Multiple LLM answers confirm that App Store is enforcing the rule that all
application must show web pages only with WKWebView. Qt 6.10 WebView support it.

Another con of the WebEngine is that the distribution is much heavier, about 100MiB - 300MiB,
and requires 10G - 12G extra space for Qt SDK.

# Build Minibrowser

```
    Components Manager: qt-6.10.1/MaintenanceTool.exe
```

The source project requires:

* The Qt WebView Component (Qt -> Qt 6.10.1 -> Additional Libraries -> Qt WebView)

* The Qt Project can be built and run with kit *Desktop Qt 6.10.1 MSVC2022 64bit (Release)* on Windows 10

* No need for Qt WebView source project.

To enable debugging, requires:

* The CDB Debugger Support (Qt Creator -> CDB Debugger Support)

# Build Qt WebView

The [source project Qt WebView](https://code.qt.io/cgit/qt/qtwebview.git/), requires:

* The Qt WebEngine Component (Extensions -> Qt WebEngine -> Qt 6.10.1 -> MSVC2022 x64 & Debug Information Files)

* The Qt Project can be built and run with the kit *Desktop Qt 6.10.1 MSVC2022 64bit (Release)* on Windows 10

The final result of Qt WebView is a dll library, and can be referenced (linked) by
the above Minibrowswer project if set the environment for *Run Settings*.

```
    Projects pane → Run → Environment → Add these variables:

    QT_PLUGIN_PATH = .../qt-io/minibrowser/build/Desktop_Qt_6_10_1_MSVC2022_64bit-Release/bin
    # where the built Qt6WebView.dll and Qt6WebViewQuick.dll live
    QML2_IMPORT_PATH = .../qt-io/minibrowser/build/Desktop_Qt_6_10_1_MSVC2022_64bit-Release/qml
    # the built qml/QtWebView/qtwebviewquickplugin.dll
    # Optionally, add build bin to PATH (prepend it):
    # PATH = C:/Users/Alice/github/qt-io/minibrowser/build/.../bin;%PATH%
    QT_DEBUG_PLUGINS=1
```

To remove these settings in the Minibrowswer project, search the CMakeList.txt.user, and remove
the xml elements:

```
   <valuelist type="QVariantList" key="PE.EnvironmentAspect.Changes">
     <value type="QString">QT_PLUGIN_PATH=...</value>
     <value type="QString">QML2_IMPORT_PATH=...</value>
     <value type="QString">QT_DEBUG_PLUGINS=1</value>
   </valuelist>
```

# Credits

* The Qt WebView Source Project at [https://code.qt.io/cgit/qt/qtwebview.git/](https://code.qt.io/cgit/qt/qtwebview.git/).

# References

* [Qt WebView](https://doc.qt.io/qt-6/qtwebview-index.html), qt.io

* [Consulting / QCefWidget](https://github.com/constling/QCefWidget), github

* [Introduction to Microsoft Edge WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH), Microsoft Edge, Learn

* [Microsoft Edge WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2), Microsoft Edge Developer, Microsoft
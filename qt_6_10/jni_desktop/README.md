# About

For test some implementation details.

## JNI Back & Forth

Google AI: Summary of Recommendations for 2025

```
  Goal 	      Recommended Tool    	Why?
  Java UI     QtJambi               Direct bindings;
  Development                       uses familiar Java syntax with Qt power.

  Simple      JNI / QJniObject	    Native performance; part of the standard Qt library.
  Java Calls

  Complex     gRPC or WebSockets    Prevents crashes;
  Logic                             allows different languages to scale independently.
```

* References

  [1] [A Developer's Guide to Qt JNI: Mastering QJniEnvironment](https://runebook.dev/en/docs/qt/qjnienvironment/operator--gt)

  [2] [Qt on Android Episode 5 - An introduction to JNI on Android, the Qt way](https://www.kdab.com/qt-android-episode-5/)

## Sharing Json Object between QML & CPP

* QML signal with QVariant (js var) to Cpp Slot

  - Binding in main.cpp, and avoid segment error before the QML page loaded.

  ```
    ////////////////////////// semantier.h //////////////////////////
    class Semantier : public QObject
    { Q_OBJECT
      public:
        Semantier();
      public slots:
        void slt_postPing(const QVariant &qvar) { }
    };

    //////////////////////////// Main.qml /////////////////////////// 
    signal sig_postPing(jserv: var)

    Button {
        onClicked: {
            sig_postPing({jserv: jservPing.text,
                          timestamp: new Date().toISOString()});
        }
    }

    //////////////////////////// main.cpp /////////////////////////// 
    Semantier myClass;
    QObject::connect(&engine,
          &QQmlApplicationEngine::objectCreated,
          &app,
          [&myClass](QObject *obj, const QUrl &objUrl) {
              QObject::connect(obj, SIGNAL(sig_postPing(QVariant)),
                               &myClass, SLOT(slt_postPing(QVariant)));
              qDebug() << "sig_postPing connected ...";
          }, Qt::QueuedConnection);
  ```

## Send Http Request to jserv

* By QML

  - Import js lib in QML:

  ```
    import "semantier_qml.js" as Semantier // Qt requires upper case

    Semantier.ping(jserv)
  ```

  - XMLHttpRequest Cannot handler jserv response

  The jserv-album/ping.serv respond with headers:

  ```
    HTTP/1.1 200 OK
    Server: Portfolio 0.7
    Date: Tue, 23 Dec 2025 08:12:43 GMT
    synode: X29
    Transfer-Encoding: chunked
  ```

  which is not the stand http header and QML will return xhr.status = 0, responseText = ''.
  
  This cannot be walk around, since

  ```
    In QML, there is no alternative native JavaScript network API to XMLHttpRequest.
    Unlike browsers, QML does not support the fetch API, and popular libraries like
    Axios or jQuery cannot be imported because they depend on browser globals (like
    window or document) that do not exist in the QML engine.
  ```

  This line won't work:

  ```
    // open()
    xhr.overrideMimeType("text/plain; charset=x-user-defined");
    // send()
  ```

## Load Json files

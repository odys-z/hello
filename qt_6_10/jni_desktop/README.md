# About

For test some implementation details.

## JNI Back & Forth

## Sharing Json Object between QML & CPP

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
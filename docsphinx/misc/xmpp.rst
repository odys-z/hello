IM Solution
===========

Server
------

`Jitsi <https://jitsi.github.io/handbook/docs/architecture#architecture-diagram>`_
could be better than `openfire projects <https://www.igniterealtime.org/projects/>`_.

Clients
-------

None are suitable?

1. No "one coding, twice use"

For React Native Sunsetting, no react native for mobile. So it is possible using
Jitsi Mobile SDK or Smack(Movim/Android?).

2. Not `Movim <https://movim.eu/>`_

Movim uses PHP for web, but should keep an eye on `Movim for Android <https://github.com/movim/movim_android>`_.

The `Activity <https://github.com/movim/movim_android/blob/master/Movim/src/main/java/com/movim/movim/MainActivity.java>`_
uses WebView & WebChromeClient. Here is
`an more about WebView <https://developer.android.com/guide/webapps/webview>`_.

3. `Jitsi has web and mobile API <https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-mobile>`_

4. `JSXC is for prosody <https://jsxc.readthedocs.io/en/latest/getting-started/requirements.html#prosody>`_,
also looks promising over javascript.

5. `Converse is usin javascript <https://conversejs.org/docs/html/quickstart.html#quickstart>`_

6. `Smack <https://download.igniterealtime.org/smack/docs/latest/documentation/overview.html>`_
is a java client.

7. `react-jitsi <https://github.com/gatteo/react-jitsi#readme>`_  is a good example
of `Jitsi Meet JS API <https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-iframe>`_.

React-jitsi's Demo failed.

8. [no open source]`react chat <https://www.npmjs.com/package/react-chat-engine>`_ is promising
but just a library.

.. image:: https://chat-engine-assets.s3.amazonaws.com/react-chat-engine.gif
    :width: 320px

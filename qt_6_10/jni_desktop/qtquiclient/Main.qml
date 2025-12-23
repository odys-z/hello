import QtQuick
import QtQuick.Controls

import "semantier_qml.js" as Semantier

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Text {
        id: jservPing
        text: 'http://192.168.0.201/jserv-album/login.serv'
    }

    Rectangle {
        id: jservrect
        anchors.centerIn: parent
        border.color: "grey"
        color: "lightgrey"
        width: parent.width
        height: 40

        TextInput {
            id: jservtxt
            anchors.centerIn: jservrect
            anchors.margins: 5 // Add some padding inside the container

            // Initial text and styling
            text: "http://192.168.0.201:8964/jserv-album/login.serv"
            font.family: "Helvetica"
            font.pointSize: 14
            color: "black"

            // Enable focus to receive keyboard input
            focus: true

            // Set text format to allow simple HTML styling
            // textFormat: TextEdit.RichText

            // Connect to a signal to react when text changes
            onTextChanged: {
                console.log("Text changed to: " + jservtxt.text)
            }
        }
    }

    Button {
        id: qmlPing
        text: "QML Get"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: jservrect.bottom
        // width: 120
        // height: 40
        leftInset: 0
        rightInset: 0
        topInset: 0
        bottomInset: 0
        padding: 10 // Now 'padding' should be the primary control
        anchors.topMargin: 20

        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: qmlPing.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            radius: 4
        }

        onClicked: {
            console.log(`${jservPing.text}`);
            console.log("Current QML file directory URL: " + Qt.resolvedUrl("."));
            console.log("Application current working directory: " + currentWorkingDirectory);
            console.log("Application binary directory: " + applicationBinaryDirectory);

            Semantier.ping({
                jserv: jservPing.text,
                onGet: (c, r) => console.log(c, r)});
        }
    }

    signal sig_postPing(jserv: string)

    Button {
        id: cppPost
        text: "Post signal to C++ slot"
        anchors.left: qmlPing.right
        anchors.top: jservrect.bottom
        leftInset: 0
        rightInset: 0
        topInset: 0
        bottomInset: 0
        padding: 10 // Now 'padding' should be the primary control
        anchors.margins: 20

        background: Rectangle {
            implicitWidth: 200
            implicitHeight: 40
            color: cppPost.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            radius: 4
        }

        onClicked: {
            sig_postPing(jservPing.text);
            console.log(`[QML.cppPost] Singaling with ${jservPing.text}`);
        }

    }
}

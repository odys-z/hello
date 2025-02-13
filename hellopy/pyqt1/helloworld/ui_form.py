# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(617, 204)
        palette = QPalette()
        brush = QBrush(QColor(235, 235, 235, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(14, 90, 118, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(144, 144, 144, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Widget.setPalette(palette)
        icon = QIcon(QIcon.fromTheme(u"battery"))
        Widget.setWindowIcon(icon)
        self.bDialog = QPushButton(Widget)
        self.bDialog.setObjectName(u"bDialog")
        self.bDialog.setGeometry(QRect(390, 39, 130, 31))
        palette1 = QPalette()
        brush3 = QBrush(QColor(83, 83, 83, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush4 = QBrush(QColor(1, 154, 177, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush4)
        brush5 = QBrush(QColor(244, 244, 244, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(158, 158, 158, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        brush7 = QBrush(QColor(10, 62, 81, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(91, 98, 102, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(191, 191, 191, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        self.bDialog.setPalette(palette1)
        icon1 = QIcon()
        icon1.addFile(u"odysz.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bDialog.setIcon(icon1)
        self.bDialog.setCheckable(True)
        self.txtIP = QLineEdit(Widget)
        self.txtIP.setObjectName(u"txtIP")
        self.txtIP.setGeometry(QRect(180, 36, 191, 31))
        self.txtIP.setMaxLength(512)
        self.lbIP = QLabel(Widget)
        self.lbIP.setObjectName(u"lbIP")
        self.lbIP.setGeometry(QRect(50, 40, 111, 20))
        font = QFont()
        font.setPointSize(10)
        self.lbIP.setFont(font)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Portfolio Settings", None))
        self.bDialog.setText(QCoreApplication.translate("Widget", u"Ping", None))
#if QT_CONFIG(shortcut)
        self.bDialog.setShortcut(QCoreApplication.translate("Widget", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.txtIP.setText(QCoreApplication.translate("Widget", u"127.0.0.1:8964", None))
        self.lbIP.setText(QCoreApplication.translate("Widget", u"http:// ip:port", None))
    # retranslateUi


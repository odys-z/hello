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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

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
        self.bDialog.setGeometry(QRect(250, 40, 130, 30))
        icon1 = QIcon()
        icon1.addFile(u"odysz.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bDialog.setIcon(icon1)
        self.bDialog.setCheckable(True)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Portfolio Settings", None))
        self.bDialog.setText(QCoreApplication.translate("Widget", u"Dialog...", None))
#if QT_CONFIG(shortcut)
        self.bDialog.setShortcut(QCoreApplication.translate("Widget", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


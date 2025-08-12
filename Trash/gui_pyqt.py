# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(668, 480)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"    min-width: 100px;\n"
"    min-height: 40px;\n"
"    padding: 8px 16px;\n"
"    color: rgb(129, 129, 129);\n"
"    background-color: rgba(150, 155, 150, 60);\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-family: Arial, sans-serif;\n"
"    border: 2px solid gray;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(150, 155, 150, 20);\n"
"    border-color: rgb(173, 173, 173);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(234, 220, 207);\n"
"    border-color: rgb(173, 173, 173);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.itemGenerator = QPushButton(self.frame)
        self.itemGenerator.setObjectName(u"itemGenerator")
        icon = QIcon()
        icon.addFile(u"res/personal_bag_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.itemGenerator.setIcon(icon)
        self.itemGenerator.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.itemGenerator)

        self.priceGenerator = QPushButton(self.frame)
        self.priceGenerator.setObjectName(u"priceGenerator")
        icon1 = QIcon()
        icon1.addFile(u"res/sell_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.priceGenerator.setIcon(icon1)
        self.priceGenerator.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.priceGenerator)

        self.messageHandler = QPushButton(self.frame)
        self.messageHandler.setObjectName(u"messageHandler")
        icon2 = QIcon()
        icon2.addFile(u"res/add_comment_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.messageHandler.setIcon(icon2)
        self.messageHandler.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.messageHandler)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.itemGenerator.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0432", None))
        self.priceGenerator.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0446\u0435\u043d\u044b", None))
        self.messageHandler.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
    # retranslateUi


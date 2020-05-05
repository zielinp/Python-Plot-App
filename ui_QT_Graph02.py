# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT_Graph03tLixji.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 531)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(774, 531))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"plot-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(50,50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.functionPattern = QLineEdit(self.centralwidget)
        self.functionPattern.setObjectName(u"functionPattern")
        self.functionPattern.setGeometry(QRect(580, 80, 151, 31))
        font = QFont()
        font.setPointSize(9)
        self.functionPattern.setFont(font)
        self.functionRange = QLineEdit(self.centralwidget)
        self.functionRange.setObjectName(u"functionRange")
        self.functionRange.setGeometry(QRect(580, 120, 151, 31))
        self.functionRange.setFont(font)
        self.functionRange.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 80, 47, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 20, 401, 31))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 120, 47, 31))
        self.label_3.setFont(font1)
        self.cleanButton = QPushButton(self.centralwidget)
        self.cleanButton.setObjectName(u"cleanButton")
        self.cleanButton.setGeometry(QRect(650, 170, 91, 41))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.cleanButton.setFont(font3)
        self.drawButton = QPushButton(self.centralwidget)
        self.drawButton.setObjectName(u"drawButton")
        self.drawButton.setGeometry(QRect(530, 170, 91, 41))
        self.drawButton.setFont(font3)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 90, 451, 381))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.userCommunication = QTextEdit(self.centralwidget)
        self.userCommunication.setObjectName(u"userCommunication")
        self.userCommunication.setGeometry(QRect(530, 230, 211, 191))
        self.userCommunication.setFont(font)
        self.userCommunication.setReadOnly(True)
        self.userCommunication.setAcceptRichText(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.functionPattern, self.functionRange)
        QWidget.setTabOrder(self.functionRange, self.drawButton)
        QWidget.setTabOrder(self.drawButton, self.cleanButton)
        QWidget.setTabOrder(self.cleanButton, self.userCommunication)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.functionPattern.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Example functions:</span></p><p><span style=\" font-size:9pt;\">F(x)=2x</span><span style=\" font-size:9pt; vertical-align:super;\">2 </span><span style=\" font-size:9pt;\">--&gt; 2*x**2</span></p><p><span style=\" font-size:9pt;\">F(x)=3sin(x) --&gt; 3*sin(x)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.functionPattern.setText("")
        self.functionPattern.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your function pattern...", None))
#if QT_CONFIG(tooltip)
        self.functionRange.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Example range and step:</span></p><p><span style=\" font-size:9pt;\">0;10;1</span></p><p><span style=\" font-size:9pt;\">-10;15;0.15</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.functionRange.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Start; Stop; Step", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"F(x)=", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Draw graphs of your functions!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"D(x)=", None))
        self.cleanButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.drawButton.setText(QCoreApplication.translate("MainWindow", u"Draw", None))
    # retranslateUi


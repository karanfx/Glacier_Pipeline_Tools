# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 438)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.project_lB = QLabel(self.frame)
        self.project_lB.setObjectName(u"project_lB")

        self.gridLayout_2.addWidget(self.project_lB, 0, 0, 1, 1)

        self.project_cB = QComboBox(self.frame)
        self.project_cB.setObjectName(u"project_cB")

        self.gridLayout_2.addWidget(self.project_cB, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shot_lB = QLabel(self.frame)
        self.shot_lB.setObjectName(u"shot_lB")

        self.horizontalLayout.addWidget(self.shot_lB)

        self.shot_cB = QComboBox(self.frame)
        self.shot_cB.setObjectName(u"shot_cB")

        self.horizontalLayout.addWidget(self.shot_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.User_lB = QLabel(self.frame)
        self.User_lB.setObjectName(u"User_lB")

        self.horizontalLayout_2.addWidget(self.User_lB)

        self.User_cB = QComboBox(self.frame)
        self.User_cB.setObjectName(u"User_cB")

        self.horizontalLayout_2.addWidget(self.User_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.subir_lB = QLabel(self.frame)
        self.subir_lB.setObjectName(u"subir_lB")

        self.horizontalLayout_3.addWidget(self.subir_lB)

        self.subdir_cB = QComboBox(self.frame)
        self.subdir_cB.setObjectName(u"subdir_cB")

        self.horizontalLayout_3.addWidget(self.subdir_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tools_lB = QLabel(self.frame)
        self.tools_lB.setObjectName(u"tools_lB")

        self.horizontalLayout_4.addWidget(self.tools_lB)

        self.tools_cB = QComboBox(self.frame)
        self.tools_cB.setObjectName(u"tools_cB")

        self.horizontalLayout_4.addWidget(self.tools_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)

        self.launch_button = QPushButton(self.frame)
        self.launch_button.setObjectName(u"launch_button")

        self.gridLayout_3.addWidget(self.launch_button, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 338, 21))
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.project_lB.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.shot_lB.setText(QCoreApplication.translate("MainWindow", u"Shot :", None))
        self.User_lB.setText(QCoreApplication.translate("MainWindow", u"User :", None))
        self.subir_lB.setText(QCoreApplication.translate("MainWindow", u"Sub Dir : ", None))
        self.tools_lB.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.launch_button.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


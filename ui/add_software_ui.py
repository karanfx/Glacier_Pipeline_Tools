# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_software_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 145)
        self.reg_buttonBox = QDialogButtonBox(Dialog)
        self.reg_buttonBox.setObjectName(u"reg_buttonBox")
        self.reg_buttonBox.setGeometry(QRect(30, 100, 341, 32))
        self.reg_buttonBox.setOrientation(Qt.Horizontal)
        self.reg_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 219, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.softname = QLabel(self.widget)
        self.softname.setObjectName(u"softname")

        self.horizontalLayout.addWidget(self.softname)

        self.softname_LE = QLineEdit(self.widget)
        self.softname_LE.setObjectName(u"softname_LE")

        self.horizontalLayout.addWidget(self.softname_LE)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 60, 245, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.softpath_LB = QLabel(self.widget1)
        self.softpath_LB.setObjectName(u"softpath_LB")

        self.horizontalLayout_2.addWidget(self.softpath_LB)

        self.softpath_LE = QLineEdit(self.widget1)
        self.softpath_LE.setObjectName(u"softpath_LE")

        self.horizontalLayout_2.addWidget(self.softpath_LE)

        self.softpath_TB = QToolButton(self.widget1)
        self.softpath_TB.setObjectName(u"softpath_TB")

        self.horizontalLayout_2.addWidget(self.softpath_TB)


        self.retranslateUi(Dialog)
        self.reg_buttonBox.accepted.connect(Dialog.accept)
        self.reg_buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.softname.setText(QCoreApplication.translate("Dialog", u"Software Name:", None))
        self.softpath_LB.setText(QCoreApplication.translate("Dialog", u"Software Path:", None))
        self.softpath_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
    # retranslateUi


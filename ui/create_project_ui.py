# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_project_ui.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(383, 202)
        Dialog.setStyleSheet(u"background-color: rgb(132, 132, 132);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.project_LB = QLabel(Dialog)
        self.project_LB.setObjectName(u"project_LB")

        self.horizontalLayout.addWidget(self.project_LB)

        self.project_LE = QLineEdit(Dialog)
        self.project_LE.setObjectName(u"project_LE")

        self.horizontalLayout.addWidget(self.project_LE)

        self.Project_TB = QToolButton(Dialog)
        self.Project_TB.setObjectName(u"Project_TB")

        self.horizontalLayout.addWidget(self.Project_TB)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Seq_LB = QLabel(Dialog)
        self.Seq_LB.setObjectName(u"Seq_LB")

        self.horizontalLayout_2.addWidget(self.Seq_LB)

        self.Seq_LE = QLineEdit(Dialog)
        self.Seq_LE.setObjectName(u"Seq_LE")

        self.horizontalLayout_2.addWidget(self.Seq_LE)

        self.Seq_TB = QToolButton(Dialog)
        self.Seq_TB.setObjectName(u"Seq_TB")

        self.horizontalLayout_2.addWidget(self.Seq_TB)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Shot_LB = QLabel(Dialog)
        self.Shot_LB.setObjectName(u"Shot_LB")

        self.horizontalLayout_3.addWidget(self.Shot_LB)

        self.Shot_LE = QLineEdit(Dialog)
        self.Shot_LE.setObjectName(u"Shot_LE")

        self.horizontalLayout_3.addWidget(self.Shot_LE)

        self.Shot_TB = QToolButton(Dialog)
        self.Shot_TB.setObjectName(u"Shot_TB")

        self.horizontalLayout_3.addWidget(self.Shot_TB)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.create_buttons = QDialogButtonBox(Dialog)
        self.create_buttons.setObjectName(u"create_buttons")
        self.create_buttons.setOrientation(Qt.Horizontal)
        self.create_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.create_buttons, 3, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.create_buttons.accepted.connect(Dialog.accept)
        self.create_buttons.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.project_LB.setText(QCoreApplication.translate("Dialog", u"Project Name :", None))
        self.Project_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.Seq_LB.setText(QCoreApplication.translate("Dialog", u"Sequance Name:", None))
        self.Seq_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.Shot_LB.setText(QCoreApplication.translate("Dialog", u"Shot Name :", None))
        self.Shot_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(436, 372)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mail_to_LB = QLabel(Form)
        self.mail_to_LB.setObjectName(u"mail_to_LB")

        self.horizontalLayout.addWidget(self.mail_to_LB)

        self.to_mail_LE = QLineEdit(Form)
        self.to_mail_LE.setObjectName(u"to_mail_LE")

        self.horizontalLayout.addWidget(self.to_mail_LE)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mail_ubject_LB = QLabel(Form)
        self.mail_ubject_LB.setObjectName(u"mail_ubject_LB")

        self.horizontalLayout_2.addWidget(self.mail_ubject_LB)

        self.mail_subject_LE = QLineEdit(Form)
        self.mail_subject_LE.setObjectName(u"mail_subject_LE")

        self.horizontalLayout_2.addWidget(self.mail_subject_LE)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.mail_body_TE = QTextEdit(Form)
        self.mail_body_TE.setObjectName(u"mail_body_TE")

        self.verticalLayout_2.addWidget(self.mail_body_TE)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.mail_send_Pbutton = QPushButton(self.frame)
        self.mail_send_Pbutton.setObjectName(u"mail_send_Pbutton")
        self.mail_send_Pbutton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_3.addWidget(self.mail_send_Pbutton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.frame)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mail_to_LB.setText(QCoreApplication.translate("Form", u"To :", None))
        self.mail_ubject_LB.setText(QCoreApplication.translate("Form", u"Subject : ", None))
        self.mail_send_Pbutton.setText(QCoreApplication.translate("Form", u"Send", None))
    # retranslateUi


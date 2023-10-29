# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_dirs.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(548, 453)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.studio_dir_LB = QLabel(Dialog)
        self.studio_dir_LB.setObjectName(u"studio_dir_LB")

        self.horizontalLayout.addWidget(self.studio_dir_LB)

        self.studio_dir_LE = QLineEdit(Dialog)
        self.studio_dir_LE.setObjectName(u"studio_dir_LE")

        self.horizontalLayout.addWidget(self.studio_dir_LE)

        self.studio_dir_TB = QToolButton(Dialog)
        self.studio_dir_TB.setObjectName(u"studio_dir_TB")

        self.horizontalLayout.addWidget(self.studio_dir_TB)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.user_LB = QLabel(Dialog)
        self.user_LB.setObjectName(u"user_LB")

        self.horizontalLayout_2.addWidget(self.user_LB)

        self.user_LE = QLineEdit(Dialog)
        self.user_LE.setObjectName(u"user_LE")

        self.horizontalLayout_2.addWidget(self.user_LE)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.H_sep = QFrame(Dialog)
        self.H_sep.setObjectName(u"H_sep")
        self.H_sep.setFrameShape(QFrame.HLine)
        self.H_sep.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.H_sep)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.houdini_dir_LB = QLabel(Dialog)
        self.houdini_dir_LB.setObjectName(u"houdini_dir_LB")

        self.horizontalLayout_3.addWidget(self.houdini_dir_LB)

        self.houdini_dir_LE = QLineEdit(Dialog)
        self.houdini_dir_LE.setObjectName(u"houdini_dir_LE")

        self.horizontalLayout_3.addWidget(self.houdini_dir_LE)

        self.houdini_tB = QToolButton(Dialog)
        self.houdini_tB.setObjectName(u"houdini_tB")

        self.horizontalLayout_3.addWidget(self.houdini_tB)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.maya_dir_LB = QLabel(Dialog)
        self.maya_dir_LB.setObjectName(u"maya_dir_LB")

        self.horizontalLayout_4.addWidget(self.maya_dir_LB)

        self.maya_dir_LE = QLineEdit(Dialog)
        self.maya_dir_LE.setObjectName(u"maya_dir_LE")

        self.horizontalLayout_4.addWidget(self.maya_dir_LE)

        self.maya_tB = QToolButton(Dialog)
        self.maya_tB.setObjectName(u"maya_tB")

        self.horizontalLayout_4.addWidget(self.maya_tB)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nuke_dir_LB = QLabel(Dialog)
        self.nuke_dir_LB.setObjectName(u"nuke_dir_LB")

        self.horizontalLayout_5.addWidget(self.nuke_dir_LB)

        self.nukedir_LE = QLineEdit(Dialog)
        self.nukedir_LE.setObjectName(u"nukedir_LE")

        self.horizontalLayout_5.addWidget(self.nukedir_LE)

        self.nuke_tB = QToolButton(Dialog)
        self.nuke_tB.setObjectName(u"nuke_tB")

        self.horizontalLayout_5.addWidget(self.nuke_tB)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.unreal_dir_LB = QLabel(Dialog)
        self.unreal_dir_LB.setObjectName(u"unreal_dir_LB")

        self.horizontalLayout_6.addWidget(self.unreal_dir_LB)

        self.unreal_dir_LE = QLineEdit(Dialog)
        self.unreal_dir_LE.setObjectName(u"unreal_dir_LE")

        self.horizontalLayout_6.addWidget(self.unreal_dir_LE)

        self.unreal_tB = QToolButton(Dialog)
        self.unreal_tB.setObjectName(u"unreal_tB")

        self.horizontalLayout_6.addWidget(self.unreal_tB)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.discord_dir_LB = QLabel(Dialog)
        self.discord_dir_LB.setObjectName(u"discord_dir_LB")

        self.horizontalLayout_7.addWidget(self.discord_dir_LB)

        self.discord_dir_LE = QLineEdit(Dialog)
        self.discord_dir_LE.setObjectName(u"discord_dir_LE")

        self.horizontalLayout_7.addWidget(self.discord_dir_LE)

        self.discord_tB = QToolButton(Dialog)
        self.discord_tB.setObjectName(u"discord_tB")

        self.horizontalLayout_7.addWidget(self.discord_tB)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.custom_LB_1 = QLineEdit(Dialog)
        self.custom_LB_1.setObjectName(u"custom_LB_1")

        self.horizontalLayout_10.addWidget(self.custom_LB_1)

        self.custom_dir_LE_1 = QLineEdit(Dialog)
        self.custom_dir_LE_1.setObjectName(u"custom_dir_LE_1")

        self.horizontalLayout_10.addWidget(self.custom_dir_LE_1)

        self.custom_tB_1 = QToolButton(Dialog)
        self.custom_tB_1.setObjectName(u"custom_tB_1")

        self.horizontalLayout_10.addWidget(self.custom_tB_1)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.custom_LB_3 = QLineEdit(Dialog)
        self.custom_LB_3.setObjectName(u"custom_LB_3")

        self.horizontalLayout_12.addWidget(self.custom_LB_3)

        self.custom_dir_LE_3 = QLineEdit(Dialog)
        self.custom_dir_LE_3.setObjectName(u"custom_dir_LE_3")

        self.horizontalLayout_12.addWidget(self.custom_dir_LE_3)

        self.custom_tB_3 = QToolButton(Dialog)
        self.custom_tB_3.setObjectName(u"custom_tB_3")

        self.horizontalLayout_12.addWidget(self.custom_tB_3)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.Save_Bbox = QDialogButtonBox(Dialog)
        self.Save_Bbox.setObjectName(u"Save_Bbox")
        self.Save_Bbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save_Bbox.setOrientation(Qt.Horizontal)
        self.Save_Bbox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.RestoreDefaults|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.Save_Bbox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.Save_Bbox.accepted.connect(Dialog.accept)
        self.Save_Bbox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Glacier", None))
        self.studio_dir_LB.setText(QCoreApplication.translate("Dialog", u"Studio Directory:", None))
        self.studio_dir_TB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.user_LB.setText(QCoreApplication.translate("Dialog", u"Username:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Tool/Software Directories", None))
        self.houdini_dir_LB.setText(QCoreApplication.translate("Dialog", u"Houdini : ", None))
        self.houdini_tB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.maya_dir_LB.setText(QCoreApplication.translate("Dialog", u"Maya: ", None))
        self.maya_tB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.nuke_dir_LB.setText(QCoreApplication.translate("Dialog", u"Nuke:  ", None))
        self.nuke_tB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.unreal_dir_LB.setText(QCoreApplication.translate("Dialog", u"Unreal: ", None))
        self.unreal_tB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.discord_dir_LB.setText(QCoreApplication.translate("Dialog", u"Discord: ", None))
        self.discord_tB.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Add Custom Softwares:", None))
        self.custom_tB_1.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.custom_tB_3.setText(QCoreApplication.translate("Dialog", u"...", None))
    # retranslateUi


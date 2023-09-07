# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crowd_preview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Crowd_Browser(object):
    def setupUi(self, Crowd_Browser):
        if not Crowd_Browser.objectName():
            Crowd_Browser.setObjectName(u"Crowd_Browser")
        Crowd_Browser.resize(749, 640)
        self.gridLayout_2 = QGridLayout(Crowd_Browser)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Crowd_Browser)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.agent_LB = QLabel(self.frame)
        self.agent_LB.setObjectName(u"agent_LB")

        self.horizontalLayout.addWidget(self.agent_LB)

        self.agent_CB = QComboBox(self.frame)
        self.agent_CB.addItem("")
        self.agent_CB.setObjectName(u"agent_CB")

        self.horizontalLayout.addWidget(self.agent_CB)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.props_LB = QLabel(self.frame)
        self.props_LB.setObjectName(u"props_LB")

        self.horizontalLayout_2.addWidget(self.props_LB)

        self.props_CB = QComboBox(self.frame)
        self.props_CB.addItem("")
        self.props_CB.setObjectName(u"props_CB")

        self.horizontalLayout_2.addWidget(self.props_CB)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clips_LB = QLabel(self.frame)
        self.clips_LB.setObjectName(u"clips_LB")

        self.horizontalLayout_3.addWidget(self.clips_LB)

        self.clips_CB = QComboBox(self.frame)
        self.clips_CB.addItem("")
        self.clips_CB.setObjectName(u"clips_CB")

        self.horizontalLayout_3.addWidget(self.clips_CB)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.clip_preview_WD = QWidget(Crowd_Browser)
        self.clip_preview_WD.setObjectName(u"clip_preview_WD")

        self.horizontalLayout_5.addWidget(self.clip_preview_WD)

        self.clip_scroll = QScrollBar(Crowd_Browser)
        self.clip_scroll.setObjectName(u"clip_scroll")
        self.clip_scroll.setOrientation(Qt.Vertical)

        self.horizontalLayout_5.addWidget(self.clip_scroll)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.frame_2 = QFrame(Crowd_Browser)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 51))
        self.frame_2.setMaximumSize(QSize(16777215, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gernerate_preview_PB = QPushButton(self.frame_2)
        self.gernerate_preview_PB.setObjectName(u"gernerate_preview_PB")

        self.horizontalLayout_4.addWidget(self.gernerate_preview_PB)

        self.Import_selected_PB = QPushButton(self.frame_2)
        self.Import_selected_PB.setObjectName(u"Import_selected_PB")

        self.horizontalLayout_4.addWidget(self.Import_selected_PB)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 1)


        self.retranslateUi(Crowd_Browser)

        QMetaObject.connectSlotsByName(Crowd_Browser)
    # setupUi

    def retranslateUi(self, Crowd_Browser):
        Crowd_Browser.setWindowTitle(QCoreApplication.translate("Crowd_Browser", u"Glacier Tools - Crowd Browser", None))
        self.agent_LB.setText(QCoreApplication.translate("Crowd_Browser", u"Agents :", None))
        self.agent_CB.setItemText(0, QCoreApplication.translate("Crowd_Browser", u"None", None))

        self.props_LB.setText(QCoreApplication.translate("Crowd_Browser", u"Props :", None))
        self.props_CB.setItemText(0, QCoreApplication.translate("Crowd_Browser", u"None", None))

        self.clips_LB.setText(QCoreApplication.translate("Crowd_Browser", u"Clips Pack :", None))
        self.clips_CB.setItemText(0, QCoreApplication.translate("Crowd_Browser", u"None", None))

        self.gernerate_preview_PB.setText(QCoreApplication.translate("Crowd_Browser", u"Generate Preview", None))
        self.Import_selected_PB.setText(QCoreApplication.translate("Crowd_Browser", u"Import Selected", None))
    # retranslateUi


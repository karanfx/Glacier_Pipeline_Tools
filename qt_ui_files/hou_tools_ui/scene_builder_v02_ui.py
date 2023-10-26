# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scene_builder_v02.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dependencies_LB = QLabel(Form)
        self.dependencies_LB.setObjectName(u"dependencies_LB")

        self.gridLayout.addWidget(self.dependencies_LB, 0, 0, 1, 1)

        self.assets_TW = QTreeWidget(Form)
        self.assets_TW.headerItem().setText(0, "")
        self.assets_TW.setObjectName(u"assets_TW")

        self.gridLayout.addWidget(self.assets_TW, 1, 0, 1, 1)

        self.Build_PB = QPushButton(Form)
        self.Build_PB.setObjectName(u"Build_PB")

        self.gridLayout.addWidget(self.Build_PB, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dependencies_LB.setText(QCoreApplication.translate("Form", u"Dependencies:", None))
        self.Build_PB.setText(QCoreApplication.translate("Form", u"Build Scene", None))
    # retranslateUi


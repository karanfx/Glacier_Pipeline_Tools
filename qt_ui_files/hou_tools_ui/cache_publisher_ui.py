# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cache_publisher.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QToolButton, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_publisher_QW(object):
    def setupUi(self, publisher_QW):
        if not publisher_QW.objectName():
            publisher_QW.setObjectName(u"publisher_QW")
        publisher_QW.resize(519, 451)
        self.gridLayout = QGridLayout(publisher_QW)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vers_name_LB = QLabel(publisher_QW)
        self.vers_name_LB.setObjectName(u"vers_name_LB")

        self.gridLayout.addWidget(self.vers_name_LB, 0, 0, 1, 1)

        self.vers_name_LE = QLineEdit(publisher_QW)
        self.vers_name_LE.setObjectName(u"vers_name_LE")

        self.gridLayout.addWidget(self.vers_name_LE, 0, 1, 1, 1)

        self.vers_path_LB = QLabel(publisher_QW)
        self.vers_path_LB.setObjectName(u"vers_path_LB")

        self.gridLayout.addWidget(self.vers_path_LB, 1, 0, 1, 1)

        self.vers_path_LE = QLineEdit(publisher_QW)
        self.vers_path_LE.setObjectName(u"vers_path_LE")

        self.gridLayout.addWidget(self.vers_path_LE, 1, 1, 1, 1)

        self.cache_tree_TW = QTreeWidget(publisher_QW)
        self.cache_tree_TW.setObjectName(u"cache_tree_TW")

        self.gridLayout.addWidget(self.cache_tree_TW, 2, 0, 1, 4)

        self.notes_LB = QLabel(publisher_QW)
        self.notes_LB.setObjectName(u"notes_LB")

        self.gridLayout.addWidget(self.notes_LB, 3, 0, 1, 1)

        self.notes_TE = QTextEdit(publisher_QW)
        self.notes_TE.setObjectName(u"notes_TE")

        self.gridLayout.addWidget(self.notes_TE, 4, 0, 1, 4)

        self.publish_PB = QPushButton(publisher_QW)
        self.publish_PB.setObjectName(u"publish_PB")
        self.publish_PB.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.publish_PB, 5, 3, 1, 1)

        self.vers_path_TB = QToolButton(publisher_QW)
        self.vers_path_TB.setObjectName(u"vers_path_TB")

        self.gridLayout.addWidget(self.vers_path_TB, 1, 3, 1, 1)


        self.retranslateUi(publisher_QW)

        QMetaObject.connectSlotsByName(publisher_QW)
    # setupUi

    def retranslateUi(self, publisher_QW):
        publisher_QW.setWindowTitle(QCoreApplication.translate("publisher_QW", u"Form", None))
        self.vers_name_LB.setText(QCoreApplication.translate("publisher_QW", u"Version Name :", None))
        self.vers_path_LB.setText(QCoreApplication.translate("publisher_QW", u"Version Path :", None))
        ___qtreewidgetitem = self.cache_tree_TW.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("publisher_QW", u"Path", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("publisher_QW", u"Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("publisher_QW", u"Cache", None));
        self.notes_LB.setText(QCoreApplication.translate("publisher_QW", u"Notes :", None))
        self.publish_PB.setText(QCoreApplication.translate("publisher_QW", u"Publish", None))
        self.vers_path_TB.setText(QCoreApplication.translate("publisher_QW", u"...", None))
    # retranslateUi


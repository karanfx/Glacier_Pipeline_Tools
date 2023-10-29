# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cache_collector.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_cacheCollector(object):
    def setupUi(self, cacheCollector):
        if not cacheCollector.objectName():
            cacheCollector.setObjectName(u"cacheCollector")
        cacheCollector.resize(574, 473)
        self.gridLayout = QGridLayout(cacheCollector)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cache_data_TW = QTreeWidget(cacheCollector)
        self.cache_data_TW.setObjectName(u"cache_data_TW")

        self.gridLayout.addWidget(self.cache_data_TW, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delete_older_cache_PB = QPushButton(cacheCollector)
        self.delete_older_cache_PB.setObjectName(u"delete_older_cache_PB")
        self.delete_older_cache_PB.setMinimumSize(QSize(0, 31))

        self.horizontalLayout.addWidget(self.delete_older_cache_PB)

        self.collect_all_cache_PB = QPushButton(cacheCollector)
        self.collect_all_cache_PB.setObjectName(u"collect_all_cache_PB")
        self.collect_all_cache_PB.setMinimumSize(QSize(0, 31))

        self.horizontalLayout.addWidget(self.collect_all_cache_PB)

        self.collect_selected_cache_PB = QPushButton(cacheCollector)
        self.collect_selected_cache_PB.setObjectName(u"collect_selected_cache_PB")
        self.collect_selected_cache_PB.setMinimumSize(QSize(0, 31))

        self.horizontalLayout.addWidget(self.collect_selected_cache_PB)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(cacheCollector)

        QMetaObject.connectSlotsByName(cacheCollector)
    # setupUi

    def retranslateUi(self, cacheCollector):
        cacheCollector.setWindowTitle(QCoreApplication.translate("cacheCollector", u"Form", None))
        ___qtreewidgetitem = self.cache_data_TW.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("cacheCollector", u"Cache Path", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("cacheCollector", u"File Count", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("cacheCollector", u"Cache Node", None));
        self.delete_older_cache_PB.setText(QCoreApplication.translate("cacheCollector", u"Only Keep Current Version", None))
        self.collect_all_cache_PB.setText(QCoreApplication.translate("cacheCollector", u"Collect All Caches", None))
        self.collect_selected_cache_PB.setText(QCoreApplication.translate("cacheCollector", u"Collect Selected Caches", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_3_treeWid.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolButton, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(565, 707)
        MainWindow.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.action_Create_Project = QAction(MainWindow)
        self.action_Create_Project.setObjectName(u"action_Create_Project")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Add_Apps = QAction(MainWindow)
        self.action_Add_Apps.setObjectName(u"action_Add_Apps")
        self.actionDoc = QAction(MainWindow)
        self.actionDoc.setObjectName(u"actionDoc")
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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.subir_lB = QLabel(self.frame)
        self.subir_lB.setObjectName(u"subir_lB")

        self.horizontalLayout_3.addWidget(self.subir_lB)

        self.subdir_cB = QComboBox(self.frame)
        self.subdir_cB.setObjectName(u"subdir_cB")

        self.horizontalLayout_3.addWidget(self.subdir_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.project_lB = QLabel(self.frame)
        self.project_lB.setObjectName(u"project_lB")

        self.gridLayout_2.addWidget(self.project_lB, 0, 0, 1, 1)

        self.project_cB = QComboBox(self.frame)
        self.project_cB.setObjectName(u"project_cB")

        self.gridLayout_2.addWidget(self.project_cB, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shot_lB = QLabel(self.frame)
        self.shot_lB.setObjectName(u"shot_lB")

        self.horizontalLayout.addWidget(self.shot_lB)

        self.shot_cB = QComboBox(self.frame)
        self.shot_cB.setObjectName(u"shot_cB")

        self.horizontalLayout.addWidget(self.shot_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.launch_button = QPushButton(self.frame)
        self.launch_button.setObjectName(u"launch_button")

        self.gridLayout_3.addWidget(self.launch_button, 8, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.User_lB = QLabel(self.frame)
        self.User_lB.setObjectName(u"User_lB")

        self.horizontalLayout_2.addWidget(self.User_lB)

        self.manual_path_Ldit = QLineEdit(self.frame)
        self.manual_path_Ldit.setObjectName(u"manual_path_Ldit")

        self.horizontalLayout_2.addWidget(self.manual_path_Ldit)

        self.manual_toolButton = QToolButton(self.frame)
        self.manual_toolButton.setObjectName(u"manual_toolButton")

        self.horizontalLayout_2.addWidget(self.manual_toolButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tools_lB = QLabel(self.frame)
        self.tools_lB.setObjectName(u"tools_lB")

        self.horizontalLayout_4.addWidget(self.tools_lB)

        self.tools_cB = QComboBox(self.frame)
        self.tools_cB.setObjectName(u"tools_cB")

        self.horizontalLayout_4.addWidget(self.tools_cB)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)

        self.dir_tree_widget = QTreeWidget(self.frame)
        QTreeWidgetItem(self.dir_tree_widget)
        QTreeWidgetItem(self.dir_tree_widget)
        self.dir_tree_widget.setObjectName(u"dir_tree_widget")

        self.gridLayout_3.addWidget(self.dir_tree_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 565, 21))
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
        self.menuMode.addAction(self.action_Create_Project)
        self.menuMode.addAction(self.action_Add_Apps)
        self.menuMode.addAction(self.action_Exit)
        self.menuHelp.addAction(self.actionDoc)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Create_Project.setText(QCoreApplication.translate("MainWindow", u"Create Project", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_Add_Apps.setText(QCoreApplication.translate("MainWindow", u"Add Apps", None))
        self.actionDoc.setText(QCoreApplication.translate("MainWindow", u"Doc", None))
        self.subir_lB.setText(QCoreApplication.translate("MainWindow", u"Sub Dir : ", None))
        self.project_lB.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.shot_lB.setText(QCoreApplication.translate("MainWindow", u"Shot :", None))
        self.launch_button.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.User_lB.setText(QCoreApplication.translate("MainWindow", u"Manual path:", None))
        self.manual_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tools_lB.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        ___qtreewidgetitem = self.dir_tree_widget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.dir_tree_widget.isSortingEnabled()
        self.dir_tree_widget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.dir_tree_widget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem2 = self.dir_tree_widget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        self.dir_tree_widget.setSortingEnabled(__sortingEnabled)

        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


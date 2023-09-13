#to connect maya with vscode - Copy paste below code to MEL Script Editor
# commandPort -name "localhost:7001" -sourceType "mel" -echoOutput;


# import maya.cmds as cmds
# dialog = cmds.loadUI(uiFile='E:\Work\python_dev\QT_project_launcher\qt_ui_files\hou_tools_ui\scene_builder.ui')
# cmds.showWindow(dialog)

layout = "E:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001/layout/"


uiFile = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/hou_tools_ui/scene_builder.ui"

# import maya.cmds as cmds
from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui 

import os
from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 

class scene_builder(QWidget):
   
    def __init__(self):
        super(scene_builder, self).__init__()
        self.ui = cmds.loadUI(uiFile='E:\Work\python_dev\QT_project_launcher\qt_ui_files\hou_tools_ui\scene_builder.ui')

        # self.ui = QtUiTools.QUiLoader().load(uiFile,parentWidget=self)
        self.setParent(mayaMainWindow)
        
        #add logo and window name
        self.setWindowTitle("Glacier Apps - Scene Builder")
        self.setWindowIcon(QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))

        # self.populate_assets()
        # self.ui.Build_PB.clicked.connect(self.build)

    # def populate_assets(self):
    #     for sub in os.listdir(layout):
    #         # dirs = os.path.join(layout,sub)
    #         # print(dirs)
    #         item = QListWidgetItem(sub)
    #         item.setCheckState(Qt.Unchecked)
        
    #         self.ui.assets_LW.addItem(item)
    #     self.ui.assets_LW.setDragDropMode(self.ui.assets_LW.InternalMove)
    #     self.ui.assets_LW.selectAll()

    # def build(self):
    #     print("build")
    #     checked = []
    #     for index in range(self.ui.assets_LW.count()):
    #         item = self.ui.assets_LW.item(index)
    #         if item.checkState() == 2:
    #             checked.append(item.text())

    #     print(checked)

    #     for sub in os.listdir(layout):
    #         for item in checked:
    #             if item == sub:
    #                 dirs = os.path.join(layout,sub)
    #                 print(dirs)
    #                 for asset in os.listdir(dirs):
    #                     asset_dirs = os.path.join(dirs,asset)
    #                     ext = os.path.splitext(asset_dirs)[1]
    #                     name = os.path.basename(asset_dirs).replace(ext,"")
    #                     # print(name)

    #                     #call imports
    #                     # import_alembic(asset_dirs)
    #                     # import_fbx(asset_dirs)
    #                     # import_usd(asset_dirs)
    #                     print(asset_dirs)

win = scene_builder()
win.show()
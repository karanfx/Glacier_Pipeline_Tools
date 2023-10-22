#Setup Env Variables 
#Setup Imports using env variables




from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui 

from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools
import os

from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 

uiFile = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/hou_tools_ui/scene_builder.ui"

layout = "E:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001/layout/"


class BuildScene(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(BuildScene, self).__init__(*args, **kwargs)
        
        self.ui = QtUiTools.QUiLoader().load(uiFile,parentWidget=self)
        self.setParent(mayaMainWindow,QtCore.Qt.Window)
        
        #Parent widget under Maya main window        
        #self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        #add logo and window name
        self.setWindowTitle("Glacier Apps - Scene Builder")
        self.setWindowIcon(QtGui.QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))

        self.populate_assets()
        self.ui.Build_PB.clicked.connect(self.build)

    def populate_assets(self):
        #get layout Dirs
        #shot_dir = os.environ.get('SHOT_DIR')
        #layout = os.path.join(shot_dir,'libs/layout')
        #anim = os.path.join(shot_dir,'libs/anim')
        # print(layout)

        for sub in os.listdir(layout):
            # dirs = os.path.join(layout,sub)
            # print(dirs)
            item = QtWidgets.QListWidgetItem(sub)
            item.setCheckState(QtCore.Qt.Unchecked)
        
            self.ui.assets_LW.addItem(item)
        self.ui.assets_LW.setDragDropMode(self.ui.assets_LW.InternalMove)
        self.ui.assets_LW.selectAll()

    def get_layout_dirs(self):
        shot_dir = os.environ.get('SHOT_DIR')
        layout = os.path.join(shot_dir,'libs','layout')
        anim = os.path.join(shot_dir,'libs','anim')
        print(layout)


    def build(self):
        # print("build")
        #get layout Dirs
        shot_dir = os.environ.get('SHOT_DIR')
        # print(shot_dir)
        layout = os.path.join(shot_dir,'libs','layout')
        anim = os.path.join(shot_dir,'libs','anim')
        # print(layout)

        checked = []
        for index in range(self.ui.assets_LW.count()):
            item = self.ui.assets_LW.item(index)
            if item.checkState() == 2:
                checked.append(item.text())

        # print(checked)

        for sub in os.listdir(layout):
            for item in checked:
                if item == sub:
                    print('item',sub)
                    dirs = os.path.join(layout,sub)
                    print('dirs',dirs)
                    # for asset in os.listdir(dirs):
                    #    asset_dirs = os.path.join(dirs,asset)
                    asset_dirs = dirs
                    ext = os.path.splitext(asset_dirs)[1]
                    name = os.path.basename(asset_dirs).replace(ext,"")
                    print('name',name)
                    print('asset_dir',asset_dirs)

                    #call imports
                    cmds.file(asset_dirs, i=True, type="FBX", ra=True, mergeNamespacesOnClash=False, namespace="FBXImport", options="v=0;", pr=True)


        #Setup Frame Range 
        

        
        
        
win = BuildScene()
win.show()
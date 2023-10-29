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

uiFile = "E:/Work/python_dev/Glacier_pipeline_tools/project_glacier/qt_ui_files/hou_tools_ui/scene_builder.ui"
glacier_icon = "E:/Work/python_dev/Glacier_pipeline_tools/project_glacier/bin/logo/favicon_sq_small.png"

# get layout Dirs
shot_dir = os.environ.get('SHOT_DIR')
shot_dir = shot_dir.strip('\"')
layout = os.path.join(shot_dir,'libs','layout')
anim = os.path.join(shot_dir,'libs/anim')


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
        self.setWindowIcon(QtGui.QIcon(glacier_icon))

        self.populate_assets()
        self.ui.Build_PB.clicked.connect(self.build)

    def populate_assets(self):

        for sub in os.listdir(layout):
            # dirs = os.path.join(layout,sub)
            # print(dirs)
            item = QtWidgets.QListWidgetItem(sub)
            item.setCheckState(QtCore.Qt.Unchecked)
        
            self.ui.assets_LW.addItem(item)
        self.ui.assets_LW.setDragDropMode(self.ui.assets_LW.InternalMove)
        self.ui.assets_LW.selectAll()


    def build(self):
        
        checked = []
        for index in range(self.ui.assets_LW.count()):
            item = self.ui.assets_LW.item(index)
            if item.checkState() == 2:
                checked.append(item.text())

        for sub in os.listdir(layout):
            for item in checked:
                if item == sub:
                    dirs = os.path.join(layout,sub)
                    asset_dirs = dirs
                    ext = os.path.splitext(asset_dirs)[1]
                    name = os.path.basename(asset_dirs).replace(ext,"")

                    #Call imports
                    # Import the ABC file
                    if ext == '.abc':
                        cmds.AbcImport(asset_dirs, mode='import')

                    # Import the OBJ file
                    if ext == '.obj':
                        cmds.file(asset_dirs, i=True, type="OBJ", ra=True, mergeNamespacesOnClash=False, namespace="OBJImport", options="mo=1;")

                    # Import the FBX file
                    if ext == '.fbx':
                        cmds.file(asset_dirs, i=True, type="FBX", ra=True, mergeNamespacesOnClash=False, namespace="FBXImport", options="v=0;", pr=True)

                    # Import the USD stage into Maya
                    if ext == '.usd':
                        from pxr import Usd, UsdGeom

                        # Initialize the USD stage
                        stage = Usd.Stage.Open(asset_dirs)
                        namespace = "USDImport"
                        cmds.usdImport(file=asset_dirs, shadingMode="none", primPath="/", mergeTransformAndShape=False, applyLayerOffset=False, name=namespace, asReference=False)

                    # print(asset_dirs)

        #Setup Frame Range 
        start_frame = os.environ.get('G_START')
        start_frame = int(start_frame.strip('\"'))
        print(start_frame)

        end_frame = os.environ.get('G_END')
        end_frame = int(end_frame.strip('\"'))
        print(end_frame)

        
        cmds.playbackOptions(edit=True,animationStartTime = start_frame)
        cmds.playbackOptions(edit=True,animationEndTime = end_frame)
        
        cmds.playbackOptions(edit=True,minTime = start_frame)
        cmds.playbackOptions(edit=True,maxTime = end_frame)
        
        
win = BuildScene()
win.show()
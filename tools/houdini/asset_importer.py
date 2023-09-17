from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide2.QtGui import QIcon, QPixmap

import os
import hou

def import_fbx(dir):
    ext = os.path.splitext(dir)[1]
    ext = os.path.splitext(dir)[1]
    name = os.path.basename(dir).replace(ext,"")
    if ext == ".fbx":
        fbx_dirs = []
        subnet = hou.hipFile.importFBX(file_name=dir, import_geometry=True)
        # print(subnet)
    else:
        pass
    
def import_alembic(dir):
    ext = os.path.splitext(dir)[1]
    name = os.path.basename(dir).replace(ext,"")
    ext = os.path.splitext(dir)[1]
    if ext == ".abc":
        obj = hou.node("obj/")
        target_node = obj.createNode("geo",name)

        alembic_sop = target_node.createNode("alembic",name)
        alembic_sop.parm("fileName").set(dir)
        alembic_sop.cook()
    else:
        pass

def import_usd(dir):
    ext = os.path.splitext(dir)[1]
    name = os.path.basename(dir).replace(ext,"")
    if ext == ".fbx":
        obj = hou.node("stage/")
        sop_import = obj.createNode("sopimport",name)
        sop_import.parm("savepath").set(dir)
        sop_import.cook()
    else:
        pass


# layout = "E:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001/layout/"

uiFile = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/hou_tools_ui/scene_builder.ui"

class scene_builder(QtWidgets.QWidget):
    """ Browser preview quicktimes of fbxs
    """
    def __init__(self):
        super(scene_builder, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(uiFile,parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(),QtCore.Qt.Window)
        
        #add logo and window name
        self.setWindowTitle("Glacier Apps - Scene Builder")
        self.setWindowIcon(QtGui.QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))

        self.populate_assets()
        self.ui.Build_PB.clicked.connect(self.build)

    def populate_assets(self):
        #get layout Dirs
        shot_dir = os.environ.get('SHOT_DIR')
        layout = os.path.join(shot_dir,'libs/layout')
        anim = os.path.join(shot_dir,'libs/anim')
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
        layout = os.path.join(shot_dir,'libs/layout')
        anim = os.path.join(shot_dir,'libs/anim')
        print(layout)


    def build(self):
        print("build")
        #get layout Dirs
        shot_dir = os.environ.get('SHOT_DIR')
        layout = os.path.join(shot_dir,'libs/layout')
        anim = os.path.join(shot_dir,'libs/anim')
        print(layout)

        checked = []
        for index in range(self.ui.assets_LW.count()):
            item = self.ui.assets_LW.item(index)
            if item.checkState() == 2:
                checked.append(item.text())

        print(checked)

        for sub in os.listdir(layout):
            for item in checked:
                if item == sub:
                    dirs = os.path.join(layout,sub)
                    print(dirs)
                    for asset in os.listdir(dirs):
                        asset_dirs = os.path.join(dirs,asset)
                        ext = os.path.splitext(asset_dirs)[1]
                        name = os.path.basename(asset_dirs).replace(ext,"")
                        print(name)

                        #call imports
                        import_alembic(asset_dirs)
                        import_fbx(asset_dirs)
                        import_usd(asset_dirs)
                        print(asset_dirs)

        #Setup Frame Range 
        start_frame = int(os.environ.get('G_START'))
        end_frame = int(os.environ.get('G_END'))
        hou.playbar.setFrameRange(start_frame, end_frame)
        hou.playbar.setPlaybackRange(start_frame, end_frame)
        hou.setFrame(start_frame)

win = scene_builder()
win.show()
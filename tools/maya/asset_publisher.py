from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui 

import os
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 

#Get Shot data
shot_dir = os.environ.get('SHOT_DIR')
task = os.environ.get('TASK')
shot_name = os.environ.get('SHOT')


#converting image seq into video
def seq_converter(ffmpeg_path,input_seq,output_dir):
    import subprocess
    ffmpeg_command = [
        ffmpeg_path,
        "-framerate", "24",
        "-i", input_seq,
        "-c:v", "libx264",
        "-vf", "fps=24",
        output_dir
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        # print("Image sequence converted to video successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)

# def save_backup_hip(vers_dir):
#     #Save backup file
#     hip_file = hou.hipFile.name()

#     hip_bak_dir = os.path.join(vers_dir,"hip")
#     os.mkdir(hip_bak_dir)
#     # print(hip_bak_dir)

#     hip_bak_file = os.path.join(hip_bak_dir,(shot_name + "_"+ task + ".hip"))
#     hou.hipFile.save(file_name=hip_bak_file)

#     #Load back current scene
#     hou.hipFile.load(file_name=hip_file)

def file_count(cache_path):
    cache_folder = os.path.dirname(cache_path)
    if os.path.exists(cache_folder):
        count = len(os.listdir(cache_folder))
        return count

#Auto version up
def version_up(version_dir):
    versions = os.listdir(version_dir)

    if versions:
        max_v = str(max(versions))
        max_v = int(max_v.strip('v'))

        max_v += 1
        vers_up = "v{:03d}".format(max_v)
    else:
        vers_up = "v001"

    output_dir = os.path.join(version_dir,vers_up)

    return output_dir



uiFile = "E:\Work\python_dev\QT_project_launcher\qt_ui_files\maya_tools_ui\cache_publisher.ui"

class publish_version(QWidget):
    """ Browser preview quicktimes of fbxs
    """
    def __init__(self):
        super(publish_version, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(uiFile,parentWidget=self)
        self.setParent(mayaMainWindow,QtCore.Qt.Window)
        
        self.setWindowFlags(Qt.Window)   

        #add logo and window name
        self.setWindowTitle("Glacier Tools - Publisher")
        self.setWindowIcon(QtGui.QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))

        self.populate_caches()
        self.ui.publish_PB.clicked.connect(self.publish)

        #Get Flipbook Path
        self.ui.vers_path_TB.clicked.connect(self.manual_dir)


    def populate_caches(self):        
        selected_object = cmds.ls(selection=True)
        #print(selected_object)
           
        for object in selected_object:                                  
            # Add items in tree widget
            item = QtWidgets.QTreeWidgetItem([object])
            item.setCheckState(0,QtCore.Qt.Unchecked)
            self.ui.cache_tree_TW.addTopLevelItem(item)

    def manual_dir(self):
        man_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if man_path:
            self.ui.vers_path_LE.setText(man_path)

        if not man_path:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, pick the path")
      
    def publish(self):
        #Publish Data
        vers_name = self.ui.vers_name_LE.text()
        seq_input = self.ui.vers_path_LE.text()
        notes = self.ui.notes_TE.toPlainText()

        #Convert the immage seq using ffmpeg and rename it using version name
        
        #get the last version and make a increment version 
        publish_dir = os.path.join(shot_dir,"libs",task)

        # #Auto version up
        # versions = os.listdir(publish_dir)

        # if versions:
        #     max_v = str(max(versions))
        #     max_v = int(max_v.strip('v')) +1
        #     vers_up = f"v{max_v:03d}"
        # else:
        #     vers_up = "v001"

        # output_dir = os.path.join(publish_dir,vers_up)

        output_dir = version_up(publish_dir)

        # print(output_dir)
        os.makedirs(output_dir,exist_ok=True)

        # #Save backup file
        # save_backup_hip(output_dir)

        #Creating Video version
        vid_out = os.path.join(output_dir,(vers_name + ".mp4"))
        # print(vid_out)
        seq_converter("ffmpeg",seq_input,vid_out)
    

        #copy notes in .txt file
        note_path = os.path.join(output_dir,(vers_name + ".txt"))

        #Get Current tine
        from datetime import datetime as time
        t = time.now()
        cur_time  = str(t.strftime("%Y-%m-%d  %H:%M:%S"))

        with open(note_path,'w') as note:
            note.write(vers_name + "\n" + cur_time + "\n" + notes)


        #copy cache to libs / create entry on SG
        cache_path = os.path.join(output_dir,"data")

        root_item = self.ui.cache_tree_TW.invisibleRootItem()

        for i in range(root_item.childCount()):
            item = root_item.child(i)
            if item.checkState(0) == QtCore.Qt.Checked:
                cache_name = item.text(0)
                cache_dir = item.text(3)
                cache_out_path = os.path.join(cache_path,cache_name)
                os.makedirs(cache_path,exist_ok=True)

                cache_dir = os.path.dirname(cache_dir)
                # print(cache_dir,cache_out_path)
                import shutil
                # for cache_file in os.listdir(cache_out_path):
                shutil.copytree(cache_dir,cache_out_path)

        
        print("Published")
        # hou.ui.displayMessage("Published Successfully",title = "Glacier Publisher")

            


win = publish_version()
win.show()
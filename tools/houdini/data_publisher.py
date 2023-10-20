from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide2.QtGui import QIcon, QPixmap

import os
import hou

# layout = "E:/Work/houdinifx/pipe_test/Show01/Seq_AB/Shot_AB001/layout/"
#get layout Dirs
shot_dir = os.environ.get('SHOT_DIR')
task = os.environ.get('TASK')

#converting image seq into video
def seq_converter(ffmpeg_path,input_seq,output_dir):
    import subprocess
    ffmpeg_command = [
        "ffmpeg",
        "-framerate", "24",
        "-i", input_seq,
        "-c:v", "libx264",
        "-vf", "fps=24",
        output_dir
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Image sequence converted to video successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)


uiFile = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/hou_tools_ui/cache_publisher.ui"

class publish_version(QtWidgets.QWidget):
    """ Browser preview quicktimes of fbxs
    """
    def __init__(self):
        super(publish_version, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(uiFile,parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(),QtCore.Qt.Window)
        
        #add logo and window name
        self.setWindowTitle("Glacier Tools - Publisher")
        self.setWindowIcon(QtGui.QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))

        self.populate_caches()
        self.ui.publish_PB.clicked.connect(self.publish)

        # cur_shot = os.environ("SHOT")
        # self.ui.task_LB.setText()

    def populate_caches(self):
        obj = hou.node("/obj")
        children = obj.allSubChildren()
        
        for child in children:

            if child.type().name() == "filecache":
                cache_path = child.parm("file").eval()
                # cache_folder = os.path.dirname(cache_path)
                    
                c,cache_type = os.path.splitext(cache_path)
                     
                #List for Tree Wid
                cache_item = [child.name(),str(cache_type),cache_path]
               
                # Add items in tree widget
                item = QtWidgets.QTreeWidgetItem(list(cache_item))
                item.setCheckState(0,QtCore.Qt.Unchecked)
                self.ui.cache_tree_TW.addTopLevelItem(item)
        
    def publish(self):
        #Publish Data
        vers_name = self.ui.vers_name_LE.text()
        vers_path = self.ui.vers_path_LE.text()
        notes = self.ui.notes_TE.toPlainText()

        #Convert the immage seq using ffmpeg and rename it using version name
        seq_input = vers_path
        vers = "v003"
        output_dir = os.path.join(shot_dir,"libs",task,vers)
        os.makedirs(output_dir,exist_ok=True)

        # #Creating Video version
        # vid_out = os.path.join(output_dir,(vers_name + ".mp4"))
        # print(vid_out)
        # seq_converter("ffmpeg",seq_input,vid_out)
    

        # #copy notes in .txt file
        # note_path = os.path.join(output_dir,(vers_name + ".txt"))
        # with open(note_path,'w') as note:
        #     note.write(vers_name + "\n" + notes)


        #copy cache to libs / create entry on SG
        cache_path = os.path.join(output_dir,"data")

        root_item = self.ui.cache_tree_TW.invisibleRootItem()

        for i in range(root_item.childCount()):
            item = root_item.child(i)
            if item.checkState(0) == QtCore.Qt.Checked:
                cache_name = item.text(0)
                cache_dir = item.text(2)
                cache_out_path = os.path.join(cache_path,cache_name)
                # os.makedirs(cache_path,exist_ok=True)

                cache_dir = os.path.dirname(cache_dir)
                print(cache_dir,cache_out_path)
                import shutil
                shutil.copytree(cache_dir,cache_path)

        # path = "SHOT_DIR/libs/FX/version_name/v001/data"
        
        print("Published")
        
    def access(self):
        root_item = self.ui.cache_tree_TW.invisibleRootItem()

        for i in range(root_item.childCount()):
            item = root_item.child(i)
            if item.checkState(0) == QtCore.Qt.Checked:
                # print(item)
                cache_name = item.text(0)
                cache_dir = item.text(2)
            


win = publish_version()
win.show()
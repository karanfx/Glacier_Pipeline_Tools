
#THIS NEED TO BE IMPLEMENTED INTO SETUP WIZARD

#setting up studio and dcc directories
from PySide6 import QtWidgets 
import PySide6.QtGui
import PySide6.QtCore
import os
import json
import qdarkstyle

import ui.setup_dirs_ui


#Create Project Dialog 
class setup_dailog(ui.setup_dirs_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(setup_dailog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier - Setup Directories")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        #set darkmode
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))

        
        self.Save_Bbox.accepted.connect(self.save_dirs)

        #Set toolButtons
        self.studio_dir_TB.clicked.connect(self.pick_studio_path)
        self.houdini_tB.clicked.connect(self.pick_houdini_path)
        self.nuke_tB.clicked.connect(self.pick_nuke_path)
        self.maya_tB.clicked.connect(self.pick_maya_path)
        self.discord_tB.clicked.connect(self.pick_discord_path)
        self.unreal_tB.clicked.connect(self.pick_unreal_path)

        
    def save_dirs(self):
        studio_dir = self.studio_dir_LE.text()
        user = self.user_LE.text()
        userdata = {'studiodir':studio_dir,'user':user}

        houdiniDir = self.houdini_dir_LE.text()
        mayaDir = self.maya_dir_LE.text()
        nukeDir = self.nukedir_LE.text()
        unrealDir = self.unreal_dir_LE.text()
        discordDir = self.discord_dir_LE.text()

        tool_dirs = {'Houdini':houdiniDir,'Maya':mayaDir,'Nuke':nukeDir,'Unreal':unrealDir,'Discord':discordDir}

        data = {'User_Data' : userdata,'tools':tool_dirs}

        print(userdata)
        print(tool_dirs)
        user_file = "/bin/data/user.json"

        
        # file_path = os.path.abspath(__file__)
        # pro_dir = os.path.dirname(file_path)
        # # pro_dir = os.path.dirname(pro_dir)
        # json_path = os.path.join(pro_dir,user_file)
        # print(json_path)

        json_path = "D:/Work/python_dev/QT_project_launcher/bin/data/user.json"

        with open(json_path,"w") as uf:
            json.dump(data,uf)



    def pick_studio_path(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.studio_dir_LE.setText(man_path)
        else:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, Pick the path")

    def pick_houdini_path(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.houdini_dir_LE.setText(man_path)
        else:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, Pick the path")

    def pick_maya_path(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.maya_dir_LE.setText(man_path)
        else:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, Pick the path")
   
    def pick_nuke_path(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.nukedir_LE.setText(man_path)
        else:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, Pick the path")

    def pick_unreal_path(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.unreal_dir_LE.setText(man_path)
        else:
            QtWidgets.QMessageBox.about(self,"path Required","Please, Pick the path")

    def pick_discord_path(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.discord_dir_LE.setText(man_path)
        else:
            QtWidgets.QMessageBox.about(self,"path Required","Please, Pick the path")

# if __name__ == '__main__':
#     app = QtWidgets.QDialog()
#     appLaunch = setup_dailog()
#     appLaunch.show()
#     app.exec()
from PySide6 import QtWidgets
import PySide6.QtGui
import qdarkstyle
import os
import json

import ui.create_project_ui

#Create Project Dialog 
class local_proj_dialog(ui.create_project_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(local_proj_dialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier App Launcher - Create Project")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        #set darkmode
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))

        self.Project_TB.clicked.connect(self.manual_dir)
        self.Seq_TB.clicked.connect(self.manual_dir)
        self.Shot_TB.clicked.connect(self.manual_dir)
        self.create_buttons.accepted.connect(self.create_pro_dirs)
        

    def manual_dir(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        
        if man_path:
            self.project_LE.setText(man_path)
            
        if not man_path:
            QtWidgets.QMessageBox.about(self,"path Required","Please, pick the path")

    def create_pro_dirs(self):
        prodir = self.project_LE.text()
        seqdir = self.Seq_LE.text()
        shotdir = self.Shot_LE.text()
        shot_subdirs = ['houdini','nuke']
        dcc_subdir = ['hip','renders','cache']

        prodir.replace('\\','/')
        # os.mkdir(prodir)
        os.mkdir(os.path.join(prodir,seqdir,shotdir))
        mkdir = prodir + '/' +seqdir + '/' + shotdir
        print(mkdir)
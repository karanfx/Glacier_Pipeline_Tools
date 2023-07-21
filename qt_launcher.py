from typing import Optional
from PySide6 import QtWidgets
import os
import json
import qdarkstyle



import PySide6.QtCore
import PySide6.QtWidgets

import main_ui_3_treeWid
import create_project_ui
import add_software_ui


studio_dir = 'D:\Work\houdinifx'
shotdir = ''
toolpicked = ''
tooldir = json.load(open('tools_path.json'))
jsonpath = "softpaths.json"


class qt_launcher(main_ui_3_treeWid.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(qt_launcher,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("App Launcher - Build 1.2.0")
        
        self.toolssetup()
        self.populate_project()
        #self.populate_shot()
        self.project_cB.currentTextChanged.connect(self.populate_shot)
        self.shot_cB.currentTextChanged.connect(self.populate_subdir)
        self.launch_button.clicked.connect(self.opentool)
        self.manual_toolButton.clicked.connect(self.manual_dir)

        self.action_Create_Project.triggered.connect(self.create_project)
        self.action_Add_Apps.triggered.connect(self.addsoft)
        self.action_Exit.triggered.connect(self.close)
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    #set darkmode


        # self.tree_wid()


    def populate_project(self):                                  #populate project dirs
        prodirs = [ name for name in os.listdir(studio_dir) if os.path.isdir(os.path.join(studio_dir, name)) ]
        self.project_cB.addItems(prodirs)

    
    def populate_shot(self):
        sel_pro = self.project_cB.currentText()
        if sel_pro:
            shotdirs = studio_dir + '\\' + sel_pro
            shotdirs = [ name for name in os.listdir(shotdirs) if os.path.isdir(os.path.join(shotdirs, name)) ]
            self.shot_cB.addItems(shotdirs)
        #def select_tools():
    
    def populate_subdir(self):
        sel_pro = self.project_cB.currentText()
        subdir = self.shot_cB.currentText()
        if subdir:
            subdirs = studio_dir + '\\' + sel_pro+'\\'+ subdir
            subdirs = [ name for name in os.listdir(subdirs) if os.path.isdir(os.path.join(subdirs, name)) ]
            self.subdir_cB.addItems(subdirs)

        cur_subdir = self.subdir_cB.currentText()
        self.manual_path_Ldit.setText(os.path.join(studio_dir,sel_pro,subdir,cur_subdir))


    def manual_dir(self):
        man_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if man_path:
            self.manual_path_Ldit.setText(man_path)

        if not man_path:
            QtWidgets.QMessageBox.about(self,"path Required","Please, pick the path")

    def create_project(self):
        
        dlg = dialog()
        dlg.exec()

    def addsoft(self):
        dlg = addsoft()
        dlg.exec()



    def toolssetup(self):
        self.tools_cB.addItems(tooldir)
    
    def opentool(self):
        toolname = self.tools_cB.currentText()
        print(str(toolname))
        os.startfile(tooldir[toolname]) 

    # def tree_wid(self):
    #     self.dir_tree_widget.clear()
    #     data = {"proj A" : ["file A","file B"],
    #             "proj B" : ["file A1","file B1"]}
    #     item = QtWidgets.QTreeWidgetItem(["value"])
    #     self.dir_tree_widget.insertTopLevelItems(0,item)
        
        

    #print("test_test")

#Create Project Dialog 
class dialog(create_project_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(dialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("App Launcher - Create Project")
        self.Project_TB.clicked.connect(self.manual_dir)
        self.Seq_TB.clicked.connect(self.manual_dir)
        self.Shot_TB.clicked.connect(self.manual_dir)
        self.create_buttons.accepted.connect(self.create_pro_dirs)
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    #set darkmode
        

    def manual_dir(self):
        man_path = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Folder')
        #QtWidgets.QFileDialog.getExistingDirectory
        if man_path:
            self.project_LE.setText(man_path)
            # self.Seq_LE.setText(man_path)
            # self.Shot_LE.setText(man_path)
            

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
        #os.mkdir(os.path.join(prodir,seqdir,shotdir))
        mkdir = prodir + '/' +seqdir + '/' + shotdir

        for sub in shot_subdirs:
            for dsub in dcc_subdir:
                os.makedirs(mkdir+'/'+sub+'/'+dsub)








    # def savepath(self):
    #     propath = ['none']
    #     pro_path = self.Shot_LE.text()
    #     #self.Shot_LE.
    #     propath.append(pro_path)
    #     print(pro_path)

# Add Software Dialog

class addsoft(add_software_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(addsoft,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Software")
        self.softpath_TB.clicked.connect(self.getsoft)
        self.reg_buttonBox.accepted.connect(self.add_to_json)
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    #set darkmode

    def getsoft(self):
        softpath,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if softpath:
            self.softpath_LE.setText(softpath)

    def add_to_json(self):
        softname = self.softname_LE.text()
        softpath = self.softpath_LE.text()
        #tooldir = json.load(open('tools_path.json'))
        # Serializing json
        
        #j_soft = "," + softname + ":" + softpath

        # j_soft = {softname:softpath}
        # j_soft.update()

        #json_object['key'] =['object'] 
        #json_object = json.dumps(j_soft, indent=4)  
        with open(jsonpath) as jsonfile:
            j_soft = json.load(jsonfile)

        j_soft['key'] = ['object']
    # Writing to sample.json
        with open(jsonpath, "a") as outfile:
            #json_object = json_object + "," + json_object 
            json.dump(j_soft,outfile)
            #outfile.write(json_object)
           
        # tooldir = json.dumps(softname,softpath)
        #print(json_object)

        

    

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    appLaunch = qt_launcher()
    appLaunch.show()
    app.exec()

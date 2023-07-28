from typing import Optional
from PySide6 import QtWidgets
import os
import json
import qdarkstyle

import PySide6.QtGui
import PySide6.QtCore
import PySide6.QtWidgets

#Import Utils
from utils.google_sheet_api import get_status
from utils.create_project_dirs import create_shot_dirs


#Import UIs
import ui.main_ui_5
import ui.create_project_ui
import ui.add_software_ui
import ui.about_page
import ui.report_form

#required data paths to refer
studio_dir = 'D:\Work\houdinifx\pipe_test'
shotdir = ''
toolpicked = ''
tooldir = json.load(open('bin/data/softpaths.json'))
jsonpath = "bin/data/softpaths.json"
username = "Karan"


class qt_launcher(ui.main_ui_5.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(qt_launcher,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier App Launcher - Build 1.5.0")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        
        # #Add logo Image
        # self.logo_LB.setStyleSheet("background-image :url(bin/logo/logo_title_cropped.png);")
        # pxmap = PySide6.QtGui.QPixmap('bin/logo/logo_title_cropped.png')
        # self.logo_LB.setPixmap(pxmap)
        # self.logo_LB.setScaledContents(True)
        # self.logo_LB.resize(50,10)
    
        
        self.toolssetup()
        self.populate_project()
        self.populate_shot()
        self.project_cB.currentTextChanged.connect(self.populate_shot)
        # self.shot_cB.currentTextChanged.connect(self.populate_subdir)
        self.launch_button.clicked.connect(self.opentool)
        self.manual_toolButton.clicked.connect(self.manual_dir)

        self.action_Create_Project_2.triggered.connect(self.create_project)
        self.action_Add_Apps.triggered.connect(self.addsoft)
        self.action_Exit.triggered.connect(self.close)
        self.actionToggle_Darkmode.triggered.connect(self.toggle_dark)

        #About Page
        self.actionAbout.triggered.connect(self.about_page)

        #Report Form
        self.actionReport.triggered.connect(self.report)

        #Load Tasks From Google Sheets API
        self.populate_status()
        self.reload_task_PB.clicked.connect(self.reload_task)

        self.dir_tree_widget.itemSelectionChanged.connect(self.get_tree_sel)
        # QtWidgets.QTreeWidgetItem.


    #Toggle Dark Mode
    def toggle_dark(self):
        self.setStyleSheet(qdarkstyle.load_stylesheet())

    #Get Data from Sheet
    def populate_status(self):
        self.dir_tree_widget.clear()
        self.dir_tree_widget.setAlternatingRowColors(True)
        
        with open("bin\data\shot_status.json") as f:
            data = json.load(f)
        # print(data)

        #Get Proper Indexes 
        # show_idx = data[0].index('Show')
        # seq_idx = data[0].index('Sequence')
        # shot_idx = data[0].index('Shot')
        # print(show_idx,seq_idx,shot_idx)

        data = data[1:]
        for task in data:
            # Clean List
            
            task.pop(1)
            task.remove(username)
            task.insert(6,task[0])
            task = task[1:]

            # print(list(shot))
            item = QtWidgets.QTreeWidgetItem(list(task))
            self.dir_tree_widget.addTopLevelItem(item)

            #Create Dirs
            create_shot_dirs(studio_dir)

    #Get Selected Task
    def get_tree_sel(self):
        #Get Selection
        sel_task = self.dir_tree_widget.selectedItems()
        curr_show = [item.text(5) for item in sel_task]
        curr_show = str(curr_show[0])
        curr_shot = [item.text(0) for item in sel_task]
        curr_shot = str(curr_shot[0])
        current_dir = os.path.join(studio_dir,curr_show,curr_shot)

        #Set selected to manual path
        self.manual_path_Ldit.setText(current_dir)
        self.project_cB.setCurrentText(curr_show)
        # self.shot_cB.setCurrentText(curr_shot)
        # print(curr_show,curr_shot)

    def reload_task(self):
        get_status(username)
        self.populate_status()

    
    #populate project dirs
    def populate_project(self):
        prodirs = [ name for name in os.listdir(studio_dir) if os.path.isdir(os.path.join(studio_dir, name)) ]
        self.project_cB.addItems(prodirs)

    
    def populate_shot(self):
        sel_pro = self.project_cB.currentText()
        if sel_pro:
            shotdirs = studio_dir + '\\' + sel_pro
            shotdirs = [ name for name in os.listdir(shotdirs) if os.path.isdir(os.path.join(shotdirs, name)) ]
            self.shot_cB.addItems(shotdirs)
        self.manual_path_Ldit.setText(os.path.join(studio_dir,sel_pro))
        #def select_tools():
    
    # def populate_subdir(self):
    #     sel_pro = self.project_cB.currentText()
    #     subdir = self.shot_cB.currentText()
    #     if subdir:
    #         subdirs = studio_dir + '\\' + sel_pro+'\\'+ subdir
    #         subdirs = [ name for name in os.listdir(subdirs) if os.path.isdir(os.path.join(subdirs, name)) ]
    #         self.subdir_cB.addItems(subdirs)

    #     cur_subdir = self.subdir_cB.currentText()
    #     self.manual_path_Ldit.setText(os.path.join(studio_dir,sel_pro,subdir,cur_subdir))


    def manual_dir(self):
        man_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if man_path:
            self.manual_path_Ldit.setText(man_path)

        if not man_path:
            QtWidgets.QMessageBox.about(self,"path Required","Please, pick the path")

    #Calling Create Project UI
    def create_project(self):
        
        dlg = dialog()
        dlg.exec()

    #Calling Add Software UI
    def addsoft(self):
        dlg = addsoft()
        dlg.exec()

    #Calling About Page
    def about_page(self):
        dlg = about_page()
        dlg.exec()

    #Calling Report Form
    def report(self):
        dlg = report_form()
        dlg.exec()

    def toolssetup(self):
        self.tools_cB.addItems(tooldir)
    
    def opentool(self):
        toolname = self.tools_cB.currentText()
        print(str(toolname))
        os.startfile(tooldir[toolname]) 


#Create Project Dialog 
class dialog(ui.create_project_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(dialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier App Launcher - Create Project")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    #set darkmode

        self.Project_TB.clicked.connect(self.manual_dir)
        self.Seq_TB.clicked.connect(self.manual_dir)
        self.Shot_TB.clicked.connect(self.manual_dir)
        self.create_buttons.accepted.connect(self.create_pro_dirs)
        
        

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
        os.mkdir(os.path.join(prodir,seqdir,shotdir))
        mkdir = prodir + '/' +seqdir + '/' + shotdir
        print(mkdir)

#Add software Directories one time thing
class addsoft(ui.add_software_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(addsoft,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Software")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    #set darkmode


        self.softpath_TB.clicked.connect(self.getsoft)
        self.reg_buttonBox.accepted.connect(self.add_to_json)
       

    def getsoft(self):
        softpath,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if softpath:
            self.softpath_LE.setText(softpath)

    def add_to_json(self):
        softname = self.softname_LE.text()
        softpath = self.softpath_LE.text()
        
        with open(jsonpath) as jsonfile:
            j_soft = json.load(jsonfile)

        j_soft['key'] = ['object']

    # Writing to sample.json
        with open(jsonpath, "a") as outfile:
            json.dump(j_soft,outfile)
            
        
#About Page
class about_page(ui.about_page.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(about_page,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("About")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    #set darkmode
    
#Email Form
class report_form(ui.report_form.Ui_Form,QtWidgets.QDialog):
    def __init__(self):
        super(report_form,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Report")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        self.setStyleSheet(qdarkstyle.load_stylesheet())   

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    appLaunch = qt_launcher()
    appLaunch.show()
    app.exec()

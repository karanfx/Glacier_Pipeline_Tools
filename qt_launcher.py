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
from utils.create_project_dirs import create_shot_dirs,create_libs



#Import UIs
import ui.main_ui_7_ui as main_ui
import ui.create_project_ui
import ui.add_software_ui
import ui.about_page
import ui.report_form

#Import userID and tool dirs
user_json_path = "bin/data/user.json"
with open(user_json_path,"r") as uf:
    user_json = json.load(uf)
userdata = user_json.get('User_Data')

username = userdata.get('user')
studio_dir = userdata.get('studiodir')

tooldata = user_json.get('tools')
# print(tooldata)


#required data paths to refer
# tooldir = json.load(open('bin/data/softpaths.json'))
# jsonpath = "bin/data/softpaths.json"
# username = "Karan"


class qt_launcher(main_ui.Ui_MainWindow,QtWidgets.QMainWindow):
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
        #Populate Combo Boxs
        self.project_cB.currentTextChanged.connect(self.populate_seq)
        self.seq_cB.currentTextChanged.connect(self.populate_shot)
        self.shot_cB.currentTextChanged.connect(self.set_dir)
        self.tools_cB.currentTextChanged.connect(self.populate_versions)

        #Launch apps
        self.launch_button.clicked.connect(self.setup_env)
        self.launch_button.clicked.connect(self.opentool)
        self.manual_toolButton.clicked.connect(self.manual_dir)

        self.launch_version_button.clicked.connect(self.open_version)


        #Set Action Menu
        self.action_Create_Project_2.triggered.connect(self.create_project)
        self.action_setup_dirs.triggered.connect(self.setup_dirs)
        self.action_Exit.triggered.connect(self.close)
        self.actionToggle_Darkmode.triggered.connect(self.toggle_dark)

        #About Page
        self.actionAbout.triggered.connect(self.about_page)

        #Report Form
        self.actionReport.triggered.connect(self.report)

        #Load Tasks From Google Sheets API
        self.populate_status()
        
        self.reload_task_PB.clicked.connect(self.reload_task)
        self.reload_task_PB.clicked.connect(self.populate_project)

        #Update data in combo boxs
        self.dir_tree_widget.itemSelectionChanged.connect(self.get_tree_sel)
        self.dir_tree_widget.itemSelectionChanged.connect(self.populate_versions)


        #Load ComboBox after loading and creating dirs
        self.populate_project()
        self.populate_seq()
        self.populate_shot()

        self.populate_versions()


    #Toggle Dark Mode
    def toggle_dark(self):
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))
        

    #Get Data from Sheet
    def populate_status(self):
        self.dir_tree_widget.clear()
        self.dir_tree_widget.setAlternatingRowColors(True)
        
        with open("bin\data\shot_status.json") as f:
            data = json.load(f)
        # print(data)

        #Get Proper Indexes 
        show_idx = data[0].index('Show')
        seq_idx = data[0].index('Sequence')
        shot_idx = data[0].index('Shot')
        # print(show_idx,seq_idx,shot_idx)

        data = data[1:]
        for task in data:
            # Clean List
            task.remove(username)
            task.insert(7,task[show_idx])
            
            # task.insert(1,task[seq_idx])
            task.insert(1,task[shot_idx])
            task.pop(3)
            
            task = task[1:]
            print(task)
            # print(list(shot))
            item = QtWidgets.QTreeWidgetItem(list(task))
            self.dir_tree_widget.addTopLevelItem(item)

            #Create Dirs
            create_shot_dirs(studio_dir)
            create_libs(studio_dir)
            
    def reload_task(self):
        get_status(username)
        self.populate_status()

    #Get Selected Task
    def get_tree_sel(self):
        #Get Selection
        sel_task = self.dir_tree_widget.selectedItems()        
     
        current_dir = ""
        for item in sel_task:
            curr_shot = str(item.text(0))
            curr_seq = str(item.text(1))
            curr_show = str(item.text(6))
            current_dir = os.path.join(studio_dir,curr_show,curr_seq,curr_shot)

        #Set selected to manual path
        self.manual_path_Ldit.setText(current_dir)
        self.project_cB.setCurrentText(curr_show)
        self.seq_cB.setCurrentText(curr_seq)
        self.shot_cB.setCurrentText(curr_shot)
        # print(curr_show,curr_shot)
        print(current_dir)

    #populate project dirs
    def populate_project(self):
        prodirs = [ name for name in os.listdir(studio_dir) if os.path.isdir(os.path.join(studio_dir, name)) ]
        prodirs.remove('libs')
        self.project_cB.addItems(prodirs)

    def populate_seq(self):
        self.seq_cB.clear()

        sel_pro = self.project_cB.currentText()
        sel_pro = os.path.join(studio_dir,sel_pro)
        seq_list = [item for item in os.listdir(sel_pro) if os.path.isdir(os.path.join(sel_pro, item))]
        seq_list.remove('libs')
        self.seq_cB.addItems(seq_list)
        
    def populate_shot(self):
        self.shot_cB.clear()

        sel_show = self.project_cB.currentText()
        sel_seq = self.seq_cB.currentText()
        sel_pro = os.path.join(studio_dir,sel_show,sel_seq)
        shot_list = [item for item in os.listdir(sel_pro) if os.path.isdir(os.path.join(sel_pro, item))]
        shot_list.remove('libs')
        self.shot_cB.addItems(shot_list)

        # self.manual_path_Ldit.setText(os.path.join(studio_dir,sel_pro))
        
    #populate versions
    def populate_versions(self):
        self.version_file_CB.clear()
        #Get Current Data
        sel_show = self.project_cB.currentText()
        sel_seq = self.seq_cB.currentText()
        sel_shot = self.shot_cB.currentText()
        tool = self.tools_cB.currentText()

        version_path = os.path.join(studio_dir,sel_show,sel_seq,sel_shot,tool,"scene")
        # print(os.listdir(version_path))
        versions = os.listdir(version_path)
        # versions = [item for item in os.listdir(version_path) if os.path.isdir(os.path.join(version_path, item))]
        
        if len(versions) is 0:
            self.version_file_CB.addItems(["No Version Found"])
        else:
            versions.sort(reverse=True)
            versions.remove('backup')
            self.version_file_CB.addItems(versions)

    def open_version(self):
        #Get the file dir 
        #Get Current Data
        sel_show = self.project_cB.currentText()
        sel_seq = self.seq_cB.currentText()
        sel_shot = self.shot_cB.currentText()
        tool = self.tools_cB.currentText()
        version = self.version_file_CB.currentText()

        version_file_path = os.path.join(studio_dir,sel_show,sel_seq,sel_shot,tool,"scene",version)
        print(tool,version_file_path)

        #Open Software with file
        import subprocess
        subprocess.Popen([tooldata[tool], version_file_path])
        # print("opening version")

    def set_dir(self):
        show = self.project_cB.currentText()
        seq = self.seq_cB.currentText()
        shot = self.shot_cB.currentText()
        studio_dir.replace('\\','/')

        self.manual_path_Ldit.setText(os.path.join(studio_dir,show,seq,shot))

    def manual_dir(self):
        man_path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Select Folder')
        if man_path:
            self.manual_path_Ldit.setText(man_path)

        if not man_path:
            QtWidgets.QMessageBox.about(self,"Path Required","Please, pick the path")

    #Calling Create Project UI
    def create_project(self):
        import utils.custom_proj as proj
        dlg = proj.local_proj_dialog()
        dlg.exec()

    #Calling Add Software UI
    def setup_dirs(self):
        
        import utils.setup_dirs
        dlg = utils.setup_dirs.setup_dailog()
        dlg.exec()

    #Calling About Page
    def about_page(self):
        dlg = about_page()
        dlg.exec()

    #Calling Report Form
    def report(self):
        import utils.report_emailer as report
        dlg = report.report_form()
        # dlg.setStyleSheet(qdarkstyle.load_stylesheet(qt_api = 'PySide6'))
        
        dlg.exec()

    def toolssetup(self):
        self.tools_cB.addItems(tooldata)
        
    #Collect Selected Shot Data
    def setup_env(self):
        env_file = "C:/Users/PERMAN/Documents/houdini18.5/houdini.env"
        search_text = "# Glacier Variables"
        num_var = 6
        
        #Cleanup the file
       # Read the file content into a list of lines
        with open(env_file, 'r') as file:
            lines = file.readlines()

        # Create an empty list to store the modified content
        modified_lines = []

        i = 0
        while i < len(lines):
            line = lines[i]

            if search_text in line:
                # Found the search text, add it to the modified content
                modified_lines.append(line)

                # Skip the next lines_to_delete lines
                for _ in range(num_var):
                    i += 1
            else:
                modified_lines.append(line)

            i += 1

        # Write the modified content back to the file
        with open(env_file, 'w') as file:
            file.writelines(modified_lines)

        print(f"Deleted {num_var} lines after each occurrence of '{search_text}'.")



        #Setup Variables
        toolname = self.tools_cB.currentText()
        proj = self.project_cB.currentText()
        seq = self.seq_cB.currentText()
        shot = self.shot_cB.currentText()
        shot_dir = self.manual_path_Ldit.text()
        shot_dir = shot_dir.replace("\\","/")

        job = os.path.join(shot_dir,toolname)

        #Set env variables

        variables = {"SHOW" : proj, "SEQ": seq, "SHOT":shot,"SHOT_DIR":shot_dir,"JOB":job}
        with open(env_file,"a") as env:
            env.write("# Glacier Variables\n")
            for var,data in variables.items():
                env.write(var +"="+ "\"" + data + "/" + "\"" + "\n")

    
    #open DCCs
    def opentool(self):
        toolname = self.tools_cB.currentText()
        proj = self.project_cB.currentText()
        seq = self.seq_cB.currentText()
        shot = self.shot_cB.currentText()
        shot_dir = self.manual_path_Ldit.text()
        shot_dir.replace("\\","/")
        scene_dir = os.path.join(shot_dir,"houdini/scene")

        # print(str(toolname))
        os.startfile(tooldata[toolname]) 

        if toolname == "Houdini_CLI":
            #open def scene
            command = tooldata[toolname]
            print(command)
            command += "hscript E:/Work/python_dev/QT_project_launcher/bin/def_scenes/hou_default.hip"
            #set variables 
            from utils.hou_utils.set_shot_def import set_hou_shot_def
            set_hou_shot_def(proj,seq,shot,username,shot_dir,1001,1200)

            command += 'hython -c "import sys; sys.path.append("E:/Work/python_dev/QT_project_launcher/utils/hou_utils/");'
            command += 'import set_hou_shot_def; set_hou_shot_def(proj,seq,shot,username,shot_dir,1001,1200)'
            # command += "python E:/Work/python_dev/QT_project_launcher/utils/hou_utils/set_shot_def.py"
            #save scene in shot dir

            os.system(command)

        
#About Page
class about_page(ui.about_page.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(about_page,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("About")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))

        #set darkmode
        self.setStyleSheet(qdarkstyle.load_stylesheet())                    
    


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    appLaunch = qt_launcher()
    appLaunch.show()
    app.exec()

import os
import sys
from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide2.QtGui import QIcon, QPixmap
# import osUtils
import glob
# import hou

crowd_ui = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/crowd_preview.ui"


agent_dir = "D:/test_studio/Show01/libs/crowd/character"
clip_dir = "D:/test_studio/Show01/libs/crowd/anim"
props_dir = "D:/test_studio/Show01/libs/crowd/props"

class ClipBrowser(QtWidgets.QWidget):
    """ Browser preview quicktimes of fbxs
    """
    def __init__(self):
        super(ClipBrowser, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(crowd_ui,parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(),QtCore.Qt.Window)

        self.populate_assets()
        self.populate_props()
        self.populate_clips()
        self.ui.gernerate_preview_PB.clicked.connect(self.generate_preview)
        self.ui.Import_selected_PB.clicked.connect(self.import_agent)

        self.ui.agent_CB.currentTextChanged.connect(self.populate_agent_clips)
        self.ui.clips_CB.currentTextChanged.connect(self.populate_agent_clips)
        self.ui.props_CB.currentTextChanged.connect(self.populate_agent_clips)
    


    def populate_assets(self):
        self.ui.agent_CB.clear()
        #get assets from shot libs/crowd/charcater
        
        assets = os.listdir(agent_dir)
        self.ui.agent_CB.addItems(assets)

    def populate_props(self):
        self.ui.props_CB.clear()
        #get assets from shot libs/crowd/charcater
        
        props = os.listdir(props_dir)
        self.ui.props_CB.addItems(props)

    def populate_clips(self):
        self.ui.clips_CB.clear()
        #get the folder name for clip pack
        
        clips_pack = os.listdir(clip_dir)
        self.ui.clips_CB.addItems(clips_pack)

    def generate_preview(self):
        agent = self.ui.agent_CB.currentText()
        clips = self.ui.clips_CB.currentText()

        agent_name = os.path.join(agent_dir,agent)
        clips_dir = os.path.join(clip_dir,clips)

        for clip in os.listdir(clips_dir):
            print(clip)
            print(agent)

    def populate_agent_clips(self):
        print("loading_clips")
        agent = self.ui.agent_CB.currentText()
        clips = self.ui.clips_CB.currentText()

        agent_dir = os.path.join(agent_dir,agent)
        clips_dir = os.path.join(clip_dir,clips)




        # Find the QWidget container within your UI
        container_widget = self.ui.clip_preview_WD
        # Create the 4x4 grid layout within the container
        grid_layout = QGridLayout()
        container_widget.setLayout(grid_layout)

        # Create and add buttons to the grid layout
        for row in range(4):
            for col in range(4):
                button = QPushButton()
                button.setFixedSize(200, 200)  # Set button size to 200x200 pixels

                # Add an image or GIF icon to the button
                icon_path = f'path_to_icon/icon_{row * 4 + col + 1}.png'  # Replace with your icon file path
                icon = QIcon(icon_path)
                button.setIcon(icon)
                button.setIconSize(button.size())  # Make the icon fit the button size

                grid_layout.addWidget(button, row, col)


    def import_agent(self):
        agent = self.ui.agent_CB.currentText()
        clips = self.ui.clips_CB.currentText()

        agent_dir = os.path.join(agent_dir,agent)
        clips_dir = os.path.join(clip_dir,clips)

        print("import")

win = ClipBrowser()
win.show()
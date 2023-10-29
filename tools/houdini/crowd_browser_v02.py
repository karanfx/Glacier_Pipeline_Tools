import os
import sys
from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QSlider
from PySide2.QtCore import Qt,QSize
from PySide2.QtGui import QIcon, QPixmap,QImage
# import osUtils
import glob
import hou

import cv2
import qimage2ndarray

crowd_ui = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/hou_tools_ui/crowd_preview.ui"


agent_dir = "D:/test_studio/Show01/libs/crowd/agents"
clip_dir = "D:/test_studio/Show01/libs/crowd/anim"
props_dir = "D:/test_studio/Show01/libs/crowd/props"

class ClipBrowser(QtWidgets.QWidget):
    
    def __init__(self):
        super(ClipBrowser, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(crowd_ui,parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(),QtCore.Qt.Window)
        # self.ui.setLayout(self.ui.gridLayout_2)

        #add logo and window name
        self.setWindowTitle("Glacier Apps - Crowd Browser")
        self.setWindowIcon(QtGui.QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))

        #Populate data
        self.populate_agents()
        self.populate_props()
        self.populate_clips()
        self.populate_agent_clips()
        self.ui.agent_CB.currentTextChanged.connect(self.populate_clips)

        #Call on action
        self.ui.gernerate_preview_PB.clicked.connect(self.generate_preview)
        self.ui.Import_selected_PB.clicked.connect(self.import_agent)

        # self.ui.clips_CB.currentTextChanged.connect(self.del_buttons)

        self.ui.agent_CB.currentTextChanged.connect(self.populate_agent_clips)
        self.ui.clips_CB.currentTextChanged.connect(self.populate_agent_clips)
        self.ui.props_CB.currentTextChanged.connect(self.populate_agent_clips)

        
    


    def populate_agents(self):
        self.ui.agent_CB.clear()
        #get agents from shot libs/crowd/charcater
        
        agents = []
        for agent in os.listdir(agent_dir):
            if agent.endswith(".fbx") is True:
                agents.append(agent)
        self.ui.agent_CB.addItems(agents)

    def populate_props(self):
        self.ui.props_CB.clear()
        #get assets from shot libs/crowd/charcater
        
        props = os.listdir(props_dir)
        self.ui.props_CB.addItems(props)

    def populate_clips(self):
        self.ui.clips_CB.clear()
        cr_agent = self.ui.agent_CB.currentText()
        #get the folder name for clip pack
        char_name = cr_agent.strip(".fbx")
        # print(char_name)
        clip_pack  = os.path.join(clip_dir,char_name)

        clips = os.listdir(clip_pack)
        self.ui.clips_CB.addItems(clips)

    def generate_preview(self):
        agent = self.ui.agent_CB.currentText()
        clips = self.ui.clips_CB.currentText()

        agent_name = os.path.join(agent_dir,agent)
        clips_dir = os.path.join(clip_dir,clips)

        for clip in os.listdir(clips_dir):
            print(clip)
            print(agent)

    #Create Button Grid
    def createButtons(self,btn_list):
        #Create Button Co-ordinate
        
        # self.ui.clip_preview_WD.deleteLater()
        # QtWidgets.QWidget.deleteLater()
        
        # for child_widget in self.ui.clip_preview_WD.findChildren(QPushButton):
        #     child_widget.deleteLater()
        

        num_cols = 4
        num_rows = (len(btn_list) + num_cols - 1) // num_cols

        video_paths = ["D:/test_seq/test_explosion_v012.mp4", "D:/test_seq/test_explosion_v002.mp4", "D:/test_seq/test_explosion_v010.mp4"]

        target_sizes = [(320, 240), (640, 480), (480, 360)]

        self.target_size = (200,200)

        # groupBox = QtWidgets.QGroupBox("This Is Group Box")

        # scroll = self.ui.clip_scroll
        vbox = QtWidgets.QGridLayout()
        # vbox.removeItem(QPushButton)
        for row in range(num_rows):
            for col in range(num_cols):
                index = row * num_cols + col
                
                if index < len(btn_list):
                    item = btn_list[index]
                    
                    # self.button = QtWidgets.QLabel("",self)
                    self.button = QtWidgets.QPushButton("",self)
                    self.button.setText(item)
                    self.button.setIconSize(QSize(self.target_size[0],self.target_size[1]))
                    # self.button.setIcon(QIcon("D:/test_seq/test_explosion_v002.jpg"))
                    #Video Dir
                    preview = "D:/test_seq/test_explosion_v012.mp4"
                    video_paths = ["D:/test_seq/test_explosion_v012.mp4", "D:/test_seq/test_explosion_v002.mp4", "D:/test_seq/test_explosion_v010.mp4"]

                    # target_sizes = [(200, 200), (640, 480), (480, 360)]
                    
                    # #Create Video Object
                    self.capture = cv2.VideoCapture(preview)

                    # Create a timer to update the video frames
                    timer = QtCore.QTimer(self)
                    timer.timeout.connect(self.update_frame)
                    timer.start(1000 // 24)  # Set the timer interval (24 FPS)
                
                    self.button.setIconSize(QSize(self.target_size[0],self.target_size[1]))

                    #Using button old
                    # #Create Button 
                    # button = QtWidgets.QPushButton("",self)
                    # button.setIcon(QtGui.QIcon("D:/test_seq/test_explosion_v002.jpg"))  #Image on button 
                    # # button.setIcon(QtGui.QIcon("D:/test_seq/explosion_gif.gif"))
                    # button.setIconSize(QtCore.QSize(200,200))

                    # print(row,col)
                    # print(item)

                    vbox.addWidget(self.button,row,col)
                    
        # groupBox.setLayout(vbox)
        dumpy_layout = QtWidgets.QFrame()
        dumpy_layout.setLayout(vbox)
        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(dumpy_layout)
        # scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(400)
        layout = QGridLayout(self)
        layout.addWidget(scroll)
        
        self.setLayout(layout)
        self.ui.clip_preview_WD.setLayout(layout)

    def update_frame(self):
        # Read a frame from the video capture
        ret, frame = self.capture.read()

        if ret:
            # Resize the frame to the target size
            frame_resized = cv2.resize(frame, self.target_size)

            # Correct the color channel ordering (BGR to RGB)
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

            # Convert the OpenCV frame to a QImage
            height, width, channel = frame_rgb.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Set the image as the button's icon
            pixmap = QPixmap.fromImage(q_image)
            self.button.setIcon(QIcon(pixmap))
            self.button.setIconSize(QSize(self.target_size[0],self.target_size[1]))

        else:
            # Video playback is finished, reset to the beginning and continue
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)


    def del_buttons(self):
        for child_widget in self.ui.clip_preview_WD.findChildren(QPushButton):
            child_widget.deleteLater()

    def populate_agent_clips(self):
        print("loading_clips")
        agent = self.ui.agent_CB.currentText()
        clips = self.ui.clips_CB.currentText()

        agent_path = os.path.join(agent_dir,agent)
        agent = agent.strip(".fbx")
        clips_dir = os.path.join(clip_dir,agent,clips)

        clip_list = os.listdir(clips_dir)
        print(clip_list)
        #btn_name and contains
        # btn_list = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8","Item 8","Item 8","Item 8","Item 8","Item 8"]

        self.createButtons(clip_list)


    def import_agent(self):
        agent = self.ui.agent_CB.currentText()
        clips = self.ui.clips_CB.currentText()

        agent_dir = os.path.join(agent_dir,agent)
        clips_dir = os.path.join(clip_dir,clips)
        #houdini import code

        print("import")

win = ClipBrowser()
win.show()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication()
#     win = ClipBrowser()
#     win.show()
#     app.exec_()

# import json
# import os

# j = open('tools_path.json')
# k = json.load(j)

# print(k)
# for i,v in k:
#     print(i)
#     print(v)
# #print(y["houdini"])

# importing libraries
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 500, 800, 400)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
    # method for widgets
    def UiComponents(self):
 
        # creating a combo box widget
        self.combo_box = QComboBox(self)
 
        # setting geometry of combo box
        self.combo_box.setGeometry(200, 150, 150, 50)
 
        # geek list
        geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
 
        # adding list of items to combo box
        self.combo_box.addItems(geek_list)
 
        # creating push button
        button = QPushButton("Show content ", self)
 
        print(self.combo_box.count())
 
        # adding action to button
        button.pressed.connect(self.find)
 
        # creating label
        self.label = QLabel(self)
 
        # setting geometry of the label
        self.label.setGeometry(200, 200, 200, 30)
 
    def find(self):
 
        # finding the current item index  in combo box
        index = self.combo_box.currentIndex()
 
        # showing content on the screen through label
        self.label.setText("Index : " + str(index))
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())
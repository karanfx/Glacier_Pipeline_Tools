from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui 

from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 


class CreatePolygonUI(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(CreatePolygonUI, self).__init__(*args, **kwargs)
        
        #Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        #Set the object name     
        self.setObjectName('CreatePolygonUI_uniqueId')        
        self.setWindowTitle('Create polygon')        
        self.setGeometry(50, 50, 250, 150)        
        self.initUI()        
        self.cmd = 'polyCone'
        
    def initUI(self):        
        #Create combo box (drop-down menu) and add menu items 
        self.combo = QComboBox(self)        
        self.combo.addItem( 'Cone' )        
        self.combo.addItem( 'Cube' )        
        self.combo.addItem( 'Sphere' )        
        self.combo.addItem( 'Torus' )        
        self.combo.setCurrentIndex(0)        
        self.combo.move(20, 20)        
        self.combo.activated[str].connect(self.combo_onActivated)        
    
        #Create 'Create' button
        self.button = QPushButton('Create', self)        
        self.button.move(20, 50)        
        self.button.clicked.connect(self.button_onClicked)                    

    #Change commmand string when combo box changes
    def combo_onActivated(self, text):        
        self.cmd = 'poly' + text + '()'            
    
    #Execute MEL command when button is clicked
    def button_onClicked(self):        
        mel.eval( self.cmd )        
        
        
win = CreatePolygonUI()
win.show()
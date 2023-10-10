# from PySide2 import QtGui
# from PySide2.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout,QGridLayout
# import sys
# class Window(QWidget):
#     def __init__(self, val):
#         super().__init__()
#         self.title = "PyQt5 Scroll Bar"
#         self.top = 200
#         self.left = 500
#         self.width = 400
#         self.height = 300
#         self.setWindowIcon(QtGui.QIcon("icon.png"))
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)


#         # formLayout =QFormLayout()
#         # groupBox = QGroupBox("This Is Group Box")
#         # labelLis = []
#         # comboList = []

#         # for i in  range(val):
#         #     labelLis.append(QLabel("Label"))
#         #     comboList.append(QPushButton("Click Me"))
#         #     formLayout.addRow(labelLis[i], comboList[i])

#         vbox = QGridLayout()

#         label = QLabel("this is a long long text\n"*200)
#         vbox.addWidget(label)

#         # groupBox.setLayout(vbox)

#         # groupBox.setLayout(formLayout)

#         scroll = QScrollArea()
#         # scroll.setWidget(groupBox)
#         scroll.setWidget(vbox)
#         # scroll.setWidgetResizable(True)
#         # scroll.setFixedHeight(400)
#         layout = QGridLayout(self)
#         layout.addWidget(scroll)
#         self.show()


# App = QApplication(sys.argv)
# window = Window(4)
# sys.exit(App.exec_())

import subprocess

# script = "E:/Work/python_dev/QT_project_launcher/test/silly_test.py"
# prog = "C:/Program Files/Side Effects Software/Houdini 18.5.596/bin/houdinifx.exe"

# subprocess.run([prog,script],shell=True)

prog = "C:/Program Files/Nuke14.0v1/Nuke14.0.exe"
script = "E:/Work/python_dev/QT_project_launcher/utils/nuke/slapcomp.py"

subprocess.run([prog,script],shell=True)

# subprocess.run(prog,shell=True)
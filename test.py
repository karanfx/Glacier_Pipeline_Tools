import json
import os
from PySide6 import QtWidgets

import create_project_ui
# j = open('tools_path.json')
# k = json.load(j)

# #print(k)
# for i in k:
#     #print(i)
#     print(k[i])
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
import create_project_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = dialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

class dialog(create_project_ui.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(dialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("App Launcher - Build 1.2.0")



# class CustomDialog(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("HELLO!")
        

#         QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

#         self.buttonBox = QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)

#         self.layout = QVBoxLayout()
#         message = QLabel("Something happened, is that OK?")
#         self.layout.addWidget(message)
#         self.layout.addWidget(self.buttonBox)
#         self.setLayout(self.layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# class createproj_window(create_project_ui.Ui_Dialog,QtWidgets.QMainWindow):
#     def __init__(self):
#         super(createproj_window,self).__init__()
#         self.setupUi(self)
#         self.setWindowTitle("App Launcher - Build 1.2.0")


# if __name__ == '__main__':
#     app = QtWidgets.QApplication()
#     appLaunch = createproj_window()
#     appLaunch.show()
#     app.exec()


# path = 'D:\Work\houdinifx'
# print("Only directories:")
# print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
# print("\nOnly files:")
# print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
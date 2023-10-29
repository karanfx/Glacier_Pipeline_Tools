from PySide6 import QtWidgets,QtGui
import qdarkstyle


import ui.about_page
#About Page
class about_page(ui.about_page.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(about_page,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Glacier Tools - About")
        self.setWindowIcon(QtGui.QIcon("bin/logo/favicon_sq_small.png"))

        #set darkmode
        self.setStyleSheet(qdarkstyle.load_stylesheet())   
#Submit the concerns and reports
from PySide6 import QtWidgets
import PySide6.QtGui
import os
import json

import ui.report_form


#Email Form
class report_form(ui.report_form.Ui_Form,QtWidgets.QDialog):
    def __init__(self):
        super(report_form,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Report")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        
#Submit the concerns and reports
from PySide6 import QtWidgets
import PySide6.QtGui
import os
import json
import yagmail
import keyring



import ui.report_form


#Email Form
class report_form(ui.report_form.Ui_Form,QtWidgets.QDialog):
    def __init__(self):
        super(report_form,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Report")
        self.setWindowIcon(PySide6.QtGui.QIcon("bin/logo/favicon_sq_small.png"))
        
        self.mail_send_Pbutton.clicked.connect(self.send_mail)


    def send_mail(self):
        print("Excuted")
        to = self.to_mail_LE.text()
        
        subj = self.mail_subject_LE.text()
        desc = self.mail_body_TE.toPlainText()
        yagmail.register("karanmirajkar.td@gmail.com","perman51@td")
        yagm = yagmail.SMTP("karanmirajkar.td@gmail.com","perman51@td")
        yagm.send(to,subj,desc)
        print("Email Sent!!!!!!!!!!!!!!!")


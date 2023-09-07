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
        
        self.mail_send_Pbutton.clicked.connect(self.send_mail)


    def send_mail(self):
        import smtplib
        from email.message import EmailMessage

        my_email = "karanmirajkar.td@gmail.com"
        password = "hyalfpkltzctppbm"

        receiver = ['karanmirajkar.td@gmail.com']

        msg = EmailMessage()
        msg['Subject'] = 'test email from python'
        msg['From'] = my_email
        msg['To'] = receiver

        msg.set_content('this is test email body')


        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(my_email,password)
            smtp.send_message(msg)
    
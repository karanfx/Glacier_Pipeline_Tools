#Submit the concerns and reports
from PySide6 import QtWidgets
import PySide6.QtGui
import json


import ui.report_form

#get email and password
with open("bin\creds\gmail_app.json") as config_file:
    config = json.load(config_file)

MAIL_ID = config.get("MAIL_ID")
PASSWORD = config.get("PASSWORD")

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
        try:
            receiver = ['karanmirajkar.td@gmail.com']

            msg = EmailMessage()
            msg['Subject'] = self.mail_subject_LE.text()
            msg['From'] = MAIL_ID
            msg['To'] = receiver
            body = self.mail_body_TE.toPlainText()
            msg.set_content(body)


            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(MAIL_ID,PASSWORD)
                smtp.send_message(msg)

            #Dialog
            QtWidgets.QMessageBox.about(self,"Report Sent","Thank you for submitting you concern.")

        except smtplib.SMTPException as e:
            print("Email delivery failed:", e)
            QtWidgets.QMessageBox.about(self,"Error Sending Report","Please check you credentials")
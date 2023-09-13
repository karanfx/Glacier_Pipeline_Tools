#copy this file into User/Documents/houdini_18.x.xxx/scripts/ 
#will load at houdini startup


import hou

hou.hipFile.merge("E:/Work/python_dev/QT_project_launcher/bin/def_scenes/hou_default.hip")
# print("from docs")

#Add functions to hou.session

def email_notif():
    import smtplib
    from email.message import EmailMessage
    import hou
    import time
    #Creds
    my_email = "karanmirajkar.td@gmail.com"
    password = "hyalfpkltzctppbm"

    receiver = ['karanmirajkar.td@gmail.com']

    #mail template
    render_name = hou.pwd()
    render_dir = hou.pwd().parm("picture").eval()
    subject = "Render {} is Complete!".format(render_name)
    body = """Hey,
        Your render task for {} is successfully done at {}. And saved in {}.
        
        Regards,
        Glacier Tools""".format(render_name,str(time.ctime()),render_dir)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = my_email
    msg['To'] = receiver

    msg.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_email,password)
        smtp.send_message(msg)

hou.session.email_notif = email_notif
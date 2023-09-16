#copy this file into User/Documents/houdini_18.x.xxx/scripts/ 
#will load at houdini startup


import hou
import json

hou.hipFile.merge("E:\Work\python_dev\QT_project_launcher\tools\houdini\def_scenes\hou_default.hip")

#get email and password
with open("bin\creds\gmail_app.json") as config_file:
    config = json.load(config_file)

MAIL_ID = config.get("MAIL_ID")
PASSWORD = config.get("PASSWORD")

# print("from docs")
def email_notif():
    import smtplib
    from email.message import EmailMessage
    import hou
    import time

    #Creds
    my_email = MAIL_ID
    password = PASSWORD

    receiver = ['karanmirajkar.td@gmail.com']

    #mail template
    render_name = hou.pwd()

    #All Supported output nodes
    out_nodes = {"filecache":"sopoutput","rop_alembic":"filename",
                 "opengl":"picture","ifd":"vm_picture","usdexport":"lopoutput",
                 "file":"file","usdrender":"outputimage"}

    #Set Up the render dirs 
    render_dir = ""
    for type,out_path in out_nodes.items():
        print(type,out_path)
        if hou.pwd().type().name() == type:
            render_dir = hou.pwd().parm(out_path).eval()

    print(render_dir)


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

    print(body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_email,password)
        smtp.send_message(msg)

hou.session.email_notif = email_notif
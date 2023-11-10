import os
import json


api_cred = "E:/Work/python_dev/Glacier_pipeline_tools/creds/gmail_app.json"

#get email and password
with open(api_cred) as config_file:
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

    receiver = [MAIL_ID]

    #mail template
    current_node = hou.pwd()

    #All Supported output nodes
    out_nodes = {"filecache":"file","rop_alembic":"filename","rop_geometry":"sopoutput",
                 "opengl":"picture","ifd":"vm_picture","usdexport":"lopoutput",
                 "file":"file","usdrender":"outputimage"}

    #Set Up the render dirs 
    render_dir = ""
    for type,out_path in out_nodes.items():
        # print(type,out_path)
        if current_node.type().name() == type:
            if type == "rop_geometry":
                render_dir = current_node.parm(out_path).eval()
                current_node = current_node.parent()
            else:
                render_dir = current_node.parm(out_path).eval()


    # print(render_dir)
    # print(current_node)


    subject = "Render {} is Complete!".format(current_node)
    body = """Hey,
        Your render task for {} is successfully done at {}. And saved in {}.
        
        Regards,
        Glacier Tools""".format(current_node,str(time.ctime()),render_dir)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = my_email
    msg['To'] = receiver

    msg.set_content(body)

    # print(body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_email,password)
        smtp.send_message(msg)

# hou.session.email_notif = email_notif

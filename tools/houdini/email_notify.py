
def email_notif():
    import smtplib
    from email.message import EmailMessage
    import hou
    import time

    api_cred = "E:/Work/python_dev/Glacier_pipeline_tools/creds/gmail_app.json"


    #get email and password
    import json
    with open(api_cred) as config_file:
        config = json.load(config_file)

    MAIL_ID = config.get("MAIL_ID")
    PASSWORD = config.get("PASSWORD")
    

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
    msg['From'] = MAIL_ID
    msg['To'] = receiver

    msg.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(MAIL_ID,PASSWORD)
        smtp.send_message(msg)

email_notif()
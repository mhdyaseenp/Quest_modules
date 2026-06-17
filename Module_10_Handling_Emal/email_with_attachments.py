import smtplib                                  #connect to SMTP server to send emails

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender='mhdyaseenporoli@gmail.com'
em_password='ckuf uchl xrbr cyoy'
resever="yaseensachu188@gmail.com"

msg=MIMEMultipart()

msg["From"]=sender
msg["To"]=resever
msg["Subject"]="Test Email attachment"

# with open("work-card-animation.html",'r',encoding="utf-8")as file:
#     body=file.read()
    
with open("work-card-animation.html",'r',encoding="utf-8")as file:
    body = file.read()
    
    
# body="Hello,\nThis email contains an attachment.\nRegards,\nPython Script"


msg.attach(MIMEText(body,'html'))

# file_path =r"/Users/muhammedyaseen/Python/Module_10_Handling_Emal/2.class.py"
# file_name='2.class.py'

file_path =r"/Users/muhammedyaseen/Python/Module_10_Handling_Emal/haihello.png"
file_name='sachu.png'


try:
    with open(file_path,'rb')as attachment:
        mime=MIMEBase("application","octet-stream")         #application\octet-stream, This is some binary application data.
        
        mime.set_payload(attachment.read())                 #attachment read -Reads the entire file into memmory,set_patload-Store the file daaata inside the MIME object
        
        encoders.encode_base64(mime)                        #Email was originally designed for text only.SMTP cannot safely transmit arbitrary binary data.So Python converts it to Base64:
        
        mime.add_header("Content-Disposition",f"attachment ; filename={file_name}")      # this is an attachment, Display its name as sachu.png
        
        msg.attach(mime)
except Exception as e:
    print(f"An exception occured{e}")
    
    
try:
    with smtplib.SMTP("smtp.gmail.com",587)as server:
        server.starttls()
        server.login(sender,em_password)
        server.send_message(msg)
    print("Message sent successfully")
except Exception as e:
    print(f"an exception occured{e}")
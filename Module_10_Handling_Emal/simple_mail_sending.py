# import smtplib

# s=smtplib.SMTP("smtp.gmail.com",587)

# s.starttls()

# s.login('mhdyaseenporoli@gmail.com','ckuf uchl xrbr cyoy')

# msg='this is a testing mail'

# s.sendmail('mhdyaseenporoli@gmail.com','yaseensachu188@gmail.com',msg)
 
# s.quit()






import smtplib
from email.mime.text import MIMEText



sender_emial='mhdyaseenporoli@gmail.com'
app_pass='ckuf uchl xrbr cyoy'

reseve_email="yaseensachu188@gmail.com"

# with open("work-login.html",'r',encoding="utf-8")as file:
#     html = file.read()

with open("work-card-animation.html",'r',encoding="utf-8")as file:
    html = file.read()
    
# html = " <h2 style='color: blue;background-color: pink;'> Hello Welcome Najad...</h2><br> <p style='color: green; background-color: lightgray;'> You are hired......</p>"


mesg=MIMEText(html,'html')
mesg["Subject"]='whats app..'
mesg["From"]=sender_emial
mesg["To"]=reseve_email

with smtplib.SMTP("smtp.gmail.com",587) as server:
    server.starttls()
    server.login(sender_emial,app_pass)
    server.send_message(mesg)
print("Email sended successfull......")
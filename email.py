import smtplib, ssl
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "mariarapirova@gmail.com"
to_email = "mariarapirova@gmail.com"
password = input("Type your password(copied gmail) ")
#create a secure SSL conntex
context = ssl.create_default_context()
msg = "tere tulemast"
#"try to log to server and email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() #can be omitted
    server.starttls(context = context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, to_email, msg)
except Exception as Viga:
    print("vale andmet ")
finally:
    server.quit()


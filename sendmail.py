
import smtplib
sender_email="arundsnew@gmail.com"
rec_email="arundsnew@gmail.com"
password=input(str("Enter your password :"))
message="Jenkins Notification Email"

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender_email,password)
print("LogIn Successfull")
server.sendmail(sender_email,rec_email,message)
print("Your Email has been sent to : ",rec_email)
#instagram.com/machinelearning.teknoboost

import smtplib
sender_email="hemantgangwar9@gmail.com"
rec_email="hemantgangwar543@gmail.com"
password=input(str("Enter your password :"))
message="This email was sent using python."

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender_email,password)
print("LogIn Successfull")
server.sendmail(sender_email,rec_email,message)
print("Your Email has been sent to : ",rec_email)
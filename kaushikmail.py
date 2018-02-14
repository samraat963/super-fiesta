#email program

import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iamnotkoushik007@gmail.com","162110110")

msg = "happy valentines day"
server.sendmail("iamnotkoushik007@gmail.com","iamnotkaushik007@gmail.com",msg)
print ("message sent successfull")
server.quit()



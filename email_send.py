import smtplib




host="smtp.gmail.com"
port=587
file=open("D:/data.txt","r")
line=file.read()
words=line.split()
username=words[0]
password=words[1]
to_list=words[2:]

from_email=username

email_connection=smtplib.SMTP(host,port)
email_connection.ehlo()
email_connection.starttls()
email_connection.login(username,password)
email_connection.sendmail(from_email, to_list, "Hello, this is a testing EMAIL !")




email_connection.quit()


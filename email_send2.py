import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host="smtp.gmail.com"
port=587
file=open("D:/data.txt","r")
line=file.read()
words=line.split()
username=words[0]
password=words[1]
to_list=words[2:]

from_email=username

pass_wrong=SMTP(host,port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
	pass_wrong.login("haha","lala")
	pass_wrong.sendmail(from_email, to_list, "Hello, this is a testing EMAIL !")
except SMTPAuthenticationError:
	print ("Could not login")
except:
	print ("Pass or login failed")
pass_wrong.quit
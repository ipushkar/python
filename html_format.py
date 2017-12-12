import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host="smtp.gmail.com"
port=587
file=open("D:/data.txt","r")
line=file.read()
words=line.split()
username=words[0]
password=words[1]
to_list=words[2:]

from_email=username

try:
	email_connection=smtplib.SMTP(host,port)
	email_connection.ehlo()
	email_connection.starttls()
	email_connection.login(username,password)
	
	the_msg=MIMEMultipart("alternative")
	the_msg["Subject"]="Hello There!"
	the_msg["From"]=from_email
	the_msg["To"]=to_list[0]
	plain_text="Testing the message"
	html_text="""
	<html>
		<head></head>
		<body>
			<p>Hey!<br>
				Testing this email <b>message</b>. Made by <a href="http://joincfe.com">Team CFE</a>.
			</p>
		</body>
	</html>
	"""
	part_1=MIMEText(plain_text,"plain")
	part_2=MIMEText(html_text,"html")
	the_msg.attach(part_1)
	the_msg.attach(part_2)

	#print(the_msg.as_string())

	email_connection.sendmail(from_email,to_list,the_msg.as_string())
	email_connection.quit()

except smtplib.SMTPException:
	print ("error sending message")
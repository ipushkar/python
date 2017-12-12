import datetime
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


class MessageUser():
	user_details=[] 
	messages=[]
	email_message=[]
	base_message="""Hi there {name}!!! 
		Thanks for a great work.
		{date} was a good day
		Your purchuase {total} 
		Support TEAM
		"""
	def add_user(self,name,amount,email=None):
		name=name[0].upper()+name[1:].lower()
		today=datetime.date.today()
		date_text='{today.month}/{today.day}/{today.year}'.format(today=today)
		amount="%.2f"%(amount)
		detail={
			"name":name,
			"amount":amount,
			"date":date_text
		}
		if email is not None:
			detail["email"]=email
		self.user_details.append(detail)

	def get_details(self):
		return self.user_details
 
	def make_messages(self):
		if len(self.user_details)>0:
			for detail in self.get_details():
				name=detail["name"]
				date=detail["date"]
				amount=detail["amount"]
				message=self.base_message
				new_msg=message.format(
					name=name,
					date=date,
					total=amount
					)
				user_email=detail.get("email")
				if user_email:
					user_data={
						"email":user_email,
						"message":new_msg
					}
					self.email_message.append(user_data)
				else:
					self.messages.append(new_msg)
				self.messages.append(new_msg)
			return self.messages
		return []
	def send_email(self):
		self.make_messages()
		if len(self.email_message)>0:
			for detail in self.email_message:
				user_email=detail["email"]
				user_message=detail["message"]
				try:
					email_connection=smtplib.SMTP(host,port)
					email_connection.ehlo()
					email_connection.starttls()
					email_connection.login(username,password)
					the_msg=MIMEMultipart("alternative")
					the_msg["Subject"]="Updates Guys !"
					the_msg["From"]=from_email
					the_msg["To"]=user_email
					part_1=MIMEText(user_message,"plain")
					the_msg.attach(part_1)
					email_connection.sendmail(from_email,[user_email],the_msg.as_string())
					email_connection.quit()
				except smtplib.SMTPException:
					print ("error sending message")  
			return True
		return False


new=MessageUser()
new.add_user("igor",23.4,email=to_list)
new.add_user("stePhan",9898.2222,email=to_list)
new.get_details()
new.send_email()

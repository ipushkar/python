import datetime

class MessageUser():
	user_details=[] 
	messages=[]
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
				self.messages.append(new_msg)
			return self.messages
		return []
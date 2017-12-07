items=["La", "One", "Two",1,2,3,5,"new","Igorku"]

def list_parser(list):
	str_list=[]
	num_list=[]
	for i in list:
		if isinstance (i, (float, int)):
			num_list.append(i)
		elif isinstance (i, str):
			str_list.append(i)
		else:
			pass
	return str_list, num_list


print (list_parser(items))

items2=['ala','m3m',3,67,78,8]
print(list_parser(items2))

def my_sum(my_list):
	total=0
	for i in my_list:
		if isinstance (i, (int,float)):
			total=total+i
	return total

print(my_sum(items2))


def my_avg(my_list):
	the_sum=my_sum(my_list)
	num_of_items=len(my_list)
	return the_sum/(num_of_items*1.0)

my_avg(items2)




def count_sum_avg(my_list):
	total=0
	count=0
	for i in my_list:
		if isinstance(i, (float,int)):
			count=count+1
			total=total+i
	return count,total, total/count

count_sum_avg(items2)


text="this is {a} formatted string".format(a="new")
print(text)

def count(a,b):
	return a*b
def plus (a,b):
	return a+b
def minus(a,b):
	return a-b
def divide(a,b):
	return a*1.0/b

count(6,10)
plus(6,10)
minus(6,10)
divide(6,10)


text_2="new {0}".format("blabla")
print(text_2)

print("lala %.3f") %(2.12312313)

import datetime
today=datetime.date.today()
text='{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

now=datetime.datetime.utcnow()
text_3=now.strftime('%Y-%m-%d %H:%M:%S.%f')


default_name=["Igor","Ivan","Stepan","Olga","Roman","Yuriy"]
default_amounts=[122.50, 23.99, 124.32, 323.4,20.22, 99.99]

unf_message="""Hi there {name}!!! 

Thanks for a great work.
{date} was a good day
Your purchuase total is {total}

Support TEAM
"""

today=datetime.date.today()
text='{today.month}/{today.day}/{today.year}'.format(today=today)


def make_messages(names,amounts):
	message=[]
	if len(names)==len(amounts):
		i=0
		for name in names:
			name=name[0].upper()+name[1:].lower()
			new_msg=unf_message.format(name=name,date=text,total=amounts[i])
			i=i+1
			print(new_msg)

make_messages(default_name,default_amounts)




class animal():
	def __init__(self,name,color,kind):
		self.name=name
		self.color=color
		self.kind=kind

class animal():
		name="Whisper"
		color="Red"
		kind="Birds"

class bird(animal):
		size=20


class bird(animal):
	def __init__(self,size):
		self.size=size

dog=animal
dog.color="red"



	name="Lucky"
	color="Black"


class Dog():
	name();
	color();
	height()




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


pizdez=MessageUser()
pizdez.add_user("igor",23.4)
pizdez.add_user("stePhan",2323.232)
pizdez.add_user("YuREZS",2323.232,email="yura@rambler.ru")


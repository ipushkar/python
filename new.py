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
			new_msg=unf_message.format(name=str.lower(name),date=text,total=amounts[i])
			i=i+1
			print(new_msg)

make_messages(default_name,default_amounts)


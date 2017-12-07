from folder_user.message_user import MessageUser

test=MessageUser()
test.add_user("lala",20.234)
test.add_user("igor",23.4)
test.add_user("stePhan",2323.232)
test.add_user("LLALA",2323.232,email="yura@rambler.ru")


print(test.user_details)
print(test.make_messages())

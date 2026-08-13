#Write a program to check if user has entered correct userid and password.
id = 'FirstBit@gmail.com'
pw = 'Sumit123'

userid = str(input("Enter userid: "))
password = str(input("Enter password: "))


if(userid == id and password == pw):
    print(f"Welcome to firstbit")
else:
    print(f"Check the username and password")    
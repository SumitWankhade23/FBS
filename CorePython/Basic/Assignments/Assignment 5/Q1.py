#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.
id = 'Firstbitsolution'
pw = 'Sumit123'


attempt = 1
while( attempt <= 3):
    userid = str(input("Enter number: "))
    password = str(input("Enter number: "))

    if( id == userid and pw == password):
        print(f"Successfully login")
        break
    else:
        print(f"Re-enter credentials")
        attempt += 1
else:
    print(f"You have exceeded 3 attempts try after sometime")            
 
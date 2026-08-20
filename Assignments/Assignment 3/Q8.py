#Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

id = 'FirstBit'
pd ='Sumit123'

userid = str(input("Enter userid: "))
password = str(input("Enter password: "))

if(id == userid and pd == password):
    
    import random
    x = random.randint(1000,5000)

    print(f"Your verification number is {x}")

    captcha = int(input("Enter verification number: "))
    if(x == captcha):
        print("Successfully loggin in...")
    else:
        print("Invalid captcha!")

else:
    print("Invalid User ID or Password")            
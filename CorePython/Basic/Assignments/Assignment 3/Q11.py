#Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
age = int(input("Enter age of person: "))
Ticket_price = int(input("Enter ticket price: "))

if(age < 12):
    pay = Ticket_price -  (Ticket_price * 0.30)
    print(f"You have to pay {pay} rupees")
elif(age > 59):
    pay = Ticket_price - (Ticket_price * 0.50)
    print(f"You have to pay {pay} rupees")
else:
    print(f"You have to pay {Ticket_price}")        
    

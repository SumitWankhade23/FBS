# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passenger = int(input("Enter number of passenger: "))
ticket = float(input("Enter ticket price: "))
total_amount = 0

for i in range(1, passenger+1):
    age = int(input(f"Enter age of passenger {i}: "))
    if( age < 12):
        ticket_price = ticket - (ticket * 0.30)
        total_amount += ticket_price
    elif( age > 59 ):
        ticket_price = ticket - (ticket * 0.5)
        total_amount += ticket_price
    else:
        total_amount = total_amount + ticket
print(f"Total amount to ticket travel = {total_amount}")                
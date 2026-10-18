#--------------------- Python Test 5 - (Data Structures)-------------------------------
# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.
D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))

if amount % 5 != 0:
    print("Amount must be more than 5")
else:
    total_notes = 0
    remaining = amount

    for note in D:
        count = remaining // note        
        if count > 0:
            print(f"{note} x {count}")
            total_notes += count
            remaining = remaining % note 

    print("Minimum number of notes needed:", total_notes)




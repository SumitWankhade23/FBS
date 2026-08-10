#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount.
amount = int(input("Enter amount: "))
R500_notes = amount//500
amount = amount % 500
R200_notes = amount//200
amount = amount % 200
R100_notes = amount//100
amount = amount % 100
R50_notes = amount//50
amount = amount % 50
R20_notes = amount//20
amount = amount % 20
R10_notes = amount//10
amount = amount % 10




print(f"500 notes: {R500_notes}")
print(f"200 notes: {R200_notes}")
print(f"100 notes: {R100_notes}")
print(f"50 notes: {R50_notes}")
print(f"20 notes: {R20_notes}")

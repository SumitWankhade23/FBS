#Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

total_unit = int(input("Enter total units: "))

if total_unit <= 50:
    bill = total_unit * 0.50

elif total_unit <= 150:
    bill = (50 * 0.50) + ((total_unit - 50) * 0.75)

elif total_unit <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((total_unit - 150) * 1.20)

else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((total_unit - 250) * 1.50)

surcharge = bill * 0.20
total_bill = bill + surcharge

print(f"Electricity Bill = Rs. {bill}")
print(f"Surcharge = Rs. {surcharge}")
print(f"Total Electricity Bill = Rs. {total_bill}")


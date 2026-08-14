are_wall = float(input("Enter area: "))
cost = float(input("Enter cost price: "))

Total_area = (are_wall * 8) + (are_wall * 6)

Total_cost = Total_area * cost
print(f"Total cost: {Total_cost}")

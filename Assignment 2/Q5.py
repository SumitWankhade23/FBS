#WAP to calculate selling price of book based on cost price and discount.
cost_price = float(input("Enter cost of book: "))
discount = float(input("Enter discount: "))/100

selling_price = cost_price - (cost_price*discount)
print(f"Selling price will be: {selling_price}")
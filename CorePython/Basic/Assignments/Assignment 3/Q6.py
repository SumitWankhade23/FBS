#Write a program to calculate profit or loss.
cost_price = float(input("Enter cost price: "))
sell_price = float(input("Enter selling price: "))



if (sell_price > cost_price):
    profit = sell_price - cost_price
    print(f"Prifit = {profit} ")
elif(sell_price < cost_price):
    loss = cost_price - sell_price
    print(f"Loss = {loss}")

else:
    print(f"No profit no loss condition")
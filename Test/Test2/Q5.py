# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST
product_1 = float(input("Enter product1 price: "))
product_2 = float(input("Enter product2 price: "))
product_3 = float(input("Enter product3 price: "))
product_4 = float(input("Enter product4 price: "))
product_5 = float(input("Enter product5 price: "))

total_price = product_1 + product_2 + product_3 + product_4 + product_5
gst = total_price * 0.18
total_bill = total_price + (gst)

print("---------------------------------------------")
print(f"Total price (before GST) : Rs {total_price:.2f}")
print(f"GST (18%)                : Rs {gst:.2f}")
print("---------------------------------------------")
print(f"Total bill               : Rs {total_bill:.2f}")
print("---------------------------------------------")
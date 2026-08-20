l = float(input("Enter lenght: "))
b = float(input("Enter breadth: "))
r = float(input("Enter redius: "))

area_Rect = l * b
area_Halfcircle = (3.14 * (r**2))/2

total_area = area_Rect + area_Halfcircle
print(f"Total area = {total_area:.2f}")
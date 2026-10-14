# 4. Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.
cost = float(input("Enter painting rate: "))
l_wall = int(input("Enter length of wall: "))
w_wall = int(input("enter width of the wall: "))
area_wall = l_wall * w_wall

Total_area = 4 * area_wall
Tota_cost = cost * Total_area

print(f"Total cost of painting = {Tota_cost} Rs") 


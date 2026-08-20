#Convert distant given in feet and inches into meter and centimeter.
dist = float(input("Enter number: "))

#1 Feet = 12 inches
# 1 inch = 2.54 centimeters
# 100 centimeters = 1 meter
# 1 meter = 100 centimeters

Inches = (dist * 12) 
centimeters = Inches * 2.54 
meter = centimeters/100


print(f"Distance in inches: {Inches}")
print(f"Distance in centimeters: {centimeters}")
print(f"Distance in meter: {meter}")
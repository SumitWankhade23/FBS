#5. Python Program to Count the Number of Vowels in a String
def count_vovel(text):
    vov = 'aeiou'
    total = 0
    for char in text.lower():
        if char in vov:
            total = total +  1
    return total

text = "Mere brother ki dulhan"
result = count_vovel(text)
print(result)

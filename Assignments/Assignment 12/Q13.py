# 13. Python Program to count number of digits and letters in a string.
def count_digits_letters(text):
    dig_count = 0
    let_count = 0
    for ch in text:
        if "a" <= ch <= "z" or "A" <= ch <= "Z":
            let_count += 1
        elif "0" <= ch <= "9":
            dig_count += 1
    return dig_count,let_count 
text = "Sumit23"
result = count_digits_letters(text)
print(result)
           

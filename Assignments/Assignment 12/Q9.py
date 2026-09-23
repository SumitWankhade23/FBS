# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
def cal_charNum(data):
    chr_count = 0
    words_count = 0
    in_word = False
    for ch in data:
        if ch != " ":
            chr_count = chr_count + 1
        
            if in_word == False:
                words_count = words_count + 1
                in_word = True
        else:
            in_word = False
    
    return chr_count,words_count

data = str(input("Enter string: "))
result = cal_charNum(data)
print(f"Charechter couunt = {result[0]}") 
print(f"Word count = {result[1]}")           



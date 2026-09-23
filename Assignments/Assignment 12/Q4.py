#4. Python Program to Form a New String where the First Character and
#   he Last Character have been Exchanged
def swap_first_last(text):
    if len(text) <= 1:
        return text

    new_text = text[-1]              
    for i in range(1, len(text) - 1):
        new_text = new_text + text[i]   
    new_text = new_text + text[0]    

    return new_text


text = str(input("Enter text: "))
print(swap_first_last(text))

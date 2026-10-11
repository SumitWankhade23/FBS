# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)
#-------------------------------------------------------------------
text = input("Enter text: ")
l_word = {i: len(i) for i in text.split()}
print(l_word)

#Alternative program
di = {}
for i in text.split():
    di[i] = len(i)
print(di)


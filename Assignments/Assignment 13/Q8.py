# 8. Python Program to Count the Frequency of Words Appearing in a String Using
#    a Dictionary
def word_appear(text):
    freq = {}
    words = text.split()          
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
  
text = "Two One Two Fourty One Three One"
result = word_appear(text)
print(result)

#Shorter approch 
from collections import Counter
text = "Two One Two Fourty One Three One"
print(Counter(text.split()))

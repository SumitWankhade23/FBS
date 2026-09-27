# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
def Uniquewords_occuranceCount(data):
    One_stringList = []
    for ch in data:
        One_stringList.extend(ch.split())

    unique = set(One_stringList)

    occurance = {}
    for word in unique:
        occurance[word] = One_stringList.count(word)

    return unique, occurance

data = [
    "Cricket is my fvrt game",
    "I play Cricket every day",
    "Dhoni is successfull capton in Indian Cricket histry"
] 
unique,freq = Uniquewords_occuranceCount(data)
print(f"Unique words = {unique}")
print("\nWord frequency:")
for word,count in freq.items():
    print(f"{word} = {count}")

    

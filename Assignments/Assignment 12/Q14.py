# 14. Python Program to count the occurrences of ach word in a string.
def count_words(text):
    word_count = {}
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


text = "python is easy and python is powerful"
result = count_words(text)
print(result)

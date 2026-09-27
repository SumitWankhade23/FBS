# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.
def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))   
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print("Grouped anagrams:", result)

# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.
def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = ""
    shortest = min(strings, key=len)  

    for i, char in enumerate(shortest):
        chars_at_position = {s[i] for s in strings}

        if len(chars_at_position) == 1:
            prefix += char
        else:
            break  

    return prefix


strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print("Longest common prefix:", result)


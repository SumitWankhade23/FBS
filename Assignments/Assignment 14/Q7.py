# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
def find_missing_numbers(set1, set2):
    missing_in_set2 = set1 - set2   
    missing_in_set1 = set2 - set1   

    return missing_in_set2, missing_in_set1


set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

missing_in_set2, missing_in_set1 = find_missing_numbers(set1, set2)

print("Numbers in set1 but missing from set2:", missing_in_set2)
print("Numbers in set2 but missing from set1:", missing_in_set1)



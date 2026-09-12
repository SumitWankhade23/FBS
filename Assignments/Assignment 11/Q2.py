#2. Python Program to Merge Two Lists and Sort it
def merge_and_sort(list1, list2):
    merged = list1 + list2
    
    # Sort using bubble sort (without using built-in sort())
    n = len(merged)
    for i in range(n):
        for j in range(n - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    
    return merged


list1 = [10, 25, 3, 47, 8]
list2 = [15, 2, 33, 9, 41]

result = merge_and_sort(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Merged and sorted list:", result)
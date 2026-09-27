# 4. Write a def find_pairs(numbers, target_sum):
def find_pairs(numbers, target_sum):
    pairs = []
    seen = set()

    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs


numbers = [2, 4, 3, 5, 7, 8, 1]
target_sum = 9

result = find_pairs(numbers, target_sum)
print("Pairs with sum", target_sum, ":", result)   
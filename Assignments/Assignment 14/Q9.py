# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.
def three_sum(numbers, target):
    numbers.sort()
    result = set()
    n = len(numbers)

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if current_sum == target:
                result.add((numbers[i], numbers[left], numbers[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return list(result)


numbers = [1, 4, 2, -3, 3, 0, -1, 5]
target = 6

result = three_sum(numbers, target)
print("Unique triplets that sum to", target, ":", result)

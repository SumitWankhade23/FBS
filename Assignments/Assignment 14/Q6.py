# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
from itertools import combinations
def max_product_pair(numbers):
    unique_numbers = set(numbers)   

    max_product = None
    best_pair = None

    for pair in combinations(unique_numbers, 2):
        product = pair[0] * pair[1]
        if max_product is None or product > max_product:
            max_product = product
            best_pair = pair

    return best_pair, max_product

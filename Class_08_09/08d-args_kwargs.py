def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(4, 5, 6, 7))  # Output: 22
# Example of Shallow Copy:

"""In Python, shallow copy and deep copy are ways to copy objects, but they handle nested objects (like lists within lists) differently.

Shallow Copy
Definition: Creates a new object but does not create copies of nested objects. Instead, it references the nested objects from the original."""

import copy

# Original list with nested list
original_list = [[1, 2], [3, 4]]

# Shallow copy of the list
shallow_copy = copy.copy(original_list)

# Modifying the nested list in the shallow copy
shallow_copy[0][0] = 'X'

print("Original List:", original_list)  # Output: [['X', 2], [3, 4]]
print("Shallow Copy:", shallow_copy)    # Output: [['X', 2], [3, 4]]



# Original list with nested lists
original_list0 = [[1, 2, 3], [4, 5, 6]]

# Create a shallow copy of the original list
shallow_copied_list = copy.copy(original_list0)

# Modify the nested list in the shallow copy
shallow_copied_list[0][0] = 'X'

print("Original List:", id(original_list0))
print("Shallow Copied List:",id(shallow_copied_list))


# Deep Copy
# Definition: Creates a new object and recursively copies all nested objects, making the copy completely independent of the original.
# Example:

# Original list with nested list
original_list1 = [[1, 2], [3, 4]]

# Deep copy of the list
deep_copy = copy.deepcopy(original_list1)

# Modifying the nested list in the deep copy
deep_copy[0][0] = 'X'

print("Original List:", original_list1)  # Output: [[1, 2], [3, 4]]
print("Deep Copy:", deep_copy)          # Output: [['X', 2], [3, 4]]


print("Original List:", id(original_list1))  # Output: [[1, 2], [3, 4]]
print("Deep Copy:", id(deep_copy))        # Output: [['X', 2], [3, 4]]

# Original list with nested lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a deep copy of the original list
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copied_list[0][0] = 'X'

print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)



numbers1 :list[int] = [1,2,3,4,5,5,6,7,8,9,10]

print(numbers1[0:6])

# [start:stop:step]

print(numbers1[4:8])

print(numbers1[-6:-8])

print(numbers1[0::2])

numbers1 :list[int] = [1,2,3,4,5,5,6,7,8,9,10]
print(numbers1[::-1])
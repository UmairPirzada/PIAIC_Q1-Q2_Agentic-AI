# Assignment 1
shallow copy and deep copy in list

in nested_list append 
slicing and indexing


In Python, copying objects can be done in two primary ways: shallow copy and deep copy. Both are used to create copies of existing objects, but they differ in how they handle objects that contain other objects (e.g., lists of lists).

# Shallow Copy
A shallow copy creates a new object, but it does not create copies of nested objects inside the original object. Instead, it inserts references to the nested objects into the new object. This means that changes made to nested objects in the shallow copy will reflect in the original object and vice versa.


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

print("Original List:", original_list0)
print("Shallow Copied List:", shallow_copied_list)



# Deep Copy
A deep copy creates a new object and recursively copies all objects found in the original object, including nested objects. This means the new object and the original object are completely independent of each other.

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



# Original list with nested lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a deep copy of the original list
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copied_list[0][0] = 'X'

print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

squares : list[int]  = []
for x in range(1, 6):
    squares.append(x**2)

print(squares)  # Output: [1, 4, 9, 16, 25]

# The Solution: Simplify Code with List Comprehensions
squares : list[int] = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]


numbers : list[int] = [2,4,6,8]


for number in numbers:
    squares.append(number**2)
    print(squares)
    
    
# List Comprehensions 

# [expression for number in numbers]
# Example: Creating a List of Squares

squares : list[int] = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

squares2 = [number**2 for number in numbers]
print(squares2)

# we will fine square of even number from  to 10
# use range fn
# for loop
# conditional statement to find even numbers
# calculate the squares of even numbers
squares3 : list[int] = []
for i in range (1,11):
    if i % 2 ==0:
        squares = i**2
        squares3.append(squares)
print (squares3)

# Adding Conditions: Filtering with List Comprehensions
even_squares : list[int] = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]


squares4 = [i**2 for i in range (1,11) if i % 2==0]

# print(dir(str))

methods = [method for method in dir (str) if '_' not in method ]
print(methods)
# even_squares : list[int] = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(even_squares)  # Output: [4, 16, 36, 64, 100]

# More Advanced Examples
# Nested List Comprehensions
# We can use nested list comprehensions to create lists of lists or perform more complex operations.

# Flattening a List of Lists
# We can flatten a list of lists into a single list using a list comprehension.

# Example:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
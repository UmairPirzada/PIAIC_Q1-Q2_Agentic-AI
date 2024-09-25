# Tuples in Python
# The Solution: Using Tuples for Immutable Sequences
coordinates : tuple[int,int] = (10, 20)
print(coordinates)  # Output: (10, 20)

# coordinates[0] = 15
# Trying to modify a tuple will raise an error
# coordinates[0] = 15  # This will raise a TypeError

my_tuple : tuple[int, int, int] = (1, 2, 3)

# Example: Storing Multiple Values

point : tuple[int, int, int] = (1, 2, 3)
print(point)  

# Creating a Tuple Without Parentheses
my_tuple : tuple[int, int, int] = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)

# Single-Element Tuples
single_element_tuple = (5,)
print(single_element_tuple)  # Output: (5,)
not_a_tuple = (5)
print(type(not_a_tuple))  # Output: <class 'int'>

my_tuple = (1)
print(type(my_tuple))
my_tuple = 1,2,3
my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))

my_tuple : tuple [int, ...] = (1,2,3,4,5,6)


tup : tuple [int, ...] = (1,2,3,4,5,6)

print(tup[0])

# Operations with Tuples
# Accessing Elements

'''We can access elements in a tuple using indexing, similar to lists:'''

my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[1])  


# Slicing Tuples
# We can slice tuples to get a range of elements:

my_tuple = ('apple', 'banana', 'cherry', 'date')
print(my_tuple[1:3])  # Output: ('banana', 'cherry')

# Tuple Concatenation and Repetition
# Tuples can be concatenated using the + operator and repeated using the * operator:


# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)

# Repetition
repeated_tuple = ('A',) * 3
print(repeated_tuple)  # Output: ('A', 'A', 'A')


# Tuple Unpacking
"""Tuple unpacking allows us to assign each element of a tuple to a variable in a single statement:"""


scores = (10, 20)
x, y = scores
print(x)  # Output: 10
print(y)  # Output: 20


names : tuple [str,str] = ("umair" , "ali")
name1 ,name2 = names

print(names)
print(name1)
print(name2)

# Nesting Tuples
# Tuples can contain other tuples, which is useful for organizing data hierarchically:

nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5, 6))


# Use as Dictionary Keys
# Because tuples are immutable, they can be used as keys in dictionaries, unlike lists.

location = {}
point = (10, 20)
location[point] = "Park"
print(location)  # Output: {(10, 20): 'Park'}

# Swapping Variables

a = 5
b = 10
a, b = b, a
print(a)  # Output: 10
print(b)  # Output: 5

a = 5
b = 10
c = a
a = b
b = c
print(a)
print(b)

t1 = (1,2)
t2 = (2,3)
print(f"Before swapping: t1={t1} and t2={t2}") # Output: Before swapping: t1=(1, 2) and t2=(2, 3)
t1, t2 = t2, t1
print(f"After swapping: t1={t1} and t2={t2}") # Output: After swapping: t1=(2, 3) and t2=(1, 2)


test_tup = (1, 2, [100, 200])

# The Solution: Using Tuples for Immutable Sequences
# Operations with Tuples
# Accessing Elements
# We can access elements in a tuple using indexing, similar to lists:

my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[1])  # Output: banana

# Slicing Tuples
# We can slice tuples to get a range of elements:

my_tuple = ('apple', 'banana', 'cherry', 'date')
print(my_tuple[1:3])  # Output: ('banana', 'cherry')

# Tuple Concatenation and Repetition
# Tuples can be concatenated using the + operator and repeated using the * operator:

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)

# Repetition
repeated_tuple = ('A',) * 3
print(repeated_tuple)  # Output: ('A', 'A', 'A')

# Tuple Unpacking
# Tuple unpacking allows us to assign each element of a tuple to a variable in a single statement:

scores = (10, 20)
x, y = scores
print(x)  # Output: 10
print(y)  # Output: 20

# Nesting Tuples
# Tuples can contain other tuples, which is useful for organizing data hierarchically:

nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5, 6))

# Use as Dictionary Keys
# Because tuples are immutable, they can be used as keys in dictionaries, unlike lists.

location = {}
point = (10, 20)
location[point] = "Park"
print(location)  # Output: {(10, 20): 'Park'}

# Tuple Methods and Operations
# 1. count()
# The count() method returns the number of occurrences of a specified value in the tuple.

# Example:
my_tuple = (1, 2, 3, 2, 2, 4)
count_of_twos = my_tuple.count(2)
print(count_of_twos)  # Output: 

# index()
# The index() method returns the index of the first occurrence of a specified value. If the value is not found, it raises a ValueError.

# Example:
my_tuple = ('apple', 'banana', 'cherry')
index_of_banana = my_tuple.index('banana')
print(index_of_banana)  # Output: 1

# Tuple Operations
# 1. Accessing Elements
# We can access elements of a tuple using square brackets [] with the index of the element. Remember that tuple indices start at 0.

my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[0])  # Output: apple
# Slicing
# We can slice a tuple to get a subset of elements:

my_tuple = ('apple', 'banana', 'cherry', 'date')
print(my_tuple[1:3])  # Output: ('banana', 'cherry')

# Concatenation
# Tuples can be concatenated using the + operator:

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
# We can repeat a tuple a certain number of times using the * operator:

my_tuple = ('A', 'B')
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: ('A', 'B', 'A', 'B', 'A', 'B')


# Membership Test
# We can check if an item exists in a tuple using the in keyword:

my_tuple = ('apple', 'banana', 'cherry')
print('banana' in my_tuple)  # Output: True
print('grape' in my_tuple)   # Output: False

# Iterating Over a Tuple
# We can iterate over the elements of a tuple using a for loop:

my_tuple = ('apple', 'banana', 'cherry')
for fruit in my_tuple:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Tuple Usage Examples
# 1. Swapping Variables
# Tuples can be used for swapping the values of two variables without needing a temporary variable.

a = 5
b = 10
a, b = b, a
print(a)  # Output: 10
print(b)  # Output: 5

# Swapping Tuples
# Tuples themselves can be swapped.

t1 = (1,2)
t2 = (2,3)
print(f"Before swapping: t1={t1} and t2={t2}") # Output: Before swapping: t1=(1, 2) and t2=(2, 3)
t1, t2 = t2, t1
print(f"After swapping: t1={t1} and t2={t2}") # Output: After swapping: t1=(2, 3) and t2=(1, 2)

# Storing Related Data
# Tuples can store related data, like coordinates or RGB color values.

point = (10, 20)
color = (255, 0, 0)

print(point)  # Output: (10, 20)
print(color)  # Output: (255, 0, 0)

# Using Tuples as Dictionary Keys
# Because tuples are immutable, they can be used as keys in dictionaries.

locations = {}
point = (10, 20)
locations[point] = "Park"
print(locations)  # Output: {(10, 20): 'Park'}


# Tuple Methods and Operations
# 1. count()
# The count() method returns the number of occurrences of a specified value in the tuple.



# Example:

my_tuple = (1, 2, 3, 2, 2, 4)
count_of_twos = my_tuple.count(2)
print(count_of_twos)  # Output: 3


# index()
# The index() method returns the index of the first occurrence of a specified value. If the value is not found, it raises a ValueError.

# Example:

my_tuple = ('apple', 'banana', 'cherry')
index_of_banana = my_tuple.index('banana')
print(index_of_banana)  # Output: 1

# Membership Test
# We can check if an item exists in a tuple using the in keyword:

my_tuple = ('apple', 'banana', 'cherry')
print('banana' in my_tuple)  # Output: True
print('grape' in my_tuple)   # Output: False


# Iterating Over a Tuple
# We can iterate over the elements of a tuple using a for loop:

my_tuple = ('apple', 'banana', 'cherry')
for fruit in my_tuple:
    print(fruit)
    
    # Assignment: Try to change the elements in the list.
test_tup = (1, 2, [100, 200])
print(test_tup)
print(type(test_tup))
     
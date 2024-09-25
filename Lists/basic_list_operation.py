# What is List?

"""A list in Python is like a container that can hold multiple items, one after another. Imagine you have a shopping list where you write down everything you need to buy. A Python list is very similar, but instead of just groceries, it can hold all kinds of things like numbers, words, or even other lists!

Store Multiple Items Together:
A list allows you to keep multiple items in one place. For example, if you want to keep track of all your students' names, you can store them in a list."""

students = ["umair", "mahmood" , "ali"]

print(students)
# Access Items by Position:

"""Lists keep items in the order you put them in. 
You can access any item by telling Python where it is in the list (starting from 0)."""

print(students[0])

print(students[1])

print(students[-1])


# Change Items:
    
"""You can easily change an item in 
the list if you need to update it."""

students[0] = "Fahad"

print(students)




# Adding or Removing elements from list

students = ["Rehan", "Muzhar", "Ibtisam" , "umair", "mahmood" , "ali", "Fahad"]

print(students)
# Append a new student

students.append("haseeb")

print(students)


# Pop the last student

last_student = students.pop()

print(last_student)

print(students)


# Remove a specific student by name

students.remove("Fahad")

print(students)


# Initial list of students

students1 : list[str] = ["Rehan", "Muzhar", "Ibtisam" , "umair", "mahmood" , "ali", "Fahad"]

print(students1)

# New students to be added

new_students: list[str] = ["Usman", "Ahmed"]

print(f"print:{new_students}")

# Extend the original students list with the new students
students1.extend(new_students)

print(students1)


# Indexing

"""Indexing is how you access individual elements in a list using their position in the list. 
In Python, lists are zero-indexed, meaning that the first element in a list is at index 0, the second element is at index 1, and so on."""

print(students1)


# Slicing with Indexes

phrase = list("LongLivePakistan!")

# Positive Indexing

part1 = phrase[0:4]
print(part1)  


part2 = phrase[4:8]
print(part2)  


part3 = phrase[8:16]
print(part3)  


# Negative Indexing

part4 = phrase[-9:-1]
print(part4)  


part5 = phrase[-14:-10]
print(part5)  


part6 = phrase[:-1]
print(part6)  


# Slicing with Steps

part7 = phrase[::2]
print(part7)  



part8 = phrase[0:8:2]
print(part8)  


# Reversing the entire string

reversed_phrase = phrase[::-1]
print(reversed_phrase)

# Combining Positive and Negative Indexing with Steps

part10 = phrase[6:-2:2]
print(part10) 


# Some interesting concepts in Lists

zero_list = [0] * 5
print(zero_list)  

# list concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  

# list repetition
repeated_list = list1 * 3
print(repeated_list)  

# list membership
a = 1 in list1
print(a)  

b = 7 in list1
print(b)  

# list length
length = len(list1)
print(length)  

# list and range function
new_list = list(range(10))
print(new_list)  

message = "Hello, World!"
characters = list(message)
print(characters)  

# list unpacking
numbered_list = [4, 8, 6]
a, b, c = numbered_list
print(a)  
print(b)  
print(c)  

another_list = [1,2,3,4,5,6,7,8,9,10]
x, *y, z = another_list
print(x)  
print(y)  
print(z)  
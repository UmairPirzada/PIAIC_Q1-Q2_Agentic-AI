

print("Hi Alice, you’re invited to my birthday party!")
print("Hi Bob, you’re invited to my birthday party!")
print("Hi Charlie, you’re invited to my birthday party!")
# ...and so on, for 50 friends

# Loops



friends = ["Alice", "Bob", "Charlie", "David", "Eve"]  # and so on, up to 50 names

for friend in friends:
    print(f"Hi {friend}, you’re invited to my birthday party!")
    
    
    
# For Look

# for letter in "Python":
    
    
for i in range (5):
    print(i)    


for i in range (5):
    print(f"umair {i}")  
    
for i in range (5):
    print(f"{i} umair")      
    
for i in range (5,12):
    print(f"{i} umair")     
    
for i in range (1,12,2):
    print(f"{i} umair")    
    
    
    
# for Loop with zip()

# Iterating over two lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]


for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
    
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35 , 45]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
    
    
names = ["Alice", "Bob", "Charlie", "umair"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
    
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
ages2 = [5, 3, 3]
for name, age, age2 in zip(names, ages , ages2):
    print(f"{name} is {age} years old  {age2}")



# Nested for Loops
# Nested for loops are used when you need to perform an action that involves iterating over multiple sequences or when dealing with multi-dimensional data (like a matrix or list of lists).

# Iterating over a list of lists

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()
    
    
    
    
values = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for value in values:
    for sub_value in value:
        print (f" Innerloop : {sub_value}")
        
    print(f"outerloop : {value}")
    
    
print ("loop end")


# Generating the multiplication table for 2
number = 2
print(f"Multiplication Table for {number}:")
for multiplier in range(1, 11):  # Loop through multipliers from 1 to 10
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")


for number in range(2, 11):  # Outer loop for each number from 2 to 10
    print(f"\nMultiplication Table for {number}:")
    for multiplier in range(1, 11):  # Inner loop for each multiplier from 1 to 10
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")



# for numbers1 in range (2,11):
#     # print(numbers1)
    
#     print(f"\nMultiplication Table for {numbers1}: ")

    
#     for mul in range (1,11):
        
        

# The While Loop:

# While Loop

# while condition:
    # Code block to be executed repeatedly
    
# condition = ""
# while condition !=  "exit":
#     user_in = input("enter command: ")
#     if user_in != "exit":exit
#         print(user_in)
#     elif user_in == "exit" :
#     condition = user_in
    
    
# condition = ""
# while condition != "exit":
#     user_in = input("Enter command: ")  # Corrected 'inter' to 'input'
#     if user_in != "exit":
#         print(user_in)
#     elif user_in == "exit":
#         condition = user_in  # Corrected indentation here



count = 0
while count < 5:
    print("Count is:", count)
    count += 1 # count = count + 1
    
    
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    
    
# shopping_cart : list [str] = ["apple", "salt", "abc", "advfff"]


# print 2 to 10 


for number in range (1,18):
    if (number==10):
        continue
    print(f"iteration number : {number}")



for number in range (1,18):
    if (number==10):
        break
    print(f"iteration number : {number}")
    
    
for table_number in range (2, 10):
    for inner_val in range (1,11):
        if (table_number == 3 and inner_val >5):
            continue
        print(f"{table_number} * {inner_val} = {table_number * inner_val}")
    print("")    
    
    
for table_number in range (2, 10):
    for inner_val in range (1,11):
        if (table_number == 3 and inner_val >5):
            break
        print(f"{table_number} * {inner_val} = {table_number * inner_val}")
    print("")  
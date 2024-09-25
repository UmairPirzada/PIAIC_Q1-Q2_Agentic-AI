# Introduction to Dictionaries in Python

students : list[str ]= ["Alice", "Bob", "Charlie"]
scores : list[int] = [85, 92, 78]
print(f"results : {scores}")

# students_scores : dict{str,int} = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78
# }
students_scores= {"Alice":22,"Bob":22, "Charlie":44}
students_scores= {"Alice","Bob", "Charlie" }
scores  = {85, 92, 78}

# Creating a Dictionary
# can create a dictionary using curly braces {} or the dict() function.

# Example:
# Using curly braces
student_scores : dict[str, int] = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
# Using dict() function
student_scores : dict[str,int] = dict(Alice=85, Bob=92, Charlie=78)


# Accessing Values
# can access values in a dictionary using the key inside square brackets [] or with the .get() method.

# Example:
# Accessing a value using a key
print(student_scores["Alice"])  # Output: 85

# print(students_scores["ali"])
print(student_scores.get("ali"))  # Output: 92

# Using the get() method
print(student_scores.get("Bob"))  # Output: 92

names = {1:"umair", 2: "ali"}

names = {1.7:"umair", 2.8: "ali"}

names = {True:"umair", False: "ali"}

# names = {[1,2,3]:"umair", False: "ali"}
# key must be different
names = {True:{1:"umair"}, False: "ali"}
names = {True:{1:"umair"}, False: ["a","b"], 3:"ali", False: "fahad"}
print(names)
print(names[False])

# add valuse in dict
student_details = {}
student_details["names"] = "Rehan"
print(student_details)

del student_details["names"]

# student_details.append("name":)


# Removing Items
# can remove items using the del statement, the .pop() method, or the .popitem() method.



# Example:
# # Removing a specific key-value pair using del
# del student_scores["Charlie"]
# print(student_scores)  # Output: {'Alice': 90, 'Bob': 92, 'David': 88}

# # Removing a specific key-value pair using pop()
# removed_score = student_scores.pop("David")
# print(removed_score)  # Output: 88
# print(student_scores)  # Output: {'Alice': 90, 'Bob': 92}

# # Removing the last inserted key-value pair using popitem()
# last_item = student_scores.popitem()
# print(last_item)  # Output: ('Bob', 92)
# print(student_scores)  # Output: {'Alice': 90}




students_scores= {"Alice":22,"Bob":22, "Charlie":44}
for score in student_scores:
    print(score)
    
# students_scores= {"Alice":22,"Bob":22, "Charlie":44}
# for score in student_scores:
#     print(f"{score} {student_scores{score}}")
    
print(student_scores.values())

print(student_scores.items())

students_scores= {"Alice":22,"Bob":22, "Charlie":44}
for score in student_scores:
    print(f"{score} {student_scores[score]}")
    
students_scores= {"Alice":22,"Bob":22, "Charlie":44}
for key,value in student_scores.items():
    print(f"key is {key} and correcponding value is {value}")    
    
    
values : dict[int,int] = {x:x for x in range(5)}
print(values)  # Output: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}    


values : dict[int,int] = {x:x for x in range(5)}
print(values)  # Output: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}   

fruits : list[str] = ["apple", "banana", "orange"]
for fruit in fruits:
    print (fruits)
    
for i,fruit in enumerate (fruits):
    print (i,fruits)    

# fruits : list[str] = ["apple", "banana", "orange"]
fruits_dict : dict[int,str] = {key: value for i, fruit in enumerate(fruits)}
print(fruits_dict)  # Output: {0: 'apple', 1: 'banana', 2: 'orange'}


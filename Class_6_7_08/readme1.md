
# Membership and Identity Operators

# Membership Operators

# in and not in

fruits = ["apple" , "banana" , "cheery"]
print("apple" in fruits)

print("banana" in fruits)

print("banana" not in fruits)

print("orange" not in fruits)


# Identity Operators

name :str = "umair"
name1 : str = "ali"

if name == name1:
    print ("names are same")


print(id(name))


a = [1,2,3]

b = a
c = a.copy()
print(a is b)
print(id(a))
print(id(b))
print(id(c))

c = [ 1,2 ,3]


# zip function

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35, 45]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
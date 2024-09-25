colours :list[str] = ["Green", "Yellow" , "Blue", "Red"]


print(f"My sublist is {colours[1:3]}")

print(f"My favourite colour is {colours[2]}")


print(f"The first colours is {colours[-1]}")


# Slicing

# [start:end:step]

numbers: list[int]= [1,2,3,4,5] #2,3,4
print (f"{numbers[1:4]}")
# include last 


colours2 :list[str] = colours [:] #shallow copy (here) || and deep copy
print(colours2)

print(f" ")


# colours:list[str | int ] = colours [:] #shallow copy (here) || and deep copy
# print(colours2) 

# colours2 :list[any] = colours [:] #shallow copy (here) || and deep copy
# print(colours2)


colours12 :list[str] = ["Green", "Yellow" , "Blue", "Red"]

print(f"My sublist is {colours[1:]}")

# 3 Slicing with setps

numbers1 :list[int] = [1,2,3,4,5,5,6,7,8,9,10]

# [start:end:step]

print(numbers1[0::2])


print(numbers1[::])


print(numbers1[-6:-2])

print(numbers1[-6:-8])


print(numbers1[-6:-7])

print(numbers1[-6:-6])

# numbers1 :list[int] = [1,2,3,4,5,5,6,7,8,9,10]
print(numbers1[-6:-8:-1])

print(numbers1[-6:-8:-2])


print(numbers1[::-1]) #reverse


print(numbers1[-8:-2:-1])

print(numbers1[-2:-8:-1])



# nested_list
nested_list= [ [1,2,3,], ['a','b','c']]

print(nested_list[0][1])

print(nested_list[1][1])


students =[ ["Ali", 70,60,80], ["Umair",69,80,50,],["fahad",47,80,90]]

print(students [2][2])

print(students [2][:])

print(students [2][1::2])

print(students [0::][::])


print(students [0::2][::])



three_dim = [[['a','b'],['c','d'],[23,34]],[['x','y','z'],[41,56]],[['r','tt','yy'],[11,33]]]

print(three_dim[0][1])

print(three_dim[0][2][1])

print(three_dim[2][1])

classroom = [
    ["Rehan", [85, 90, 88]],   # Rehan's grades: Math, Science, English
    ["Muzhar", [78, 85, 82]],  # Muzhar's grades: Math, Science, English
    ["Ibtisam", [92, 88, 91]], # Ibtisam's grades: Math, Science, English
    ["Usman", [60, 59, 65]]    # Usman's grades: Math, Science, English
]

rehan_science_grade = classroom[0][1][1]
print(rehan_science_grade)  

usman_english_grade = classroom[3][1][2]
print(usman_english_grade)  

classroom[1][1][0] = 83
print(classroom[1])  



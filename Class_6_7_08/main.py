# print 2 to 10 table but make sure 5 table only print 1 to 5

for table_nmbr in range(2, 10):
    for inner_val in range(1, 11):
        if (table_nmbr == 3 and inner_val > 5):
            continue
        print(f" {table_nmbr} X {inner_val} = {table_nmbr * inner_val}")
    print("")
    
for nmber in range(1, 18):
    if (nmber == 10):
        break
    print(f'iteration number : {nmber}')    
    
for nmber in range(1, 18):
    if (nmber == 10):
        continue
    print(f'iteration number : {nmber}')
    
    
    
numbers: list[int] = [2, 4, 6, 8]
squares: list[int] = []

for number in numbers:
    square = number**2
    squares.append(square)
    # squares.append(number**2)

print(squares)

# [expression for item in iterable]
squares2 = [number**2 for number in numbers]
print(squares2)

# we will find squares of even number from 1 to 10

# 1. use range function
# 2. for loop
# 3. condtional statement to find even numbers
# 4. calcualte the squares of even numebrs

squares3: list[int] = []
for i in range(1, 11):
    if i % 2 == 0:
        square = i**2
        squares3.append(square)

print(squares3)

square4 = [i**2 for i in range(1, 11) if i % 2 == 0]
print(square4)

print(dir(str))
methods = [method for method in dir(str) if '__' not in method]
print(methods)
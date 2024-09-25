# Function 
# 1- Define the function

def greet ():
    # function body (effect)
    print("Hello Class")
    
# Call a function\Invocation

greet()

# Function Parameters
def addition1 ( ):
    pass

def addition2 ( ):
    x=4
    y=8
    print(x+y)
    
    
def addition (a , b):
    
    result = a + b
    print(result)
    
# addition () # arguments missing
    
addition (5 , 10) # arguments

addition (19 , 10) 


# Function Return
a = print ("Rehan")
print (f"value of a:  {a}")

y = int("5")

print (f"value of y {y}")

# 1. Reutrn with expression
# So far we only discussed the functions which perform specific task but do not provide results. Now we'll discuss the functions which do provide a result and we get this result through return keyword.

# Let's look at example of a function which takes 2 parameters (numbers), add them (perform a task) and return the result.

# Define a function
def addition (first_number:int, second_number:int)->int:
    result : int = first_number + second_number
    return result


print(addition(5, 8)) # Output: 13
# Can also do like this
get_sum : int = addition(5,8)
print(get_sum) #Output: 13
 
# reture with expression
def addition (a , b):
    result = a + b
    return result
result1 = addition (3,5)
print (result1)

print (4*result1)

# result without expression

def addition (x,y):
    if x < 10 and y < 10 :
        return 
    else: 
        return x + y
    
print (addition (10,12))
print (addition (4,5))


# def return_mul_val (x ,y):
#     x = 4
#     y =5
#     return x , y
# print(return_mul_val(10 , 4))

def sub (x ,y):
    return x - y
print (sub(10,33))


full_name (f_n , l_n):
    
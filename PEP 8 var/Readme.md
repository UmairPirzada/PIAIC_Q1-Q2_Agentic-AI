# Python Enhancement Proposal.
# A_PEP 8 Guidelines
# 1.Descriptive Naming:
count=1
total_price=200.50
# 2.Lowercase with Underscores:
umair_pirzada="umair"
item_count=43

# 3.Avoid single character Names:
for i in range (10):
    print(i)
 
# 4.Constants in ALL CAPITALS:
MAX_CONNECTIONS =100
PI=3.14149

# 5.Class Names:
class MyClass:
    pass

class EmployeeRecord:
    pass
# 6.Instance and Class Varibles:
class ExampleClass:
    
    
    class_varibles=0
    
    def __init__(self,value):
        self.instance_varible=value
# 7. Function and Method Names:
def my_function():
    pass 


class MyClass:
    def my_method(self):
        pass 
# 8.Private Varibles
_private_varible=45
class MyClass:
    
    
    def __init__(self):
      self._private_instance_varible="private"
# 9.Avoid Trailing Underscores:
class_="AI"

# 10. Double Leading Underscores:
class MyClass:
    
    
    def __init__(self):
        self.__mangled_name="mangled"


# 11. Variables with Special Meanings:
__all__=["module1", "module2"]
__version__="1.0"
__author__="Umair"

# B _ Indentation and Line Length
 
# 1.Indentation
def example_function():
    a=3
    b=10
    return a+b

if True:
    print("Hello, World!")
    

# 2. Maximum Line Length (79):
def example_function_with_long_name(argument_one,argument_two,argument_three):
    return argument_one+argument_two+argument_three

long_varible_name="This is a very long string that goes beyond the limit of 79 characters"

# 3. Blank Lines:
class MyClass:
    
    
    def method_one(self):
        pass
    
    
    def method_two(self):
        pass

def function_one():
    pass

def function_two():
    pass

# C_Imports

# 4.Imports
import os 
import sys
from subprocess import Popen, PIPE
# from mymodule import my_function

# D _String Quotes
# 5. string
my_string="Hello, World!"
my_string1='Hello, World!'

# E-Whitespace
# 6. WhiteSpace in Expression and Statements
## correct
x=1
y=2
long_varible = 3
## Incorrect
x    =1
y     =4
long_varible =4 


# F _Comments
# 7.comments
#  This is a correct comment.
a=5 #This is a correct comment.
#  this incorrect comments 
a=6 # this incorrect comments 


# G_Naming Conventions
def my_function():
    pass

varibles_names=10 


# H_Programming Recommendation
# 9. Prog
def add (x,y):
    return x+y
# Instead of :
add= lambda x,y:x+y

# 10. Module Level Dunder Names:
"""Module docstring"""
__all__=["foo", "bar"]
__version__="1.0"
__author__="Umair"

import os
import sys

# 11. Top_Level script environment
def main():
    print("Hello , World!")
if __name__=="__main__":
    main()


# 12. Trailing commas

my_list=[
    1,
    2,
    3,
]

# correct :
my_list = [1,2,3]

# 13. Method Definitions:
class MyClass:
    def method(self):
        pass
    
# I- line Breaks and statement

# 14.Line Breaks
total = item_one +item_two+item_three+ \
    item_four+item_five
    
    
# 15. Compound statement
#Correct 
if foo =="bar":
    do_something()
# incorrect:
if foo =="bar": do_something()


# J-Accessing Names:
import mypkg.sibling
from mypkg import sibling 
from mypkg.sibling import example_function
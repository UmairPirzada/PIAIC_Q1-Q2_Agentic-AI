# Python String Methods with Examples
 # Basic String Methods
# 1. capitalize() Capitalizes the first character of the string.
text="hello, world!"
capitalized_text=text.capitalize()
print(capitalized_text)

# 2. casefold() Converts the string to lowercase for caseless comparisons.
text = "HELLO WORLD"
casefolded_text = text.casefold()
print(casefolded_text)  # Output: hello world

# 3. center() Returns a centered string of a specified length.
text = "hello"
centered_text = text.center(10, "*")
print(centered_text)  # Output: ***hello***

# 4. count() Returns the number of occurrences of a substring.
text = "banana"
count_a = text.count("a")
print(count_a)  # Output: 3

# 5. encode() Encodes the string into a bytes object using a specified encoding.
# The `encode()` method in Python is used to encode the string into a bytes object using a specified
# encoding. This method takes an encoding parameter and returns the encoded version of the string as a
# bytes object.

text = "hello"
encoded_text = text.encode("utf-8")
print(encoded_text)  # Output: b'hello'

# 6. endswith() Checks if the string ends with a specified suffix.
text = "hello, world!"
ends_with_world = text.endswith("world!")
print(ends_with_world)  # Output: True

# 7. expandtabs() Replaces tabs with spaces.
text = "hello\tworld"
expanded_text = text.expandtabs(4)
print(expanded_text)  # Output: hello    world

# 8. find() Returns the index of the first occurrence of a substring.
text = "hello, world!"
index = text.find("world")
print(index)  # Output: 7

# 9. format() Formats a string using placeholders.
name = "Alice"
age = 30
formatted_string = "Hello, my name is {} and I am {} years old.".format(name, age)
print(formatted_string)  
# Output: Hello, my name is Alice and I am 30 years old.

# 10. format_map() Formats a string using a mapping.
values = {'name': 'Alice', 'age': 30}
formatted_string = "Hello, my name is {name} and I am {age} years old.".format_map(values)
print(formatted_string)  # Output: Hello, my name is Alice and I am 30 years old.

# 11. index() Returns the index of the first occurrence of a substring, raising a ValueError if not found.
text = "hello, world!"
index = text.index("world")
print(index)  # Output: 7

# 12. isalnum() Returns True if all characters are alphanumeric.
text = "hello123"
is_alnum = text.isalnum()
print(is_alnum)  # Output: True

# 13. isalpha() Returns True if all characters are alphabetic.
text = "hello"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True

# 14. isascii() Returns True if all characters are ASCII.
text = "hello"
is_ascii = text.isascii()
print(is_ascii)  # Output: True

# 15. isdecimal() Returns True if all characters are decimal digits.
text = "123"
is_decimal = text.isdecimal()
print(is_decimal)  # Output: True

# 16. isdigit() Returns True if all characters are digits.
text = "123"
is_digit = text.isdigit()
print(is_digit)  # Output: True

# 17. isidentifier() Returns True if the string is a valid identifier.
text = "my_variable"
is_identifier = text.isidentifier()
print(is_identifier)  # Output: True

# 18. islower() Returns True if all characters are lowercase.
text = "hello"
is_lower = text.islower()
print(is_lower)  # Output: True

# 19. isnumeric() Returns True if all characters are numeric.
text = "123"
is_numeric = text.isnumeric()
print(is_numeric)  # Output: True

# 20. isprintable() Returns True if all characters are printable.
text = "hello world"
is_printable = text.isprintable()
print(is_printable)  # Output: True

# 21. isspace() Returns True if all characters are whitespace.
text = "  \t\n"
is_space = text.isspace()
print(is_space)  # Output: True

# 22. istitle() Returns True if the string is a titlecased string.
text = "Hello, World!"
is_title = text.istitle()
print(is_title)  # Output: True

# 23. isupper() Returns True if all characters are uppercase.
text = "HELLO"
is_upper = text.isupper()
print(is_upper)  # Output: True

# 24. join() Concatenates elements of an iterable into a string.
words = ["hello", "world"]
text = " ".join(words)
print(text)  # Output: hello world

# 25. ljust() Returns a left-justified string of a specified length.
text = "hello"
left_justified = text.ljust(10, "*")
print(left_justified)  # Output: hello*****

# 26. lower() Converts all characters to lowercase.
text = "HELLO"
lower_text = text.lower()
print(lower_text)  # Output: hello


# 27. lstrip() Removes leading whitespace from the string.
text = "  hello, world!  "
stripped_text = text.lstrip()
print(stripped_text)  # Output: hello, world!  

# 28. maketrans() Creates a translation table for use with the translate() method.

translation_table = str.maketrans("aeiou", "12345")
text = "hello"
translated_text = text.translate(translation_table)
print(translated_text)  # Output: h1ll0


# 29. partition() Splits the string into a tuple of three parts based on the first occurrence of a separator.

text = "hello, world!"
parts = text.partition(", ")
print(parts)  # Output: ('hello', ', ', 'world!')

# 30. removeprefix() Removes a prefix from the string if it exists.
text = "hello world"
removed_prefix = text.removeprefix("hello ")
print(removed_prefix)  # Output: world

# 31. removesuffix() Removes a suffix from the string if it exists.

text = "hello world!"
removed_suffix = text.removesuffix(" world!")
print(removed_suffix)  # Output: hello

# 32. replace() Replaces occurrences of a substring with another substring.

text = "hello, world!"
replaced_text = text.replace("world", "Python")
print(replaced_text)  # Output: Hello, Python!

text = "hello, world!"
replaced_text = text.replace("hello", "Python")
print(replaced_text)  # Output: world, Python!

# 33. rfind() Returns the index of the last occurrence of a substring.

text = "hello, world, hello"
index = text.rfind("hello")
print(index)  # Output: 14

# 34. rindex() Returns the index of the last occurrence of a substring, raising a ValueError if not found.

text = "hello, world, hello"
index = text.rindex("hello")
print(index)  # Output: 14

# 35. rjust() Returns a right-justified string of a specified length.

# text = "hello"

# right_justified =

text = "hello"
right_justified = text.rjust(10)
print(right_justified)
#     hello



# More in Strings

# String Operators

# 1. String Concatenation (+)

# + operator is used to concatenate two strings.

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"

# 2. Repetition (*)

# The * operator is used to repeat a string a specified number of times.

str1 = "Hello"
result = str1 * 3
print(result)  # Output: "HelloHelloHello"

# 3. Membership (in, not in)

# 3a. Membership Operators

# The in and not in operators are used to check whether a substring exists within a string.

str1 = "Hello World"
print("Hello" in str1)    # Output: True
print("Python" not in str1)  # Output: True

# 4. String Length (len())

# The len() function is used to get the length of a string.

str1 = "Hello World"
print(len(str1))  # Output: 11

# 5. Indexing ([])

# Indexing allows to access individual characters in a string using their position.

str1 = "Hello"
print(str1[0])  # Output: "H"
print(str1[-1]) # Output: "o"

# 6. Slicing ([start:stop:step])

# Slicing allows to select a range of characters in a string.

str1 = "Hello World"
print(str1[0:5])  # Output: "Hello"
print(str1[6:11]) # Output: "World"

# 7. String Comparison (==, !=, <, >, <=, >=)

# 7a. Comparison Operators

# Compare two values and return a Boolean result (True or False).

# Equal to: == Not equal to: != Greater than: > Less than: < Greater than or equal to: >= Less than or equal to: <=

result_equal: bool = 5 == 5
result_not_equal: bool = 10 != 7
result_greater_than: bool = 8 > 3
result_less_than: bool = 6 < 9
result_greater_equal: bool = 5 >= 5
result_less_equal: bool = 3 <= 4


# Strings can be compared using comparison operators.
str1 = "Hello"
str2 = "World"
print(str1 == str2)  # Output: False
print(str1 != str2)  # Output: True
print(str1 < str2)   # Output: True (since "H" comes before "W" lexicographically)

# 8. String Formatting (%, .format(), f-strings)

# Strings can be formatted using different methods.

name = "Alice"
age = 30

# Using % operator

print("My name is %s and I am %d years old." % (name, age))  # Output: "My name is Alice and I am 30 years old."

# Using .format()

print("My name is {} and I am {} years old.".format(name, age))  # Output: "My name is Alice and I am 30 years old."

# Using f-strings (Python 3.6+)

print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 30 years old."


# 8a. Common format specifiers

""" # %s (String Format Specifier):

# %s is used as a placeholder for a string. It tells Python to insert the string representation of the corresponding variable into the position where %s appears in the string. In our example:
# %s corresponds to the variable name, which has the value "Alice".

# "My name is %s" becomes "My name is Alice"."""

# 2. %d (Integer Format Specifier):

""" #%d is used as a placeholder for an integer. It tells Python to insert the integer value of the corresponding variable into the position where %d appears in the string. 
In our example:
%d corresponds to the variable age, which has the value 30.
I am %d years old" becomes "I am 30 years old"."""

# 3. %f (Float Format Specifier)

pi = 3.14159
formatted_string = "The value of pi is approximately %.2f" % pi
print(formatted_string)  # Output: "The value of pi is approximately 3.14"


# 4. %x (Integers in Hexadecimal Format Specifier)

number = 255
formatted_string = "The hexadecimal representation of %d is %x" % (number, number)
print(formatted_string)  # Output: "The hexadecimal representation of 255 is ff"

# 5. %o (Integers in Octal Format Specifier)

number = 255
formatted_string = "The octal representation of %d is %o" % (number, number)
print(formatted_string)  # Output: "The octal representation of 255 is 377"


#6.  %e (Scientific Format Specifier) e.g 2.5e+02

large_number = 25000
formatted_string = "The scientific notation of %d is %e" % (large_number, large_number)
print(formatted_string)  # Output: "The scientific notation of 25000 is 2.500000e+04"


# 7 .%c (Character Format Specifier)

char_code = 65
formatted_string = "The character for ASCII code %d is %c" % (char_code, char_code)
print(formatted_string)  # Output: "The character for ASCII code 65 is A"


# 8. %r (Raw Format Specifier)


text = "Hello\nWorld"
formatted_string = "Raw representation: %r" % text
print(formatted_string)  # Output: "Raw representation: 'Hello\\nWorld'"



# 9. Escape Sequence

"""\   -> Escape character
\n  -> Escape sequence
\n  -> inserts new line
\\  -> inserts backslach
\'  -> inserts single quote
\"  -> inserts double quote
\t  -> inserts tab
\r  -> moves the cursor to the start of the line
\a  -> Beeps
\b  -> Backspace """

print("Python Programming in \"PIAIC\"")
print("Python Programming in \\PIAIC")
print("Python Programming in \nPIAIC")
print("Python Programming in \tPIAIC")
print("Python Programming in PIAIC\rpiaic")
print("Python Programming in a\bPIAIC")
print("Python Programming in \aPIAIC")


# 10. Assignment Operators:

"""Assign values to variables and perform operations in a concise way.

Assignment: = Addition assignment: += Subtraction assignment: -= 
Multiplication assignment: *= Division assignment: /= 
Modulus assignment: %= Floor division assignment: //= 
Exponentiation assignment: **="""

x: int = 5
x += 3  # Equivalent to x = x + 3
y: float = 10
y /= 2  # Equivalent to y = y / 2




# 11. Comments.

"""In Python, comments are lines of text in your code that are not executed as part of the program. 
They are meant for human readers to understand the code better. Python supports two types of comments: single-line comments and multi-line comments."""

# 1. Single-line Comment

"""Single-line comments start with 
the # symbol and continue to the end of the line. 
Everything after # on that line is considered a comment and is ignored by the Python interpreter."""

# This is a single-line comment

print("Hello, World!")  # This is also a comment

# Provides a brief comment on a single line.


# 2. Multi-line Comments:

# """While Python doesn't have a built-in syntax for multi-line comments, 
# you can use triple-quotes (''' or """) """to create a multi-line string, and it's often used as a way to add multi-line comments. 
# Although it's not ignored like a traditional comment, it serves the purpose of commenting out multiple lines."""

'''
This is a multi-line comment
spanning multiple lines.
'''
print("Hello, World!")

# Demonstrates a comment spanning multiple lines.



# 12. Type conversion

"""# This is the process of changing the data type of a value. 
Python provides functions like int(), float(), and complex() 
for type conversion."""

float_value: float = 3.75
int_value: int = 2

float_to_int: int = int(float_value)
int_to_float: float = float(int_value)

# Illustrates converting between data types. 

# 13. type, dir, id functions

"""type provides the type of a variable
dir provides the list of attributes and methods of a variable
id provides the memory address of a variable"""

w = True
x = 5
y = 3.0
z = "Hello"

print(type(w)) 
print(type(x))  
print(type(y))  
print(type(z))  

print(dir(w))  
print(dir(x)) 
print(dir(y))
print(dir(z))

print(id(w))  
print(id(x)) 
print(id(y))
print(id(z))
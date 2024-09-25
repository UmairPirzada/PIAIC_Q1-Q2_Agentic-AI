# The Order of Operations in Python

The order of operations, also known as operator precedence, dictates the order in which Python evaluates expressions. The rules of precedence are similar to those in arithmetic. To help remember them, the acronym PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) is often used. Here is the full list of operations from highest to lowest precedence:

### 1 .Parentheses ():

Operations inside parentheses are performed first. Parentheses can be used to force an expression to evaluate in a certain order or to clarify the order of operations in complex expressions.


### 2. Exponents **:

Exponentiation is performed next. Note that in Python, exponentiation is evaluated from right to left.

### 3. Unary Plus and Minus +x, -x:

These operations indicate the sign of a number (positive or negative). They are performed after parentheses and exponentiation, but before any multiplication or division.


### 4. Multiplication *, Division /, Floor Division //, and Modulus %:

These operations are performed from left to right as they appear in the expression. They have the same level of precedence.

### 5. Addition + and Subtraction -:

Addition and subtraction are performed from left to right as they appear in the expression.

### 6. Bitwise Shifts <<, >>:

These operators shift the bits of a number to the left or right. They are less commonly used but come next in precedence.


### 7. Bitwise AND &:

This operator compares each bit of two numbers and returns a new number, based on the AND logic.

### 8 .Bitwise XOR ^:

This operator compares each bit of two numbers and returns a new number, based on the XOR logic.

### 9. Bitwise OR |:

This operator compares each bit of two numbers and returns a new number, based on the OR logic.

### 10. Comparison Operators ==, !=, >, >=, <, <=:

These operators compare two values and return a Boolean (True or False).

### 11. Assignment Operators =, +=, -=, *=, /=, etc.:

These are used to assign values to variables.

### 12. Logical NOT not:

This negates a Boolean expression, meaning if the expression is True, it becomes False, and vice versa.

### 13. Logical AND and:

This operator returns True if both operands are true.

### 14. Logical OR or:

This operator returns True if at least one of the operands is true.

### 15. Conditional Expressions (Ternary Operator) if - else:

These evaluate conditions and return values based on the condition.


# Example for Fahrenheit to Celsius Conversion

To demonstrate the order of operations, let's use the example of converting Fahrenheit to Celsius:

print(75 - 32 * 5 / 9)


### Incorrect Conversion Breakdown

Multiplication: 32 * 5 results in 160.
Division: 160 / 9 results in approximately 17.7778.
Subtraction: 75 - 17.7778 results in approximately 57.2222.
So, the output is 57.2222, which is incorrect for a temperature conversion.

Correct Conversion
To ensure the conversion is computed correctly:

print((75 - 32) * 5 / 9)

Parentheses: (75 - 32) results in 43.
Multiplication: 43 * 5 results in 215.
Division: 215 / 9 results in approximately 23.8889.


### Example Showing Full Order of Operations
Let's look at a more complex expression:

print(3 + 4 * 2 / (1 - 5) ** 2)

Step-by-Step Evaluation:
Parentheses: Compute (1 - 5), which results in -4.
Exponentiation: Compute (-4) ** 2, which results in 16.
Multiplication: Compute 4 * 2, which results in 8.
Division: Compute 8 / 16, which results in 0.5.
Addition: Compute 3 + 0.5, which results in 3.5Thus, the output of the expression is 3.5.

Thus, the output of the expression is 3.5.


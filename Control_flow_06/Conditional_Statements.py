# # Conditional Statements

# # The Problem: Making Decisions in Code

# """ 
# If you've money, you can eat pizza.
# Otherwise, you've to eat whatever is cooked by Mama.
# """

is_money: bool = False

if is_money:
    # Indentation. Look how our 'if' block code is indented by 4 spaces.
    print("Eat Pizza")
else:
    print("Eat whatever is cooked by Mama")


# """ 
# If you've money, you can eat pizza.
# Otherwise, you've to eat whatever is cooked by Mama.
# """

is_money: bool = True

if is_money:
    # Indentation. Look how our 'if' block code is indented by 4 spaces.
    print("Eat Pizza")
else:
    print("Eat whatever is cooked by Mama")

is_money=True

# #indentation

if is_money:
    print(f"eat Pizza")
    
else:
    print(f"patient")
    
    

is_money1=False

# #indentation

if is_money1:
    print(f"eat Pizza")
    
else:
    print(f"patient")


# """ 
# Enter the amount of money you've.
# The code will check wheter you can eat pizza or not.
# """
# money: int = int(input("Enter the amount of money you've: "))

# # indentation
if money > 2000:
    print("Eat Pizza")

else:
    print("Eat whatever is cooked by Mama")


money=100

# #indentation

if money>2000:
    print(f"eat Pizza")
    
else:
    print(f"patient")
    
money=2500

# #indentation

if money>2000:
    print(f"eat Pizza")
    
else:
    print(f"patient")
    
# # if-elif-else
# # When we have multiple conditions (choices) to evaluate, we use if-elif-else chain.
# # Remember, only one condition in this case will be evaulated to True.
    
# marks_obtained: int = int(
#     input("Enter the marks obtained to check what grade you got: "))

if marks_obtained >= 80:
    print("A+")
elif marks_obtained >= 70:
    print("A")
elif marks_obtained >= 60:
    print("B")
else:
    print("Needs Improvement")
    
    
    
    marks_obtain1 = 50
    if marks_obtain1 >= 80:
        print("A+")
    elif marks_obtain1>=70:
        print("A")
    elif marks_obtain1 >=60:
        print("B")
    else :
        print("Need Improvement")
        
# # Nested if-elif-else

# destination_city: str = input(
#     "Choose your desitantion among 'lahore' or 'peshawar': ")

# if destination_city.lower() == "lahore":
#     """
#     lower() is a string method which converts the string to lowercase. 
#     Here if user inputs 'Lahore', 'LAHORE', or 'lahore', we can confidently compare it with 'lahore'.
#     """
    bus: str = input("Choose among 'faisal movers' or 'daewoo': ")
    if bus.lower() == 'faisal movers':
        print("Buy Ticket from Faisal Movers Terminal")
    elif bus.lower() == 'daewoo':
        print("Buy Ticket from Daewoo Terminal")
    else:
        print("User choose something else")

    # elif destination_city.lower() == "peshawar":
    #       print("You will user Car to go to Peshawar")
    # beverage_preference: str = input(
    #     "What you prefer to drink? choose one among 'tea' or 'cold drink'")
    # if beverage_preference.lower() == 'tea':
    #     print("Tea is a good choice. It won't let you sleep")
    # elif beverage_preference.lower() == "cold drink":
    #     print("Enjoy you cold drink")
    # else:
    #     print("User input was not 'tea' or 'cold drink'")
    # else:
    # print("User choose the destination other than Peshawar or Lahore")
# # Nested Conditional Statements

city = "Lahore"
bus = "FaisalMovers"

if city == "Lahore":
    print("Bus")
    if bus == "FaisalMovers":
        print("sabar")
elif city == "Peshawar":
    print("Car")

city = "Peshawar"
bus = "FaisalMovers"

if city == "Lahore":
    print("Bus")
    if bus == "FaisalMovers":
        print("sabar")
elif city == "Peshawar":
    print("Car")








is_handsome = True
is_rich = True
if is_handsome and is_rich:
    print("proposal accepted")
else:
    print("Rejected")
    
    
is_handsome = False
is_rich = True
if is_handsome or is_rich:
    print("proposal accepted")
else:
    print("Rejected")
    
    
is_handsome = False
is_rich = True

if is_handsome or is_rich:
    print("proposal accepted")
else:
    print("Rejected")

    
is_handsome = False
is_rich = True
living = "USA"
if is_handsome and is_rich and living == 'USA':
    print("proposal accepted")
else:
    print("Rejected")
    
    
is_handsome = False
is_rich = True
living = "USA"
if is_handsome or is_rich or living == 'USA':
    print("proposal accepted")
else:
    print("Rejected")


weather : str = "sunny"

if weather == "sunny":
    print("It's a beautiful day! Go for a walk.")
    
    
weather1 : str = "Rainy"

if weather1 == "sunny":
    print("It's a beautiful day! Go for a walk.")
else:
    print("Read the book")
    
    # Ternary Operator (Optional):
# We can also write the above example like so.
weather2 : str =  "sunny"

if weather2 == "sunny":
    message : str = "It's a beautiful day! Go for a walk."
else:
    message : str = "Read the Book"
print(message)

# Use of Ternary Operator
weather3 : str == "sunny"
message : str = "It's a beautiful day! Go for a walk." if weather == "sunny" else "Read the book"
print(message)


weather4 : str = "cloudy"

if weather4 == "sunny":
    print("It's a beautiful day! Go for a walk.")
elif weather4 == "cloudy":
    print("It might rain. Better take an umbrella.")
    
    
    
    
weather5 : str = "rainy"

if weather5 == "sunny":
    print("It's a beautiful day! Go for a walk.")
elif weather5 == "cloudy":
    print("It might rain. Better take an umbrella.")
else:
    print("Stay indoors and read a book.")
    
# Nested Conditional Statements
    
#  Simple if Statement

# Scenario: A user wants to check if they have enough balance to make a purchase.

balance : int = 150
price : int = 100

if balance >= price:
    print("Purchase successful!")
    
# if-elif-else Chain

# Scenario: A system that grades students based on their score.

score : int = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    
# Nested if Statement
# Scenario: A store offers a discount only to members who have also made purchases above a certain amount.

is_member : bool = True
purchase_amount : int = 250

if is_member:
    if purchase_amount > 200:
        print("You are eligible for a 10% discount!")
    else:
        print("Spend more than $200 to get a discount.")
else:
    print("Become a member to enjoy discounts.")
    
is_member : bool = False
purchase_amount : int = 250

if is_member:
    if purchase_amount > 200:
        print("You are eligible for a 10% discount!")
    else:
        print("Spend more than $200 to get a discount.")
else:
    print("Become a member to enjoy discounts.")
    
    
# Multiple if Statements (Independent Conditions)
# Scenario: A smart home system that checks several independent conditions to set up the house for the night.

lights_on : bool = True
doors_locked : bool = False
windows_closed : bool = True

if lights_on:
    print("Turning off the lights.")
if not doors_locked:
    print("Locking the doors.")
if windows_closed:
    print("All windows are closed.")
    
# Nested if with elif and else
# Scenario: A restaurant ordering system that checks if a user has chosen a meal and then checks for special requests.

meal_selected : str = "burger"
add_cheese : bool = True

if meal_selected == "burger":
    print("Burger selected.")

    if add_cheese:
        print("Adding cheese.")
    else:
        print("No cheese added.")

elif meal_selected == "pizza":
    print("Pizza selected.")
else:
    print("Please select a meal.")
    
meal_selected : str = "pizza"
add_cheese : bool = True

if meal_selected == "burger":
    print("Burger selected.")

    if add_cheese:
        print("Adding cheese.")
    else:
        print("No cheese added.")

elif meal_selected == "pizza":
    print("Pizza selected.")
else:
    print("Please select a meal.")
    
    
    
# Logical Operators:

# """Logical operators are used to combine conditions(choices)
# If we want to evaluate more than one condition simultaneously, we combine the conditions with logical operators.
# and --> aur or --> yaaa not --> Naheeeeeeee"""


# The Solution: Combining Conditions with Logical Operators

"""In Python, Logical Operators (and, or, not) are essential tools that allow we to combine multiple conditions in our code. They enable our program to make complex decisions by evaluating whether a group of conditions are true or false.

The Story of Complex Decisions: and, or, and not
Let's explore how Python uses logical operators to manage complex scenarios in our code.
"""
# The And Operator:

"""Imagine we need to check if two conditions are both true. The and operator allows we to combine these conditions so that the flow of our program continues only if both are met.
In our smart home example, we want to lock the doors only if it’s nighttime and the user is away."""

is_night : bool = True
is_user_away : bool = True

if is_night and is_user_away:
    print("Lock the doors.")

# The "Or" Operator:

# """Sometimes, we want to take action if at least one of several conditions is true. The or operator allows our program to proceed if any of the combined conditions are met.
# For instance, we want to lock the doors if it’s either nighttime and the user is away or if the system is in "vacation mode.""""

is_vacation_mode : bool = True

if (is_night and is_user_away) or is_vacation_mode:
    print("Lock the doors.")

# The "Not" Operator:

"""There are situations where we need to reverse a condition. The not operator inverts the truth value of a condition, allowing our program to act when something is not true.
In our case, we don’t want to lock the doors if the user is home, regardless of the other conditions."""

is_user_home : bool = False

if (is_night and is_user_away) or is_vacation_mode and not is_user_home:
    print("Lock the doors.")
else:
    print("Do not lock the doors.")

is_handsome = True
is_rich = False

if is_handsome and is_rich:
    print("Proposal Accepted")
else:
    print("Rejected")
    
is_handsome = True
is_rich = False

if is_handsome or is_rich:
    print("Proposal Accepted")
else:
    print("Rejected")
    
"""Trick to remember logical operators
Consider the followings

True = 1
False = 0
and = *
or = +
For and operator
0 * 0 = 0 --> False and False = False
1 * 0 = 0 --> True and False = False
0 * 1 = 0 --> False and True = False
1 * 1 = 1 --> True and True = True
For or operator
0 + 0 = 0 --> False or False = False
1 + 0 = 1 --> False or True = True
0 + 1 = 1 --> False or True = True
1 + 1 = 1 --> True or True = True"""

"""Shortcircuiting of 'and' operator
In one expression where all the conditions are chained with and, If the Python Interpreter finds first value to False, it will not check the remaining conditions(values) and will evaluate the whole expression to be False.
Why it is so? Because in and operator operation, if we have one False value, then all the and operations evaluates to False and else block will be executed.
"""

is_handsome = False
is_rich = True
living = 'USA'

if is_handsome and is_rich and living == 'USA':
    print("Proposal Accepted")
else:
    print("Rejected")
    
# Shortcircuiting of 'or' operator

"""In one expression where all the conditions are chained with or, If the Python Interpreter finds first value to True, it will not check the remaining conditions(values) and will evaluate the whole expression to be true.
Why it is so? Because in or operator operation, if we have one True value, then all the or operations evaluates to True and if block will be executed."""


is_handsome = True
is_rich = False
living = 'USA'

if is_handsome or is_rich or living == 'USA':
    print("Proposal Accepted")
else:
    print("Rejected")



# Example of not Logical Operator
# not simply reverse the value.

is_member: bool = False

if is_member:
    print("You're welcomed")
else:
    print("Please become a member first")

is_member: bool = True
# Now check with `not` operator. See how it inverts the value.
if not is_member:
    print("The if block was executed because the if condition evaluated to 'True'")
else:
    print("The 'else' block is executed because the if condition was evaluated to 'False'")
    
temperature = 30

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("The weather is nice.")
elif temperature > 10:
    print("It's a bit chilly.")
else:
    print("It's cold outside.")
    
    
# Examples

# Scenario: Finding a Life Partner

# Imagine you're looking for a life partner, and you have certain qualities in mind that are important to you. Specifically, you want your partner to be either handsome and also well-educated. You can use logical operators to determine if a potential partner meets these criteria.

# 1. Using the and Operator

# You want to ensure that the person is both handsome and well-educated. Both conditions must be true for the person to be considered.

is_handsome : bool = True
is_well_educated : bool = True

if is_handsome and is_well_educated:
    print("This person might be a great match!")
else:
    print("Keep looking for someone with both qualities.")
    
    
# Using the or Operator

# Now, let's say you’re a bit more flexible, and you’re open to considering someone who either has good looks or is well-educated (or both).

is_handsome : bool = False
is_well_educated : bool= True

if is_handsome or is_well_educated:
    print("This person could be a good match!")
else:
    print("Keep looking for someone who meets at least one of your criteria.")
    
# Using the not Operator
# Let’s add another layer. Suppose you want to avoid someone who is not well-educated, regardless of whether they are handsome.

is_handsome : bool = True
is_well_educated : bool = False

if is_handsome and not is_well_educated:
    print("This person is attractive but not well-educated.")
else:
    print("This person is either well-educated, or both attractive and well-educated.")
    
    
# Combining Multiple Logical Operators

# Finally, let's say you have a scenario where you want to find someone who is either well-educated and handsome, or at least has one of these qualities.

is_handsome : bool = False
is_well_educated : bool = True
is_high_income : bool = True

if (is_handsome and is_well_educated) or is_high_income:
    print("This person is well-educated, which is important to you.")
else:
    print("Keep looking for someone who fits your criteria better.")

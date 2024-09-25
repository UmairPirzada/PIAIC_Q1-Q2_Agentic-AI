# Example 1: Basic while Loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    
# Example 2: while Loop with a Condition
"""You can use a while loop to keep prompting the user until they enter a valid input."""

password = ""
while password != "Pass123":
    password = input("Enter the password: ")

print("Access granted")

# Example 3: Infinite while Loop
"""A while loop can run indefinitely if the condition never becomes False. 
This is known as an infinite loop, and it will continue to run until 
you manually stop it or break out of it with a break statement."""

while True:
    print("This loop will run forever")
    # You can include a break condition to exit the loop
    
    
while True:
    print("This loop will run forever")
    # Example break condition
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break

condition = ""
while condition != 'exit':
    user_in = input("Enter command: ")
    if user_in != 'exit':
        print(user_in)
    elif user_in == 'exit':
        condition = user_in
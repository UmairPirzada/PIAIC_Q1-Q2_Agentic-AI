print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Power")
print("6 - Modulus")
print("7 - Floor Division")
option = int(input("Choose an Operation (1-7): "))

if option in [1, 2, 3, 4, 5, 6, 7]:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    
    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif option == 5:
        result = num1 ** num2
    elif option == 6:
        result = num1 % num2
    elif option == 7:
        result = num1 // num2

    print(f"The Result of the Operation is: {result}")
else:
    print("Invalid Operation Entered. Please choose a number between 1 and 7.")

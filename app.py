# num1 = input("Enter a number")

# num2 = input("Enter a second number")


# result = float(num1) + int(num2) 


# print(result)

num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")
operator = input("Enter an operator (+, -, *, /): ")

# Define a dictionary to map operators to functions
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

# Check if the operator is valid
if operator in operations:
    result = operations[operator](float(num1), float(num2))
    print('Result is', result)
else:
    print("Invalid operator. Please enter one of the following: +, -, *, /")

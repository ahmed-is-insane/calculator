
print (" TASK NUMBER 2 \n \n ")
print("Calculator performing two arithmetic operations")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options: \n ")
    print("Enter 'add' for addition \n")
    print("Enter 'subtract' for subtraction \n")
    print("Enter 'multiply' for multiplication \n")
    print("Enter 'divide' for division \n")
    print("Enter 'quit' to end the program \n")

    input_data = input(": ")
    
    if input_data == "quit":
        break

    elif input_data in ("add", 'subtract', "multiply", "divide"):
        Number1 = float(input("Enter the first number: "))
        Number2 = float(input("Enter the second number: "))
        print("First number:", Number1, "\n Second number:", Number2)

        print("Enter a desired arithmetic operation:")
        input_data = input_data.lower()

        if input_data == "add":
            print("Addition:", add(Number1, Number2) )
        elif input_data == "subtract":
            print("Subtraction:", subtract(Number1, Number2))
        elif input_data == "divide":
            print("Division:", divide(Number1, Number2))
        elif input_data == "multiply":
            print("Multiplication:", multiply(Number1, Number2))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
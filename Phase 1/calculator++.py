x = input("Enter a value for x: ")
operation = input("Enter an operation (+, -, *, /, ^, /2): ")
y = input("Enter a value for y: ")

if operation == "+":
    result = int(x) + int(y)
    print(f"The result of addition is: {result}")
else:
    if operation == "-":
        result = int(x) - int(y)
        print(f"The result of subtraction is: {result}")
    else:
        if operation == "*":
            result = int(x) * int(y)
            print(f"The result of multiplication is: {result}")
        else:
            if operation == "/":
                result = int(x) / int(y)
                print(f"The result of division is: {result}")
            else:
                if operation == "^":
                    result = int(x) ** int(y)
                    print(f"The result of exponentiation is: {result}")
                else:
                    if operation == "/2":
                        result1 = int(x) ** 0.5
                        result2 = int(y) ** 0.5
                        print(f"the square root of {x} is: {result1}")
                        print(f"the square root of {y} is: {result2}")
                    else:
                        print("Invalid operation.")

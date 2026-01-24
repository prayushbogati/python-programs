def add(a, b):
   return a + b

def sub(a, b):
   return a - b

def mul(a, b):
   return a * b

def div(a, b):
   return a / b

def exe_op(num1, num2):
    if op == "+":
        result = add(num1, num2)

    elif op == "-":
        result = sub(num1, num2)

    elif op == "*":
        result = mul(num1, num2)

    elif op == "/":
        result = div(num1, num2)

    return result

# to take valid number inputs
while True:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        if isinstance(int(num1), (int)) and isinstance(int(num2), (int)):
            num1 = int(num1)         
            num2 = int(num2)         
            break
    except:
        print("Enter integer values!")

# to take valid operation
while True:
    op = input("Enter the operation: ")
    if op in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operation! Enter again.")

result = 0

result = exe_op(num1, num2)

print("Result:", result)

# for executing another op with result
while True:
    currentVal = result
    new_op = input("do another operation? (y/n) ").lower()
    if new_op == "y":
        while True:
            op = input("Enter the operation: ")
            if op in ["+", "-", "*", "/"]:
                break
            else:
                print("Invalid operation! Enter again.")
    
        num2 = int(input("Enter other number: "))

        result = exe_op(currentVal, num2)

        print("Result:", result)

    else:
        break

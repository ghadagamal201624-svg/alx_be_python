num1 = input("Enter the first number:")
num2 = input("enter the second number:")
operation = input("choose the operation (+,-,*,/):")
match operation: 
    case"+":
        result = num1 + num2
        print(f"the result is {result}")
    case"-":
        result = num1 - num2
        print(f"the result is {result}")
    case"*":
        result = num1 * num2
        print(f"the result is {result}")
    case"/":
        if num2 == 0:
            print("Erorr: Division by zero os not allowed!")
        else:
            result = num1 / num2
            print(f"the result is {result}")
num1 = int(input("Enter a number1 : "))
num2 = int(input("Enter a number2 : "))

operator = input("Enter a operator")

match operator:
    case "+":
        print("Sum is ",num1 + num2)
    case "-":
        print("Subtraction is ",num1 - num2)
    case "*":
        print("Multiplication is",num1/num2)
    case "/":
        print("Division is",num1 / num2)
    case _ : #default statement
        print("Enter a valid operator")

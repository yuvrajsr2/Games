
num1 = float(input("Enter a number: "))
unit = input("+, -, *, /, %: ")
num2 = float(input("Enter another number: "))

if unit == "+":
    print(num1 + num2)

elif unit == "-":
    print(num1 - num2)

elif unit == "*":
    print(num1 * num2)

elif unit == "/":
    print(num1 / num2)

elif unit == "%":
    percentage = (num1 / 100) * num2

    print(percentage)

else:
    print("Invalid Input")



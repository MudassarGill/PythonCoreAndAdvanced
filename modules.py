from calculator import Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

calc = Calculator(num1, num2)

print("Addition:", calc.add())
print("Subtraction:", calc.sub())
print("Multiplication:", calc.mul())
print("Division:", calc.div())


while True:

    print("1 Add")
    print("2 Sub")
    print("3 Mul")
    print("4 Div")
    print("5 Exit")

    choice = int(input("Choice: "))

    if choice == 5:
        break

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    calc = Calculator(n1, n2)

    if choice == 1:
        print(calc.add())

    elif choice == 2:
        print(calc.sub())

    elif choice == 3:
        print(calc.mul())

    elif choice == 4:
        print(calc.div())

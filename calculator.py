import logging

class Calculator:

    # Logger setup
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("calculator.log")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Calculator started")

    def __init__(self):
        self.num1 = int(input("Enter your first number: "))
        self.num2 = int(input("Enter your second number: "))
        self.logger.info("Numbers received")

    def add(self):
        result = self.num1 + self.num2
        self.logger.info("Addition performed")
        print(f"The sum of {self.num1} and {self.num2} is {result}")

    def sub(self):
        result = self.num1 - self.num2
        self.logger.info("Subtraction performed")
        print(f"The difference of {self.num1} and {self.num2} is {result}")

    def mul(self):
        result = self.num1 * self.num2
        self.logger.info("Multiplication performed")
        print(f"The product of {self.num1} and {self.num2} is {result}")

    def div(self):
        try:
            result = self.num1 / self.num2
            self.logger.info("Division performed")
            print(f"The division of {self.num1} and {self.num2} is {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero")
            self.logger.error("Division by zero attempted")


def main():
    while True:
        print("\nWelcome to the Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting calculator...")
            break

        calc = Calculator()

        if choice == 1:
            calc.add()
        elif choice == 2:
            calc.sub()
        elif choice == 3:
            calc.mul()
        elif choice == 4:
            calc.div()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
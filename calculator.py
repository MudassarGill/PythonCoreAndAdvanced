#Here we make a simple calculator using oop in python
import logging
class calculator:

    #---------------- Logger Setup ---------------- #
 logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("calculator.log")
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Preparing started")

def __init__(self,num1,num2):
        logger.info("Calculator initialized")
        user_input_num1=int(input('Enter your first number'))
        user_input_num2=int(input('Enter your second number'))
        self.num1=user_input_num1
        self.num2=user_input_num2
def add(self):
        logger.info("Addition performed")
        print(f'The sum of {self.num1} and {self.num2} is {self.num1+self.num2}')
        return self.num1+self.num2
def sub(self):
        logger.info("Subtraction performed")
        print(f'The difference of {self.num1} and {self.num2} is {self.num1-self.num2}')
        return self.num1-self.num2
def mul(self):
        logger.info("Multiplication performed")
        print(f'The product of {self.num1} and {self.num2} is {self.num1*self.num2}')
        return self.num1*self.num2
def div(self):
        logger.info("Division performed")
        print(f'The division of {self.num1} and {self.num2} is {self.num1/self.num2}')
        return self.num1/self.num2

#main menu

def main():
    print("Welcome to the calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        calc=calculator(0,0)
        calc.add()
    elif choice==2:
        calc=calculator(0,0)
        calc.sub()
    elif choice==3:
        calc=calculator()
        calc.mul()
    elif choice==4:
        calc=calculator()
        calc.div()
    elif choice==5:
        exit()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
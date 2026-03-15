import logging

class Calculator:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("calculator.log")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.logger.info("Calculator object created")

    def add(self):
        self.logger.info("Addition performed")
        return self.num1 + self.num2

    def sub(self):
        self.logger.info("Subtraction performed")
        return self.num1 - self.num2

    def mul(self):
        self.logger.info("Multiplication performed")
        return self.num1 * self.num2

    def div(self):
        self.logger.info("Division performed")
        return self.num1 / self.num2

        
#Bank Management System

from dataclasses import dataclass
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BankManagementSystem")

class Account(ABC):
    logger.info("Account class is created")
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        logger.info("Account is created with account number: %s and balance: %s", account_number, balance)

    @abstractmethod
    def deposit(self, amount):
        logger.info("Deposit amount: %s", amount)
        pass

    @abstractmethod
    def withdraw(self, amount):
        logger.info("Withdraw amount: %s", amount)
        pass

    def get_balance(self):
        logger.info("Balance: %s", self.balance)
        return self.balance

class SavingsAccount(Account):
    logger.info("SavingsAccount class is created")
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        logger.info("SavingsAccount is created with account number: %s and balance: %s", account_number, balance)
    def deposit(self, amount):
        logger.info("Deposit amount: %s", amount)
        self.balance += amount
        logger.info("Balance: %s", self.balance)
    def withdraw(self, amount):
        logger.info("Withdraw amount: %s", amount)
        if self.balance < amount:
            logger.info("Insufficient balance")
            return False
        self.balance -= amount
        logger.info("Balance: %s", self.balance)
        return True


class CurrentAccount(Account):
    logger.info("CurrentAccount class is created")
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        logger.info("CurrentAccount is created with account number: %s and balance: %s", account_number, balance)
    def deposit(self, amount):
        logger.info("Deposit amount: %s", amount)
        self.balance += amount
        logger.info("Balance: %s", self.balance)
    def withdraw(self, amount):
        logger.info("Withdraw amount: %s", amount)
        if self.balance < amount:
            logger.info("Insufficient balance")
            return False
        self.balance -= amount
        logger.info("Balance: %s", self.balance)
        return True


#create obj

c1=CurrentAccount("John", 1000)
s1=SavingsAccount("Jane", 2000)

#deposit and withdraw
c1.deposit(500)
c1.withdraw(200)
s1.deposit(1000)
s1.withdraw(500)

#check balance
print("Current Account Balance:", c1.get_balance())
print("Savings Account Balance:", s1.get_balance())
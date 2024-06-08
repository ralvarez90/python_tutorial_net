import unittest


class InsufficientFund(Exception):
    pass


class BankAccount:

    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError('Ampunt `balance` can not be negative.')
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('The amount must be positive')
        self._balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError('The withdrawal amount must be more than 0')

        if amount > self._balance:
            raise InsufficientFund('Insuficient ammount for withdrawal')
        self._balance -= amount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)

    def testDeposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 200)

    def testWithdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def tearDown(self):
        self.account = None

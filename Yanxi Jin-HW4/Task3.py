import unittest
from Task2 import ATM
import random


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()
        self.password = 'a_random_code'

    def test_withdraw(self):
        self.atm.login(self.password)
        amount = random.uniform(0, 200)
        print(f'testing amount is {amount}')
        if amount <= self.atm.balance:
            self.atm.withdraw(amount)
            self.assertEqual(self.atm.balance, 100-amount)  # add assertion here
        else:
            with self.assertRaises(ArithmeticError):
                self.atm.withdraw(amount)

    def test_show_balance(self):
        self.assertIsNone(self.atm.balance)
        self.atm.login(self.password)
        self.assertIsInstance(self.atm.balance, float)

    def test_status(self):
        self.assertFalse(self.atm.signed_in)
        self.atm.login(self.password)
        self.assertTrue(self.atm.signed_in)

    def test_login(self):
        self.assertEqual(self.atm.login(self.password), 1)


if __name__ == '__main__':
    unittest.main()
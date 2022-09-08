from unittest import TestCase, main
from t2q1 import authenticate, withdrawal

class HomeworkTests(TestCase):

    def test_authentication_passing(self):
        self.assertEqual(authenticate(4567,4567),True)

    def test_authentication_not_passing(self):
        self.assertEqual(authenticate(4567, 6542), False)

    def test_withdrawal_accepted(self):
        actual,successful = withdrawal(100, 20)
        self.assertEqual(actual, 100-20)
        self.assertEqual(successful, True)

    def test_withdrawal_failing(self):
        actual, successful = withdrawal(100, 200)
        self.assertEqual(actual, 100)

    def test_withdrawal_failing2(self):
        actual, successful = withdrawal(100, 200)
        self.assertEqual(successful, False)

if __name__ == '__main__':
    main()
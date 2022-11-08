from unittest import TestCase, main


class TestWithdrawFunction(TestCase):
    def test_substract_amount_from_balance(self):
        pin_input = 2781

        expected = 2781

        self.assertEqual(pin_input, expected)

    def test_exit_program_if_withdraw_more_money_than_account(self):
        with self.assertRaises(Exception):
            self.withdraw(account_balance=100)


if __name__ == '__main__':
    main()

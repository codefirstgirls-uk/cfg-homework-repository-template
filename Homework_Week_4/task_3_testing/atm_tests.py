import unittest
import builtins
from unittest import TestCase, main
from unittest.mock import Mock
from atm import cash_withdraw, verify_pin, log_in
from unittest.mock import patch

class ATMTests(TestCase):

    def test_verify_pin_should_return_true(self):
        expected = True
        actual = verify_pin('1234')
        self.assertEqual(expected, actual)

    def test_cash_withdraw(self):
        expected = 98
        result = cash_withdraw(2)
        self.assertEqual(expected, result)

    def test_cash_withdraw_exception(self):
        with self.assertRaises(Exception): cash_withdraw()

    @patch('atm.cash_withdraw')
    def test_log_in__should_call_cash_withdraw_for_correct_pin(self, mock_cash_withdraw):
        builtins.input = Mock()
        builtins.input.side_effect = ['1234']
        log_in()
        mock_cash_withdraw.assert_called_once()

    def test_cash_withdraw_should_raise_type_error(self):
        with self.assertRaises(TypeError):
            cash_withdraw('asf')

if __name__ == '__main__':
    main()













if __name__ == '__main__':
    main()
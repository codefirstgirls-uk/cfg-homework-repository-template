# TASK 2 (Exception Handling)
# Question 1

account_balance = 100
pin_num = 2781


def withdraw():
    while True:
        try:
            amount = int(input('Please enter the amount you wish to withdraw: £'))
            print(' ')
        except (ValueError, TypeError):
            print('Please enter a correct amount')
            print(' ')
        else:
            if amount > account_balance:
                raise Exception('You do not have sufficient funds in your account to make this withdrawal')

            else:
                balance = account_balance - amount
                print(str('You have withdrawn £{}, Your remaining balance is £{}'.format(amount, balance)))
                print(' ')
        finally:
            print('Transaction Ended')

            quit()


def pin_input():
    tries = 0
    while tries < 3:
        try:
            pin = int(input('Please enter your four digit pin code: '))
            print(' ')
        except (ValueError, TypeError):
            print('Please type in the correct pin')
            print(' ')
            tries += 1
        else:
            if pin != pin_num:
                print('Pin does not match. Try again')
                print(' ')
                tries += 1
            else:
                withdraw()

    if tries == 3:
        print('PIN INCORRECTLY ENTERED THREE TIMES')
        print(' ')
        print('YOUR CARD HAS BEEN BLOCKED')


if __name__ == '__main__':
    pin_input()



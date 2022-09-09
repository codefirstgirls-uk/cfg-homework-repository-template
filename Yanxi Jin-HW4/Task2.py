class ATM(object):
    def __init__(self, balance=100):
        self.__balance = float(balance)
        self.__password = 'a_random_code'
        self.__signed_in = False
        self.chance = 3

    @property
    def balance(self):
        if self.__signed_in:
            return self.__balance

    @property
    def signed_in(self):
        return self.__signed_in

    def login(self, pwd=None):
        if self.chance > 0:
            password = pwd or input("password:")
            if password == self.__password:
                self.__signed_in = True
                print('Success')
                return 1
            else:
                self.chance += -1
                print(f'wrong password, {self.chance} chance(s) left')
                self.login()
        else:
            print("no chance left")
            exit()

    def withdraw(self, amount):
        amount = float(input('how much do you want to withdraw:'))
        assert isinstance(amount, float), 'the amount is not a number'
        if not self.__signed_in:
            print('you have not signed in')
            self.login()
        else:
            if amount > self.__balance:
                raise ArithmeticError
            else:
                self.__balance -= amount
                print(f'your balance after withdraw:{self.__balance}')


if __name__ == '__main__':
    atm = ATM()
    atm.login()
    try:
        atm.withdraw(float(input('how much do you want to withdraw:')))
    except ValueError:
        print('please check your number')
    except ArithmeticError:
        print('no enough balance')


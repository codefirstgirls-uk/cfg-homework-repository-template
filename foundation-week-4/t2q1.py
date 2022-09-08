#Task 1
tries = 3
account_balance= 100
pin_code = 4567

def authenticate(pin_code, user_pin_code):
    return user_pin_code == pin_code

def withdrawal(account_balance, withdrawal_sum):
    if withdrawal_sum <= account_balance:
       return account_balance - withdrawal_sum, True
    else:
        return account_balance, False

def ATM(pin_code, account_balance):
    try:
        successful = False
        for login_attempt in range(tries):
            login_attempt += 1
            user_pin_code = int(input(f"Enter your PIN code ({login_attempt}): "))
            successful = authenticate(pin_code, user_pin_code)
            if successful:
                print("Logged in!")
                break
        if not successful:
            raise Exception
    except:
        print("You have entered password wrong three times.")
    else:
        withdrawal_sum = int(input(f"How much money do you want to withdrawal(account has {account_balance} euros): "))
        try:
            account_balance, successful = withdrawal(account_balance,withdrawal_sum)
            if successful:
                print("Withdrawal was successful!")
                print(f"Now you have {account_balance} euros in your account.")
            else:
                raise Exception
        except:
            print("You do not have enough money to withdrawal money.")
    finally:
        print("End of Session!")

if __name__ == '__main__':
    ATM(pin_code, account_balance)


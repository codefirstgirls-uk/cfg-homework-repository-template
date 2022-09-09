def cash_withdraw(amount):
    balance = 100
    if amount < balance:
        balance = balance - amount
        return balance
    else:
        raise Exception("Withdrawal amount can't be more than balance")

def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    attempt = 0
    while attempt < 3:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Correct pin")
            cash_withdraw()
            break
        else:
            print("Invalid pin")
            attempt += 1
    print("Thank you for using the ATM.")

def main_menu():
    print("Welcome to the atm!")
    log_in()


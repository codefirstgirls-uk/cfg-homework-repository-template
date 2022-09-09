def cash_withdraw():
    balance = 100.00
    print("Your balance is",balance,)
    try:
        withdrawal_amount = float(input("How much would you like to withdraw? "))
        if withdrawal_amount > balance:
            raise Exception
            return
        else:
            balance = balance - withdrawal_amount
            print("The remaining balance in your account is $:{:2f}".format(balance))
    except:
        print("Insufficient funds to withdraw this amount")

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

main_menu()
user = {
    'PIN': 9876,
    'balance': 100
}



for i in range(3):
    PIN = int(input('PROVIDE PIN: '))
    try:
        if len(str(PIN)) !=4:
            raise Exception
    except:
        print('PIN must have 4 digits')
    else:
        if PIN != user['PIN']:
            print('incorrect PIN')

        if PIN == user['PIN']:
            print('PIN is correct')
            break
    finally:
        print('test run 1')
else:
    print('access blocked after 3 attempts!')

print('Amount of withdrawal: \n 1. 20 \n 2. 50 \n 3. 100 \n 4. 200 ')

if PIN == user['PIN']:
    while True:
        select = int(input('select one of above: 1, 2, 3, 4: '))


        try:
            if select > 4:
                raise Exception
        except:
                print('ERROR, Select between 1 - 4')
        else:
            print('you have:')
            print(user['balance'])
            if select ==1:
                result1 = user['balance'] - 20

                try:
                    if result1 < 0:
                        raise Exception
                except:
                        print('You do not have enough money')
                        break
                else:
                    print('withdrawal accepted')
                    print(f'now your balance is {result1} ')
                break
            elif select == 2:
                result2 = user['balance'] - 50
                try:
                    if result2 < 0:
                        raise Exception
                except:
                    print('You do not have enough money')
                    break
                else:
                    print('withdrawal accepted')
                    print(f'now your balance is {result2}')
                    break

            elif select == 3:
                result3 = user['balance'] - 100
                try:
                    if result3 < 0:
                        raise Exception
                except:
                    print('You do not have enough money')
                    break
                else:
                    print('withdrawal accepted')
                    print(f'now your balance is {result3}')
                    break
            elif select == 4:
                resul4 = user['balance'] - 200
                try:
                    if resul4 < 0:
                        raise Exception
                except:
                    print('You do not have enough money')
                    break
                else:
                    print('withdrawal accepted')
                    print(f'now your balance is {result4}')
                finally:
                    print('test run 2')
            else:
                print('can not do that')
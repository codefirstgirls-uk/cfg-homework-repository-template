"""
TASK 1
Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items
Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""


class CashRegister:
    number_of_items = 0
    total_price = 0

    def __init__(self, item, price):

        self.item = item
        self.price = price


        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0
        CashRegister.number_of_items += 1
        CashRegister.total_price += price


    def add_item(self, item, price):
        self.append(item,price)

    def remove_item(self, item, price):
        self.item.remove(item, price)

    def apply_discount(discount):
        if self.total_price > 10:
            reduce = self.total_price - self.discount * self.total_price
            return reduce
        return False


    def get_total(self):
        return self.total_price


    def show_items(self, item):
        return self.item

    def reset_register(self):
        pass
i = CashRegister('milk',3)
i2 = CashRegister('bread',1.5)
i3 = CashRegister('tea',4)
i4 = CashRegister('candy', 2.25)



print(CashRegister.number_of_items)
print(CashRegister.total_price)



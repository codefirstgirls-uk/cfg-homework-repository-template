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

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[item.capitalize()] = price
        self.total_price += price
        print(f"{item.capitalize():>30s}{price:>10.2f}")

    def remove_item(self, item):
        try:
            removed = self.total_items.pop(item.capitalize())
        except KeyError:
            print("Item not found.")  # Display message when removing an item that's not on the receipt
        else:
            self.total_price -= removed
            item_str = f"*CANCELLED* {item.capitalize()}"  # Assign output messages to variables
            price_str = f"–{removed:.2f}"                  # so I can align within print function.
            print(f"{item_str:>30s}{price_str:>10}")

    def apply_discount(self, percentage_discount):
        self.discount = (percentage_discount/100) * self.total_price
        self.total_price = self.total_price - self.discount

    def get_total(self):
        print(f"————————————————————————————————————————")
        # Add discount details if discount was applied
        if self.discount:
            discount_str = "DISCOUNT APPLIED"
            discount_amount_str = f"-£{self.discount:.2f}"
            print(f"{discount_str:>30s}{discount_amount_str:>10}")
        total_str = "TOTAL"
        total_price_str = f"£{self.total_price:.2f}"
        print(f"{total_str:>30s}{total_price_str:>10}\n"
              f"————————————————————————————————————————")
# EXAMPLE code run:

# ADD————————————————————————————————————————————————————————————————————————————

# Creates object of the CashRegister class.
till = CashRegister()

# Example of a customer receipt with a discount of 15%
# and an item removed from their order
till.add_item('milk Chocolate Pillows', 1.89)
till.add_item('tropical Juice Drink', 1.09)
till.add_item('mini Battenberg', 0.99)
till.add_item('yogDrink Peach-Passi', 1.49)
till.add_item('diced Chicken Breast', 2.69)
till.remove_item('tropical Juice Drink')
till.apply_discount(15)
till.get_total()

# Example of customer receipt without a discount
# or cancelled items.
till.add_item('white grape', 1.24)
till.add_item('black forest', 1.39)
till.add_item('s&B Smoothie', 1.13)
till.add_item('mango', 1.79)
till.get_total()



"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


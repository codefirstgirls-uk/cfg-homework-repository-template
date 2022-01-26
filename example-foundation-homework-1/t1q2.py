"""Task2, Question 2"""
import unittest
from t2q1 import add
# Notice how we can import and reuse code defined in other questions using imports;
# note that if the import does not work, it is likely that you are missing an __init__.py file in the homework directory. 

class AddTests(unittest.TestCase):
    """This is a test to ensure that the code defined in question 2 is behaving correctly"""
    
    def test_number_input(self):
        self.assertEqual(add(2,2), 4)

    def test_string_input(self):
        self.assertEqual(add("hello, ", "world!"), "hello, world!")

    def test_mixed_input(self):
        self.assertRaises(TypeError, add, "1", 2)


# this magic line runs all the test if you run this file
# e.g. while standing in the homework folder and running the command: python3 question3.py
if __name__ == "__main__":
    unittest.main()
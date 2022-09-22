from unittest import TestCase, main
from Utt_Christelle_assessment_two import square_function

class TestingSquareFunction(TestCase):

    def test_square_function_positive(self):
        expected = [1,4,9,25,36,64,81]
        result = square_function([1,2,3,5,6,8,9])
        self.assertEqual(expected,result)

    def test_square_function_square_negative_numbers(self):
        with self.assertRaises(Exception):
            square_function([-1,-3,-4,-5])




if __name__== '__main__':
    main()
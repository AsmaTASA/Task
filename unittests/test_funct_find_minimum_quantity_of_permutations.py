import unittest
from module_part1 import find_minimum_quantity_of_permutations
class TestFunc2(unittest.TestCase):
#unittests of function find_minimum_quantity_of_permutations

    def test_find_minimum_quantity_of_permutations(self):
        """
        test the nominal case
        """
        a = [1, 1, 0, 0, 1, 0]
        verdict, value = find_minimum_quantity_of_permutations(a)
        self.assertTrue(verdict)
        self.assertEqual(value, 1)


    def test_find_minimum_quantity_of_permutations_with_value_in_list_isNOK(self):
        """
        test the case of one element of the sequence is different from zero or one
        """
        a = [1, 1, 0, 0, 'a', 0]
        verdict, msg = find_minimum_quantity_of_permutations(a)
        self.assertFalse(verdict)
        self.assertEqual(msg, "Sequence must be a list of 0 and 1 elements")

    def test_find_minimum_quantity_of_permutations_with_not_equal_values_1_and_0(self):
        """
        test the case of one element number of 1 and 0 not equal
        """
        a = [1, 1, 0, 0, 0, 0]
        verdict, msg = find_minimum_quantity_of_permutations(a)
        self.assertFalse(verdict)
        self.assertEqual(msg, "Number of 1 elements must be equal to number of 0 elements")


    def test_find_minimum_quantity_of_permutations_with_empty_sequence(self):
        """
        test the case of and empty sequence
        """
        a = []
        verdict, msg = find_minimum_quantity_of_permutations(a)
        self.assertFalse(verdict)
        self.assertEqual(msg, "input sequence must be non empty list")

    def test_find_minimum_quantity_of_permutations_with_non_list_sequence(self):
        """
        test the case of and non list sequence
        """
        a = 'hell'
        verdict, msg = find_minimum_quantity_of_permutations(a)
        self.assertFalse(verdict)
        self.assertEqual(msg, "input sequence must be non empty list")

unittest.main(argv=[''],verbosity=2, exit=False)


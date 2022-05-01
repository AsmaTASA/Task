import unittest
from module_part1 import printFirstRepeatingElement
class TestFunc1(unittest.TestCase):
#unittests of method printFirstRepeatingElement

    def test_printFirstRepeatingElement(self):
        """
        test te nominal case
        """
        a = [1, 1, 15, 1234, 1, 1]
        b = [0, 15, 33, 4, 32, 115, 6]
        verdict, value = printFirstRepeatingElement(a, b)
        self.assertTrue(verdict)
        self.assertEqual(15, value)

    def test_printFirstRepeatingElement_no_repeated_element_present(self):
        """
        test the case of ne repeated element
        """
        a = [1, 1, 2, 2, 1, 1]
        b = [123, 15, 33]
        verdict, msg = printFirstRepeatingElement(a, b)
        self.assertFalse(verdict)
        self.assertEqual(msg, "there is no repeated number")

    def test_printFirstRepeatingElement_value_not_int_on_list1(self):
        """
        test the case of element not int on the first vector
        """
        a = [1, 'a', 0, 0, 1, 1]
        b = [1, 1, 2, 2, 1, 1]
        verdict, msg = printFirstRepeatingElement(a, b)
        self.assertFalse(verdict)
        self.assertEqual(msg, "input vector 1 should contain only int values")

    def test_printFirstRepeatingElement_value_not_int_on_list2(self):
        """
        test the case of element not int on the second vector
        """
        a = [1, 3, 0, 0, 1, 1]
        b = [1, 'a', 2, 2, 1, 1]
        verdict, msg = printFirstRepeatingElement(a, b)
        self.assertFalse(verdict)
        self.assertEqual(msg, "input vector 2 should contain only int values")

    def test_printFirstRepeatingElement_vector_not_list(self):
        """
        test te case of input vector not list
        """
        a = 'hello'
        b = [1, 3, 2, 2, 1, 1]
        verdict, msg = printFirstRepeatingElement(a, b)
        self.assertFalse(verdict)
        self.assertEqual(msg, "input vectors must be non empty list")

    def test_printFirstRepeatingElement_vector_empty_list(self):
        """
        test te case of input vector is an empty list
        """
        a = []
        b = [1, 3, 2, 2, 1, 1]
        verdict, msg = printFirstRepeatingElement(a, b)
        self.assertFalse(verdict)
        self.assertEqual(msg, "input vectors must be non empty list")

unittest.main(argv=[''],verbosity=2, exit=False)